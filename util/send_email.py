__author__ = 'Administrator'
import smtplib
from email.mime.text import MIMEText


class SendEmail:
    global send_user
    global email_host
    global password

    email_host = "smtp.sina.com"
    send_user = "litianle910124@sina.com"
    password = "was123"

    def send_mail(self, user_list, sub, content):
        user = "litianle" + "<" + send_user + ">"
        message = MIMEText(content, _subtype='plain', _charset='utf-8')
        message['Subject'] = sub
        message['From'] = user
        message['To'] = ";".join(user_list)
        server = smtplib.SMTP()
        server.connect(email_host)
        server.login(send_user, password)
        server.sendmail(user, user_list, message.as_string())
        server.close()

    def send_main(self, pass_list, fail_list):
        pass_num = float(len(pass_list))
        fail_num = float(len(fail_list))
        count_num = pass_num + fail_num

        pass_result = round(float(pass_num / count_num * 100),2)
        fail_result = round(float(fail_num / count_num * 100),2)

        user_list = ['407378019@qq.com']
        sub = "接口自动化测试报告"
        content = "此次一共运行接口个数为{0}个，通过个数为{1}个，失败个数为{2},通过率为{3}%,失败率为{4}%".format(
            int(count_num), int(pass_num), int(fail_num), pass_result, fail_result)
        self.send_mail(user_list, sub, content)


if __name__ == '__main__':
    send = SendEmail()
    send.send_main([1, 2, 3, 4], [2, 3, 4, 5, 6, 7])
