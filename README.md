XuetangX Server
===============

http://xuetangxserver.sinaapp.com/


Design
------

```
- xuetangx  => main

- client    => handle http(s) request

- ^student/ -- ^verify/$    POST email, password => true/false
            |- ^info/$      POST email, password => name, nickname

- ^courses/ -- ^$           POST email, password => courses selected
            |- ^upcoming/$  POST email, password => upcoming courses
            |- ^current/$   POST email, password => current courses
            |- ^past/$      POST email, password => past courses
            |- ^search/$    POST category, started, hasTA => satisfied courses
            |- ^about/$     POST url => course introduction page
            |- ^info/$      POST email, password, url => course main page
            |- ^ware/$      POST email, password, url => courseware page

```
