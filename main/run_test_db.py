__author__ = 'Administrator'
from base.run_method import RunMethod
from util.send_email import SendEmail
from util.common_util import CommonUtil
from util.connect_db import OperationMySQL
from util.operation_json import OperationJson


class RunTest(object):
    def __init__(self):
        self.common_util = CommonUtil()
        self.send_email = SendEmail()
        self.connect_db = OperationMySQL()
        self.run_method = RunMethod()
        self.op_json = OperationJson()

    def run(self):
        res = None
        pass_count = []
        fail_count = []
        rows_count = self.connect_db.get_count()
        print(rows_count)
        for i in range(0, rows_count):
            run = self.connect_db.search('run', i)
            if run:
                url = self.connect_db.search('url', i)
                request_method = self.connect_db.search('request_method', i)
                request_data = self.op_json.get_data(self.connect_db.search('request_data', i))
                expect = self.connect_db.search('expect', i)
                print(expect)
                res = self.run_method.run_main(request_method, url, request_data)
                print(res)
                if self.common_util.is_contain(expect, res) == 1:
                    self.connect_db.write('pass', i+1)
                    pass_count.append(i+1)
                    print(pass_count)
                else:
                    self.connect_db.write(res, i+1)
                    fail_count.append(i+1)
                    print(fail_count)
        self.send_email.send_main(pass_count, fail_count)


if __name__ == '__main__':
    run = RunTest()
    run.run()