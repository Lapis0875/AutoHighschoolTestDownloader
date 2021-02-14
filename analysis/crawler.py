import json
from typing import List, Optional
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
import re


URL_PATTERN: re.Pattern = re.compile(r'(https?:\/\/\w+)?(.\w+)*(\/\w+)+\.(\w)+')


def extractUrlParamFromJSFunction(js_func: str) -> Optional[str]:
    print(f'js_func = {js_func}')
    url_match: Optional[re.Match] = URL_PATTERN.search(js_func)
    print(url_match)
    print(url_match.group())
    return url_match.group() if url_match is not None else None


options = Options()
# options.add_argument('--headless')
driver = Chrome('./chromedriver.exe', options=options)
driver.implicitly_wait(3)

driver.get('http://www.ebsi.co.kr/ebs/xip/xipc/previousPaperList.ebs')

data = {}


# 1 ~ n  페이지
pages = 20
ignored_exceptions = (NoSuchElementException, StaleElementReferenceException,)
for num in range(1, pages+1):
    print(f'Crawling page {num}\n')
    # tbody 태그 가져오기
    # tbody = driver.find_element_by_class_name('boardtest').find_element_by_tag_name('tbody')
    tbody = WebDriverWait(driver, 10, ignored_exceptions=ignored_exceptions) \
        .until(lambda driver: driver.find_element_by_class_name('boardtest').find_element_by_tag_name('tbody'))
    # tr 태그 가져오기
    # Prevent stale element reference.
    # elements = tbody.find_elements_by_tag_name('tr')
    elements: List[WebElement] = WebDriverWait(driver, 10, ignored_exceptions=ignored_exceptions) \
        .until(lambda driver: driver.find_elements_by_tag_name('tr'))
    for element in elements[1:]:
        print(f'Parsing WebElement : {element.tag_name}, {element.location}')

        # 시험 이름 가져와서 처리하기
        tInfoTag: WebElement = element.find_element_by_class_name('t_info')
        testTitleRaw: str = tInfoTag.find_element_by_tag_name('strong').text
        testTitle: str = testTitleRaw.strip()
        if testTitle.endswith('형'):
            subjectName, subjectType = testTitle.split(' ')[-2:]
        else:
            subjectName = testTitle.split(' ')[-1]
            subjectType = None
        print(f'Crawling test : test={testTitle},subject={subjectName},type={subjectType}')
        testData: dict = {
            'title': testTitle,
            'type': subjectType if subjectType is not None else '없음',
            'download': {}
        }

        # 다운로드 링크 및 코드 가져오기
        downTag: WebElement = element.find_element_by_class_name('down')
        downloads: List[WebElement] = downTag.find_element_by_tag_name('span').find_elements_by_tag_name('a')
        for download in downloads:
            href = download.get_attribute('href')
            print(f'{download.text} > href={href}')
            # functionInfo = parseJSFunc(href)
            # print(f'Parsed {download.text} href : {functionInfo}')
            # testData['download'][download.text] = {
            #     'url': functionInfo['arg'].split(',')[0],
            #     'function_info': functionInfo
            # }
            testData['download'][download.text] = {
                'href': href,
                'comment': 'due to catastrophic backtracking issue, javascript function-call expression parsing with regexp temporarily stopped.'
            }

        try:
            data[subjectName].append(testData)
        except KeyError:
            data[subjectName] = [testData]
        print('-'*10)
    print('='*10)

    # 다음 페이지 넘기기
    if num != pages:    # 실행하는 마지막 페이지가 아닐 때
        if pages % 10 == 0: # 10 배수
            tuple(filter(
                lambda e: e.get_attribute('onclick') == f'goPage({num+1});',
                driver.find_element_by_class_name('mT15').find_elements_by_tag_name('a')
            ))[0].click()
        else:
            tuple(filter(
                lambda e: e.text == str(num+1),
                driver.find_element_by_class_name('vA-1')
                    .find_elements_by_tag_name('a')
            ))[0].click()

with open('raw_data.json', mode='wt', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
