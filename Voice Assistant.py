import speech_recognition as sr
from playsound import playsound
from gtts import gTTS
import os
import time
import requests
import json
import wolframalpha
from googletrans import Translator

# import yfinance

crypto_api='https://api.coingecko.com/api/v3/simple/price?ids=bitcoin%2Cdogecoin%2Cethereum&vs_currencies=usd'
wolfram_api='6V9L46-T73W33J9JV'
chuck_norris_api="https://api.chucknorris.io/jokes/random"
new_api_key="e03e4c1d4b2040bab673e23c7b243260"
weather_api_key="9963e71b6a74489296855a0919a0d61f"

def listen():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source);
        text="";
         
        try:
            text=r.recognize_google(audio)
        
        except sr.RequestError as re:
            print(re)

        except sr.UnknownValueError as uve:
            print(uve)

        except sr.WaitTimeoutError as wte:
            print(wte)

    text=text.lower()
    return text;


def talk(text):
    file_ka_naam="audio.mp3"
    voice=gTTS(text=text,lang="en",slow=False)
    voice.save(file_ka_naam)
    #time.sleep(1)
    playsound(file_ka_naam)
    os.remove(file_ka_naam)

def talkInDestLang(text,lang):
    file_ka_naam="audio.mp3"
    voice=gTTS(text=text,lang=lang,slow=False)
    voice.save(file_ka_naam)
    #time.sleep(1)
    playsound(file_ka_naam)
    os.remove(file_ka_naam)



#talk("main hemant hu or main apne project par kaam kar raha hu")

def reply(text):

    #smallTalk
    if 'what' in text and 'name' in text:
        talk("mera naam reema hai main teri assistant hu")

    #smallTalk
    elif 'stop' in text:
        talk("mujhe bhi baat karke maza aaya")

    #smallTalk
    elif 'when' in text and 'sleep' in text:
        talk("waise to jaldi so jati hu par aaj kal 2 baje so rhi hu")

    #smallTalk
    elif 'favourite' in text and 'song' in text:
        talk("mera favourite gaana Rowdy Baby hai")

    #smallTalk
    elif 'you' in text and 'stupid' in text:
        talk("nahi main nahi stupid hu")
    
    #cryptoCurrency - Bitcoin
    elif 'bitcoin' in text:
        response=requests.get(crypto_api)
        crypto_json=response.json()
        talk("Abhi bitcoin ka price hai" + str(crypto_json['bitcoin']['usd'])+" US Dollar")

    #cryptoCurrency - Dogecoin
    elif 'dogecoin' in text:
        response=requests.get(crypto_api)
        crypto_json=response.json()
        talk("Abhi dogecoin ka price hai" + str(crypto_json['dogecoin']['usd'])+" US Dollar")

    #cryptoCurrency - Ethereum
    elif 'ethereum' in text:
        response=requests.get(crypto_api)
        crypto_json=response.json()
        talk("Abhi ethereum ka price hai" + str(crypto_json['ethereum']['usd'])+" US Dollar")

    # Basic Questions
    elif 'prime minister' in text or 'president' in text or 'capital' in text or 'date of birth'in text or 'ceo' in text or 'wife' in text or 'husband' in text or 'city' in text or 'country' in text :
        walfram_alpha(text)

    # Calculator
    elif '+' in text or '-' in text or 'multiply' in text or '*' in text or '/' in text or 'root' in text:
        walfram_alpha_calculator(text)

    elif 'translate' in text:
        while True:
            talk("What do you need to translate?")
            text=listen()
            if text!='turn off translator' and text!=' ':
                translate(text)
            else:
                talk("Translator is turned off,what else you want to do")
                break

    elif 'chuck norris' in text:
        chuck_norris()

    elif 'news' in text:
        talk("let me tell you some headlines");
        get_news()
    
    elif 'weather' in text:
        get_weather()

    else:
        talk("samajh nahi aara kya bol rha hai")

def execute():
    talk("hi main Reema,apna naam bata");
    name=listen()
    talk("or" + name + "kya haal hai");
    while True:
        message=listen()
        print(message)
        reply(message)

        if 'goodbye' in message:
            break;

def walfram_alpha(text):
    client =wolframalpha.Client(wolfram_api)
    res = client.query(text)
    ans=next(res.results).text
    print(ans)
    talk(ans);


def walfram_alpha_calculator(text):
    client =wolframalpha.Client(wolfram_api)
    res = client.query(text)
    ans=next(res.results).text
    print(ans)
    talk(ans);

def translate(text):
    translator=Translator()
    out=translator.translate(text,dest="de").text
    talkInDestLang(out,"de")

def chuck_norris():
    data=requests.get(chuck_norris_api);
    json=data.json()
    joke=json['value'];
    print(joke)
    talk(joke)

def get_news():
    news_url="https://newsapi.org/v2/top-headlines?country=in&apiKey=" +new_api_key
    data=requests.get(news_url).json()
    articles = data['articles']
    news_headlines=[]
    for art in articles:
        headlines=art['title']
        news_headlines.append(headlines)
    for i in range(3):
        print(news_headlines[i])
        talk(news_headlines[i])

def get_weather():
    talk("what city are u interested in?")
    city=listen()
    print(city)
    weather_api_url="https://api.weatherbit.io/v2.0/current?&city="+ city + "&key=" + weather_api_key
    data=requests.get(weather_api_url)
    json=data.json()
    temp=json['data'][0]['temp']
    weather=json['data'][0]['weather']['description']
    final_weather="Temperature in "+city+" is "+str(temp) +" degrees and you can see "+weather
    print(final_weather)
    talk(final_weather)

# execute()
















