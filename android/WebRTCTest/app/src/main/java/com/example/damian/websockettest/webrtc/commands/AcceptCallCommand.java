package com.example.max.websockettest.webrtc.commands;

import org.json.JSONException;
import org.json.JSONObject;

/**
 * Created by Max on 13-4-2015.
 */
public class AcceptCallCommand extends RtcCommandBase {
    private final String from;
    private final String sdpOffer;

    public AcceptCallCommand(String from, String sdpOffer) {
        this.from = from;
        this.sdpOffer = sdpOffer;
    }

    @Override
    public String compile() throws JSONException {
        JSONObject json = new JSONObject();
        json.put("id", "incomingCallResponse");
        json.put("from", from);
        json.put("callResponse", "accept");
        json.put("sdpOffer", sdpOffer);
        return json.toString();
    }
}
