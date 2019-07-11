package com.example.max.websockettest;

import android.app.Activity;
import android.content.Context;
import android.graphics.Point;
import android.opengl.GLSurfaceView;
import android.os.Build;
import android.os.Bundle;
import android.util.Log;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import com.example.max.websockettest.webrtc.Peer;
import com.example.max.websockettest.webrtc.PeerConnectionParameters;
import com.example.max.websockettest.webrtc.RtcListener;
import com.example.max.websockettest.webrtc.WebRtcClient;
import com.example.max.websockettest.webrtc.commands.AcceptCallCommand;
import com.example.max.websockettest.webrtc.commands.RegisterNameCommand;
import com.example.max.websockettest.webrtc.commands.RejectCallCommand;
import com.koushikdutta.async.ByteBufferList;
import com.koushikdutta.async.DataEmitter;
import com.koushikdutta.async.callback.DataCallback;
import com.koushikdutta.async.http.AsyncHttpClient;
import com.koushikdutta.async.http.WebSocket;
import com.koushikdutta.async.http.socketio.Acknowledge;

import org.json.JSONException;
import org.json.JSONObject;
import org.webrtc.MediaStream;
import org.webrtc.PeerConnectionFactory;
import org.webrtc.SessionDescription;
import org.webrtc.VideoRenderer;
import org.webrtc.VideoRendererGui;


public class MainActivity extends Activity implements RtcListener {
    private static final String TAG = MainActivity.class.getSimpleName();

    private WebRtcClient rtcClient;

    private final static int VIDEO_CALL_SENT = 666;
    private static final String VIDEO_CODEC_VP9 = "VP8";
    private static final String AUDIO_CODEC_OPUS = "opus";
    // Local preview screen position before call is connected.
    private static final int LOCAL_X_CONNECTING = 0;
    private static final int LOCAL_Y_CONNECTING = 0;
    private static final int LOCAL_WIDTH_CONNECTING = 100;
    private static final int LOCAL_HEIGHT_CONNECTING = 100;
    // Local preview screen position after call is connected.
    private static final int LOCAL_X_CONNECTED = 72;
    private static final int LOCAL_Y_CONNECTED = 72;
    private static final int LOCAL_WIDTH_CONNECTED = 25;
    private static final int LOCAL_HEIGHT_CONNECTED = 25;
    // Remote video screen position
    private static final int REMOTE_X = 0;
    private static final int REMOTE_Y = 0;
    private static final int REMOTE_WIDTH = 100;
    private static final int REMOTE_HEIGHT = 100;
    private VideoRendererGui.ScalingType scalingType = VideoRendererGui.ScalingType.SCALE_ASPECT_FILL;
    private GLSurfaceView vsv;
    private VideoRenderer.Callbacks localRender;
    private VideoRenderer.Callbacks remoteRender;

    private String currentFrom;
    private String ourName;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        vsv = (GLSurfaceView) findViewById(R.id.glview_call);
        vsv.setPreserveEGLContextOnPause(true);
        vsv.setKeepScreenOn(true);
        VideoRendererGui.setView(vsv, new Runnable() {
            @Override
            public void run() {
                init();
            }
        });

        // local and remote render
        remoteRender = VideoRendererGui.create(
                REMOTE_X, REMOTE_Y,
                REMOTE_WIDTH, REMOTE_HEIGHT, scalingType, false);
        localRender = VideoRendererGui.create(
                LOCAL_X_CONNECTING, LOCAL_Y_CONNECTING,
                LOCAL_WIDTH_CONNECTING, LOCAL_HEIGHT_CONNECTING, scalingType, true);
    }

    private void init() {
        Point displaySize = new Point();
        getWindowManager().getDefaultDisplay().getSize(displaySize);
        PeerConnectionParameters params = new PeerConnectionParameters(
                true, false, displaySize.x, displaySize.y, 30, 1, VIDEO_CODEC_VP9, true, 1, AUDIO_CODEC_OPUS, true);
        rtcClient = new WebRtcClient(this, "ws://192.168.0.10:8080/call", params, VideoRendererGui.getEGLContext());
    }


    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.menu_main, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();

        //noinspection SimplifiableIfStatement
        if (id == R.id.action_settings) {
            return true;
        }

        return super.onOptionsItemSelected(item);
    }

    public void onClick(View view) {
        switch(view.getId()) {
            case R.id.register_name_button:
                EditText editText = (EditText)findViewById(R.id.register_name_text);
                ourName = editText.getText().toString();
                rtcClient.sendMessage(new RegisterNameCommand(ourName));
                rtcClient.setCamera();
                break;
            case R.id.call_answer_button:
                Peer peer = rtcClient.getPeer(currentFrom);
                peer.pc.createOffer(peer, rtcClient.pcConstraints);
                break;
            case R.id.call_reject_button:
                rtcClient.sendMessage(new RejectCallCommand((String) view.getTag(), RejectCallCommand.USER_REJECT));
            default:
                Toast.makeText(this, "Not yet implemented", Toast.LENGTH_SHORT).show();
        }
    }

    @Override
    public void onCallReceived(String from) {
        runOnUiThread(new Runnable() {
            @Override
            public void run() {
                Button answerButton = (Button) findViewById(R.id.call_answer_button);
                answerButton.setVisibility(View.VISIBLE);
                Button rejectButton = (Button) findViewById(R.id.call_reject_button);
                rejectButton.setVisibility(View.VISIBLE);
            }
        });

        currentFrom = from;
    }

    @Override
    public void onCallReady(String callId) {

    }

    @Override
    public void onStatusChanged(String newStatus) {

    }

    @Override
    public void onLocalStream(MediaStream localStream) {
        Log.d(TAG, "onLocalStream");
        localStream.videoTracks.get(0).addRenderer(new VideoRenderer(localRender));
        VideoRendererGui.update(localRender,
                LOCAL_X_CONNECTING, LOCAL_Y_CONNECTING,
                LOCAL_WIDTH_CONNECTING, LOCAL_HEIGHT_CONNECTING,
                scalingType);
    }

    @Override
    public void onAddRemoteStream(MediaStream remoteStream) {
        Log.d(TAG, "onAddRemoteStream");
        remoteStream.videoTracks.get(0).addRenderer(new VideoRenderer(remoteRender));
        VideoRendererGui.update(remoteRender,
                REMOTE_X, REMOTE_Y,
                REMOTE_WIDTH, REMOTE_HEIGHT, scalingType);
        VideoRendererGui.update(localRender,
                LOCAL_X_CONNECTED, LOCAL_Y_CONNECTED,
                LOCAL_WIDTH_CONNECTED, LOCAL_HEIGHT_CONNECTED,
                scalingType);
    }

    @Override
    public void onRemoveRemoteStream(int endPoint) {
        Log.d(TAG, "onRemoveRemoteStream");
        VideoRendererGui.update(localRender,
                LOCAL_X_CONNECTING, LOCAL_Y_CONNECTING,
                LOCAL_WIDTH_CONNECTING, LOCAL_HEIGHT_CONNECTING,
                scalingType);
    }
}
