from typing import List, Tuple, Optional
import json
import re
import bs4


URL_PATTERN: re.Pattern = re.compile(r'(https?:\/\/\w+)?(.\w+)*(\/\w+)+\.(\w)+')
print(f'url pattern = {URL_PATTERN!r}\n')


def extractUrlParamFromJSFunction(js_func: str) -> Optional[str]:
    print(f'js_func = {js_func}')
    url_match: Optional[re.Match] = URL_PATTERN.search(js_func)
    print(url_match)
    print(url_match.group())
    return url_match.group() if url_match is not None else None


def parseUrlCode(tag: bs4.element.Tag) -> Tuple[str, str]:
    url = extractUrlParamFromJSFunction(tag['href'])
    print(f'url : {url}')
    code = url.split('/')[-1].split('.')[0]   # http://wdown.ebsi.co.kr/W61001/01exam/20190410/go3/kor_mun_FRaqbC8w.pdf -> kor_mun_FRaqbC8w
    return url, code


with open('EBS_기출문제다운로드_2020전체_1페이지.html', mode='rt', encoding='euc-kr') as html_f:
    soup = bs4.BeautifulSoup(html_f, 'html.parser')

data = {}

table = soup.find('body')\
    .find('div', {'id': 'wrap'})\
    .find('div', {'id': 'reNcontainer'})\
    .find('div', {'id': 'reNcontainer_in'})\
    .find('div', {'id': 'reNcontents'})\
    .find('div', {'id': 'lmsWrap'})\
    .find('div', {'class': 'newLecture'})\
    .find('div', {'id': 'apply'})\
    .find('div', {'id': 'wrap'})\
    .find('div', {'class': 'container'})\
    .find('div', {'class': 'midarea'})\
    .find('div', {'class': 'contentarea'})\
    .find('div', {'class': 'hiddencontents tab_01 on'})\
    .find('form', {'id': 'paperListFrm'})\
    .find('div', {'class': 'samplewrap'})\
    .find('div', {'class': 'q_testbox'})\
    .find('div', {'id': 'div_contentList'})\
    .find('table', {'class': 'boardtest'})
subject_objects: List[bs4.element.Tag] = table.find('tbody').find_all('tr')[1:]

print('Start parsing subject test objects...\n')

for subject in subject_objects:
    test_name = subject.find('td', {'class': 't_info'}).find('strong').string
    print(f'Parsing test : raw_name="{test_name}"')
    test_name = test_name.strip()
    print(f'Parsing test : name="{test_name}"')
    if test_name.endswith('형'):
        test_subject, test_type = test_name.split(' ')[-2:]     # 2020년 2021 대학수학능력시험 국어 홀수형 -> [국어, 홀수형]
    else:
        test_subject = test_name.split(' ')[-1]
        test_type = '없음'
    print(f'Parsed test info : subject="{test_subject}",type="{test_type}"')
    downloads: List[bs4.element.Tag] = subject.find('td', {'class': 'down'}).find('span').find_all('a')
    test_download = downloads[0]
    test_url, test_code = parseUrlCode(test_download)
    answer_download = downloads[1]
    answer_url, answer_code = parseUrlCode(answer_download)
    solution_download = downloads[2]
    solution_url, solution_code = parseUrlCode(solution_download)

    parsed_data = {
            '시험': test_name,
            '유형': test_type,
            '다운로드': {
                '문제': {
                    'url': test_url,
                    'code': test_code
                },
                '정답': {
                    'url': answer_url,
                    'code': answer_code
                },
                '해설지': {
                    'url': solution_url,
                    'code': solution_code
                }
            }
        }
    try:
        data[test_subject].append(parsed_data)
    except:
        data[test_subject] = [parsed_data]

with open('data.json', mode='wt', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
