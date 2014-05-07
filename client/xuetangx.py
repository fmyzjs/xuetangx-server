#!/usr/bin/env python
# encoding: utf-8

import urllib
from datetime import datetime

from client.csrfopner import CSRFOpenerDirector
from bs4 import BeautifulSoup

HTTP = 'http://'
HTTPS = 'https://'
HOST = 'www.xuetangx.com'
LOGIN_PAGE = HTTPS + HOST + '/login'
LOGIN_URL = HTTPS + HOST + '/login_ajax'
DASHBOARD = HTTPS + HOST + '/dashboard'
BASE_URL = HTTPS + HOST

def full_url(path):
    if path[0] == '/':
        return BASE_URL + path
    return path

class AuthenticationError(Exception):
    pass

def __get_opener__(email, password):
    """
    email: str
    password: str
    => CSRFOpenerDirector
    """
    opener = CSRFOpenerDirector()
    opener.open(LOGIN_PAGE)
    postdata = urllib.urlencode({
        'email': email,
        'password': password}).encode('utf-8')
    resp = opener.open(LOGIN_URL, postdata).read()

    import json
    success = json.loads(resp)['success']

    if not success:
        raise AuthenticationError()

    return opener

def __get_page__(url, email, password):
    opener = __get_opener__(email, password)
    return opener.open(url).read()

def verify(email, password):
    """
    email: str
    password: str
    => bool. May raise Exception.
    """
    opener = __get_opener__(email, password)
    return (True if opener else False)

def student_info(email, password):
    """
    email: str
    password: str
    => (name, nickname)
    """
    page = __get_page__(DASHBOARD, email, password)

    from bs4 import BeautifulSoup
    page = BeautifulSoup(page)
    name = page.body.find('span', attrs={'class': 'data'}).text
    nickname = page.body.find('h1', attrs={'class': 'user-name'}).text

    return (name, nickname)

def __upcoming__(course):
    date_block = course.find('p', attrs={'class': 'date-block'}).text.strip().split()
    start_date = datetime.strptime(date_block[-1], '%Y-%m-%d')
    university = course.find('h2', attrs={'class': 'university'}).text
    id_title = course.find('section', attrs={'class': 'info'}).find('h3').find('span').text.split()
    course_id = id_title[0]
    title = id_title[1]
    img_url = full_url(course.find('img').attrs['src'])
    return {
        'university': university,
        'id': course_id,
        'title': title,
        'start_date': {
            'year': start_date.year,
            'month': start_date.month,
            'day': start_date.day
        },
        'img_url': img_url,
    }

def __current__(course):
    date_block = course.find('p', attrs={'class': 'date-block'}).text.strip().split()
    start_date = datetime.strptime(date_block[-1], '%Y-%m-%d')
    university = course.find('h2', attrs={'class': 'university'}).text
    id_title = course.find('section', attrs={'class': 'info'}).find('h3').find('a').text.split()
    course_id = id_title[0]
    title = id_title[1]
    img_url = full_url(course.find('img').attrs['src'])
    course_info_url = full_url(course.find('a', attrs={'class': 'enter-course'}).attrs['href'])
    return {
        'university': university,
        'id': course_id,
        'title': title,
        'start_date': {
            'year': start_date.year,
            'month': start_date.month,
            'day': start_date.day
        },
        'img_url': img_url,
        'course_info_url': course_info_url,
    }

def __past__(course):
    date_block = course.find('p', attrs={'class': 'date-block'}).text.strip().split()
    start_date = datetime.strptime(date_block[-1], '%Y-%m-%d')
    university = course.find('h2', attrs={'class': 'university'}).text
    id_title = course.find('section', attrs={'class': 'info'}).find('h3').find('a').text.split()
    course_id = id_title[0]
    title = id_title[1]
    img_url = full_url(course.find('img').attrs['src'])
    course_info_url = full_url(course.find('a', attrs={'class': 'enter-course'}).attrs['href'])
    return {
        'university': university,
        'id': course_id,
        'title': title,
        'start_date': {
            'year': start_date.year,
            'month': start_date.month,
            'day': start_date.day
        },
        'img_url': img_url,
        'course_info_url': course_info_url,
    }

def courses_selected(email, password):
    """
    email: str
    password: str
    => (courses_upcoming, courses_current, courses_past)
    """
    upcoming = []
    current = []
    past = []
    page = __get_page__(DASHBOARD, email, password)
    page = BeautifulSoup(page)
    for course in page.findAll('article', attrs={'class': 'my-course'}):
        date_block = course.find('p', attrs={'class': 'date-block'}).text.strip().split()
        if date_block[0] == u'课程开始':
            upcoming.append(__upcoming__(course))
        elif date_block[0] == u'课程已开始':
            current.append(__current__(course))
        elif date_block[0] == u'课程完成度':
            past.append(__past__(course))

    return (upcoming, current, past)

def courses_upcoming(email, password):
    """
    email: str
    password: str
    => list(course*)
    """
    upcoming = []
    page = __get_page__(DASHBOARD, email, password)
    page = BeautifulSoup(page)
    for course in page.findAll('article', attrs={'class': 'my-course'}):
        date_block = course.find('p', attrs={'class': 'date-block'}).text.strip().split()
        if date_block[0] == u'课程开始':
            upcoming.append(__upcoming__(course))

    return upcoming

def courses_current(email, password):
    """
    email: str
    password: str
    => list(course*)
    """
    current = []
    page = __get_page__(DASHBOARD, email, password)
    page = BeautifulSoup(page)
    for course in page.findAll('article', attrs={'class': 'my-course'}):
        date_block = course.find('p', attrs={'class': 'date-block'}).text.strip().split()
        if date_block[0] == u'课程已开始':
            current.append(__current__(course))

    return current

def courses_past(email, password):
    """
    email: str
    password: str
    => list(course*)
    """
    past = []
    page = __get_page__(DASHBOARD, email, password)
    page = BeautifulSoup(page)
    for course in page.findAll('article', attrs={'class': 'my-course'}):
        date_block = course.find('p', attrs={'class': 'date-block'}).text.strip().split()
        if date_block[0] == u'课程完成度':
            past.append(__past__(course))

    return past
