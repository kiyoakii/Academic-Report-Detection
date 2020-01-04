import urllib.request
from bs4 import BeautifulSoup
from lxml import etree
import json
import smtplib
from email.header import Header
from email.mime.text import MIMEText
import time
import sys

def get_list():
    limit = 1
    UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
    result = []
    #School of Mathematical Sciences
    url = 'http://math.ustc.edu.cn/xsbg_18822/list1.htm'
    req = urllib.request.Request(url, headers={'User-Agent': UA})
    rsp = urllib.request.urlopen(req)
    html_str = rsp.read().decode('utf-8', 'ignore')
    html = BeautifulSoup(html_str, 'html.parser')

    cut = url.find('ustc.edu.cn/') + len('ustc.edu.cn')
    prefix = url[:cut]

    for link in html.find_all(class_='Article_Title', limit=limit):
        info_link = prefix + link.a.get("href")
        info_text = link.get_text(strip=True)
        result.append(info_text+'\n'+info_link)

    #School of Physical Sciences
    url = 'https://physics.ustc.edu.cn/xsbg/list.htm'
    req = urllib.request.Request(url, headers={'User-Agent': UA})
    rsp = urllib.request.urlopen(req)
    html_str = rsp.read().decode('utf-8', 'ignore')
    html = BeautifulSoup(html_str, 'html.parser')

    cut = url.find('ustc.edu.cn/') + len('ustc.edu.cn')
    prefix = url[:cut]

    for link in html.find_all(class_='hero-unify', limit=limit):
        info_link = prefix + link.p.h4.a.get("href")
        info_text = link.get_text(strip=True)
        result.append(info_text+'\n'+info_link)
        

    #School of Chemistry and Materials Science
    url = 'https://scms.ustc.edu.cn/2403/list.htm'
    req = urllib.request.Request(url, headers={'User-Agent': UA})
    rsp = urllib.request.urlopen(req)
    html_str = rsp.read().decode('utf-8', 'ignore')
    html = BeautifulSoup(html_str, 'html.parser')

    cut = url.find('ustc.edu.cn/') + len('ustc.edu.cn')
    prefix = url[:cut]

    for link in html.find(id='wp_news_w5').find_all('li', limit=limit):
        info_link = prefix + link.a.get("href")
        info_text = link.get_text(strip=True)
        result.append(info_text+'\n'+info_link)
        

    #School of Engineering Science
    url = 'https://ses.ustc.edu.cn/1686/list.htm'
    req = urllib.request.Request(url, headers={'User-Agent': UA})
    rsp = urllib.request.urlopen(req)
    html_str = rsp.read().decode('utf-8', 'ignore')
    html = BeautifulSoup(html_str, 'html.parser')

    cut = url.find('ustc.edu.cn/') + len('ustc.edu.cn')
    prefix = url[:cut]

    for link in html.find_all(class_="Article_Title", limit=limit):
        info_link = prefix + link.a.get("href")
        info_text = link.get_text(strip=True)
        result.append(info_text+'\n'+info_link)
        

    #School of Earth and Space Sciences
    url = 'http://ess.ustc.edu.cn/report/loaditems-1.html'
    req = urllib.request.Request(url, headers={'User-Agent': UA})
    rsp = urllib.request.urlopen(req)
    html_str = rsp.read().decode('utf-8', 'ignore')
    h = json.loads(html_str)["html"]
    html = BeautifulSoup(h, 'html.parser')

    cut = url.find('ustc.edu.cn/') + len('ustc.edu.cn')
    prefix = url[:cut]

    for link in html.find_all("li", class_="bgstyle", limit=limit):
        info_link = prefix + link.a.get("href")
        info_text = link.get_text(strip=True)
        result.append(info_text+'\n'+info_link)
        

    #School of Life Sciences
    url = 'https://biox.ustc.edu.cn/634/list.htm'
    req = urllib.request.Request(url, headers={'User-Agent': UA})
    rsp = urllib.request.urlopen(req)
    html_str = rsp.read().decode('utf-8', 'ignore')
    html = BeautifulSoup(html_str, 'html.parser')

    cut = url.find('ustc.edu.cn/') + len('ustc.edu.cn')
    prefix = url[:cut]

    for link in html.find_all("li", class_="list", limit=limit):
        info_link = prefix + link.a.get("href")
        info_text = link.get_text(strip=True)
        result.append(info_text+'\n'+info_link)
        

    #School of Computer Science and Technology
    url = 'http://cs.ustc.edu.cn/3059/list.htm'
    req = urllib.request.Request(url, headers={'User-Agent': UA})
    rsp = urllib.request.urlopen(req)
    html_str = rsp.read().decode('utf-8', 'ignore')
    html = BeautifulSoup(html_str, 'html.parser')

    cut = url.find('ustc.edu.cn/') + len('ustc.edu.cn')
    prefix = url[:cut]

    for link in html.find_all("li", attrs={"width": "30%"}, limit=limit):
        info_link = prefix + link.a.get("href")
        info_text = link.get_text(strip=True)
        result.append(info_text+'\n'+info_link)
        

    #School of Management
    url = 'http://business.ustc.edu.cn/lecture/list.htm'
    req = urllib.request.Request(url, headers={'User-Agent': UA})
    rsp = urllib.request.urlopen(req)
    html_str = rsp.read().decode('utf-8', 'ignore')
    html = BeautifulSoup(html_str, 'html.parser')

    cut = url.find('ustc.edu.cn/') + len('ustc.edu.cn')
    prefix = url[:cut]

    for link in html.find_all("li", class_="li", limit=limit):
        info_link = prefix + link.a.get("href")
        info_text = link.get_text(strip=True)
        result.append(info_text+'\n'+info_link)
        

    #School of Humanities and Social Science
    url = 'http://hsss.ustc.edu.cn/8099/list.htm'
    req = urllib.request.Request(url, headers={'User-Agent': UA})
    rsp = urllib.request.urlopen(req)
    html_str = rsp.read().decode('utf-8', 'ignore')
    html = BeautifulSoup(html_str, 'html.parser')

    cut = url.find('ustc.edu.cn/') + len('ustc.edu.cn')
    prefix = url[:cut]

    for link in html.find_all("td", attrs={"height": "20"}, limit=limit):
        info_link = prefix + link.a.get("href")
        info_text = link.get_text(strip=True)
        result.append(info_text+'\n'+info_link)
        

    #School of Data Science
    url = 'http://sds.ustc.edu.cn/15436/list.htm'
    req = urllib.request.Request(url, headers={'User-Agent': UA})
    rsp = urllib.request.urlopen(req)
    html_str = rsp.read().decode('utf-8', 'ignore')
    html = BeautifulSoup(html_str, 'html.parser')

    cut = url.find('ustc.edu.cn/') + len('ustc.edu.cn')
    prefix = url[:cut]

    for link in html.find_all(class_="Article_Title", limit=limit):
        info_link = prefix + link.a.get("href")
        info_text = link.get_text(strip=True)
        result.append(info_text+'\n'+info_link)
        

    #School of Web Security
    url = 'http://cybersec.ustc.edu.cn/'
    req = urllib.request.Request(url, headers={'User-Agent': UA})
    rsp = urllib.request.urlopen(req)
    html_str = rsp.read().decode('utf-8', 'ignore')
    html = BeautifulSoup(html_str, 'html.parser')

    cut = url.find('ustc.edu.cn/') + len('ustc.edu.cn')
    prefix = url[:cut]

    for link in html.find(id="wp_news_w12").find_all(class_="list-group-item", limit=limit):
        info_link = prefix + link.a.get("href")
        info_text = link.get_text(strip=True)
        result.append(info_text+'\n'+info_link)
    
    return result

def check(user_info, keywords):
    tmp = {'history': None}
    if(tmp['history']):
        history = tmp['history']
        now = get_list
        compare(history, now, user_info, keywords)
        tmp['history'] = now
    else:
        tmp['history'] = get_list

def compare(history, now, user_info, keywords):
    result = ''
    for a,b in zip(history, now):
        if a != b:
            result += '\n' + b
    if result != '':
        #send email
        if keywords == []:
            send_email(result, user_info)
        for word in keywords:
            if word in result:
                send_email(result, user_info)

def send_email(article, user_info):
    title = "New Academic Report"
    host = 'mail.ustc.edu.cn'
    user = user_info["user"]
    passwd = user_info["passwd"]
    sender = user
    coding = 'utf8'
    message = MIMEText(article, 'plain', coding)
    message['From'] = Header(sender, coding)
    message['To'] = Header(user_info["receiver"], coding)
    message['subject'] = Header(title, coding)
    try:
        mail_client = smtplib.SMTP_SSL(host,465)
        mail_client.connect(host)
        mail_client.login(user,passwd)
        mail_client.sendmail(sender,user_info["receiver"],message.as_string())
        mail_client.close()
        print('The email has been sent to ' + user_info["receiver"])
    except:
        print('There is an available update, but the email-sending has failed.')

if __name__ == "__main__":
    user_info = {}
    user_info["receiver"] = sys.argv[2]
    if(len(sys.argv) >= 4):
        keywords = sys.argv[3:]
    else:
        keywords = []
    user_info["user"] = input("your ustc email:")
    user_info["passwd"] = input("your passwd:")
    while True:
        check(user_info, keywords)
        time.sleep(30)
