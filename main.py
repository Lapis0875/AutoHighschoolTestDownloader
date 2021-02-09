from .models import AsyncDownloader, JSON


def start_prompt() -> str:
    print('''
    [ 기출문제 다운로더 ] [시작메뉴]
    version: 2021-02-09
    
    # 개발자의 사족
    기출문제를 보다 편리하게 다운받기 위해 제작한 다운로더입니다.
    ebs 에서 수능 기출문제를 다운받으려 했으나, 다운받기 매우 불편한 형태로 되어 있어 자동화하는 방향을 택했습니다.
    
    # 메뉴
    기출문제 다운로더의 동작 방식을 선택합니다.
    
    1. 모의고사 다운받기 : ebs 의 기출문제 페이지에서 기출문제를 다운받습니다.
    2. (추가 예정) : 아직 안만들어서 비어있습니다. 메뉴가 한개뿐이면 어색하니까 넣어뒀습니다.
    
    
    ''')
    answer: str = input('사용하시려는 기능의 번호를 입력해주세요. > ')
    return answer


def 모의고사_prompt() -> AsyncDownloader:
    print('''
    [ 기출문제 다운로더 ] [모의고사 다운로더]
    
    다운받으실 모의고사를 입력해주세요.
    4자리의 연도(YYYY), 두자리의 달(MM), 과목명 (Subject)를
    'YYYY-MM-Subject' 처럼 입력해주세요.
    ex) 2019년 3월 모의고사의 국어영역 -> 2019-03-국어
    
    여러개를 동시에 다운받으시려면, 콤마( , )로 구분해주세요. 띄어쓰기는 쓰지 않으셔도 됩니다.
    ex)2019-03-국어,2019-03-수학
    
    만약 json 문법을 다룰 수 있다면, json 파일명을 입력하시면 처리할 수 있습니다. (ex: 다운받을거.json)
    관련 포맷은 Github 저장소에 안내되어 있습니다. ()
    파일은 프로그램의 루트 경로에 위치해야 합니다. 이름은 자유롭게 쓰셔도 괜찮습니다. 파일 내용은 UTF-8로 인코딩되어야 합니다.
    ''')

    targets: str = input('입력 > ')
    if '.json' in targets:
        print('{} 파일을 읽고 있습니다...'.format(targets))
        import json
        with open(targets, mode='rt', encoding='utf-8') as f:
            target_json: JSON = json.load(f)
            return AsyncDownloader(target_json)


def main():
    mode: str = start_prompt()

