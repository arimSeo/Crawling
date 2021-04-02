from selenium import webdriver
import time

driver = webdriver.Chrome(r"C:\Users\USER\Desktop\네이버지도\chromedriver.exe")
driver.get("https://v4.map.naver.com/")

#처음에 뜨는 팝업창 닫는 코드
driver.find_elements_by_css_selector("button.btn_close")[1].click()

#검색창에 부산대 맛집 기입
search_box = driver.find_element_by_css_selector("input#search-input")
search_box.send_keys("부산대 맛집")

#검색창 바로가기 버튼 클릭
search_button = driver.find_element_by_css_selector("button.spm")
search_button.click()

page = 0
data = []

while True:
    page = page + 1
    html = driver.page_source
    stores = driver.find_elements_by_css_selector("div.lsnx")


    for store in stores:
    # 세부 데이터 수집
        name = store.find_element_by_css_selector("dt > a").text
        addr = store.find_element_by_css_selector("dd.addr").text
        try:
            if store.find_element_by_css_selector("dd.tel").text:
                phone = store.find_element_by_css_selector("dd.tel").text
        except: phone="NULL"
        data.append([name, addr, phone])

        # print(name, addr, phone)

    print(data)
    index = page % 5 + 1

    if index == 1:
        index = 6

    try:
        driver.find_element_by_class_name('paginate').find_elements_by_css_selector('*')[index].click()
        time.sleep(60)
    except: break

    
import pandas as pd
res_data = pd.DataFrame(data)
res_data.columns = ['name', 'addr', 'phone']
res_data.to_excel('pnu.xlsx')