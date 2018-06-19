__author__ = 'Administrator'
import json
import operator


class CommonUtil(object):
    def is_contain(self, str_one, str_two):
        flag = None
        if str_one in str_two:
            flag = 1
        else:
            flag = 0
        return flag

    def is_equal_dict(self, dict_one, dict_two):
        # if isinstance(dict_one, str):
        #     dict_one = json.loads(dict_one)
        # if isinstance(dict_two, str):
        #     dict_two = json.loads(dict_two)
        return operator.eq(dict_one, dict_two)

if __name__ == '__main__':
    dict_one = '"uid": "5249101"'
    print(type(dict_one))
    dict_two = '{"status": 10001, "msg": "成功", "data": {"userInfo": {"uid": "5249191"}, "url": ["http://www.imooc.com/user/ssologin?token=fvwUOAkQ0R8ExDPZnb1W_smQwP43NBtDWg_39QGmhJzy8J-FoQ_CAmIVquaxEIe5O82-mIdhXb85LgbNkKw2ub5cKwo32MAnLBWDGRdnCfRAiY1Py5mJrxGJ8JrI4r82uC_iYsJThLtVJxWI-d84BxajQm4VyHUyHB2LqA1Fqq5tOjnasCRArI9Od_a7YdtH3Y79wNw6Ed_9ySMjo2nNunBUxBCto7ydYe9rz7KIMxsgIdClmOQ_qFDLLydtQQYu-KUWZ", "http://coding.imooc.com/user/ssologin?token=58KuAV6cPWEpNM-_eBus9V1js1ksEJtPTxgs9tSJDdaT11ajewQF_trv0mI8NUudbwipfmEorPOC7mQyxm0fE_gY8gDwaoJnXocjcww8XYOcekG7Ab9vRL1bs3Mgz3lzbETOsDz2hDFFL965OwiRluGtryhAa1zQYss04xpxgIi5uAH6zy9ep9iczUPMfkqYjbFIz99vucLptCSzmoPdUyLqNtol4T2whUYtOfXZ8MqKpqiY-CLl40D8WntIhSwH-tv2bKSE3j"]}}'
    print(type(dict_two))
    common_util = CommonUtil()
    res = common_util.is_contain(dict_one,dict_two)
    print(res)