package com.example.digitrecognition;

import com.google.gson.annotations.SerializedName;

public class ImageClass {

    @SerializedName("caption")
    private String caption;

    public ImageClass(String caption) {
        this.caption = caption;
    }

    public String getCaption() {
        return caption;
    }
}
