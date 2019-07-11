package com.example.max.websockettest.webrtc.commands;

import org.json.JSONException;
import org.json.JSONObject;

/**
 * Created by Max on 13-4-2015.
 */
public abstract class RtcCommandBase {
    public abstract String compile() throws JSONException;
}
