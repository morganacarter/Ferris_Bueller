#Possible to scrape twitter for games, day of?

import csv
import requests
from yelpapi import YelpAPI

with open('nats.csv') as nats_csvfile:
    nats_response = requests.get("http://api.openweathermap.org/data/2.5/weather?q=Washington,DC&units=imperial&cnt=7").json()
    nats_direction = requests.get("http://api.wmata.com/StationPrediction.svc/json/GetPrediction/E04?api_key=YOUR_KEY_HERE").json()
    nats_game_list = csv.reader(nats_csvfile)
    user_date = raw_input("What date are you going to the ballgame?")

    nats_game_dates_list = []
    for nats_game in nats_game_list:
        nats_game_dates_list.append(nats_game[0])
        if user_date == nats_game[0] and nats_game[4] == "Nationals Park":
            print "Great news, there is a Nationals home game! Here is some information:"
            
            print "The game starts at {0} and it is the {1} \n".format(nats_game[1],nats_game[3])
            print "The current temperature is {0} degrees and the expected forecast is {1}".format(nats_response["main"]["temp"],nats_response["weather"][0]["description"])
            print "The next train to Nats Yard will arrive at the Columbia Heights station in {0} minutes \n".format(nats_direction["Trains"][3]["Min"])
            print "Now let's get something in your tummy! Check out one of these restaurants:"
            yelp_api = YelpAPI("YOUR_CONSUMER_KEY", "YOUR_CONSUMER_SECRET", "YOUR_TOKEN", "YOUR_TOKEN_SECRET")
            search_results = yelp_api.search_query(term='restaurant', ll='38.87,-77.01', limit = 4)
            for business in search_results['businesses']:
                print business['name']
        elif user_date == nats_game[0] and nats_game[4] != "Nationals Park":
            print "There is an away game today. You can catch it on the local radio affiliate"
    if user_date not in nats_game_dates_list:
        bal_response = raw_input("There is no Nationals Game today. Do you want to see if there's an Orioles game?")

        if bal_response == "yes" or bal_response == "Yes":
            with open('orioles.csv') as orioles_csvfile:
                orioles_response = requests.get("http://api.openweathermap.org/data/2.5/weather?q=Baltimore&units=imperial&cnt=7").json()
                orioles_game_list = csv.reader(orioles_csvfile)
                orioles_game_dates_list = []
                for orioles_game in orioles_game_list:
                    orioles_game_dates_list.append(orioles_game[0])
                    if user_date == orioles_game[0] and orioles_game[4] == "Oriole Park at Camden Yards":
                        print "Okay, great news! The Orioles are playing at home today, you can go up to Baltimore and see them!"
                        print "The game starts at {0} and it is the {1} \n".format(orioles_game[1],orioles_game[3])
                        
                        print "\nThe current temperature is {0} degrees and the expected forecast is {1}".format(orioles_response["main"]["temp"],orioles_response["weather"][0]["description"])
                        
                        print "\nTime for some Baltimore eats!"
                        yelp_api = YelpAPI("YOUR_CONSUMER_KEY", "YOUR_CONSUMER_SECRET", "YOUR_TOKEN", "YOUR_TOKEN_SECRET")
                        search_results = yelp_api.search_query(term='restaurant', ll='39.285243,-76.620103', limit = 4)
                        for business in search_results['businesses']:
                            print business['name']
                        bal_hotel = raw_input("Do you need a hotel?")
                        if bal_hotel == "yes" or bal_hotel == "Yes":
                            hotel = requests.get("http://dev.api.ean.com/ean-services/rs/hotel/v3/list?minorRev=[]&cid=55505&apiKey=YOUR_KEY_HERE&customerUserAgent=[]&customerIpAddress=xxx&locale=en_US&currencyCode=USD&city=Baltimore&stateProvinceCode=MD&countryCode=US&supplierCacheTolerance=MED&arrivalDate=MM/DD/YYYY&departureDate=MM/DD/YYYY&room1=2&numberOfResults=3").json()
                            print "\nGreat! Let's try booking a room at {0} . They have a {1} at ${2} a night.".format(hotel["HotelListResponse"]["HotelList"]["HotelSummary"][1]["name"],
                                                                                           hotel["HotelListResponse"]["HotelList"]["HotelSummary"][1]["RoomRateDetailsList"]["RoomRateDetails"]["roomDescription"],
                                                                                           hotel["HotelListResponse"]["HotelList"]["HotelSummary"][1]["RoomRateDetailsList"]["RoomRateDetails"]["RateInfo"]["ChargeableRateInfo"]["@averageRate"])

                    elif user_date == orioles_game[0] and orioles_game[4] != "Oriole Park at Camden Yards":
                        print "No Orioles home game either. Go outside and have fun today"
                if user_date not in orioles_game_dates_list:
                    print "No O's game either. Guess you'll have to find another way to entertain yourself."
        else:
            print "Okay. Well go outside and have fun today."
