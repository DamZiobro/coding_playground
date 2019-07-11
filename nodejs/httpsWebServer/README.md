node.js HTTPs server
=============

This is simple node.js app which create HTTPS Web Server based on self-signed
certificate.

Prerequisites
-----
1. Create self-signed certicates:
```
./createSelfSignedCert.sh
```

Usage
----
1. Run HTTPs web server
```
nodejs index.js
```
2. Open it in yur web browser:
```
firefox https://localhost:4433
```

