# -*- coding: utf-8 -*-

import sys
import traceback
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

screenShotsPath = '~/Documents/FMBT_scripts/techtalk/screens'
url = 'http://techtalk.pl'
driver = webdriver.Chrome("//home//jb//Downloads//chromedriver")
wait = WebDriverWait(driver, 10)

def init():
        driver.get(url)
        time.sleep(3)
        driver.find_element_by_css_selector("i.spu-icon.spu-icon-close").click()
        time.sleep(1)
        driver.find_element_by_id('cn-accept-cookie').click()
                
def cleanUp():
        driver.quit()

def clickMainPage():

        moduleName = 'clickMainPage'
        now = time.strftime("%Y_%m_%d_%X")
        screenPath = "screens/" + moduleName + "_" + now + '.png'
        
        driver.get('http:/techtalk.pl/')

        try:
                assert "Page Not Found" not in driver.page_source
        except AssertionError:
                    now = time.strftime("%Y_%m_%d_%X")
                    print "Assertion error! Taking snapshot to: " + screenPath
                    driver.save_screenshot(screenPath)
        
def clickAboutSubPage():
        
        moduleName = 'clickAboutSubPage'
        now = time.strftime("%Y_%m_%d_%X")
        screenPath = "screens/" + moduleName + "_" + now + '.png'
        
        time.sleep(1)
        driver.find_element_by_link_text('ABOUT').click()

        try:
                assert "Page Not Found" not in driver.page_source
        except AssertionError:
                    now = time.strftime("%Y_%m_%d_%X")
                    print "Assertion error! Taking snapshot to: " + screenPath
                    driver.save_screenshot(screenPath)
        
def clickTalksSubPage():

        moduleName = 'clickTalksSubPage'
        now = time.strftime("%Y_%m_%d_%X")
        screenPath = "screens/" + moduleName + "_" + now + '.png'
        
        time.sleep(1)
        driver.find_element_by_link_text('TALKS').click()
        try:
                assert "Page Not Found" not in driver.page_source
        except AssertionError:
                    now = time.strftime("%Y_%m_%d_%X")
                    print "Assertion error! Taking snapshot to: " + screenPath
                    driver.save_screenshot(screenPath)

def clickBookASeatSubPage():

        moduleName = 'clickBookASeatSubPage'
        now = time.strftime("%Y_%m_%d_%X")
        screenPath = "screens/" + moduleName + "_" + now + '.png'
        
        time.sleep(1)
        driver.find_element_by_link_text('BOOK A SEAT').click()

        try:
                assert "Page Not Found" not in driver.page_source
        except AssertionError:
                    now = time.strftime("%Y_%m_%d_%X")
                    print "Assertion error! Taking snapshot to: " + screenPath
                    driver.save_screenshot(screenPath)    

def clickMoreInfoSubPage():

        moduleName = 'clickMoreInfoSubPage'
        now = time.strftime("%Y_%m_%d_%X")
        screenPath = "screens/" + moduleName + "_" + now + '.png'
        
        time.sleep(1)
        driver.find_element_by_link_text('MORE INFO').click()

        try:
                assert "Page Not Found" not in driver.page_source
        except AssertionError:
                    now = time.strftime("%Y_%m_%d_%X")
                    print "Assertion error! Taking snapshot to: " + screenPath
                    driver.save_screenshot(screenPath)

def searchModuleCheck():

        moduleName = 'searchModuleCheck'
        now = time.strftime("%Y_%m_%d_%X")
        screenPath = "screens/" + moduleName + "_" + now + '.png'
        
        searchInput = ["1234", "asdasdd", "@#$@##$@#", "%$", "%$fdgdfg@#$@#$@###$@%3454352354325452FDGDFGDFGDFSBCVXBZBZBAGdfagfdsgdsgdsdfsg////]]", "="] 
        for i in range(len(searchInput)):
            time.sleep(1)
            driver.find_element_by_id("tt-search-open").click()    
            element = driver.find_element_by_name("s")
            element.clear()
            element.send_keys(searchInput[i], Keys.ENTER)
            try:
                    assert "We have found" in driver.page_source
                    assert "/home/users/marlena345" not in driver.page_source
                    assert "TechTalk Wroclaw #2" not in driver.page_source
            except AssertionError:
                    now = time.strftime("%Y_%m_%d_%X")
                    print "Assertion error! Taking snapshot to: " + screenPath
                    driver.save_screenshot(screenPath)
            i+=1

def bookingProcedureCheck():

        moduleName = 'bookingProcedureCheck'
        now = time.strftime("%Y_%m_%d_%X")
        screenPath = "screens/" + moduleName + "_" + now + '.png'
        
        userData = ["userName", "userLastName", "userEmail@gmail.com" , "primarySkill", "Gdansk", "Poland"]
        nbOfTickets = ["1"]
        
        time.sleep(1)

        #iFrame switch
        myFrame = driver.find_element_by_id('weemss_integration_4060')
        
        driver.switch_to_frame(myFrame)
        
        driver.find_element_by_id("form_ticketCategory_9160").send_keys(nbOfTickets[0])
        driver.find_element_by_class_name("btn").click()
                
        driver.find_element_by_id("form_main_element_17678_firstName").send_keys(userData[0])
        driver.find_element_by_id("form_main_element_17678_lastName").send_keys(userData[1])
        driver.find_element_by_id("form_main_element_17680").send_keys(userData[2])
        driver.find_element_by_id("form_main_element_17681").click()
        driver.find_element_by_id("form_main_element_17682").send_keys(userData[3])
        driver.find_element_by_id("form_main_element_17683").send_keys(userData[4])
        driver.find_element_by_id("form_main_element_17684").send_keys(userData[5])
        driver.find_element_by_id("form_copyBuyerInformation").click()
        driver.find_element_by_class_name("btn").click()
        
        driver.switch_to_default_content()      

        try:
                assert driver.find_element_by_css_selector('section.section.section--book-a-seat')
        except AssertionError:
                now = time.strftime("%Y_%m_%d_%X")
                print "Assertion error! Taking snapshot to: " + screenPath
                driver.save_screenshot(screenPath)

def contactUsModule():
        
        moduleName = 'contactUsModule'
        now = time.strftime("%Y_%m_%d_%X")
        screenPath = "screens/" + moduleName + "_" + now + '.png'
        
        userComment = ["userName", 'userEmail@gmail.com', "Subject example", "Massage: djskahfdjskhfdjs dsf sdf ds f##@#$@#$@# dfds s"]
        time.sleep(1)

        driver.find_element_by_id('tt-contacts__open-btn').click()

        driver.find_element_by_css_selector("input.wpcf7-form-control.wpcf7-text.wpcf7-validates-as-required").send_keys(userComment[0])
        driver.find_element_by_css_selector("input.wpcf7-form-control.wpcf7-text.wpcf7-email.wpcf7-validates-as-required.wpcf7-validates-as-email").send_keys(userComment[1])
        driver.find_element_by_xpath("//*[@id=\"wpcf7-f260-o1\"]/form/div[2]/div[1]/span[3]/input").send_keys(userComment[2])
        driver.find_element_by_xpath("//*[@id=\"wpcf7-f260-o1\"]/form/div[2]/div[2]/span/textarea").send_keys(userComment[3])        

        driver.find_element_by_css_selector("input.wpcf7-form-control.wpcf7-submit.btn").click()
        time.sleep(1)

        try:
                assert "Sorry, there was an error. Please be sure JavaScript and Cookies are enabled in your browser and try again." not in driver.page_source
        except AssertionError:
                now = time.strftime("%Y_%m_%d_%X")
                print "Assertion error! Taking snapshot to: " + screenPath
                driver.save_screenshot(screenPath)







