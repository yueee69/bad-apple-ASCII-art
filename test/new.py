from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

# 创建 WebDriver 实例
driver = webdriver.Chrome()

# 打开网页
driver.get("https://www.junyiacademy.org/exam/227105cfb60542b7a7292db0a81c6873")

# 等待元素可点击
button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "watch-report-directly-input-small-screen")))

# 如果按钮可点击，则点击
if button:
    print("按钮可以点击")
    button.click()

# 关闭 WebDriver 实例
driver.quit()
