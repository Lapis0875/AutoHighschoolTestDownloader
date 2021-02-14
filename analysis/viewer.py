import json

with open('data.json', mode='rt', encoding='utf-8') as f:
    data = json.load(f)


def viewer() -> int:
    subject_name = input("과목명 입력 > ")
    subject_data = data[subject_name]



def main():
    while True:
        if doClose := True if viewer() != 0 else False: break
