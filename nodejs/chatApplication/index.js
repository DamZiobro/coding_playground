/*
 * index.js
 * Copyright (C) 2017 damian <damian@damian-work>
 *
 * Distributed under terms of the MIT license.
 */

var app = require('express')();
var http = require('http').Server(app);
var io = require('socket.io')(http)

app.get('/', function(req, res){
  res.sendFile(__dirname + "/index.html");
});

io.on('connection', function(socket) {
  console.log('new user connected');

  socket.on('disconnect',function(){
    console.log('user disconnected');
  });

  socket.on('chat message', function(msg){
    console.log('message: ' + msg); 
    io.emit('chat message', msg);
  });
});

http.listen(3000, function(){
  console.log('Start http server listen on *:3000');
});
   

