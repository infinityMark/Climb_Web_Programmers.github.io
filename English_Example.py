from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import os
import wget

PATH = 'E:/个人/Class_resource/chromedriver.exe'
driver = webdriver.Chrome(PATH)
driver.get("https://www.hkeaa.edu.hk/tc/hkdse/hkdse_subj.html?A1&1&2_25")

# years = driver.find_elements_by_class_name("tdodd")
test_decades = 23
for x in range(0,6):
    # years = driver.find_elements_by_class_name("tdodd")
    test_decades = test_decades - 1
    test_decades_word = str(test_decades)
    test_years = f"20{test_decades_word}年考試"
    each_year = driver.find_element_by_link_text(test_years)
    each_year.click()

    paper_arry = ["試卷二 (只提供英文版)", "試卷三 (只提供英文版)"]
    for i in range(0, 2):
        papers = driver.find_element_by_link_text(paper_arry[i])
        count = 0
        save_as = os.path.join(paper_arry[i] + '.pdf')
        # save_as_palce = os.path.join("ha")
        print(papers.get_attribute("href"))
        # download
        wget.download(papers.get_attribute("href"), save_as)
        # driver.quit()
    driver.back()
