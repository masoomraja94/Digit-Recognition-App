package com.example.digitrecognition;

import retrofit2.Call;
import retrofit2.http.Field;
import retrofit2.http.FormUrlEncoded;
import retrofit2.http.Headers;
import retrofit2.http.POST;

public interface ApiInterface {

    //@Headers("Content-Type: application/json")
    @FormUrlEncoded
    @POST("/")
    Call<ImageClass> uploadImage(@Field("image") String image);
}
