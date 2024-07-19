package com.example.service;

import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

@Service
public class WeatherService {

    private final String apiUrl = "http://api.weatherapi.com/v1/current.json?key=YOUR_API_KEY&q=London";

    public String getWeather() {
        RestTemplate restTemplate = new RestTemplate();
        return restTemplate.getForObject(apiUrl, String.class);
    }
}
