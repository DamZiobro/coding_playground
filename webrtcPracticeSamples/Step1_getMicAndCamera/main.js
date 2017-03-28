/*
 * main.js
 * Copyright (C) 2017 Damian Ziobro <damian@xmementoit.com>
 *
 * Distributed under terms of the MIT license.
 */


var getMediaErrorCallback = function(e) {
  console.log("Rejected...", e);
};

var getMediaSuccessCallback = function(localMediaStream) {
  console.log("Getting audio/video media successfull...");
  var video = document.querySelector('video#usermedia');
  video.src = window.URL.createObjectURL(localMediaStream);

  video.onloadedmetadata = function(e) {
    console.log("Getting metadata...");
  }
}

//getting users audio and vidoe (mic and camera)
options = {
  video: true,
  audio: true
}

navigator.getUserMedia(options, getMediaSuccessCallback, getMediaErrorCallback);
