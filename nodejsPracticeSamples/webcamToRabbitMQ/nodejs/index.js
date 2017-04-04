/*
 * index.js
 * Copyright (C) 2017 damian <damian@damian-work>
 *
 * Distributed under terms of the MIT license.
 */

var app = require('express')();
var http = require('http').Server(app);
var io = require('socket.io')(http)
var fs = require('fs');
var rabbitmq = require('amqplib/callback_api');

function rabbitMQFrames(rabbitMQAddress, callback) {
  rabbitmq.connect(rabbitMQAddress, function amqpConnectCallback(err, rabbitMQConn){
    if(err){
      return callback(err);
    }

    rabbitMQExchangeName = 'html.Q.frames';
    rabbitMQQueueName = 'html.Q.frames';

    rabbitMQConn.createChannel(function(err, channel) {
        if(err){
          return callback(err);
        }
        
        channel.assertExchange(rabbitMQExchangeName, 'fanout', {durable:true});

        channel.assertQueue(rabbitMQQueueName, {exclusive: false}, function(err, rabbitMQqueue) {
          if(err) {
            return callback(err);
          }

          channel.bindQueue(rabbitMQqueue.queue, rabbitMQExchangeName, '');
          
          var options = {
            emitMessage : emitMessage ,
            onMessageReceived: onMessageReceived
          }

          channel.consume(rabbitMQqueue.queue, function(message) {
            options.onMessageReceived(message);
          }, {noAck: true});

          callback(null, options);

          function emitMessage(message){
            console.log("publish message in rabbitMQ");
            channel.publish(rabbitMQExchangeName, '', new Buffer(message)); 
          }

          function onMessageReceived() {
            console.log("Message received.") 
          }
        });
         
    });
  });
}

app.get('/', function(req, res){
  res.sendFile(__dirname + "/index.html");
});

var rabbitMQHandler = rabbitMQFrames("amqp://localhost", function(err, options){
  if(err) {
    throw err; 
  }
  options.onMessageReceived = onMessageReceived;

  //function for sending messages back from nodejs to client site
  function onMessageReceived(message){
    io.emit('videoFrame', message);
  }

    
  io.on('connection', function(socket) {
    console.log('new user connected');

    socket.on('disconnect',function(){
      console.log('user disconnected');
    });

    socket.on('videoFrame', function(msg){
      //========================================================================
      // write that frame received to console log
      console.log('frame received'); 

      //========================================================================
      // save frame to file
      fs.writeFile("/tmp/frame.jpg", msg, function(err){
        if(err) {
          return console.log(err);
        }
        console.log("Frame saved to file/tmp/frame.jpg ");
      });

      //========================================================================
      // push frame to RabbitMQ queue
      options.emitMessage(msg);
      
      //========================================================================
      
    });
  });
});

http.listen(3000, function(){
  console.log('Start nodejs HTTP server listen on *:3000');
});
   

