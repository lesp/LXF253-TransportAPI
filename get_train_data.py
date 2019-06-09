"""
The audio file BingBong.mp3 is provided by the_bloke33 via freesound. https://freesound.org/people/the_bloke33/sounds/83005/ and is provided via a CC-BY 3.0 licence https://creativecommons.org/licenses/by/3.0/
"""
import requests
import vlc
from time import sleep
from gtts import gTTS
from secrets import *
from datetime import datetime, date

current_time = str(datetime.now().time())
current_date = str(date.today())
current_time = current_time[0:5]


url = "https://transportapi.com/v3/uk/train/station/BPN/"+current_date+"/"+current_time+"/timetable.json?app_id="+app_id+"&app_key="+api_key+"&train_status=passenger"
r = requests.get(url)
if r :
        media = vlc.MediaPlayer("bingbong.mp3")
        media.play()
        sleep(4.2)
        for i in range(len(r.json()['departures']['all'])):
                destination = (r.json()['departures']['all'][i]['destination_name'])
                departure = (r.json()['departures']['all'][i]['aimed_departure_time'])
                platform = (r.json()['departures']['all'][i]['platform'])
                operator_name = (r.json()['departures']['all'][i]['operator_name'])
                print("At "+departure+" the train to "+destination+" will depart from platform "+platform+". This service is provided by "+operator_name)
                tts = gTTS("At "+departure+" the train to "+destination+" will depart from platform "+platform+". This service is provided by "+operator_name, lang="en-us")
                tts.save("announce.mp3")
                media = vlc.MediaPlayer("announce.mp3")
                media.play()
                sleep(10)
        else:
                print("There has been an error")