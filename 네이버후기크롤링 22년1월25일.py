def crilling():
    #각종 필요한 모듈.
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.common.by import By
    from selenium import webdriver   #인터넷 키는 모듈
    from bs4 import BeautifulSoup
    import openpyxl     #엑셀 관련 모듈
    import time         #프로그램 중간에 쉬는것 모듄
    import math         #총 페이지 계산에 필요한 모듈


    file_name = "1월25일테스트본"      #입력받은 파일이름을 가져오는 함수
    url = "https://smartstore.naver.com/deproject/products/672496361?"             #입력받은 URL을 저장하는 함수.
    Se = Service('C:/Users/rlckd/PycharmProjects/colling/chromedriver.exe')
    binary = "chromedriver.exe"       #크롬창을 키기위해 이것 필요.

    driver =webdriver.Chrome(service=Se)    #크롬 시작페이지 띄우기
    driver.get(url)                 #url을 쳐서 띄우기
    driver.implicitly_wait(10)      #창이 켜질때까지 기다리는 함수


    #평점 낮은순 클릭
    #print(driver.find_element_by_xpath("/html/body/div/div/div[3]/div[2]/div[2]/div/div[3]/div[6]/div/div[3]/div/div[1]/div[1]/ul/li[4]/a").text)
    driver.find_element_by_xpath("/html/body/div/div/div[3]/div[2]/div[2]/div/div[3]/div[6]/div/div[3]/div/div[1]/div[1]/ul/li[4]/a").click()
    #
    driver.implicitly_wait(10)



    while (True):
         pass



    #Total_review_data = driver.find_elements_by_css_selector('#area_review_list > div.header_review._review_list_header > strong > span')
    driver.implicitly_wait(10)


if __name__ == '__main__':
    crilling()