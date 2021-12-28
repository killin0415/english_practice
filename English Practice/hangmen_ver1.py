import random
import os
import time
import json

with open('English_data.json', 'r', encoding='utf-8') as f:
        English_Dictionary = json.load(f)

def answer_library(key):#題庫
    answer_dict=English_Dictionary
    return answer_dict[key]
def display_hangmen(tries):#圖像輸出(目前別動
    hangmen=["""
            ------﹁
            |      
            |    
            |      
            |     
            |
           ---
            """,  
            """
            ------﹁
            |      O
            |    
            |      
            |     
            |
           ---
            """,    
            """   
            ------﹁
            |      O
            |      | 
            |      |
            |     
            |
           ---
            """,
            """    
            ------﹁
            |      O
            |    \\ | 
            |      |
            |     
            |
           ---
            """,
            """    
            ------﹁
            |      O
            |    \\ | /
            |      |
            |     
            |
           ---
            """,
            """    
            ------﹁
            |      O
            |    \\ | /
            |      |
            |     /
            |
           ---
            """,
            """    
            ------﹁
            |      O
            |    \\ | /
            |      |
            |     / \\
            |
           ---
            """  
    ]
    return hangmen[tries]
def play():#遊玩主程式
    global depend
    global Answer_list
    global answer

    Try=0
    answer_list=list(answer)
    answer_list[0]=0
    answer_list[-1]=0
    display_answer=[answer[0]]
    letter_list=[]
    
    for i in range(len(answer)-2):
        display_answer.append("_ ")
    display_answer.append(answer[-1])

    

    while Try<6:
        final_answer="".join(display_answer)

        if final_answer.isalpha() and final_answer==answer:
            os.system("cls")
            print("Congradulation,you have solved the qustion")
            print("the answer is " ,answer)
            os.system("pause")
            break

        os.system("cls")

        print("you have finished these word:{}".format(",".join(Answer_list)))
        print("your score is {}".format(score))

        if len(letter_list)>0:
            print("you have guessed these word:"+",".join(letter_list))

        print(display_hangmen(Try))
        print("".join(display_answer))

        respond=input("please input a letter or word: ")

        if respond.isalpha() and len(respond)==1:
            if respond not in answer_list:
                print(respond,"is not in word,please try it again")
                Try+=1
                letter_list.append(respond)
                print("\n")
                time.sleep(0.3)
                os.system("pause")
            
            else:
                while respond in answer_list:
                    display_answer[answer_list.index(respond)]=respond
                    answer_list[answer_list.index(respond)]=0
                print (respond.upper(),"is in the answer")
                letter_list.append(respond)
                print("\n")
                time.sleep(0.3)
                os.system("pause")

        elif respond.isalpha() and len(respond)==len(answer):
            if respond==answer:
                
                print("Congradulation,you have solved the qustion")
                print("the answer is " ,answer)
                os.system("pause")
                break

            else:
                print("you guess the wrong answer,plese try it again ")
                Try+=1
                time.sleep(0.3)
                os.system("pause")

        else:
            print("this input is not valid...please input again!")

    if Try==6:
        os.system("cls")
        print(display_hangmen(Try))        
        print("the hangmen is dead...I feel sorry about that,god bless you")
        print("the answer is " ,answer)
        
        depend=0
while True:
    score=0
    depend=1
    answer_copy=[0]
    Answer_list=["nothing"]
    os.system("cls")
    print("please enter the level that you want to play.")
    WORD_LIST = list(English_Dictionary.keys())
    WORDS = ""
    for i in range(len(WORD_LIST)):
        WORDS += "({}): ".format(i) + str(WORD_LIST[i])    
    choice=WORD_LIST[int(input(WORDS))]
    answer_copy=answer_library(choice)
    while True:
        os.system("cls")
        answer=random.choice(answer_copy)
        print(display_hangmen(0))
        print("_ "*len(answer))
        play()
        answer_copy.remove(answer)
        if depend==0:
            break
        else:
            score+=1
            if score==1:
                Answer_list[0]=answer
            else:
                Answer_list.append(answer)
                
        if len(answer_copy)==0:
            print("Congradulation!you have solved all the questions in this level")
            break

    print("your score is {}".format(score))
    os.system("pause")