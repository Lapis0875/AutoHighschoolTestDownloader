from selenium.webdriver import Chrome

driver = Chrome('./chromedriver.exe')
driver.implicitly_wait(3)

driver.get('http://www.ebsi.co.kr/ebs/xip/xipc/previousPaperList.ebs')

for num in range(1, 10+1):
    tbody = driver.find_element_by_xpath('/html/body/div/div[3]/div[3]/div[2]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/form/div/div[2]/div/table/tbody')
    elements = tbody.find_element_by_tag_name('tr')

