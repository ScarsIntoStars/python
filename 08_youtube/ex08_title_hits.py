from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def scroll_fun():
    while True:
        h2 = driver.execute_script("return document.documentElement.scrollHeight")
        driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight)")
        time.sleep(3)
        last = driver.execute_script("return document.documentElement.scrollHeight")
        if h2==last:
            break


# 크롬 브라우저 실행
driver = webdriver.Chrome()

# 접속할 주소
# driver.get("https://www.youtube.com/")
# 인기 금상승 페이지 접속
driver.get("https://www.youtube.com/feed/trending/")


# 검색창 접근
# search_element = driver.find_element(By.CSS_SELECTOR, 'input#search')

# # 검색어 입력
# search_element.send_keys("르세라핌")


# 검색버튼 클릭
# search_click = driver.find_element(By.CSS_SELECTOR, 'button#search-icon-legacy')
# search_click.click()

# # 엔터치기
# search_element.send_keys(Keys.RETURN)
time.sleep(5)

# 제목 가져오기
title_list = []
# 제목 저장을 위한 리스트
hits_list = []
# 조회수 저장을 위한 리스트
scroll_fun()
titles = driver.find_elements(By.XPATH, '//*[@id="video-title"]')
for title in titles:
    if title.get_attribute("aria-label"): # shorts 영상을 걸러내기 위한 조건문         
        # aria-label 속성값 가져오기
        aria_label = title.get_attribute("aria-label")
        # 조회수 값만 출력하기
        start_index = aria_label.rfind("조회수")+4
        end_index = aria_label.rfind("회")
        hits = aria_label[start_index:end_index]
        hits = int(hits.replace(",",""))
      
        title_list.append(title.text)
        hits_list.append(hits)
    
# 제목, 조회수 리스트 함께 조회
for title, hit in zip(title_list, hits_list):
    print(title, hit)