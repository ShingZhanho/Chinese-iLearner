import getpass
import os
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36',
}
clearScreen = lambda: os.system('cls')
session = requests.Session()


def login_to_platform(uname, pwd):
    print('正在登入......')
    url = 'https://chinese3.i-learner.com.hk/login.php'
    data = {
        'loginsys': 'reading',
        'username': uname,
        'password': pwd
    }
    session.post(url, headers=headers, data=data)
    response = session.request('https://chinese1.i-learner.com.hk/report2_new.php', headers)
    print(response.status_code)
    print(response.text)


if __name__ == '__main__':
    print('=== 歡迎使用智愛中文平台答案解析工具 ===')
    print('= Version 0.1           28/04/2020 =')
    print('====================================')

    username = 'CPCs20171109'
    password = 's24216337'
    login_to_platform(username, password)
    clearScreen()
