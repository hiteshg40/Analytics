from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import zomatopy
import json
import simpleemail


class ActionSearchRestaurants(Action):
    def name(self):
        return 'action_search_restaurants'

    def run(self, dispatcher, tracker, domain):
        #Update the Zomato api user key here-------------------------
        config = {"user_key": ""}
        zomato = zomatopy.initialize_app(config)
        loc = tracker.get_slot('location')
        cuisine = tracker.get_slot('cuisine')
        budget = tracker.get_slot('budget')
        lst_data = []
       
        '''
        The code below identified the range for the low , mid and high budget as asked by the bot
        The values budget_high and budget low is used later in this function to filter out the relevant records from 
        the Zomato api response.
        '''

        if budget == 'low':
            budget_high = 300
            budget_low = 0
        elif budget == 'mid':
            budget_high = 700
            budget_low = 300
        else:
            budget_high = 10000
            budget_low = 700

        location_detail = zomato.get_location(loc, 1)
        d1 = json.loads(location_detail)
        lat = d1["location_suggestions"][0]["latitude"]
        lon = d1["location_suggestions"][0]["longitude"]
        cuisines_dict = {'mexican': 73, 'chinese': 25, 'american': 1,
                         'italian': 55, 'biryani': 7, 'north indian': 50, 'south indian': 85}
        results = zomato.restaurant_search(
            "", lat, lon, str(cuisines_dict.get(cuisine)), 1000)
        d = json.loads(results)
        response = ""
        rest_str = ""
        count_rest = 0
        if d['results_found'] == 0:
            response = "no results"
        else:
            for restaurant in d['restaurants']:
                '''
                Check the budget category of the results 
                Only pick the results which fall in the correct average price category given by the user of the bot
                In this code the budget_high and budget_low values are used 
                '''
                if (restaurant['restaurant']['average_cost_for_two'] <= budget_high and \
                    restaurant['restaurant']['average_cost_for_two'] > budget_low):
                    rest_str = str(count_rest+1) + ". " +  restaurant['restaurant']['name'] + " in " + restaurant['restaurant']['location']['address'] \
                                + " has a rating of " + restaurant['restaurant']['user_rating']['aggregate_rating'] \
                                + " and the average cost for 2 people is " + \
                                str(restaurant['restaurant']['average_cost_for_two']) 
                    lst_data.append(rest_str)
                    count_rest += 1
                    if count_rest == 10:
                        break
        
        '''
        Top 10 restaurants list needed for the email. This stored int he data slot so that it will be available in the session
        '''

        data = "\n".join(lst_data[:])

        '''Top 5 restaurants list needed for the response to chat'''

        lmt = len(lst_data)
        if (len(lst_data) >= 5):
            lmt = 5
        response = "\n".join(lst_data[:lmt])

        dispatcher.utter_message("----- Found \n"+response+" \n Do you want this to be emailed to your email id?")
        return [SlotSet('data', data)] #save the list of 10 restaurant in the slot so that it is available in the session for email

class ActionSendEmail(Action):
    def name(self):
        return 'action_send_restaurants'

    def run(self, dispatcher, tracker, domain):
        # configuratio will work only for gmail id sender
        # enable the -allowe insecure app to send email setting in gmaiil
        # Also disallow 2 step authentication    
        # Update the email id and password for the email
        config = {"Email": "@gmail.com", "Pwd":""}
        sendmail = simpleemail.initialize_app(config)        
         
        email = tracker.get_slot('email')
        data = tracker.get_slot('data')
        resp = sendmail.send_email(data,email)
        print (resp)
        dispatcher.utter_message("Email has been sent")


class ActionValidateLocation(Action):
    def name(self):
        return 'action_validate_location'

    def run(self, dispatcher, tracker, domain):
        loc = tracker.get_slot('location')        
        if loc != "":
            resp = self.ValidateLocation(loc)
        else:
            resp = "No Valid city selected. Please choose a valid Tier1 and Tier 2 city."
        print (resp)
        if resp != 'Valid City' :
            dispatcher.utter_message(resp)
            return [SlotSet('location', "" )]



    def ValidateLocation (self, loc):
        '''
        Read the cities in the location.txt file and load it into a list
        Find the location provided by the user in this list and accordingly validate the city.
        '''
        f = open("data/location.txt", "r")
        lst_cities = [x.upper() for x in f.read().splitlines()]
        if loc.upper() in lst_cities:
            return 'Valid City'
        else:
            return 'This service is not available in the city provided.Please select a Tier 1 or tier 2 city OR check the spelling of the city provided.'



