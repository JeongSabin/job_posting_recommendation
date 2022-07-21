from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import pandas as pd
from selenium.common.exceptions import NoSuchElementException
import time
import warnings
from selenium.webdriver.common.keys import Keys
import datetime


# 카카오 ID와 PW 를 입력해주세요.
ID = ''
PW = ''

options = webdriver.ChromeOptions()

options.add_argument('lang=ko_KR')
driver = webdriver.Chrome('./chromedriver', options=options)

warnings.filterwarnings('ignore')

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

# 로그인
driver.get('https://www.wanted.co.kr/wdlist/518?country=kr&job_sort=company.response_rate_order&years=-1&locations=all')
time.sleep(1)
# driver.find_element('xpath', '//*[@id="gnbSignupBtn"]').click()
# time.sleep(1)
# driver.find_element('xpath', '//*[@id="MODAL_BODY"]/div[2]/div[2]/div[3]/div[1]/button').click()
# # username = driver.find_element("xpath", '//*[@id="id_email_2_label"]/span[1]')
# driver.find_element('name', 'email').send_keys(f'{ID}')
# driver.find_element('name', 'password').send_keys(f'{PW}')
#
# driver.find_element('xpath', '//*[@id="login-form"]/fieldset/div[8]/button[1]').click()
time.sleep(60)

for i in range(2,5):
    driver.get('https://www.wanted.co.kr/wdlist/518?country=kr&job_sort=company.response_rate_order&years=-1&locations=all')
    time.sleep(5)
    button = driver.find_element('xpath', '//*[@id="__next"]/div[3]/article/div/div[2]/button/span[2]')
    time.sleep(1)
    driver.execute_script("arguments[0].click();", button)  # click()으로 에러가나서 써줌
    category = '//*[@id="__next"]/div[3]/article/div/div[2]/section/div[1]/div/button[{}]'.format(i)
    driver.find_element("xpath",category).click()
    # 카테고리 text 위치
    category_name = driver.find_element("xpath", category).text
    print(category_name)
    button2 = driver.find_element("css selector",'#__next > div.JobList_cn__t_THp > article > div > div.JobCategory_JobCategory__uTt2E > section > div.JobCategoryOverlay_JobCategoryOverlay__bottom__6Q_OM > button > span')
    driver.execute_script("arguments[0].click();", button2)  # click()으로 에러가나서 써줌
    time.sleep(1)

    # 무한 스크롤
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:  # 페이지 끝까지 다운
        # 끝까지 스크롤 다운
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # 1초 대기
        time.sleep(1)
        # 스크롤 다운 후 스크롤 높이 다시 가져옴
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    # 페이지 방문
    xpath_cut = 0
    flag = True
    while flag :
        xpath_cut += 1
        page = '#__next > div.JobList_cn__t_THp > div > div > div.List_List_container__JnQMS > ul > li:nth-child({}) > div > a > header'.format(xpath_cut)
        button3 = driver.find_element('css selector', '#__next > div.JobList_cn__t_THp > div > div > div.List_List_container__JnQMS > ul > li:nth-child({}) > div > a > header'.format(xpath_cut))
        driver.execute_script("arguments[0].click();", button3)
        time.sleep(1)
        # 페이지 링크, 그림 링크 text 위치
        page_url = driver.current_url
        print(page_url)
        try:
            picture_url = driver.find_element("css selector", '#__next > div.JobDetail_cn__WezJh > div.JobDetail_contentWrapper__DQDB6 > div.JobDetail_relativeWrapper__F9DT5 > div > section.JobImage_JobImage__OFUyr > div > div:nth-child(1) > img').get_attribute('src')
            print(picture_url)
        except:
            picture_url = '없음'
        # 제목과 회사 text 위치
        title = driver.find_element("xpath", '//*[@id="__next"]/div[3]/div[1]/div[1]/div/section[2]/h2').text
        print(title)
        company = driver.find_element("xpath", '//*[@id="__next"]/div[3]/div[1]/div[1]/div/section[2]/div[1]/h6/a').text
        print(company)
        # 회사 소개 text 위치
        try :
            Introduction = driver.find_element("xpath", '//*[@id="__next"]/div[3]/div[1]/div[1]/div/div[2]/section[1]/p[1]/span').text
            print(Introduction)
        except :
            Introduction = '없음'
            pass
        # 주요 업무 text 위치
        try :
            work = driver.find_element("xpath", '//*[@id="__next"]/div[3]/div[1]/div[1]/div/div[2]/section[1]/p[2]/span').text
            print(work)
        except :
            work = '없음'
            pass
        # 자격 요건 text 위치
        try :
            qualification = driver.find_element("xpath", '//*[@id="__next"]/div[3]/div[1]/div[1]/div/div[2]/section[1]/p[3]/span').text
            print(qualification)
        except :
            qualification = '없음'
            pass
        # 우대 사항 text 위치
        try:
            favor = driver.find_element("xpath", '//*[@id="__next"]/div[3]/div[1]/div[1]/div/div[2]/section[1]/p[4]/span').text
            print(favor)
        except:
            favor = '없음'
            pass
        # 혜택 및 복지 text 위치
        try:
            welfare = driver.find_element("xpath", '//*[@id="__next"]/div[3]/div[1]/div[1]/div/div[2]/section[1]/p[5]/span').text
            print(welfare)
        except:
            welfare = '없음'
            pass
        # 기술 스택 text 위치
        try:
            stack_cut = 1
            stack_flag = True
            skill_stack = []
            while stack_flag :
                stack_cut += 1
                stack = driver.find_element("xpath", '//*[@id="__next"]/div[3]/div[1]/div[1]/div/div[2]/section[1]/p[6]/div/div[{}]'.format(stack_cut)).text
                skill_stack.append(stack)

                if NoSuchElementException:
                    stack_flag = False
        except:
            skill_stack = '없음'
        # 근무 지역 text 위치
        print(stack_cut)
        try:
            place = driver.find_element("xpath", '//*[@id="__next"]/div[3]/div[1]/div[1]/div/div[2]/section[2]/div[2]/span[2]').text
            print(place)
        except:
            place = '없음'
            pass
    # 회사 페이지 방문
        driver.find_element('css selector', '#__next > div.JobDetail_cn__WezJh > div.JobDetail_contentWrapper__DQDB6 > div.JobDetail_relativeWrapper__F9DT5 > div.JobContent_className___ca57 > section.JobHeader_className__HttDA > div:nth-child(2) > h6 > a').click()
        # button4 = driver.find_element('css selector', page)
        # driver.execute_script("arguments[0].click();", button4)  # click()으로 에러가나서 써줌
        # 무한 스크롤
        last_height = driver.execute_script("return document.body.scrollHeight")
        while True:  # 페이지 끝까지 다운
            # 끝까지 스크롤 다운
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            # 1초 대기
            time.sleep(1)
            # 스크롤 다운 후 스크롤 높이 다시 가져옴
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

        time.sleep(10)
        # 연봉 text 위치
        all_money = []
        try:
            money1 = driver.find_elements("xpath", '//*[@id="__next"]/div[3]/div[2]/div[2]/div[3]/div/div[1]/div/div[2]/div/div/div[1]').text
            money2 = driver.find_elements("xpath", '//*[@id="__next"]/div[3]/div[2]/div[2]/div[3]/div/div[1]/div/div[2]/div/div/div[3]').text
            money3 = driver.find_elements("xpath", '//*[@id="__next"]/div[3]/div[2]/div[2]/div[3]/div/div[1]/div/div[2]/div/div/div[4]').text
            money4 = driver.find_elements("xpath", '//*[@id="__next"]/div[3]/div[2]/div[2]/div[3]/div/div[1]/div/div[2]/div/div/div[5]').text
            print(money1)
            print(money2)
            print(money3)
            print(money4)
            all_money.append(money1)
            all_money.append(money2)
            all_money.append(money3)
            all_money.append(money4)
            print(all_money)
            all_money = all_money.astype('int')
        except:
            all_money = '없음'
            pass
        print(all_money)
        # # 직원수 text 위치
        # try:
        #     number = driver.find_element("css selector", '#__next > div.CompanyDetail_companyDetailClass__rdAtq > div.CompanyDetail_innerWrapper__tMmW5 > div.CompanyDetail_contentColumn__qNdI_ > div.KreditData_kreditDataWrapperClass__H7IlD > div > div.Size_sizeClass__qp2Cn > div.Size_totalMemberBlock__NuVv0').text
        #     print(number)
        # except:
        #     number = '없음'
        #     pass
    # 내용 모두 저장하기
        category_list.append(category_name)
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
        money_list.append(all_money)
        # number_list.append(number)
        if NoSuchElementException:
            driver.back()
            driver.back()
            pass

        df = pd.DataFrame({'category': category_list, 'page_url': page_url_list, 'picture_url': picture_url_list, 'title': title_list, 'company': company_list,
                           'work': work_list, 'qualification': qualification_list, 'favor': favor_list, 'welfare': welfare_list, 'skill_stack': skill_stack_list,
                           'place': place_list, 'money': money_list})
    df.to_csv('./crawling_ERP전문가{}.csv'.format(xpath_cut), index=False)
