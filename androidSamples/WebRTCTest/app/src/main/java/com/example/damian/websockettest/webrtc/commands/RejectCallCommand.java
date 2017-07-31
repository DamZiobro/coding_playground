package com.example.max.websockettest.webrtc.commands;

import org.json.JSONException;
import org.json.JSONObject;

/**
 * Created by Max on 13-4-2015.
 */
public class RejectCallCommand extends RtcCommandBase {
    public static final String USER_REJECT = "user rejected";
    public static final String USER_BUSY = "bussy";
    private String from;
    private String reason;

    public RejectCallCommand(String from, String reason) {
        this.from = from;
        this.reason = reason;
    }

    @Override
    public String compile() throws JSONException {
        JSONObject json = new JSONObject();
        json.put("id", "incomingCallResponse");
        json.put("from", from);
        json.put("callResponse", "reject");
        json.put("message", reason);
        return json.toString();
    }
}
