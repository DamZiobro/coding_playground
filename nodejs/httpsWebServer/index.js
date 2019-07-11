/*
 * index.js
 * Copyright (C) 2017 damian <damian@damian-desktop>
 *
 * Distributed under terms of the MIT license.
 */

var https = require('https');
var fs = require('fs');

var httpsOptions = {
    key: fs.readFileSync('key.pem'),
    cert: fs.readFileSync('cert.pem')
};

var app = function (req, res) {
  res.writeHead(200);
  res.end("hello world\n");
}

https.createServer(httpsOptions, app).listen(4433);
