import getpass
import os


clearScreen = lambda : os.system('cls')

if __name__ == '__main__':
    username = input('輸入使用者名稱：')
    password = getpass.getpass(prompt='輸入密碼：')
    clearScreen()

