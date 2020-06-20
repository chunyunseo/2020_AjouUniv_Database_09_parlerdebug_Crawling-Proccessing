import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

def save_file(location_high, location_mid, location_low, name, desc, spec, creature_tool):
    f = open("log.txt", 'a', -1, "utf-8")
    f.write(location_high + '\t' + location_mid + '\t' + location_low + '\t' + name + '\t' + desc + '\t' + spec + '\t' + creature_tool + '\n')
    f.close()
    print(location_high + '\t' + location_mid + '\t' + location_low + '\t' + name + '\t' + desc + '\t' + spec + '\t' + creature_tool + '\n')

def delete_spliter(original_string):
    return original_string.replace('\n', ' ').replace('\t', ' ')



options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument('disable-gpu')

file_dir = r"C:\Users\MCOM\AppData\Local\Programs\Python\chromedriver.exe"
driver = webdriver.Chrome(file_dir, options=options)



driver.implicitly_wait(20)
driver.get("https://species.nibr.go.kr/geo/html/index.do?ktsn=120000017791")
dosi = driver.find_element_by_xpath('//*[@id="snb"]/div[1]/div[1]/ol').find_elements_by_tag_name("li")
time.sleep(1)
count = 0;

my_btn_sido = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[1]/div[1]/ul/li[1]/a')
my_btn_sigun = driver.find_element_by_xpath('//*[@id="btnSigungu"]')
my_btn_dong = driver.find_element_by_xpath('//*[@id="btnDong"]')

sido_list = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/ol').find_elements_by_tag_name('li')
sido_list = sido_list[10:]
my_btn_sido.click()
for sido in sido_list:
    sido = sido.find_element_by_tag_name('a')
    sido.click()
    creature_loc_big = sido.get_attribute("textContent")
    print(creature_loc_big)
    time.sleep(1)
    sigun_list = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/ol').find_elements_by_tag_name('li')
    for sigun in sigun_list:
        sigun = sigun.find_element_by_tag_name('a')
        creature_loc_mid = sigun.get_attribute("textContent")
        print(creature_loc_mid)
        sigun.click()
        time.sleep(1)
        dong_list = driver.find_element_by_xpath('//*[@id="snb"]/div[1]/div[3]/ol').find_elements_by_tag_name('li')
        try:
            for dong in dong_list:
                dong = dong.find_element_by_tag_name('a')
                creature_loc_low = dong.get_attribute("textContent")
                dong.click()
                time.sleep(1)
                driver.find_element_by_xpath('//*[@id="snb"]/div[2]').click() #검색 버튼 클릭
                time.sleep(1)
                #여기서 뭔가 동작을 수행
                creature_list = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[3]/div[2]/div[1]/ul').find_elements_by_tag_name('li')
                for creature_spec in creature_list:
                    creature_tool = creature_spec.find_element_by_tag_name('table').find_element_by_tag_name('tbody').find_elements_by_tag_name('tr')[1].find_element_by_tag_name('td').get_attribute('textContent')
                    creature_tool = delete_spliter(creature_tool)
                    creature_spec = creature_spec.find_element_by_tag_name('p').find_element_by_tag_name('span').find_element_by_tag_name('a')
                    creature_spec.click()

                    # 여기서 상세페이지로 들어감
                    try:
                        tabs = driver.window_handles
                        driver.switch_to.window(tabs[-1])
                        time.sleep(1)
                        driver.switch_to.frame('gwpMain')
                        creature_name = delete_spliter(driver.find_element_by_xpath('/html/body/div/div[1]/div/div/div[1]/div[2]/p').get_attribute('textContent'))
                        creature_spec = delete_spliter(driver.find_element_by_xpath('//*[@id="contents"]/div[1]/div[2]/table/tbody/tr[1]/td').get_attribute("textContent"))
                        creature_desc = delete_spliter(driver.find_element_by_xpath('//*[@id="divTabDetail"]/div[1]/div[1]/div[1]/p[2]').get_attribute("textContent"))
                        save_file(creature_loc_big, creature_loc_mid, creature_loc_low, creature_name, creature_desc, creature_spec, creature_tool)
                        count = count + 1
                        print(count)
                        #여기서 상세페이지 닫힘.
                    except:
                        print("상세 페이지 에러 발생")
                    finally:
                        driver.switch_to.default_content()
                        driver.close()
                        driver.switch_to.window(tabs[0])
                        time.sleep(2)
                my_btn_dong.click()
            my_btn_sigun.click()
        except:
            print("에러발생")
            my_btn_sigun.click()
my_btn_sido.click()








