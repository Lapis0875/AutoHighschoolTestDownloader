from typing import List

from selenium.webdriver import Chrome
from selenium.webdriver.remote.webelement import WebElement

driver = Chrome('./chromedriver.exe')
driver.implicitly_wait(3)

driver.get('http://www.ebsi.co.kr/ebs/xip/xipc/previousPaperList.ebs')


# 1 ~ 10  페이지
for num in range(1, 1+1):
    # tbody 태그 가져오기
    tbody = driver.find_element_by_class_name('boardtest').find_element_by_tag_name('tbody')
    # tr 태그 가져오기
    elements: List[WebElement] = tbody.find_elements_by_tag_name('tr')
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
        
        # 다운로드 링크 및 코드 가져오기
        downTag: WebElement = element.find_element_by_class_name('down')
        downloads: List[WebElement] = downTag.find_element_by_tag_name('span').find_elements_by_tag_name('a')

        problemLink = downloads[0].get_attribute('href')
        print(f'Problem link : {problemLink}')
        answerLink = downloads[1].get_attribute('href')
        print(f'Answer link : {answerLink}')
        solutionLink = downloads[2].get_attribute('href')
        print(f'Solution link : {solutionLink}')


