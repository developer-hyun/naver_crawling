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
  #  url = "https://smartstore.naver.com/deproject/products/672496361?"       #디프로젝트 디불      #입력받은 URL을 저장하는 함수.
    #url = "https://smartstore.naver.com/siestern/products/5319139287?"         #스턴미키
    #url = "https://shopping.naver.com/play/play/stores/100566881/products/4736711991"  #에이비방향제 #사이트가다름
    #url = "https://smartstore.naver.com/store-ab/products/5214229210?"  #에이비방향제 도베르만 메탈타입
   # url = "https://smartstore.naver.com/l-kshop/products/5205442576?" #쓰리나인방향제
    #url = "https://smartstore.naver.com/scentmonster/products/5108811877?" #센트몬스터방향제
    url = "https://smartstore.naver.com/gti/products/4748622246"  #밴볼릭 방향제


    Se = Service('C:/Users/rlckd/PycharmProjects/colling/chromedriver.exe')
    binary = "chromedriver.exe"       #크롬창을 키기위해 이것 필요.

    driver =webdriver.Chrome(service=Se)    #크롬 시작페이지 띄우기
    driver.get(url)                 #url을 쳐서 띄우기
    driver.implicitly_wait(10)      #창이 켜질때까지 기다리는 함수

    excel_file = openpyxl.Workbook()  # 엑셀로 저장을 위해 쓰는 엑셀 관련 함수들.
    excel_sheet = excel_file.active
    excel_sheet.append(['score', 'message', 'date', 'option_one', 'option_two', 'option_three'])  # 매장마다 바뀜
    excel_sheet.column_dimensions['B'].width = 100
    time.sleep(1)
    driver.find_element(By.XPATH,"/html/body/div/div/div[3]/div[2]/div[2]/div/div[3]/div[3]/ul/li[2]/a").click()
    time.sleep(1)


    #평점 낮은순 클릭
    #print(driver.find_element_by_xpath("/html/body/div/div/div[3]/div[2]/div[2]/div/div[3]/div[6]/div/div[3]/div/div[1]/div[1]/ul/li[4]/a").text)
    #driver.find_element(By.XPATH,"/html/body/div/div/div[3]/div[2]/div[2]/div/div[3]/div[6]/div/div[3]/div/div[1]/div[1]/ul/li[4]/a").click()
    #

    #평점높은순 클릭
    driver.find_element(By.XPATH,"//*[@id='REVIEW']/div/div[3]/div/div[1]/div[1]/ul/li[3]").click()
    driver.implicitly_wait(10)

    driver.find_element()
    #driver.fiond_em




if __name__ == '__main__':
    crilling()