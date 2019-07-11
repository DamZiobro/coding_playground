package com.example.max.websockettest.webrtc;

import android.content.Context;
import android.opengl.EGLContext;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;

import com.example.max.websockettest.R;
import com.example.max.websockettest.webrtc.commands.RejectCallCommand;
import com.example.max.websockettest.webrtc.commands.RtcCommandBase;
import com.koushikdutta.async.http.AsyncHttpClient;
import com.koushikdutta.async.http.WebSocket;

import org.json.JSONException;
import org.json.JSONObject;
import org.webrtc.AudioSource;
import org.webrtc.IceCandidate;
import org.webrtc.MediaConstraints;
import org.webrtc.MediaStream;
import org.webrtc.PeerConnection;
import org.webrtc.PeerConnectionFactory;
import org.webrtc.SessionDescription;
import org.webrtc.VideoCapturer;
import org.webrtc.VideoCapturerAndroid;
import org.webrtc.VideoSource;

import java.net.Socket;
import java.net.URISyntaxException;
import java.util.HashMap;
import java.util.LinkedList;

/**
 * Created by Max on 10-4-2015.
 */
public class WebRtcClient implements AsyncHttpClient.WebSocketConnectCallback, WebSocket.StringCallback {
    private final static String TAG = WebRtcClient.class.getCanonicalName();
    private final static int MAX_PEER = 2;
    private static final int CALLSTATE_IN_CALL = 3;
    private boolean[] endPoints = new boolean[MAX_PEER];
    public PeerConnectionFactory factory;
    private HashMap<String, Peer> peers = new HashMap<>();
    public LinkedList<PeerConnection.IceServer> iceServers = new LinkedList<>();
    private PeerConnectionParameters pcParams;
    public MediaConstraints pcConstraints = new MediaConstraints();
    public MediaStream localMS;
    private VideoSource videoSource;
    public RtcListener mListener;
    private WebSocket socket;

    private int callState;

    private static final int CALLSTATE_NO_CALL = 0;
    private static final int CALLSTATE_POST_CALL = 1;
    private static final int CALLSTATE_DISABLED = 2;

    public WebRtcClient(RtcListener listener, String host, PeerConnectionParameters params, EGLContext mEGLcontext) {
        mListener = listener;
        pcParams = params;
        PeerConnectionFactory.initializeAndroidGlobals(listener, true, true,
                params.videoCodecHwAcceleration, mEGLcontext);
        factory = new PeerConnectionFactory();

        AsyncHttpClient.getDefaultInstance().websocket(host, null, this);

        iceServers.add(new PeerConnection.IceServer("stun:23.21.150.121"));
        iceServers.add(new PeerConnection.IceServer("stun:stun.l.google.com:19302"));

        pcConstraints.mandatory.add(new MediaConstraints.KeyValuePair("OfferToReceiveAudio", "true"));
        pcConstraints.mandatory.add(new MediaConstraints.KeyValuePair("OfferToReceiveVideo", "true"));
        pcConstraints.optional.add(new MediaConstraints.KeyValuePair("DtlsSrtpKeyAgreement", "true"));
    }

    public void sendMessage(RtcCommandBase message) {
        if(socket != null && socket.isOpen()) {
            try {
                socket.send(message.compile());
            } catch(JSONException jse) {
                Log.e(TAG, jse.getMessage());
            }
        }
    }

    private Peer addPeer(String id, int endPoint) {
        Peer peer = new Peer(this, id, endPoint);
        peers.put(id, peer);

        endPoints[endPoint] = true;
        return peer;
    }

    private void removePeer(String id) {
        Peer peer = peers.get(id);
        mListener.onRemoveRemoteStream(peer.endPoint);
        peer.pc.close();
        peers.remove(peer.id);
        endPoints[peer.endPoint] = false;
    }

    private int findEndPoint() {
        for(int i = 0; i < MAX_PEER; i++) if (!endPoints[i]) return i;
        return MAX_PEER;
    }

    @Override
    public void onCompleted(Exception ex, WebSocket webSocket) {
        socket = webSocket;
        socket.setStringCallback(this);
    }

    @Override
    public void onStringAvailable(final String s) {
        System.out.println("I got a string: " + s);
        JSONObject parsedMessage = null;
        try {
            parsedMessage = new JSONObject(s);
        } catch (JSONException e) {
            e.printStackTrace();
        }

        if (parsedMessage != null) {
            String messageId = "";
            try {
                messageId = parsedMessage.getString("id");
                if(parsedMessage.has("from")) {
                    String from = parsedMessage.getString("from");
                    if(!peers.containsKey(from)) {
                        int endPoint = findEndPoint();
                        if(endPoint != MAX_PEER) {
                            Peer peer = addPeer(from, endPoint);
                            peer.pc.addStream(localMS);
                        }
                    }
                }
            } catch (JSONException e) {
                e.printStackTrace();
            }
            switch (messageId) {
                case "resgisterResponse":
                    registerResponse(parsedMessage);
                    break;
            /* case 'callResponse':
                callResponse(parsedMessage);
                break;*/

                case "incomingCall":
                    incomingCall(parsedMessage);
                    break;

                case "startCommunication":
                    startCommunication(parsedMessage);
                    break;
            /*
            case 'stopCommunication':
                console.info("Communication ended by remote peer");
                stop(true);
                break;
            case 'playResponse':
                playResponse(parsedMessage);
                break;
            case 'playEnd':
                playEnd();
                break;*/
                default:
                    Log.i(TAG, "JSON Request not handled");
            }
        } else {
            Log.i(TAG, "Invalid JSON");
        }
    }

    private void incomingCall(JSONObject parsedMessage) {
        // If bussy just reject without disturbing user
        String from = "";
        try {
            from = parsedMessage.getString("from");
        } catch (JSONException e) {
            e.printStackTrace();
        }

        if (callState != CALLSTATE_NO_CALL && callState != CALLSTATE_POST_CALL) {
            sendMessage(new RejectCallCommand(from, RejectCallCommand.USER_BUSY));
        } else {
            mListener.onCallReceived(from);
        }

        setCallState(CALLSTATE_DISABLED);
    }

    private void startCommunication(JSONObject parsedMessage) {
        setCallState(CALLSTATE_IN_CALL);
        Log.d(TAG,"SDP answer received, setting remote description");
        try {
            SessionDescription sdpAnswer = new SessionDescription(SessionDescription.Type.ANSWER, parsedMessage.getString("sdpAnswer"));
            String from = parsedMessage.getString("from");
            Peer peer = peers.get(from);
            peer.pc.setRemoteDescription(peer, sdpAnswer);
        } catch (JSONException e) {
            e.printStackTrace();
        }
    }

    private void setCallState(int newState) {
        callState = newState;
    }

    private void registerResponse(JSONObject message) {
        try {
            String response = message.getString("response");
            if (response.equalsIgnoreCase("accepted")) {
                Log.i(TAG, "Register success");
            } else {
                String errorMessage = !message.getString("message").isEmpty() ? message.getString("message") : "Unknown register rejection reason";
                Log.e("RegisterResponse", errorMessage);
                Log.i(TAG, "Error registering user. See console for further information.");
            }
        } catch (JSONException e) {
            e.printStackTrace();
        }
    }

    public void setCamera(){
        localMS = factory.createLocalMediaStream("ARDAMS");
        if(pcParams.videoCallEnabled){
            MediaConstraints videoConstraints = new MediaConstraints();
            videoConstraints.mandatory.add(new MediaConstraints.KeyValuePair("maxHeight", Integer.toString(pcParams.videoHeight)));
            videoConstraints.mandatory.add(new MediaConstraints.KeyValuePair("maxWidth", Integer.toString(pcParams.videoWidth)));
            videoConstraints.mandatory.add(new MediaConstraints.KeyValuePair("maxFrameRate", Integer.toString(pcParams.videoFps)));
            videoConstraints.mandatory.add(new MediaConstraints.KeyValuePair("minFrameRate", Integer.toString(pcParams.videoFps)));

            videoSource = factory.createVideoSource(getVideoCapturer(), videoConstraints);
            localMS.addTrack(factory.createVideoTrack("ARDAMSv0", videoSource));
        }

        AudioSource audioSource = factory.createAudioSource(new MediaConstraints());
        localMS.addTrack(factory.createAudioTrack("ARDAMSa0", audioSource));

        mListener.onLocalStream(localMS);
    }

    private VideoCapturer getVideoCapturer() {
        String frontCameraDeviceName = VideoCapturerAndroid.getNameOfFrontFacingDevice();
        return VideoCapturerAndroid.create(frontCameraDeviceName);
    }

    public Peer getPeer(String id) {
        return peers.get(id);
    }
}
