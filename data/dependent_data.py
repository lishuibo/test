__author__ = 'Administrator'
import json

from jsonpath_rw import parse

from util.operation_excel import OperationExcel
from base.run_method import RunMethod
from data.get_data import GetData


class DependentData(object):
    def __init__(self, case_id):
        self.case_id = case_id
        self.op_excel = OperationExcel()
        self.data = GetData()

    def get_case_line_data(self):
        rows_data = self.op_excel.get_rows_data(self.case_id)
        return rows_data

    def run_dependent(self):
        run_method = RunMethod()
        row_num = self.op_excel.get_row_num(self.case_id)
        request_data = self.data.get_data_for_json(row_num)
        # header = self.data.get_header(row_num)
        method = self.data.get_request_method(row_num)
        url = self.data.get_url(row_num)
        res = run_method.run_main(method, url, request_data)
        return json.loads(res)

    def get_data_for_key(self, row):
        data_depend = self.data.get_data_depend(row)
        response_data = self.run_dependent()
        json_exe = parse(data_depend)
        madle = json_exe.find(response_data)
        return [math.value for math in madle][0]


if __name__ == '__main__':
    order = {
        "data": {
            "_input_charset": "utf-8",
            "body": "慕课网订单-1710141907182334",
            "it_b_pay": "1d",
            "notify_url": "http://order.imooc.com/pay/notifyalipay",
            "out_trade_no": "1710141907182334",
            "partner": "2088002966755334",
            "payment_type": "1",
            "seller_id": "yangyan01@tcl.com",
            "service": "mobile.securitypay.pay",
            "sign": "kZBV53KuiUf5HIrVLBCcBpWDg%2FnzO%2BtyEnBqgVYwwBtDU66Xk8VQUTbVOqDjrNymCupkVhlI%2BkFZq1jOr8C554KsZ7Gk7orC9dDbQlpr%2BaMmdjO30JBgjqjj4mmM%2Flphy9Xwr0Xrv46uSkDKdlQqLDdGAOP7YwOM2dSLyUQX%2Bo4%3D",
            "sign_type": "RSA",
            "string": "_input_charset=utf-8&body=慕课网订单-1710141907182334&it_b_pay=1d&notify_url=http://order.imooc.com/pay/notifyalipay&out_trade_no=1710141907182334&partner=2088002966755334&payment_type=1&seller_id=yangyan01@tcl.com&service=mobile.securitypay.pay&subject=慕课网订单-1710141907182334&total_fee=299&sign=kZBV53KuiUf5HIrVLBCcBpWDg%2FnzO%2BtyEnBqgVYwwBtDU66Xk8VQUTbVOqDjrNymCupkVhlI%2BkFZq1jOr8C554KsZ7Gk7orC9dDbQlpr%2BaMmdjO30JBgjqjj4mmM%2Flphy9Xwr0Xrv46uSkDKdlQqLDdGAOP7YwOM2dSLyUQX%2Bo4%3D&sign_type=RSA",
            "subject": "慕课网订单-1710141907182334",
            "total_fee": 299
        },
        "errorCode": 1000,
        "errorDesc": "成功",
        "status": 1,
        "timestamp": 1507979239100
    }
    res = "data.out_trade_no"
    json_exe = parse(res)
    madle = json_exe.find(order)
    print([math.value for math in madle][0])
