XuetangX Server
===============

http://xuetangxserver.sinaapp.com/


**NOTE**: Remember to CHANGE POST TO GET after dev


Design
------

- xuetangx  => main

- ^student/ -- ^verify/$    POST email, password => true/false
            |- ^info/$      POST email, password => name, nickname

- ^courses/ -- ^selected$   POST email, password => all selected courses
            |- ^upcoming/$  POST email, password => upcoming courses
            |- ^current/$   POST email, password => current courses
            |- ^past/$      POST email, password => past courses
            |- ^search/$    POST category, started, hasTA => satisfied courses
            |- ^about/$     POST url => course introduction page
            |- ^info/$      POST email, password, url => course main page
            |- ^ware/$      POST email, password, url => courseware page

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


APIs
----

### student

#### verify (atually, no extra field is needed)

    POST { 'email': str, 'password': str }
    => { 'student.verify': bool }

#### info

    POST { 'email': str, 'password': str }
    => { 'student.name': str, 'student.nickname': str }


### courses

#### selected

    POST { 'email': str, 'password': str }
    =>

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
        'course_info_url': str,
    }

#### past

    POST { 'email': str, 'password': str }
    =>

#### search

    POST { 'key': str, 'category': str, 'started': bool, 'hasTA': bool }
    =>

#### about

    POST { 'url': str }
    =>

#### info

    POST { 'email': str, 'password': str, 'url': str }
    =>

#### ware

    POST { 'email': str, 'password': str, 'url': str }
    =>

