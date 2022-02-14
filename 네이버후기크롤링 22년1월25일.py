def crilling():
    #각종 필요한 모듈.
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.common.by import By
    from selenium import webdriver   #인터넷 키는 모듈
    from bs4 import BeautifulSoup
    import openpyxl     #엑셀 관련 모듈
    import time         #프로그램 중간에 쉬는것 모듄
    import math         #총 페이지 계산에 필요한 모듈
    # selenium으로 무엇인가 입력하기 위한 import
    from selenium.webdriver.common.keys import Keys


    file_name = "1월25일테스트본"      #입력받은 파일이름을 가져오는 함수
    url = "https://smartstore.naver.com/deproject/products/672496361?"             #입력받은 URL을 저장하는 함수.
    Se = Service('C:/Users/rlckd/PycharmProjects/colling/chromedriver.exe')
    binary = "chromedriver.exe"       #크롬창을 키기위해 이것 필요.

    driver =webdriver.Chrome(service=Se)    #크롬 시작페이지 띄우기
    driver.get(url)                 #url을 쳐서 띄우기
    driver.implicitly_wait(10)      #창이 켜질때까지 기다리는 함수

    excel_file = openpyxl.Workbook()  # 엑셀로 저장을 위해 쓰는 엑셀 관련 함수들.
    excel_sheet = excel_file.active
    excel_sheet.append(['score', 'message', 'date', 'option_one', 'option_two', 'option_three'])  # 매장마다 바뀜
    excel_sheet.column_dimensions['B'].width = 100
    #평점 낮은순 클릭
    #print(driver.find_element_by_xpath("/html/body/div/div/div[3]/div[2]/div[2]/div/div[3]/div[6]/div/div[3]/div/div[1]/div[1]/ul/li[4]/a").text)
    driver.find_element(By.XPATH,"//*[@id='REVIEW']/div/div[3]/div/div[1]/div[1]/ul/li[4]").click()
    #
    driver.implicitly_wait(10)



    for page in range(3,35):
        time.sleep(1)
        review_data = driver.find_elements(By.XPATH,
            '//*[@id="REVIEW"]/div/div[3]/div/div[2]/ul/li/div/div[1]/div/div[1]/div/div[1]/div[2]/div/span')  # 리뷰 텍스트 내용 선택
        driver.implicitly_wait(20)
        revier_star = driver.find_elements(By.XPATH,
            '//*[@id="REVIEW"]/div/div[3]/div/div[2]/ul/li/div/div[1]/div/div[1]/div/div[1]/div[1]/div[2]/div[1]/em')  # 평점이 몇점인지 선택ㄱ
        review_date = driver.find_elements(By.XPATH,
            '//*[@id="REVIEW"]/div/div[3]/div/div[2]/ul/li/div/div[1]/div/div[1]/div/div[1]/div[1]/div[2]/div[2]/span')
        review_op_fu_total = driver.find_elements(By.XPATH,
            '//*[@id="REVIEW"]/div/div[3]/div/div[2]/ul/li/div/div[1]/div/div[1]/div/div[1]/div[1]/div[2]/div[3]/div/button/span')
        driver.implicitly_wait(20)

        for (j, k, l, s) in zip(revier_star, review_data, review_date,
                                review_op_fu_total):  # 리뷰 텍스트 내용이랑 평점 몇점인지 내용 을 for문으로 하나하나 씩 가져온다.
            l = l.text.replace('.', '')

            driver.implicitly_wait(20)
            excel_sheet.append([j.text, k.text + "\n", l, s.text])  # 엑셀에다가 내용을 추가함.
            driver.implicitly_wait(20)

        if page<=12:
            pass
        if 13<=page<=22:
            page-=10
        if 23<=page<=32:
            page-=20
        if 33<=page<=42:
            page-=30
        print(page)
       # print(page)
       # print("/html/body/div/div/div[3]/div[2]/div[2]/div/div[3]/div[6]/div/div[3]/div/div[2]/div/div/a[%s]"%str(page))
        driver.find_elements(By.XPATH,"/html/body/div/div/div[3]/div[2]/div[2]/div/div[3]/div[6]/div/div[3]/div/div[2]/div/div/a[%s]"%str(page))[0].click()

        #driver.find_element(By.CSS_SELECTOR,"#REVIEW > div > div._2y6yIawL6t > div > div.cv6id6JEkg > div > div > a:nth-child(%s)"%str(page)).click()
        print("페이지")
        time.sleep(1)


    #
    #
    excel_file.save("{}.xlsx".format("테스트버전"))
    excel_file.close()
    time.sleep(1)
    time.sleep(1000)





    #Total_review_data = driver.find_elements_by_css_selector('#area_review_list > div.header_review._review_list_header > strong > span')
    driver.implicitly_wait(10)


if __name__ == '__main__':
    crilling()