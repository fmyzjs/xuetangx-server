#!/usr/bin/env python
# encoding: utf-8

import re
import json
import urllib
from datetime import datetime

from client.csrfopner import CSRFOpenerDirector
from bs4 import BeautifulSoup

HTTP = 'http://'
HTTPS = 'https://'
HOST = 'www.xuetangx.com'
BASE_URL_S = HTTPS + HOST
BASE_URL = HTTP + HOST
LOGIN_PAGE = BASE_URL_S + '/login'
LOGIN_URL = BASE_URL_S + '/login_ajax'
DASHBOARD = BASE_URL_S + '/dashboard'
SEARCH = BASE_URL_S + '/courses/search'
COURSES = BASE_URL + '/courses'
ENROLLMENT = BASE_URL_S + '/change_enrollment'
_COURSEWARE = '/courseware'
_VIDEO2SRC = BASE_URL_S + '/videoid2source/'

def full_url(path):
    import urlparse
    return urlparse.urljoin(BASE_URL_S, path)

class AuthenticationError(Exception):
    pass

def __get_opener__(email=None, password=None):
    """
    email: str
    password: str
    => CSRFOpenerDirector
    """
    opener = CSRFOpenerDirector()
    opener.open(LOGIN_PAGE)
    if email is None or password is None:
        return opener

    postdata = urllib.urlencode({
        'email': email,
        'password': password}).encode('utf-8')
    resp = opener.open(LOGIN_URL, postdata).read()

    success = json.loads(resp)['success']

    if not success:
        raise AuthenticationError()

    return opener

def __get_page__(url, email=None, password=None, data=None):
    opener = __get_opener__(email, password)
    return opener.open(url, data=data).read()

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

def courses_categories():
    page = __get_page__(COURSES)
    page = BeautifulSoup(page)

    categories = []
    for item in page.find('div', attrs={'class': 'xkfl'}).findAll('a'):
        cid = item.attrs['data-id']
        pattern = re.compile(u'([^\(]+)\(\s*(\d+)\s*\)', re.UNICODE)
        m_title = pattern.search(item.text)
        title = m_title.group(1)
        count = int(m_title.group(2))
        categories.append({
            'id': cid,
            'title': title,
            'count': count,
        })

    return categories

def __bool2_str__(b):
    return ('true' if b else 'false')

def courses_search(query=None, cid=None, started=False, hasTA=False):
    query_dict = {
        'offset': 0,
        'limit': 1000000,
    }
    if query is not None:
        query_dict['query'] = query.encode('utf-8')
    if cid is not None:
        query_dict['cid'] = cid
    query_dict['started'] = __bool2_str__(started)
    query_dict['hasTA'] = __bool2_str__(hasTA)
    postdata = urllib.urlencode(query_dict).encode('utf-8')

    page = __get_page__(SEARCH, data=postdata)
    page = json.loads(page)

    result = []
    for course in page['data']:
        owner = course['owner']
        university = course['org']
        course_id = course['course_num']
        title = course['name']
        img_url = full_url(course['thumbnail'])
        course_about_url = full_url(course['href'])
        teacher_name = course.get('staff_name', '')
        teacher_title = course.get('staff_title', '')
        update_info = course['modified'] # 更新于`几天前`，str
        serialized_no = course['serialized'] # 连载至第`几`讲，int, default -1
        hasTA = course['hasTA'] # bool
        subtitle = course['subtitle'] # 课程简介
        result.append({
            'owner': owner,
            'university': university,
            'id': course_id,
            'title': title,
            'img_url': img_url,
            'course_about_url': course_about_url,
            'teacher': {
                'name': teacher_name,
                'title': teacher_title,
            },
            'update_info': update_info,
            'serialized_no': serialized_no,
            'hasTA': hasTA,
            'subtitle': subtitle,
        })

    return result

def __extract_course_id__(url):
    pattern = re.compile('/courses/(.+)/[(about)(info)]')
    m_id = pattern.search(url)
    return m_id.group(1)

def courses_enrollment(email, password, url, action):
    course_id = __extract_course_id__(url)
    postdata = {
        'course_id': course_id,
        'enrollment_action': action,
    }
    postdata = urllib.urlencode(postdata).encode('utf-8')
    opener = __get_opener__(email, passworsd)

    conn = opener.open(ENROLLMENT, data=postdata)

    return conn.code == 200

def __courseware_url__(about_or_info_url):
    course_id = __extract_course_id__(about_or_info_url)
    return BASE_URL + '/courses/' + course_id + _COURSEWARE

def courses_lectures(email, password, url):
    url = __courseware_url__(url)
    opener = __get_opener__(email, password)

    return __ware__(opener, url, need_items=False)

def courses_lecture(email, password, url):
    opener = __get_opener__(email, password)
    return __items__(opener, url)

def __items__(opener, lecture_url):
    raw_page = opener.open(lecture_url).read()
    ptn_video = '&lt;source type=&#34;video/mp4&#34; src=&#34;([^&#;]+)&#34;/&gt;'
    video_ids = re.findall(ptn_video, raw_page)
    video_ids_idx = 0

    page = BeautifulSoup(raw_page)

    items = []
    for item in page.find('ol', attrs={'id': 'sequence-list'}).findAll('li'):
        item_class = item.find('a').attrs['class']
        if 'seq_video' in item_class:
            item_type = 'video'
            get_item_url = _VIDEO2SRC + video_ids[video_ids_idx]
            video_ids_idx += 1
            item_urls_json = json.loads(opener.open(get_item_url).read())['sources']
            item_url = {}
            item_url['high-quality'] = []
            for src in item_urls_json['quality20']:
                item_url['high-quality'].append(src)
            item_url['low-quality'] = []
            for src in item_urls_json['quality10']:
                item_url['low-quality'].append(src)
        elif 'seq_problem' in item_class or 'seq_other' in item_class:
            item_type = 'problem'
            item_url = lecture_url
        else:
            raise AttributeError('Lecture item not consistent: %s, %s' % (item_class, lecture_url))
        items.append({
            'item_type': item_type,
            'item_url': item_url,
        })

    return items

def __ware__(opener, url, need_items=True):
    page = opener.open(url).read()
    page = BeautifulSoup(page)

    chapters = []
    for chapter in page.findAll('div', attrs={'class': 'chapter'}):
        ch_title = chapter.find('h3').text.strip()

        lectures = []
        for lecture in chapter.findAll('li', attrs={'class': ' graded'}):
            le_title = lecture.find('p').text
            le_url = full_url(lecture.find('a').attrs['href'])
            lecture_basis = {
                'lecture_title': le_title,
                'lecture_url': le_url,
            }
            if need_items:
                lecture_basis['lecture_items'] = __items__(opener, le_url)

            lectures.append(lecture_basis)

        chapters.append({
            'chapter_title': ch_title,
            'chapter_lectures': lectures,
        })

    return chapters

def courses_ware(email, password, url):
    url = __courseware_url__(url)
    opener = __get_opener__(email, password)

    return __ware__(opener, url, need_items=True)
