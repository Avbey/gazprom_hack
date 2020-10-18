from rest_framework.views import APIView
from rest_framework.response import Response
from tdmt.tenders.models import Transaction
from tdmt.tenders.views import TransactionSerializer
from tdmt.visualizations.chart import LineChart

NUMERIC_VALUES = [
    (1000 * 1000 * 1000 * 1000, " трлн"),
    (1000 * 1000 * 1000, " млрд"),
    (1000 * 1000, " млн"),
    (1000, " тыс."),
    (1, ""),
]


def get_display_data(data):
    divider, suffix = NUMERIC_VALUES[-1]
    if data is None:
        return {"display_value": None, "display_suffix": "", "value": ""}
    for divider, suffix in NUMERIC_VALUES:
        if (abs(data) // divider) > 0:
            break

    return {"display_value": data / divider, "display_suffix": suffix, "value": data}


class HighchartLine(APIView):
    def get(self, request, *args, **kwargs):
        series = []
        client_id = request.query_params.get("client_id")
        # mcc = request.query_params.get("mcc")

        client_trans_q = Transaction.objects.filter(client_id=client_id)
        client_trans = list(
            TransactionSerializer(
                client_trans_q, many=True, context={"fields": ["TRANSACTION_DT", "CARD_AMOUNT_EQV_CBR"]}
            ).data
        )

        date_value = {}
        for trans in client_trans:
            d = date_value.get(trans["TRANSACTION_DT"], False)
            if d:
                date_value[trans["TRANSACTION_DT"]] += int(float(trans["CARD_AMOUNT_EQV_CBR"]))
            else:
                date_value.update({trans["TRANSACTION_DT"]: int(float(trans["CARD_AMOUNT_EQV_CBR"]))})
        data = [{"x": key, "y": value, **get_display_data(value), "unit": "руб."} for key, value in date_value.items()]
        data.sort(key=lambda x: x["x"])
        se = {
            "data": data,
            "name": "",
        }
        series.append(se)
        visualization = LineChart(caption="",)
        visualization.add_series(data=series)
        viz_json = visualization.export_json()

        if viz_json is not None:
            result = {"data": {"type": "chart_line", "attributes": viz_json}}
            return Response(result)
