XuetangX Server
===============

http://xuetangxserver.sinaapp.com/


Design
------

```
- xuetangx  => main

- client    => handle http(s) request

- ^user/ ----- verify/$             POST email, password
         |---- info/$               POST email, password
         |---- courses/$            POST email, password
         |---- courses/upcoming/$   POST email, password
         |---- courses/current/$    POST email, password
         |---- courses/past/$       POST email, password

- ^courses/ -- search/$             POST category, started, hasTA
            |- about/$              POST url
            |- info/$               POST email, password, url
            |- ware/$               POST email, password, url

```
