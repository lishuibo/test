__author__ = 'Administrator'
import requests


class RunMain(object):
    def send_get(self, url, data):
        res = requests.get(url=url, data=data).json()
        return res

    def send_post(self, url, data):
        res = requests.get(url=url, data=data).json()
        return res

    def run_main(self, url, method, data=None):
        res = None
        if method == 'GET':
            res = self.send_get(url, data)
        else:
            res = self.send_post(url, data)
        return res


if __name__ == '__main__':
    url = 'http://www.imooc.com/m/web/shizhanapi/loadmorepingjia.html?cart=11'
    data = {'cart': '11'}
    run = RunMain()
    res = run.run_mian(url, 'GET', data)
    print(res)