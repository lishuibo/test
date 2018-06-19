__author__ = 'Administrator'


class global_var(object):
    id = '0'
    module = '1'
    url = '2'
    run = '3'
    request_method = '4'
    header = '5'
    case_depend = '6'
    depend_response_data = '7'
    data_depend = '8'
    request_data = '9'
    expect = '10'
    result = '11'


def get_id():
    return global_var.id


def get_module():
    return global_var.module


def get_url():
    return global_var.url


def get_run():
    return global_var.run


def get_request_method():
    return global_var.request_method


def get_header():
    return global_var.header


def get_case_depend():
    return global_var.case_depend


def get_depend_response_data():
    return global_var.depend_response_data


def get_data_depend():
    return global_var.data_depend


def get_request_data():
    return global_var.request_data


def get_expect():
    return global_var.expect


def get_result():
    return global_var.result
