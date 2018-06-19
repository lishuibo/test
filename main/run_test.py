__author__ = 'Administrator'
from base.run_method import RunMethod
from data.get_data import GetData
from util.common_util import CommonUtil
from data.dependent_data import DependentData
from util.send_email import SendEmail
from util.operation_json import OperationJson
from util.operation_header import OperationHeader


class RunTest(object):
    def __init__(self):
        self.run_method = RunMethod()
        self.data = GetData()
        self.common_util = CommonUtil()
        self.send_email = SendEmail()

    def run(self):
        res = None
        pass_count = []
        fail_count = []
        rows_count = self.data.get_case_lines()
        for i in range(1, rows_count):
            run = self.data.get_run(i)
            if run:
                url = self.data.get_url(i)
                request_method = self.data.get_request_method(i)
                request_data = self.data.get_data_for_json(i)
                expect = self.data.get_expect(i)
                print(expect)
                header = self.data.get_header(i)
                # case_depend = self.data.get_case_depend(i)
                # if case_depend != None:
                #     self.depend_data = DependentData(case_depend)
                #     depend_response_data = self.depend_data.get_data_for_key(i)
                #     depend_key = self.data.get_depend_response_data(i)
                #     request_data[depend_key] = depend_response_data
                if header == 'write':
                    res = self.run_method.run_main(request_method, url, request_data)
                    op_header = OperationHeader(res)
                    op_header.write_cookie()
                elif header == 'yes':
                    op_json = OperationJson('../dataconfig/cookie.json')
                    cookie = op_json.get_data('apsid')
                    cookies = {'apsid': cookie}
                    res = self.run_method.run_main(request_method, url, request_data, cookies)
                else:
                    res = self.run_method.run_main(request_method, url, request_data)
                    print(res)
                if self.common_util.is_contain(expect, res) == 1:
                    self.data.write_result(i, 'pass')
                    pass_count.append(i)
                    print(pass_count)
                else:
                    self.data.write_result(i, res)
                    fail_count.append(i)
                    print(fail_count)
        self.send_email.send_main(pass_count, fail_count)


if __name__ == '__main__':
    run = RunTest()
    run.run()