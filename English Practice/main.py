import json
import os
import time
from random import shuffle
from login import login_system


cool = login_system()


def login():
    while True:
        login_option = int(input(" 1:註冊 \n 2:登入 \n 3:離開 \n 您選擇的是： "))
        if login_option == 3:
            break
        elif login_option == 1:
            cool.register()
            continue
        elif login_option == 2:
            cool.login()
            if cool.logged_in:
                break
            else:
                continue
        else:
            print('error')
            continue


def depend(known) -> bool:
    return known == 'Y' or known == 'y'


English_to_Chinese_dictionary = {}
English_Dictionary = {}


if __name__ == '__main__':
    os.system('cls')
    login()
    os.system('cls')
    if cool.user == "potato":
        while True:
            choose = int(input(" 1:英文\n 2:離開\n 您選擇的是： ")) or None
            if choose == 1:
                while True:
                    os.system('cls')
                    select = int(
                        input(" 1:English to Chinese\n 2:Chinese to English\n 3:exit\n 您選擇的是： "))
                    if select == 1:
                        with open('English_data.json', 'r', encoding='utf-8') as f:
                            English_Dictionary = json.load(f)
                        key_list = list(English_Dictionary.keys())
                        for i in range(len(key_list)):
                            print(" {}: {}".format(i+1, key_list[i]))
                        key = key_list[int(input("\n 您選擇的是: "))-1]
                        English_to_Chinese_dictionary = English_Dictionary[key]
                        key_list = list(English_to_Chinese_dictionary.keys())
                        shuffle(key_list)
                        Yes = 0
                        No = 0
                        sum = 0
                        wrong_list = []
                        for i in key_list:
                            sum += 1
                            os.system('cls')
                            print(f" 第{sum}個單字\n")
                            print(' ' + i)
                            os.system('pause')
                            print(' ' + English_to_Chinese_dictionary[i])
                            if depend(input(" Y/N: ")):
                                Yes += 1
                            else:
                                No += 1
                                wrong_list.append(
                                    [i, English_to_Chinese_dictionary[i]])
                        os.system('cls')
                        print("Your English task is complete!")
                        print(f"the task which you chose: {key}\n")
                        print("you got {} coorect and {} wrong\n".format(Yes, No))
                        if len(wrong_list) > 0:
                            print(
                                "the word that you're wrong\n" + '-'*60)
                            for val in wrong_list:
                                print('{:<20} {:<20}'.format(val[0], val[1]))
                        os.system('pause')
                        continue
                    elif select == 2:
                        pass
                    elif select == 3:
                        print("loading...")
                        time.sleep(0.3)
                        os.system('cls')
                        break
            elif choose == 2:
                print('正在關閉系統...')
                time.sleep(1.0)
                os.system('cls')
                break
