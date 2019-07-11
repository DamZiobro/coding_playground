package com.example.max.websockettest.webrtc.commands;

import org.json.JSONException;
import org.json.JSONObject;

/**
 * Created by Max on 13-4-2015.
 */
public class RegisterNameCommand extends RtcCommandBase{
    private String name;

    public RegisterNameCommand(String name) {
        this.name = name;

    }

    @Override
    public String compile() throws JSONException {
        JSONObject json = new JSONObject();
        json.put("id", "register");
        json.put("name", name);
        return json.toString();
    }
}
