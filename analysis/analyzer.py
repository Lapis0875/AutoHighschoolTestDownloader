import json
with open('data.json', mode='rt', encoding='utf-8') as f:
    data = json.load(f)


subject_name = input("과목명 입력 > ")
