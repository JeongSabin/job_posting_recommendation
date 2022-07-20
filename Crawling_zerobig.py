from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd
from selenium.common.exceptions import NoSuchElementException
import time
import os
import requests
from bs4 import BeautifulSoup
import datetime

options = webdriver.ChromeOptions()
# options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
options.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 1})
options.add_argument('lnag=ko_KR')
# print('debug3')
driver = webdriver.Chrome('./chromedriver.exe', options=options)
def infinite_loop():
    #스크롤 내리기
    last_page_height = driver.execute_script("return document.documentElement.scrollHeight")

    while True:
        driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
        time.sleep(1.0)
        new_page_height = driver.execute_script("return document.documentElement.scrollHeight")
        if new_page_height == last_page_height:
            time.sleep(1.0)
            if new_page_height == driver.execute_script("return document.documentElement.scrollHeight"):
                break
        else:
            last_page_height = new_page_height

driver.get(
    'https://www.wanted.co.kr/wdlist/518?country=kr&job_sort=company.response_rate_order&years=-1&locations=all')
time.sleep(1)
driver.find_element('xpath', '//*[@id="gnbSignupBtn"]').click()
time.sleep(1)
driver.find_element('xpath', '//*[@id="MODAL_BODY"]/div[2]/div[2]/div[3]/div[1]/button').click()
time.sleep(1)
# username = driver.find_element("xpath", '//*[@id="id_email_2_label"]/span[1]')
driver.find_element('name', 'email').send_keys('realove-u@nate.com')

driver.find_element('name', 'password').send_keys('speed')

driver.find_element('xpath', '//*[@id="login-form"]/fieldset/div[8]/button[1]').click()
time.sleep(2)
df = pd.DataFrame()
name_tag = ['주요업무', '자격요건', '우대사항', '혜택 및 복지', '기술스택 ・ 툴']
category_list = []
page_url_list = []
picture_url_list = []
title_list = []
company_list = []
work_list = []
qualification_list = []
favor_list = []
welfare_list = []
skill_stack_list = []
place_list = []
money_list = []
number_list = []

for i in range(38, 39):
    # print('debug7')
    time.sleep(1)
    url = 'https://www.wanted.co.kr/wdlist/518?country=kr&job_sort=company.response_rate_order&years=-1&locations=all'
    time.sleep(3)
    # print('debug1')
    driver.get(url)
    # page_url = driver.current_url
    # print(page_url)
    # 페이지주소.append(page_url)
    time.sleep(2)
    #
    button1 = driver.find_element('xpath','//*[@id="__next"]/div[3]/article/div/div[2]/button/span[2]') ##세모클릭
    driver.execute_script("arguments[0].click();", button1)
    # driver.find_element('xpath', ).click()
    # print('debug2')
    time.sleep(1)
    # button2 = driver.find_element('xpath', '//*[@id="__next"]/div[3]/article/div/div[2]/section/div[1]/div/button[{}]'.format(i)) #직군선택
    # driver.execute_script("arguments[0].click();", button2)
    driver.find_element('xpath',
                        '//*[@id="__next"]/div[3]/article/div/div[2]/section/div[1]/div/button[{}]'.format(i)).click()

    time.sleep(0.3)
    button3 = driver.find_element('xpath', '//*[@id="__next"]/div[3]/article/div/div[2]/section/div[2]/button')  #선택완료 클릭
    driver.execute_script("arguments[0].click();", button3)
    # driver.find_element('xpath',
    #                     '//*[@id="__next"]/div[3]/article/div/div[2]/section/div[2]/button').click()
    # print('debug3')
    time.sleep(0.9)
    category = driver.find_element('xpath','//*[@id="__next"]/div[3]/article/div/div[2]/button/span[1]').text

    # print('debug4')
    page_url = driver.current_url
    print(page_url)
    # 페이지주소.append(page_url)
    # print(category)
    # 직군.append(category)


    # 무한 스크롤 코드ㅜ
    SCROLL_PAUSE_SEC = 1
    last_height = driver.execute_script('return document.body.scrollHeight')

    while True:
        # 끝까지 스크롤 다운
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # 1초 대기
        time.sleep(SCROLL_PAUSE_SEC)

        # 스크롤 다운 후 스크롤 높이 다시 가져옴
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    print('스크롤 완료')


    # try:
    for j in range(1, 6):  # 2 , 12
        time.sleep(2)
        button5 = driver.find_element('css selector', '#__next > div.JobList_cn__t_THp > div > div > div.List_List_container__JnQMS > ul > li:nth-child({}) > div > a > header'.format(j))
        driver.execute_script("arguments[0].click();", button5)
        # driver.find_element('css selector', '#__next > div.JobList_cn__t_THp > div > div > div.List_List_container__JnQMS > ul > li:nth-child({}) > div > a > header'.format(j)).click()  # 공고문 클릭
        time.sleep(2)


        # print(href)
        time.sleep(2)
        button4 = driver.find_element('css selector', '#__next > div.JobDetail_cn__WezJh > div.JobDetail_contentWrapper__DQDB6 > div.JobDetail_relativeWrapper__F9DT5 > div.JobContent_className___ca57 > section.JobHeader_className__HttDA > div:nth-child(2) > h6 > a')
        driver.execute_script("arguments[0].click();", button4)
        # driver.find_element('css selector','#__next > div.JobDetail_cn__WezJh > div.JobDetail_contentWrapper__DQDB6 > div.JobDetail_relativeWrapper__F9DT5 > div.JobContent_className___ca57 > section.JobHeader_className__HttDA > div:nth-child(2) > h6 > a').click()
        time.sleep(3)
        print('bug1')


        driver.execute_script("window.scrollTo(0, 700);")

        print('bug2')
        # driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(3)
        money_all = []

        try :
            money1 = driver.find_element('xpath', '//*[@id="__next"]/div[3]/div[2]/div[2]/div[3]/div/div[1]/div/div[2]/div/div/div[1]/div').get_attribute('style')
            money2 = driver.find_element('xpath', '//*[@id="__next"]/div[3]/div[2]/div[2]/div[3]/div/div[1]/div/div[2]/div/div/div[3]/div').get_attribute('style')
            money3 = driver.find_element('xpath', '//*[@id="__next"]/div[3]/div[2]/div[2]/div[3]/div/div[1]/div/div[2]/div/div/div[4]/div').get_attribute('style')
            money4 = driver.find_element('xpath', '//*[@id="__next"]/div[3]/div[2]/div[2]/div[3]/div/div[1]/div/div[2]/div/div/div[5]/div').get_attribute('style')
            money = int( money1[7] + money2[7] + money3[7] + money4[7])
        except :
            money = '없음'
            pass
        print(money)
        try:
            try:
                imployee1 = driver.find_element('xpath','//*[@id="__next"]/div[3]/div[2]/div[2]/div[3]/div/div[2]/div[1]/div/div/div/div').get_attribute('style')
                imployee = int(imployee1[7])
            except:
                pass
            try:
                imployee1 = driver.find_element('xpath','//*[@id="__next"]/div[3]/div[2]/div[2]/div[3]/div/div[2]/div[1]/div/div/div[1]/div').get_attribute('style')
                imployee2 = driver.find_element('xpath',
                                                '//*[@id="__next"]/div[3]/div[2]/div[2]/div[3]/div/div[2]/div[1]/div/div/div[2]/div').get_attribute(
                    'style')
                imployee = int(imployee1[7] + imployee2[7])
            except:
                pass
            try:
                imployee1 = driver.find_element('xpath',
                                                '//*[@id="__next"]/div[3]/div[2]/div[2]/div[3]/div/div[2]/div[1]/div/div/div[1]/div').get_attribute(
                    'style')
                imployee2 = driver.find_element('xpath',
                                            '//*[@id="__next"]/div[3]/div[2]/div[2]/div[3]/div/div[2]/div[1]/div/div/div[2]/div').get_attribute(
                'style')
                imployee3 = driver.find_element('xpath','//*[@id="__next"]/div[3]/div[2]/div[2]/div[3]/div/div[2]/div[1]/div/div/div[3]/div').get_attribute('style')
                imployee = int(imployee1[7] + imployee2[7] + imployee3[7])
            except:
                pass
        except:
            pass
        print(imployee)
        driver.back()
        time.sleep(2)
        # exit(1)
        # print('debug')
        picture_url = driver.find_element("css selector",
                                          '#__next > div.JobDetail_cn__WezJh > div.JobDetail_contentWrapper__DQDB6 > div.JobDetail_relativeWrapper__F9DT5 > div > section.JobImage_JobImage__OFUyr > div > div:nth-child(1) > img').get_attribute(
            'src')
        title = driver.find_element("xpath", '//*[@id="__next"]/div[3]/div[1]/div[1]/div/section[2]/h2').text
        print(title)
        company = driver.find_element("xpath", '//*[@id="__next"]/div[3]/div[1]/div[1]/div/section[2]/div[1]/h6/a').text
        print(company)
        # 회사 소개 text 위치
        try:
            Introduction = driver.find_element("xpath",
                                               '//*[@id="__next"]/div[3]/div[1]/div[1]/div/div[2]/section[1]/p[1]/span').text
            print(Introduction)
        except:
            Introduction = '없음'
            pass
        # 주요 업무 text 위치
        try:
            work = driver.find_element("xpath",
                                       '//*[@id="__next"]/div[3]/div[1]/div[1]/div/div[2]/section[1]/p[2]/span').text
            print(work)
        except:
            work = '없음'
            pass
        # 자격 요건 text 위치
        try:
            qualification = driver.find_element("xpath",
                                                '//*[@id="__next"]/div[3]/div[1]/div[1]/div/div[2]/section[1]/p[3]/span').text
            print(qualification)
        except:
            qualification = '없음'
            pass
        # 우대 사항 text 위치
        try:
            favor = driver.find_element("xpath",
                                        '//*[@id="__next"]/div[3]/div[1]/div[1]/div/div[2]/section[1]/p[4]/span').text
            print(favor)
        except:
            favor = '없음'
            pass
        # 혜택 및 복지 text 위치
        try:
            welfare = driver.find_element("xpath",
                                          '//*[@id="__next"]/div[3]/div[1]/div[1]/div/div[2]/section[1]/p[5]/span').text
            print(welfare)
        except:
            welfare = '없음'
            pass
        # 기술 스택 text 위치
        try:
           stack = driver.find_element('xpath', '//*[@id="__next"]/div[3]/div[1]/div[1]/div[1]/div[2]/section[1]/p[6]/div').text
           skill_stack.append(stack)
           print(stack)

        except:
            skill_stack = '없음'
        # 근무 지역 text 위치

        try:
            place = driver.find_element("xpath",
                                        '//*[@id="__next"]/div[3]/div[1]/div[1]/div/div[2]/section[2]/div[2]/span[2]').text
            print(place)
        except:
            place = '없음'
            pass
        driver.back()
        category_list.append(category)
        page_url_list.append(page_url)
        picture_url_list.append(picture_url)
        title_list.append(title)
        company_list.append(company)
        work_list.append(work)
        qualification_list.append(qualification)
        favor_list.append(favor)
        welfare_list.append(welfare)
        skill_stack_list.append(skill_stack)
        place_list.append(place)
        money_list.append(money)
        number_list.append(imployee)

        df = pd.DataFrame({'category': category_list, 'page_url': page_url_list, 'picture_url': picture_url_list, 'title': title_list, 'company': company_list,
                           'work': work_list, 'qualification': qualification_list, 'favor': favor_list, 'welfare': welfare_list, 'skill_stack': skill_stack_list,
                           'place': place_list, 'money': money_list, 'employee': number_list})
        df.to_csv('./crawling_ERP전문가_{}.csv'.format(j), index=False)
        print('save', j)

driver.back()




time.sleep(1)

