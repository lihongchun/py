#! /usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
options.add_argument("--start-maximized")
driver = webdriver.Chrome(chrome_options=options)
driver.get("https://www.baidu.com/")
print driver.title
driver.find_element_by_id('kw').send_keys("123")
driver.find_element_by_id('su').click()
