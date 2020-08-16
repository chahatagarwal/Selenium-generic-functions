#!/usr/bin/python
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import ActionChains
from selenium.common.exceptions import UnexpectedAlertPresentException, StaleElementReferenceException
import sys
import os
import socket
from urllib.parse import urljoin
import time
import traceback
from selenium.webdriver.common.keys import Keys


class seleniumAuto():
    def __init__(self):
        #assign path of Chrome Selenium driver
        self.driver = webdriver.Chrome(executable_path=r'path_to_Chrome/chromedriver')

    # Back to previous page
    def goBack(self):
        self.driver.back()

    # refresh the page
    def refreshPage(self):
        self.driver.refresh()

    # Close the browser instance
    def closeBrowser(self):
        self.driver.close()

    # get the current page URL
    def getURL(self):
        url = self.driver.current_url
        return url

    # Switch to a new tab
    def switchTab(self, handle):
        if self.intelliConnection():
            while True:
                try:
                    window_after = self.driver.window_handles[handle]
                    self.driver.switch_to_window(window_after)
                    break
                except:
                    continue
        return

    # Accept the alert box
    def acceptAlert(self):
        # self.wait_for_and_accept_alert()
        try:
            WebDriverWait(self.driver, 19).until(EC.alert_is_present())
        except TimeoutException:
            # print ("Quiting process no stable internet connection")
            pass

    # Connect to URL
    def intelliConnect(self, elements):
        if self.intelliConnection():
            try:
                self.driver.get(elements)
            except TimeoutException:
                print("Internet is not stable.")
        else:
            print("No Internet Connection")

    # Login to the page
    def intelliLogin(self, userid, passid):
        if self.intelliConnection():
            try:
                username = self.driver.find_element_by_name("Username")
                password = self.driver.find_element_by_name("Password")
                username.send_keys(str(userid))
                password.send_keys(str(passid))
                login_attempt = self.driver.find_element_by_id("mybutton")
                login_attempt.click()
            except:
                return
        else:
            print("No Internet Connection")

    # Check the title of the current page
    def intelliCheckTitle(self, title):
        if self.intelliConnection():
            try:
                WebDriverWait(self.driver, 30).until(EC.title_contains(title))
                return True
            except:
                self.driver.close()
                return False

    # Wait Until Title found
    def intelliWaitTitle(self, title):
        if self.intelliConnection():
            try:
                if title == 'Inbox' or title == 'Sent' or title == 'New Message':
                    WebDriverWait(self.driver, 180).until(
                        lambda x: self.driver.title.strip().lower() == title.strip().lower()
                    )
                else:
                    WebDriverWait(self.driver, 180).until(lambda x: "".join(
                        self.driver.title.strip().lower().split()) == "".join(title.strip().lower().split()))
                return True
            except TimeoutException:
                print("Quiting process no stable internet connection")
                return False
        else:
            print("No Internet Connection")

    # Switch Frames
    def intelliActionChain(self):
        return ActionChains(self.driver)

    def getCurrentContainer(self):
        return self.driver

    # Find elements based on ID
    def intelliFindID(self, id):
        if self.intelliConnection():
            try:
                WebDriverWait(self.driver, 300).until(
                    EC.presence_of_element_located((By.ID, id)))
            except TimeoutException:
                print("Quiting process no stable internet connection")
            out_ = self.driver.find_element_by_id(id)
            return out_
        else:
            print("No Internet Connection")

    # Find elements based on Xpath
    def intelliFindXPath(self, xpath):
        if self.intelliConnection():
            try:
                WebDriverWait(self.driver, 180).until(
                    EC.presence_of_element_located((By.XPATH, xpath)))
            except TimeoutException:
                print("Quiting process no stable internet connection")
            out_ = self.driver.find_element_by_xpath(xpath)
            return out_
        else:
            print("No Internet Connection")

    # Find elements in a given container using XPath
    def intelliFindXPathInContainer(self, xpath, container):
        if self.intelliConnection():
            try:
                WebDriverWait(container, 180).until(
                    EC.presence_of_element_located((By.XPATH, xpath)))
            except TimeoutException:
                print("Quiting process no stable internet connection")
            out_ = container.find_element_by_xpath(xpath)
            return out_
        else:
            print("No Internet Connection")

    # Find elements based on CSS Selector
    def intelliFindCSSSelector(self, container, selector, flag):
        if self.intelliConnection():
            try:
                WebDriverWait(container, 180).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, selector)))
            except TimeoutException:
                print("Quiting process no stable internet connection")
            if flag == 1:
                out_ = container.find_elements_by_css_selector(selector)
            else:
                out_ = container.find_element_by_css_selector(selector)
            return out_
        else:
            print("No Internet Connection")

    # Find element based on Class Name
    def intelliFindClassName(self, cname):
        if self.intelliConnection():
            try:
                WebDriverWait(self.driver, 600).until(
                    EC.presence_of_element_located((By.CLASS_NAME, cname)))
            except TimeoutException:
                print("Quiting process no stable internet connection")
            out_ = self.driver.find_element_by_class_name(cname)
            return out_
        else:
            print("No Internet Connection")

    # Find elements based on Class Name
    def intelliFindClassNames(self, cname):
        if self.intelliConnection():
            try:
                WebDriverWait(self.driver, 180).until(
                    EC.presence_of_element_located((By.CLASS_NAME, cname)))
            except TimeoutException:
                print("Quiting process no stable internet connection")
            out_ = self.driver.find_elements_by_class_name(cname)
            return out_
        else:
            print("No Internet Connection")

    # Find elements based on Tag Name
    def intelliFindTagName(self, tname):
        if self.intelliConnection():
            try:
                WebDriverWait(self.driver, 180).until(
                    EC.presence_of_element_located((By.TAG_NAME, tname)))
            except TimeoutException:
                print("Quiting process no stable internet connection")
            out_ = self.driver.find_element_by_tag_name(tname)
            return out_
        else:
            print("No Internet Connection")

    def intelliFindPartialText(self, text):
        if self.intelliConnection():
            try:
                WebDriverWait(self.driver, 180).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, text)))
            except TimeoutException:
                print("Quiting process no stable internet connection")
            out_ = self.driver.find_element_by_partial_link_text(text)
            return out_
        else:
            print("No Internet Connection")

    # wait for class element 
    def intelliWaitClassName(self, cname):
        if self.intelliConnection():
            try:
                WebDriverWait(self.driver, 180).until(
                    EC.presence_of_element_located((By.CLASS_NAME, cname)))
                return True
            except TimeoutException:
                print("Quiting process no stable internet connection")
                return False     
        else:
            print("No Internet Connection")

    def newWindow(self,msg):
        another_window = list(set(self.driver.window_handles) - {self.driver.current_window_handle})[0]
        return self.driver.switch_to.window(another_window).current_url

    def Switch(self,main_page):
    #changing the handles to access login page 
        for handle in self.driver.window_handles: 
            if handle != main_page: 
                new = handle 
        #change the control to signin page         
        self.driver.switch_to.window(new) 
        return

    def getWindowHandle(self,msg):
        return self.driver.current_window_handle 
    
    #to get the selected option from the select menu using XPath (Dropdown)
    def getSelectedOptionXPath(self,path):
        select = Select(path)
        selected_option = select.first_selected_option
        return selected_option.text

    #Select option based on value passed 
    def Select_value(self, path,value):
        select = Select(path)
        select.select_by_visible_text(value)
        return

    #to Scroll down on the same web page
    def Scroll_down(self,htmltagname):
        htmltagname.send_keys(Keys.END)
        return
