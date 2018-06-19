__author__ = 'Administrator'
from util.operation_excel import OperationExcel
from util.operation_json import OperationJson
from util.connect_db import OperationMySQL
from data import data_config

class GetData(object):
    def __init__(self):
        self.op_excel = OperationExcel()

    def get_case_lines(self):
        return  self.op_excel.get_lines()

    def get_run(self,row):
        flag = None
        col = int(data_config.get_run())
        run_model = self.op_excel.get_cell_value(row,col)
        if run_model == 'yes':
            flag = True
        else:
            flag = False
        return flag

    def get_header(self,row):
        col = int(data_config.get_header())
        header = self.op_excel.get_cell_value(row,col)
        if header != '':
            return header
        else:
            return None

    def get_request_method(self,row):
        col = int(data_config.get_request_method())
        request_method = self.op_excel.get_cell_value(row,col)
        return request_method

    def get_url(self,row):
        col = int(data_config.get_url())
        url = self.op_excel.get_cell_value(row,col)
        return url

    def get_request_data(self,row):
        col = int(data_config.get_request_data())
        request_data = self.op_excel.get_cell_value(row,col)
        if request_data == "":
            return None
        return request_data

    def get_data_for_json(self,row):
        op_json = OperationJson()
        request_data_for_json = op_json.get_data(self.get_request_data(row))
        return request_data_for_json

    def get_expect(self,row):
        col = int(data_config.get_expect())
        expect = self.op_excel.get_cell_value(row,col)
        if expect == "":
            return None
        return expect

    def get_expect_data_for_mysql(self,row):
        op_mysql = OperationMySQL()
        sql = self.get_expect(row)
        res = op_mysql.search_one(sql)
        return res

    def write_result(self,row,value):
        col = int(data_config.get_result())
        self.op_excel.write_value(row,col,value)

    def get_data_depend(self,row):
        col = int(data_config.get_data_depend())
        data_depend = self.op_excel.get_cell_value(row,col)
        if data_depend == "":
            return None
        else:
            return data_depend

    def get_case_depend(self,row):
        col = int(data_config.get_case_depend())
        case_depend = self.op_excel.get_cell_value(row,col)
        if case_depend == "":
            return None
        else:
            return case_depend

    def get_depend_response_data(self,row):
        col = int(data_config.get_depend_response_data())
        depend_response_data = self.op_excel.get_cell_value(row,col)
        if depend_response_data == "":
            return None
        else:
            return depend_response_data