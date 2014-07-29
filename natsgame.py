import csv
import requests

with open('nats.csv') as nats_csvfile:
    nats_response = requests.get("http://api.openweathermap.org/data/2.5/weather?q=Washington,DC&units=imperial&cnt=7").json()
    nats_direction = requests.get("http://api.wmata.com/StationPrediction.svc/json/GetPrediction/E04?api_key=kfgpmgvfgacx98de9q3xazww").json()
    nats_game_list = csv.reader(nats_csvfile)
    user_date = raw_input("What date are you going to the ballpark?")
    nats_game_dates_list = []
    for nats_game in nats_game_list:
        nats_game_dates_list.append(nats_game[0])
        if user_date == nats_game[0] and nats_game[4] == "Nationals Park":
            print "Great news, there is a Nationals home game! Here is some information:"
            print "The game starts at {0} and it is the {1}".format(nats_game[1],nats_game[3])
            print "The current temperature is {0} degrees and the expected forecast is {1}".format(nats_response["main"]["temp"],nats_response["weather"][0]["description"])
            print "The next train to Nats Yard will arrive at the Columbia Heights station in {0} minutes".format(nats_direction["Trains"][3]["Min"])
            print nats_game
        elif user_date == nats_game[0] and nats_game[4] != "Nationals Park":
            print "There is an away game today. You can catch it on the local radio affiliate"
    if user_date not in nats_game_dates_list:
        print "There is no Nationals Game today. Do you want to check if there's a Baltimore game?"
        with open('orioles.csv') as orioles_csvfile:
            orioles_response = requests.get("http://api.openweathermap.org/data/2.5/weather?q=Baltimore&units=imperial&cnt=7").json()
            orioles_game_list = csv.reader(orioles_csvfile)
            orioles_game_dates_list = []
            for orioles_game in orioles_game_list:
                orioles_game_dates_list.append(orioles_game[0])
                if user_date == orioles_game[0] and orioles_game[4] == "Camden Yards":
                    print "Okay, great news! The Orioles are playing at home today, you can go up to Baltimore and see them!"
                    print "The game starts at {0} and it is the {1}".format(orioles_game[1],orioles_game[3])
                    print "The current temperature is {0} degrees and the expected forecast is {1}".format(orioles_response["main"]["temp"],orioles_response["weather"][0]["description"])
