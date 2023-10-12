from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select
import time

async def shoki_app(source_language_value,desire_language_value,transcript_or_summary_xpath,video_url):
    try:
        max_timeout = 180

        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        driver = webdriver.Chrome(options=options)

        driver.get("https://shoki.app")
        # try:
        time.sleep(3)
        input_text = driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[2]/div[2]/input')
        input_text.send_keys(video_url)
        source_language= driver.find_element(By.XPATH, "//select[@class='chakra-select css-g6la20'][1]")
        source_language_dropdown = Select(source_language)
        source_language_dropdown.select_by_value(source_language_value)
        desired_language = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[2]/div[3]/div[3]/select')
        # Click on the desired language dropdown to open it
        desired_language_dropdown = Select(desired_language)

        desired_language_dropdown.select_by_value(desire_language_value)
        driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[2]/div[4]/label[1]/span').click()
        time.sleep(3)
        driver.find_element(By.XPATH,transcript_or_summary_xpath).click()
        element = WebDriverWait(driver, max_timeout).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div[2]/div[5]/div/div/p[1]'))
        )
        p_elements = driver.find_elements(By.XPATH,'//*[@id="__next"]/div/div[2]/div[5]/div/div/p')
        all_p_text = "\n".join([element.text for element in p_elements])
        driver.quit()
        return all_p_text

    except Exception as e:
        driver.quit()
        return "Uzur videoni subtitle yo'qga o'xshaydi"


            # else:
            #     try:
            #         time.sleep(3)
            #         input_text = driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[2]/div[2]/input')
            #         input_text.send_keys(message.text)
            #
            #         source_language_dropdown = Select(source_language)
            #         source_language_dropdown.select_by_value('English')

            #         desired_language = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[2]/div[3]/div[3]/select')

            #         # Click on the desired language dropdown to open it
            #         desired_language_dropdown = Select(desired_language)

            #         # Now, select the option you want (e.g., "Spanish") by its value attribute
            #         desired_language_dropdown.select_by_value('English')

            #         driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[2]/div[4]/label[1]/span').click()

            #         time.sleep(3)

            #         driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[2]/div[4]/button[1]').click()

            #
            #         element = WebDriverWait(driver, max_timeout).until(
            #             EC.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/div/div[2]/div[5]/div/div/p[1]'))
            #         )
            #         p_elements = driver.find_elements(By.XPATH, '//*[@id="__next"]/div/div[2]/div[5]/div/div')

            #         # Extract text from all the <p> elements and concatenate them
            #         all_p_text = "\n".join([element.text for element in p_elements])


            #         driver.quit()

            #     except Exception as e:
            #         print(f"An error occurred: {str(e)}")
