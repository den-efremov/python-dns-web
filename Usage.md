# Introduction #

When you've started the application you can test if its working by typing http://127.0.0.1/ in your browser.


# Http Actions #

## Add zone entry ##
http://127.0.0.1/dns/add
  * **parameters**
  * name
  * host
**example**
http://127.0.0.1/dns/add?name=olav&host=192.168.1.5

## Update zone name ##
http://127.0.0.1/dns/editName
  * **parameters**
  * from
  * to
**example**
http://127.0.0.1/dns/editName?from=olav&to=james


## Update zone host ##
http://127.0.0.1/dns/editHost
  * **parameters**
  * host
  * name
**example**
http://127.0.0.1/dns/editHost?name=olav&host=example.org
(The webservice will automaticly add the last dot if it's not supplied)


## Delete zone entry ##
http://127.0.0.1/dns/delete
  * **parameters**
  * name
**example**
http://127.0.0.1/dns/delete?name=olav