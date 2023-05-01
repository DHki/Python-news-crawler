from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# 웹 드라이버 설정
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # 브라우저 백그라운드 실행
options.add_argument('--disable-blink-features=AutomationControlled')
driver = webdriver.Chrome(options=options)

def main():
    
    tmp = [] # 새로 크롤링한 게시글들을 저장하는 리스트 #
    
    url = 'https://bizug.hanyang.ac.kr/-3'
    className = '.tables-board'
    path = '//*[@id="p_p_id_board_WAR_bbsportlet_"]/div/div/div/div[2]/table/tbody/tr/td/div[2]/div/p[1]/a'
    
    
    driver.get(url)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, className)))
    
    posts = driver.find_elements(By.XPATH, path)
    
    
    for post in posts:
        title = post.get_attribute('innerText').strip()
        tmp.append(title)
        
    
    print(tmp)

if __name__ == '__main__':
    main()