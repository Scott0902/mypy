import time
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
prefs = {"": ""}
prefs["credentials_enable_service"] = False
prefs["profile.password_manager_enabled"] = False
options.add_experimental_option("prefs", prefs) ##关掉密码弹窗
options.add_argument('–-disable-gpu') # 谷歌文档提到需要加上这个属性来规避bug
options.add_argument('lang=zh_CN.UTF-8') # 设置默认编码为utf-8
options.add_argument("--disable-extensions")
options.add_experimental_option('useAutomationExtension', False) # 取消chrome受自动控制提示
options.add_experimental_option('excludeSwitches', ['enable-automation']) # 取消chrome受自动控制提示
driver = webdriver.Chrome(options=options)
driver.execute_cdp_cmd("Network.setExtraHTTPHeaders",
                       {"headers":
                        {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                        'Accept-Encoding': 'gzip, deflate',
                        'Accept-Language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8,en;q=0.7',
                        'Connection': 'keep-alive',
                        }
                       })
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": """
            Object.defineProperty(navigator, 'webdriver', {
                get: () => False
            })
        """})
#driver.get('https://cnc.xitek.com/member.php?mod=logging&action=login&referer=http://forum.xitek.com/')
driver.get('https://forum.xitek.com/index/logging')
driver.find_element(By.NAME,'username').send_keys('Scott0902')
driver.find_element(By.NAME,'password').send_keys('akashi0902')
driver.find_element(By.CLASS_NAME,'btn-primary').click()
time.sleep(3)
driver.get('https://cnc.xitek.com/checkin.php')
driver.find_element(By.XPATH,'//*[@id="messagetext"]/p').text
time.sleep(3)
driver.quit()

