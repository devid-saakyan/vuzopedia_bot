from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
import os


def get_vuzi(url):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
    driver.get(url)
    sleep(2)
    univers = []
    ssilkis = []
    infos = []
    scores = []
    index = []
    naprs = []
    for i in driver.find_elements(By.CLASS_NAME, 'linknap'):
        driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((i))))
    sleep(3)
    for i in driver.find_elements(By.CLASS_NAME, 'itemVuzTitle'):
        univers.append(i.text)
    al = driver.find_elements(By.CLASS_NAME, 'vuzesfullnorm')
    for i in al:
        ssilkis.append(i.find_element(By.TAG_NAME, 'a').get_attribute('href'))
    al = driver.find_elements(By.CLASS_NAME, 'itemSpecAll')
    for j in al:
        for i in j.find_elements(By.CLASS_NAME, 'itemSpecAllParamWHide'):
            try:
                scores.append(i.find_element(By.CLASS_NAME, 'tooltipq').text)
            except:
                scores.append('нет данных')
    scores = [("💰" + scores[i].replace(' \u20cf', '')+'руб. ',  str(scores[i+2])+' баллов') for i in range(0,len(scores)-2,3)]
    for i in al:
        infos.append(i.find_element(By.CLASS_NAME, 'spectittle').text)

    for i in range(len(infos)):
        if infos[i] not in naprs:
            index.append(i)
            naprs.append(infos[i])
    print(index)
    infos_b = [i for i in set(infos)]
    infos_p = [str(infos[i]) + " " + str(scores[i]) for i in index]
    for i in infos_p:
        print(i)
    driver.quit()
    return univers, ssilkis, infos_b, infos_p
