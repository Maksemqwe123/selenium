from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
# import numpy
from PIL import Image
import pytesseract
from pytesseract import image_to_string
# import easyocr
import io

user_agents_list = [
    "best_of_the_best",
    "redfox",
    "Rejaf"
]



url = "https://www.avito.ru/all/avtomobili/novyy-ASgBAgICAUSGFMbmAQ?cd=1&user=2"

options = webdriver.ChromeOptions()
options.add_argument(f"user-agent={random.choice(user_agents_list)}:")
options.add_argument('chrome')  # Use headless if you do not need a browser UI
options.add_argument('--start-maximized')
options.add_argument('--window-size=1650,900')

driver = webdriver.Chrome(
    executable_path='C:/new life/new_life_pro/chromedriver.exe.dat',
    options=options
)

#
# find_by = {
#     'css': By.CSS_SELECTOR,
#     'xpath': By.XPATH,
#     'class_name': By.CLASS_NAME,
#     'id': By.ID,
#     'link_text': By.LINK_TEXT,
#     'name': By.NAME,
#     'partial_link_text': By.PARTIAL_LINK_TEXT,
#     'tag_name': By.TAG_NAME
# }
try:
    driver.get(url=url)
    # print(driver.window_handles)
    print(f'{driver.current_url}')
    time.sleep(5)
    # phone_number = driver.find_elements_by_class_name("iva-item-content-rejJg")
    # phone_number.send_keys('54636473')

    advertisement = driver.find_elements(By.CLASS_NAME, 'iva-item-sliderLink-uLz1v')
    advertisement[0].click()
    time.sleep(10)

    driver.switch_to.window(driver.window_handles[1])
    time.sleep(5)
    print(f'{driver.current_url}')

    phone = driver.find_element(By.CSS_SELECTOR, "div.style-item-view-actions-_MOv2").find_element(By.CSS_SELECTOR, 'div.contact-bar-wrapper-WfX0a')
    phone.click()
    time.sleep(5)
    driver.save_screenshot('avito_screenshot.png')
    time.sleep(5)


    image = driver.find_element(By.CSS_SELECTOR, 'div.item-popup-itemPhone__img-UxE8p')

    location = image.location
    size = image.size

    image = Image.open('avito_screenshot.png')
    x = location['x']
    y = location['y']
    width = size['width']
    height = size['height']

    image.crop((x, y, x+width, y + height)).save('tel.gif')

    pytesseract.pytesseract.tesseract_cmd(r"C:\Program Files\Tesseract-OCR\tesseract.exe")
    text = pytesseract.image_to_string(Image.open('tel.gif'))
    print(type(text))
    # reader = easyocr.Reader(['ru'])
    # file_path = 'tel.gif'
    # result = reader.readtext(file_path, detail=0)
    # print(file_path)


        ###Отправить реквест запрос при помощи бс4 чтобы перебрать станицы через фор

        # phone_close = driver.find_element(By.CSS_SELECTOR, 'div.popup-overlay-zm_UF')
        # phone_close(5)
        # print(f'{phone_close}')



        # phone_number = driver.find_element(By.CSS_SELECTOR, 'div.phone-button-root-QDB8q')
        # time.sleep(5)
        # print(f'{phone_number.text}')

        # driver.switch_to.window(driver.window_handles[2])
        # time.sleep(5)
        # print(f'{driver.current_url}')
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()

