XuetangX Server
===============

http://xuetangxserver.sinaapp.com/

**NOTE**: Remember to CHANGE POST TO GET after dev


APIs
----

```
response header:
    'valid':
    - false => Request format error
    - true
      => 'error':
      + true  => Server error
      + false
        => 'authen':
        - fasle => Email/password error
        - true  => ...
```

### student

#### verify

    POST { 'email': str, 'password': str }
    => { 'student.verify': bool }

#### info

    POST { 'email': str, 'password': str }
    => { 'student.name': str, 'student.nickname': str }


### courses

#### selected

    POST { 'email': str, 'password': str }
    => {
        'courses.upcoming': [@course],
        'courses.current': [@course],
        'courses.past': [@course]
    }

#### upcoming

    POST { 'email': str, 'password': str }
    => { 'courses.upcoming': [@course] }

    @course: {
        'university': str,
        'id': str,
        'title': str,
        'start_date': {
            'year': int,
            'month': int,
            'day': int
        },
        'img_url': str,
    }

#### current

    POST { 'email': str, 'password': str }
    => { 'courses.current': [@course] }

    @course: {
        'university': str,
        'id': str,
        'title': str,
        'start_date': {
            'year': int,
            'month': int,
            'day': int
        },
        'img_url': str,
        'course_info_url': str,
    }

#### past

    POST { 'email': str, 'password': str }
    => { 'courses.past': [@course] }

    @course: {
        'university': str,
        'id': str,
        'title': str,
        'start_date': {
            'year': int,
            'month': int,
            'day': int
        },
        'img_url': str,
        'course_info_url': str,
    }

#### categories

    POST Nothing
    => { 'courses.categories': [@category] }

    @category: {
        'id': str,
        'title': str,
        'count': int
    }

#### search

    POST { 'query': str, 'cid': str, 'started': str, 'hasTA': str } (All fields are optional)
    => { 'courses.search': [@course] }

    @course: {
        'owner': str,
        'university': str,
        'id': str,
        'title': str,
        'img_url': str,
        'course_about_url': str,
        'teacher': {
            'name': str, # may be empty str
            'title': str, # may be empty str
        },
        'update_info': str,
        'serialized_no': int, # -1 if none
        'hasTA': bool,
        'subtitle': str,
    }

#### unenroll # ONLY courses owner='xuetangX' can do this

    POST { 'email': str, 'password': str, 'url': str } # full course about/info url
    => { 'courses.unenroll': bool }


#### enroll # ONLY courses owner='xuetangX' can do this

    POST { 'email': str, 'password': str, 'url': str } # full course about/info url
    => { 'courses.enroll': bool }


#### lectures # get lecture content

    POST { 'email': str, 'password': str, 'url': str } # course info url
    => {
        'courses.lectures': [@chapter],
    }

    @chapter: {
        'chapter_title': str,
        'chapter_lectures': [@lecture],
    }

    @lecture: {
        'lecture_title': str,
        'lecture_url': str,
    }


#### lecture # get detail of ONE lecture

    POST { 'email': str, 'password': str, 'url': str } # lecture url
    => {
        'courses.lecture': [@item],
    }

    @item: {
        'item_type': str,
        'item_url': str, # see NOTE below
    }

    NOTE:
        if item.item_type == 'problem'
        then
            item.item_url is the full url:str to the lecture which item belonging to
        else -> item.item_type == 'video'
            {
                'high-quality': [str*],
                'low-quality': [str*],
            }


#### ware

    POST { 'email': str, 'password': str, 'url': str } # course info url
    => {
        'courses.ware': [@chapter],
    }

    @chapter: {
        'chapter_title': str,
        'chapter_lectures': [@lecture],
    }

    @lecture: {
        'lecture_title': str,
        'lecture_url': str,
        'lecture_items': [@item],
    }

    @item: {
        'item_type': str,
        'item_url': item_url, # see NOTE below
    }

    NOTE:
        if item.item_type == 'problem'
        then
            item.item_url is the full url:str to the lecture which item belonging to
        else -> item.item_type == 'video'
            {
                'high-quality': [str*],
                'low-quality': [str*],
            }
