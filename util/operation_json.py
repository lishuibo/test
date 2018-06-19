__author__ = 'Administrator'
import json


class OperationJson(object):
    def __init__(self, file_path=None):
        if file_path == None:
            self.file_path = '../dataconfig/user.json'
        else:
            self.file_path = file_path
        self.data = self.read_data()

    def read_data(self):
        with open(self.file_path) as fp:
            data = json.load(fp)
            return data

    def get_data(self, id):
        # print(type(self.data))
        return self.data[id]

    def write_data(self, data):
        with open('../dataconfig/cookie.json', 'w') as fp:
            fp.write(json.dumps(data))


if __name__ == '__main__':
    op_json = OperationJson()
    print(op_json.get_data('shop'))