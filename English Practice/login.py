import json


class login_system:

    def __init__(self) -> None:
        self.LOGIN_MAX_TIMES: int = 3
        self.DATAPATH: str = 'personal_password.json'
        self.logged_in: bool = False
        self.user: str = None

    def register(self) -> None:

        with open(self.DATAPATH, 'r', encoding='utf8') as dataFile:
            data = json.load(dataFile)

        account: str = input('Please enter your username\n') or None
        password: str = input('Please enter your password\n') or None

        if account in data:
            print('The account has been used')
            return

        data[account] = password

        with open(self.DATAPATH, 'w', encoding='utf8') as dataFile:
            json.dump(dataFile, data, ensure_ascii=False, indent=4)

    def login(self) -> None:
        with open(self.DATAPATH, 'r', encoding='utf8') as dataFile:
            data = json.load(dataFile)
        try_times: int = 0
        while try_times < self.LOGIN_MAX_TIMES:
            account: str = input('Please enter your username\n') or None
            if account in data:
                password: str = input('Please enter your password\n') or None
                if data[account] == password:
                    self.logged_in = True
                    self.user = account
                    break
                else:
                    try_times += 1
            else:
                print("this account hasn't been set up yet,please sign in and try again")
                continue
        if self.logged_in:
            print('You have logged in to the system successfully')
            return
        else:
            print('Input has reached three times, the system has been locked up')


