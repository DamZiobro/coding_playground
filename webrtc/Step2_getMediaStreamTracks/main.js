/*
 * main.js
 * Copyright (C) 2017 Damian Ziobro <damian@xmementoit.com>
 *
 * Distributed under terms of the MIT license.
 */

var stream;

function onLoadMetadataCallback(e) {
  console.log("Getting metadata...");
}

function getMediaErrorCallback(e) {
  console.log("Rejected...", e);
};

function getMediaSuccessCallback(localMediaStream) {
  stream = localMediaStream;
  console.log("Getting audio/video media successfull...");
  var video = document.querySelector('video#usermedia');
  video.src = window.URL.createObjectURL(localMediaStream);

  video.onloadedmetadata = onLoadMetadataCallback;
}

var options = {
  video: true,
  audio: true
}

//check which getUserMedai method is available in your browser
navigator.getUserMedia  = navigator.getUserMedia ||
                          navigator.webkitGetUserMedia ||
                          navigator.mozGetUserMedia ||
                          navigator.msGetUserMedia;

//getting users audio and vidoe (mic and camera) if possible
if (navigator.getUserMedia) {
  navigator.getUserMedia(options, getMediaSuccessCallback, getMediaErrorCallback);
} else {
  alert("Your browser does not support getUserMedia() element");
}

btnGetAudioTracks.addEventListener("click", function(){ 
   console.log("getAudioTracks"); 
   console.log(stream.getAudioTracks()); 
});
  
btnGetTrackById.addEventListener("click", function(){ 
   console.log("getTrackById"); 
   console.log(stream.getTrackById(stream.getAudioTracks()[0].id)); 
});
  
btnGetTracks.addEventListener("click", function(){ 
   console.log("getTracks()"); 
   console.log(stream.getTracks()); 
});
 
btnGetVideoTracks.addEventListener("click", function(){ 
   console.log("getVideoTracks()"); 
   console.log(stream.getVideoTracks()); 
});

btnRemoveAudioTrack.addEventListener("click", function(){ 
   console.log("removeAudioTrack()"); 
   stream.removeTrack(stream.getAudioTracks()[0]); 
});
  
btnRemoveVideoTrack.addEventListener("click", function(){ 
   console.log("removeVideoTrack()"); 
   stream.removeTrack(stream.getVideoTracks()[0]); 
});
