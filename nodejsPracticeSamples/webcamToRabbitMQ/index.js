/*
 * index.js
 * Copyright (C) 2017 Damian Ziobro <damian@xmementoit.com>
 *
 * Distributed under terms of the MIT license.
 */

var app = require('express')();
var http = require('http').Server(app);
var io = require('socket.io')(http)
var fs = require('fs');
var rabbitmq = require('amqplib');

function rabbitMQSendFrame(rabbitMQAddress, queue, frame) {
  //console.log("Sending RabbitMQ message to queue '%s' on address %s", queue, rabbitMQAddress);
  rabbitmq.connect(rabbitMQAddress).then(function(connection){
    //console.log("RabbitMQ connected");
    return connection.createChannel().then( function(channel){

      //console.log("RabbitMQ - channel created");
      var isChannel = channel.assertQueue(queue, {durable: true});

      return isChannel.then(function(isChannelOK) {
        //console.log("RabbitMQ - queue found");
        channel.sendToQueue(queue, new Buffer(frame));
        console.log("Frame sent to rabbitMQ queue: %s", queue);
        return channel.close();
      }).catch(console.warn);
    }).finally(function() { connection.close(); });
  }).catch(console.warn);
}

app.get('/', function(req, res){
  res.sendFile(__dirname + "/index.html");
});

io.on('connection', function(socket) {
  console.log('new user connected');

  socket.on('disconnect',function(){
    console.log('user disconnected');
  });

  socket.on('videoFrame', function(frame){
    //========================================================================
    // write that frame received to console log
    console.log('frame received'); 

    //========================================================================
    // save frame to file
    fs.writeFile("/tmp/frame.jpg", frame, function(err){
      if(err) {
        return console.log(err);
      }
      console.log("Frame saved to file/tmp/frame.jpg ");
    });

    //========================================================================
    // push frame to RabbitMQ queue
    var rabbitMQAddress = "amqp://localhost";
    var queue = "html.Q.frames";
    rabbitMQSendFrame(rabbitMQAddress, queue, frame);
    
    //========================================================================
    
  });
});

http.listen(3000, function(){
  console.log('Start nodejs HTTP server listen on *:3000');
});
   

