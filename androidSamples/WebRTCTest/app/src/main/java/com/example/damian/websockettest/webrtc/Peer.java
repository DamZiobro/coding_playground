package com.example.max.websockettest.webrtc;

import android.util.Log;

import com.example.max.websockettest.webrtc.commands.AcceptCallCommand;

import org.json.JSONException;
import org.json.JSONObject;
import org.webrtc.DataChannel;
import org.webrtc.IceCandidate;
import org.webrtc.MediaStream;
import org.webrtc.PeerConnection;
import org.webrtc.SdpObserver;
import org.webrtc.SessionDescription;

/**
 * Created by Max on 13-4-2015.
 */
public class Peer implements SdpObserver, PeerConnection.Observer {
    private static final String TAG = Peer.class.getCanonicalName();
    public PeerConnection pc;
    public String id;
    private WebRtcClient client;
    public int endPoint;

    @Override
    public void onCreateSuccess(final SessionDescription sdp) {
        // TODO: modify sdp to use pcParams prefered codecs
        Log.d(TAG, sdp.type.canonicalForm());

        switch(sdp.type.canonicalForm()) {
            case "offer":
                break;
            case "answer":
                break;
            case "pranswer":
                break;
        }

        client.sendMessage(new AcceptCallCommand(id, sdp.description));
        pc.setLocalDescription(Peer.this, sdp);
    }

    @Override
    public void onSetSuccess() {}

    @Override
    public void onCreateFailure(String s) {
        Log.d(TAG, "onCreateFailure: " + s);
    }

    @Override
    public void onSetFailure(String s) {
        Log.d(TAG, "onSetFailure: " + s);
    }

    @Override
    public void onSignalingChange(PeerConnection.SignalingState signalingState) {
        Log.d(TAG, "onSignalingChange: " + signalingState.name());
    }

    @Override
    public void onIceConnectionChange(PeerConnection.IceConnectionState iceConnectionState) {
        if(iceConnectionState == PeerConnection.IceConnectionState.DISCONNECTED) {
           // mListener.onStatusChanged("DISCONNECTED");
            //removePeer(id);
        }
    }

    @Override
    public void onIceGatheringChange(PeerConnection.IceGatheringState iceGatheringState) {}

    @Override
    public void onIceCandidate(final IceCandidate candidate) {
        try {
            Log.d("TAG", "onIceCandidate");
            JSONObject payload = new JSONObject();
            payload.put("label", candidate.sdpMLineIndex);
            payload.put("id", candidate.sdpMid);
            payload.put("candidate", candidate.sdp);
            //client.sendMessage(id, "candidate", payload);
        } catch (JSONException e) {
            e.printStackTrace();
        }
    }

    @Override
    public void onAddStream(MediaStream mediaStream) {
        Log.d(TAG, "onAddStream " + mediaStream.label());
        // remote streams are displayed from 1 to MAX_PEER (0 is localStream)
        client.mListener.onAddRemoteStream(mediaStream);
    }

    @Override
    public void onRemoveStream(MediaStream mediaStream) {
        Log.d(TAG,"onRemoveStream "+mediaStream.label());
        //removePeer(id);
    }

    @Override
    public void onDataChannel(DataChannel dataChannel) {}

    @Override
    public void onRenegotiationNeeded() {
        Log.d("TAG", "onRenegotiationNeeded");
    }

    public Peer(WebRtcClient client, String id, int endPoint) {
        Log.d("Peer","new Peer: " + id);
        this.client = client;
        this.pc = client.factory.createPeerConnection(client.iceServers, client.pcConstraints, this);
        this.id = id;
        this.endPoint = endPoint;

        pc.addStream(client.localMS); //, new MediaConstraints()

       //client.mListener.onStatusChanged("CONNECTING");
    }
}