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

    time.sleep(1)
    # 아까 계산한 총 페이지를 컴퓨터가 숫자로 인식할 수 있게 변환
    for num in Total_review_data:
        Total_review_data_text += num.text
        Total_review_data_text = Total_review_data_text.replace(',', '')
    Page_num = math.floor(int(Total_review_data_text) / 20)
    print(Page_num)
    count = Page_num
    # fp = open("gyui.txt",'w',-1,'utf-8')
    set_number = 11
    al = 0
    # 오류가 발생했을 경우에 무슨 오류인지 알기 위하여 try - except 함수 사용
    try:
        for page in range(2, Page_num + 2):  # 총 페이지 숫자까지 for문으로 돔.
            driver.implicitly_wait(10)

    for page in range(3, 35):
        time.sleep(1)
        review_data = driver.find_elements(By.XPATH,
                                           '/html/body/div/div/div[3]/div[2]/div[2]/div/div[3]/div[6]/div/div[3]/div/div[2]/ul/li/div/div[1]/div/div[1]/div/div/div[2]/div')  # 리뷰 텍스트 내용 선택
        driver.implicitly_wait(20)
        revier_star = driver.find_elements(By.XPATH,
                                           '/html/body/div/div/div[3]/div[2]/div[2]/div/div[3]/div[6]/div/div[3]/div/div[2]/ul/li/div/div[1]/div/div[1]/div/div/div[1]/div[2]/div[1]/em')  # 평점이 몇점인지 선택ㄱ
        review_date = driver.find_elements(By.XPATH,

                                           # 총 페이지 계산을 위해 사용
                                           Total_review_data=driver.find_elements_by_css_selector(
                                               '#area_review_list > div.header_review._review_list_header > strong > span')
        driver.implicitly_wait(10)
        Total_review_data_text = ""
        time.sleep(1)
        if selected.get() == 0:  # 최신순을 클릭하였을때
            driver.find_element_by_xpath('//*[@id="area_review_list"]/div[1]/ul/li[2]/a').click()
        if selected.get() == 1:  # 평점 높은순을 클릭하였을때
            driver.find_element_by_xpath('//*[@id="area_review_list"]/div[1]/ul/li[3]/a').click()
        else:  # 평점 낮은 순을 클릭 하였을 떄
            driver.find_element_by_xpath('//*[@id="area_review_list"]/div[1]/ul/li[2]/a').click()

        # cur.execute("CREATE TABLE students (id integer primary key autoincrement, score, message)")

        # driver.find_element_by_xpath('//*[@id="area_review_list"]/div[1]/ul/li[3]/a').click()  #평점 높은순
        # driver.find_element_by_xpath('//*[@id="area_review_list"]/div[1]/ul/li[4]/a').click() #평점 낮은 순 클릭.
        # driver.find_element_by_xpath('//*[@id="area_review_list"]/div[1]/ul/li[2]/a').click() #최신순 클릭.
        time.sleep(1)
        # 아까 계산한 총 페이지를 컴퓨터가 숫자로 인식할 수 있게 변환
        for num in Total_review_data:
            Total_review_data_text += num.text
        Total_review_data_text = Total_review_data_text.replace(',', '')
        Page_num = math.floor(int(Total_review_data_text) / 20)
        print(Page_num)
        count = Page_num
        # fp = open("gyui.txt",'w',-1,'


if __name__ == '__main__':
    crilling()