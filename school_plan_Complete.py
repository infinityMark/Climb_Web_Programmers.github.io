from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import os
import re
import wget

# PATH = 'E:/个人/Class_resource/chromedriver.exe'
PATH = 'E:/个人/Class_resource/chromedriver-win64/chromedriver.exe'
driver = webdriver.Chrome(PATH)

imgs = driver.find_elements_by_class_name("not-loaded")
selection_link_a = '//*[@id="template"]/section/div[2]/p[5]/span/a'
selection_link_b = '//*[@id="template"]/section/div[2]/p[5]/span/a/span/img'

count = 0
img_loop = 0
count_number = 0
per_selection = 0
page = 2
in_in_img = 0
Link_Arry = []
# //*[@id="infinite_scroll"]/li[1]/a/img
# //*[@id="infinite_scroll"]/li[26]/a/img
page_where = 2
# total_Arry = ["http://www.hkwmacsl.edu.hk/it-school/php/webcms/public/mainpage/albumindex.php?refid=&page=46"]
total_Arry = ["http://www.hkwmacsl.edu.hk/it-school/php/webcms/public/mainpage/albumindex.php"]
false_Arry = []

for w in range(0,1):
    print(w)
    driver.get(total_Arry[0])
    ul = driver.find_element_by_class_name("page")
    total_pages = (int(len(ul.find_elements_by_tag_name("li")))-2)
    for i in range(0, total_pages):
        per_selection = 0
        for i in range(0, 16):
            selection_number = 0
            selection_number = selection_number + 1
            # selection_number_enter = driver.find_elements_by_xpath((f'//*[@id="columnsf"]/div[{selection_number}]/div/a/div[2]/span[2]'))
            selection_number_enter = driver.find_elements_by_class_name("count")
            # selection_number_enter = driver.find_elements_by_tag_name(f'//*[@id="columns"]/div[{i+1}]/div/a/div[2]/span[2]')
            # selection_number_enter_text = selection_number_enter.text
            selection_number_enter_text = int(selection_number_enter[i].text)
            print(selection_number_enter_text)
            if (selection_number_enter_text > 16):
                title_name = ""
                count = 0
                img_loop = 0
                img_place = driver.find_element_by_xpath(f'//*[@id="columns"]/div[{i+1}]/div/a/div[1]/img')
                title_name_tag = driver.find_element_by_xpath(f'//*[@id="columns"]/div[{i+1}]/div/a/div[2]/span[1]')
                title_name = title_name_tag.text
                img_place.click()
                here = len(driver.find_elements_by_class_name("not-loaded"))
                # time.sleep(5)
                # selection_number_enter_text_begin = selection_number_enter_text - 16

                for i in range(16, selection_number_enter_text):
                    img_loops = i + 1
                    counts = img_loops
                    driver.execute_script('window.scrollBy(0,1000)')
                    WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, f'//*[@id="infinite_scroll"]/li[{img_loops}]/a/img')))
                    # // *[ @ id = "infinite_scroll"] / li[16] / a / img
                    # // *[ @ id = "infinite_scroll"] / li[17] / a / img
                    ture_img = driver.find_element_by_xpath(f'//*[@id="infinite_scroll"]/li[{img_loops}]/a/img')
                    save_as = os.path.join(title_name + str(counts) + '.jpg')
                    save_as = re.sub(r'[\\/*?:"<>|]', "", save_as)
                    # save_as_palce = os.path.join("ha")
                    print(save_as)
                    # download
                    try:
                        # print("Down")
                        wget.download(ture_img.get_attribute("src"), save_as)
                    except FileNotFoundError:
                        # driver.back()
                        false_Arry.append(driver.current_url)
                        break
                driver.back()
                print(false_Arry)
        page_where = page_where + 1
        img_pages = driver.find_element_by_xpath(f'//*[@id="gallery"]/div/div/div[1]/section/ul/li[{page_where}]/a')
        img_pages.click()
        print(false_Arry)