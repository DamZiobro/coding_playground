var video_element = document.querySelector('#camera-stream');

var canvas = document.querySelector('#canvas');
var ctx = canvas.getContext('2d');

var socket = new io();

navigator.getUserMedia = navigator.getUserMedia || navigator.webkitGetUserMedia || navigator.mozGetUserMedia || navigator.msGetUserMedia;
window.URL = window.URL || window.webkitURL || window.mozURL || window.msURL;

if (navigator.getUserMedia) {
  // Request the camera.
  navigator.getUserMedia(
      // Constraints
      {
        video: true,
        audio: false
      },

      // Success Callback
      function(stream) {
        if (video_element.mozCaptureStream) { // Needed to check for Firefox
          video_element.mozSrcObject = stream;
        } else {
          video_element.src = (window.URL && window.URL.createObjectURL(stream)) || stream;
        }
        video_element.play();
      },

      // Error Callback
      function(err) {
        // Log the error to the console.
        console.log('The following error occurred when trying to use getUserMedia:' + err);
      }
  );

  timer = setInterval(function() {
    ctx.drawImage(video_element, 0,0,320,240);
    var webcamFrameData = canvas.toDataURL('image/jpeg',1.0);
    var blobData = dataURItoBlob(webcamFrameData);
    //socket.emit('frameReceived', blobData);
    //socket.emit(frameReceived, "Test Text => WebSocket");
  },1000);

} else {
  alert('Sorry, your browser does not support getUserMedia');
}

function dataURItoBlob (dataURI) {
  // convert base64 to raw binary data held in a string
  // doesn't handle URLEncoded DataURIs
  var byteString;
  if (dataURI.split(',')[0].indexOf('base64') >= 0)
    byteString = atob(dataURI.split(',')[1]);
  else
    byteString = unescape(dataURI.split(',')[1]);
  // separate out the mime component
  var mimeString = dataURI.split(',')[0].split(':')[1].split(';')[0];

  // write the bytes of the string to an ArrayBuffer
  var ab = new ArrayBuffer(byteString.length);
  var ia = new Uint8Array(ab);
  for (var i = 0; i < byteString.length; i++) {
    ia[i] = byteString.charCodeAt(i);
  }

  // write the ArrayBuffer to a blob, and you're done
  return new Blob([ab],{type: mimeString});
}

socket.on ('frameReceived', function(msg) {                               
  console.log("received message from nodejs http server: " + msg);
}); 
