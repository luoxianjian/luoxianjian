# -*- coding: utf-8 -*-
# @Time : 2021/8/29 11:38 上午
# @AuthOr: xin.luo
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome(executable_path='./chromedriver 2')
driver.implicitly_wait(5)
driver.get('https://www.baidu.com/')
edit_input=driver.find_element_by_id('kw')
edit_input.send_keys('hello')
edit_input.click()
# 实例化类
action=ActionChains(driver)
#按下快捷键command
action.key_down(Keys.COMMAND)
# 点击c
action.send_keys('a')
#松开command
action.key_up(Keys.COMMAND)
#模拟command+c
action.key_down(Keys.COMMAND).send_keys('c').key_up(Keys.COMMAND)
#模拟command+v
action.key_down(Keys.COMMAND).send_keys('v').key_up(Keys.COMMAND)
action.key_down(Keys.COMMAND).send_keys('v').key_up(Keys.COMMAND)

#最后执行conform
action.perform()
