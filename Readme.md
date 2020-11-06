# Weather App

This a basic weather app made with falcon and retrieve the data from openweathermap

## how to run it

* install the dependencies
    ``` shell
    pip install -r requirements.txt
    ```
* obtain a key from openweathermap and fill .env file based on .env.example file
    ``` shell
    cp .env.example .env
    ```
* run the project
    ``` shell
    gunicorn config:app
    ```

## Get weather info
You can get weather info doing a GET request to `/weather` and add the params `country` and `city`
> country is a country code of two characters in lowercase. Example: co

> city is a string. Example: Medellín

## Get forecast information
You can get forecast information adding a `day` param to the above request.
> day is a value between 0 and 6 where 0 is today and 6 is 6 days from today
