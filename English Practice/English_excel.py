import openpyxl
import json

workbook = openpyxl.load_workbook('English_dictionary.xlsx')

sheet = workbook['工作表1']
rows = sheet.rows

with open('English_data.json', 'r', encoding='utf-8') as f:
    English_Dictionary = json.load(f)

  
English_to_Chinese_dictionary = {}

i=1



for row in rows:
    case = []
    for column in row:
        case.append(column.value)
    english, chinese = case[0], case[1]

    English_to_Chinese_dictionary[english] = chinese

name = input("please enter the dictionary name: ")
English_Dictionary[name] = English_to_Chinese_dictionary
with open('English_data.json', 'w', encoding='utf8') as dataFile:
    json.dump(English_Dictionary, dataFile, ensure_ascii=False, indent=4)

