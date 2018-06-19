__author__ = 'Administrator'
import unittest

import mock

from base.demo import RunMain
from base.mock_demo import mock_test


class TestMethod(unittest.TestCase):
    def setUp(self):
        self.run = RunMain()

    def test_01(self):
        url = 'http://coding.imooc.com/api/cate'
        data = {
            'timestamp': '1507034803124',
            'uid': '5249191',
            'uuid': '5ae7d1a22c82fb89c78f603420870ad7',
            'secrect': '078474b41dd37ddd5efeb04aa591ec12',
            'token': '7d6f14f21ec96d755de41e6c076758dd',
            'cid': '0',
            'errorCode': 1001
        }
        self.run.run_main = mock.Mock(return_value=data)
        res = mock_test(self.run.run_main, data, url, "POST", data)
        res = self.run.run_main(url, 'POST', data)

        print(res)
        self.assertEqual(res['errorCode'], 1001, '测试失败')
        print('test_01')

    def test_02(self):
        url = 'http://coding.imooc.com/api/cate'
        data = {
            'timestamp': '1507034803124',
            'uid': '5249191',
            'uuid': '5ae7d1a22c82fb89c78f603420870ad7',
            'secrect': '078474b41dd37ddd5efeb04aa591ec12',
            'token': '7d6f14f21ec96d755de41e6c076758dd',
            'cid': '0'
        }
        res = self.run.run_main(url, 'POST', data)

        print(res)
        self.assertEqual(res['errorCode'], 1001, '测试失败')
        print('test_02')


if __name__ == '__main__':
    unittest.main