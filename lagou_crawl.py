#!/usr/bin/python
# -*- coding: utf-8 -*-
from selenium import webdriver
from lxml import etree


URL = 'https://www.lagou.com/jobs/list_Python?px=default&city=%E6%B7%B1%E5%9C%B3#filterBox'
driver = webdriver.Chrome('../Documents/chromedriver')
driver.get(URL)
el = driver.find_element_by_xpath('//div[@class="company_name"]/a[0]')
print(el)
