/*
 * main.js
 * Copyright (C) 2017 Damian Ziobro <damian@xmementoit.com>
 *
 * Distributed under terms of the MIT license.
 */

function onLoadMetadataCallback(e) {
  console.log("Getting metadata...");
}

function getMediaErrorCallback(e) {
  console.log("Rejected...", e);
};

function getMediaSuccessCallback(localMediaStream) {
  console.log("Getting audio/video media successfull...");
  var video = document.querySelector('video#usermedia');
  video.src = window.URL.createObjectURL(localMediaStream);

  video.onloadedmetadata = onLoadMetadataCallback;
}

options = {
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
