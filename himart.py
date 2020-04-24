from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import os
import time

# 하이마트에서 검색 상품의 제목들을 크롤링 하는 기능을 구현해 보았습니다.

path = os.getcwd() + "/chromedriver.exe"
driver = webdriver.Chrome(path)

try :
    driver.get("http://www.e-himart.co.kr/app/display/showDisplayShop?originReferrer=himartindex")
    time.sleep(1)

    searchIndex = "갤럭시" 
    element = driver.find_element_by_class_name("searchInput")
    element.send_keys(searchIndex)
    driver.find_element_by_class_name("btnSearch").click()

    for i in range(3) :
        time.sleep(1)

        html = driver.page_source
        bs = BeautifulSoup(html, "html.parser")

        conts = bs.find_all("a", class_ = "prdLink") 

        for c in conts :
            print(c.find("div", class_ = "prdInfo").find("p").text)
        
        driver.find_element_by_xpath('//*[@id="pageNavigator"]/a[2]').click()
        
finally :
    time.sleep(3)
    driver.quit()

