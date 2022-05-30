import random
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("C:\Program Files\Webdrivers\chromedriver_win32\chromedriver.exe")
#driver = webdriver.Chrome('./chromedriver.exe')

driver.get('https://fincaraiz.com.co/apartamentos/arriendos?ubicacion=Bochalema&pagina=')

#APT_LINKS= driver.find_elements_by_xpath('//div/article/a/@href')

#APTS = driver.find_elements_by_class_name('MuiGrid-root MuiGrid-item MuiGrid-grid-xs-12 MuiGrid-grid-sm-6 MuiGrid-grid-lg-4 MuiGrid-grid-xl-4')
#APTS= driver.find_elements_by_xpath('//article[@class="MuiGrid-root MuiGrid-item MuiGrid-grid-xs-12 MuiGrid-grid-sm-6 MuiGrid-grid-lg-4 MuiGrid-grid-xl-4"]')
APTS=driver.find_elements(By.CLASS_NAME, value="MuiGrid-root MuiGrid-item MuiGrid-grid-xs-12 MuiGrid-grid-sm-6 MuiGrid-grid-lg-4 MuiGrid-grid-xl-4")


with open(f'fincaraiz.txt', 'w', encoding='utf-8') as f:
    for apt in APTS:
        price = apt.find_element_by_xpath('.//span[@class="MuiTypography-root jss352 MuiTypography-body1"]/b').text # Verificado: oki
        print(price)
        
        room = apt.find_element_by_xpath('.//div/span[3]').text # Verificado: okiiii
        print(room)

        f.write(price)
        f.write('\n\n')
        f.write(room)

for apt in APTS:
    price = apt.find_element_by_xpath('.//span[@class="MuiTypography-root jss352 MuiTypography-body1"]/b').text # Verificado: oki
    print(price)
        
    room = apt.find_element_by_xpath('.//div/span[3]').text # Verificado: okiiii
    print(room)