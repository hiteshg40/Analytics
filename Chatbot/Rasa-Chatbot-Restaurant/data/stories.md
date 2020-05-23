## Happy Path without any entity and email sent
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "chandigarh"}
    - slot{"location": "chandigarh"}
    - action_validate_location
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_budget
* restaurant_search{"budget": "high"}
    - slot{"budget": "high"}
    - action_search_restaurants
    - slot{"data": "Chili's in 312 B,  is 1300"}
* affirm
    - utter_email
* send_email{"email": "ttt@gmail.com"}
    - slot{"email": "ttt@gmail.com"}
    - action_send_restaurants
* affirm
    - utter_goodbye

## Happy Path without any entity and email not sent
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "virar"}
    - slot{"location": "virar"}
    - action_validate_location
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - utter_ask_budget
* restaurant_search{"budget": "low"}
    - slot{"budget": "low"}
    - action_search_restaurants
    - slot{"data": "Tripper Cold Cafe 0"}
* email
    - utter_goodbye

## Happy Path with location entity and email sent
* greet
    - utter_greet
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_validate_location
* restaurant_search{"location": "pune"}
    - slot{"location": "pune"}
    - action_validate_location
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_budget
* restaurant_search{"budget": "high"}
    - slot{"budget": "high"}
    - action_search_restaurants
    - slot{"data": "Santè Spa Cuisine 00"}
* affirm
    - utter_email
* send_email{"email": "trs@gmail.com"}
    - slot{"email": "trs@gmail.com"}
    - action_send_restaurants
    - utter_goodbye


## Happy Path without any entity and email not sent
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "vasai"}
    - slot{"location": "vasai"}
    - action_validate_location
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_budget
* restaurant_search{"budget": "mid"}
    - slot{"budget": "mid"}
    - action_search_restaurants
    - slot{"data": "Flax 00"}
* email
    - utter_goodbye
* restaurant_search
    - utter_ask_location
* restaurant_search
    - utter_cityNotSupported
    - utter_ask_location


## Happy Path with location entity and email not sent
* greet
    - utter_greet
* restaurant_search{"location": "indore"}
    - slot{"location": "indore"}
    - action_validate_location
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_budget
* restaurant_search{"budget": "low"}
    - slot{"budget": "low"}
    - action_search_restaurants
    - slot{"data": "Joshi Dahi Bada 100"}
* email
    - utter_goodbye

## location, cuisine entity and email sent
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Delhi"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Delhi"}
    - action_validate_location
    - utter_ask_budget
* restaurant_search{"budget": "high"}
    - slot{"budget": "high"}
    - action_search_restaurants
    - slot{"data": "Indian Accent 1200"}
* affirm
    - utter_email
* send_email{"email": "twe@yahoo.com"}
    - slot{"email": "twe@yahoo.com"}
    - action_send_restaurants
    - utter_goodbye

## location, cuisine entity and email not sent
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "mumbai"}
    - slot{"cuisine": "italian"}
    - slot{"location": "mumbai"}
    - action_validate_location
    - utter_ask_budget
* restaurant_search{"budget": "high"}
    - slot{"budget": "high"}
    - action_search_restaurants
    - slot{"data": "Yazu 2 people is 1500"}
* email
    - utter_goodbye

## location, cuisine and budget entity and email sent
* greet
    - utter_greet
* restaurant_search{"location": "pune", "cuisine": "mexican", "budget": "low"}
    - slot{"budget": "low"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "pune"}
    - action_validate_location
    - action_search_restaurants
    - slot{"data": ""}
* affirm
    - utter_email
* send_email{"email": "abc@gmail.com"}
    - slot{"email": "abc@gmail.com"}
    - action_send_restaurants
    - utter_goodbye

## location, cuisine and budget entity and email not sent
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "pune", "budget": "high"}
    - slot{"budget": "high"}
    - slot{"cuisine": "italian"}
    - slot{"location": "pune"}
    - action_validate_location
    - action_search_restaurants
    - slot{"data": "Santè Spa Cuisine  is 1700"}
* email
    - utter_goodbye

## cuisine and budget entity and email sent
* greet
    - utter_greet
* restaurant_search{"budget": "mid", "cuisine": "chinese"}
    - slot{"budget": "mid"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "pune"}
    - slot{"location": "pune"}
    - action_validate_location
    - action_search_restaurants
    - slot{"data": "Darshan is 700"}
* affirm
    - utter_email
* send_email{"email": "xyz@yahoo.com"}
    - slot{"email": "xyz@yahoo.com"}
    - action_send_restaurants
    - utter_goodbye

## cuisine and budget entity and email not sent
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "budget": "high"}
    - slot{"budget": "high"}
    - slot{"cuisine": "italian"}
    - utter_ask_location
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - action_validate_location
    - action_search_restaurants
    - slot{"data": "Indian Accent people is 800"}
* email
    - utter_goodbye

## location and budget entity and email sent
* greet
    - utter_greet
* restaurant_search{"location": "mumbai", "budget": "low"}
    - slot{"budget": "low"}
    - slot{"location": "mumbai"}
    - action_validate_location
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - slot{"data": "Sai Annapurna300"}
* affirm
    - utter_email
* send_email{"email": "abc@yahoo.com"}
    - slot{"email": "abc@yahoo.com"}
    - action_send_restaurants
    - utter_goodbye

## location and budget entity and email not sent
* greet
    - utter_greet
* restaurant_search{"location": "Delhi", "budget": "mid"}
    - slot{"budget": "mid"}
    - slot{"location": "Delhi"}
    - action_validate_location
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - slot{"data": "Oishii e is 600"}
* email
    - utter_goodbye

## city not supported
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search
    - utter_cityNotSupported
    - utter_goodbye


## city not supported 2
* restaurant_search
    - utter_cityNotSupported
    - utter_ask_location

## Happy path - with location entity
* greet
    - utter_greet
* restaurant_search{"location": "pune"}
    - slot{"location": "pune"}
    - action_validate_location
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"budget": "low"}
    - slot{"budget": "low"}
    - action_search_restaurants
    - slot{"data": ""}
* email
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "ppune"}
    - slot{"location": "ppune"}
    - action_validate_location
    - slot{"location": ""}
* restaurant_search{"location": "pune"}
    - slot{"location": "pune"}
    - action_validate_location
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_budget
* restaurant_search{"budget": "mid"}
    - slot{"budget": "mid"}
    - action_search_restaurants
    - slot{"data": "Darshan in Amarle is 700"}
* email
    - utter_goodbye

## interactive_story_2
* greet
    - utter_greet
* restaurant_search{"location": "muumbai"}
    - slot{"location": "muumbai"}
    - action_validate_location
    - slot{"location": ""}
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_validate_location
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - utter_ask_budget
* restaurant_search{"budget": "low"}
    - slot{"budget": "low"}
    - action_search_restaurants
    - slot{"data": "Tripper ColdC, Ghansoli, Navi Mumbai has a rating of 4.8 and the average cost for 2 people is 300"}
* email
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search
    - utter_cityNotSupported
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"budget": "low"}
    - slot{"budget": "low"}
    - action_search_restaurants
    - slot{"data": "Sai Annapurna Pure Veg in Shop 18, Plot 14/15, Yashodeep Heights, Sector 29C, Ghansoli, Navi Mumbai has a rating of 4.8 and the average cost for 2 people is 300\nSai Annapurna Pure Veg in Shop 02, Plot 163/02, Kusum Heritage, Sector 12E, Kopar Khairane, Navi Mumbai has a rating of 4.8 and the average cost for 2 people is 300"}
* email
    - utter_goodbye
* greet
    - utter_greet
* restaurant_search{"location": "muumbai"}
    - slot{"location": "muumbai"}
    - action_validate_location
    - slot{"location": ""}
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_validate_location
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"budget": "low"}
    - slot{"budget": "low"}
    - action_search_restaurants
    - slot{"data": "Sai Annapurna Pure Veg in Shop 18, Plot 14/15, Yashodeep Heights, Sector 29C, Ghansoli, Navi Mumbai has a rating of 4.8 and the average cost for 2 people is 300\nSai Annapurna Pure Veg in Shop 02, Plot 163/02, Kusum Heritage, Sector 12E, Kopar Khairane, Navi Mumbai has a rating of 4.8 and the average cost for 2 people is 300"}
* email
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search
    - utter_cityNotSupported
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"budget": "low"}
    - slot{"budget": "low"}
    - action_search_restaurants
    - slot{"data": "Sai Annapurna Pure Veg in Shop 18, Plot 14/15, Yashodeep Heights, Sector 29C, Ghansoli, Navi Mumbai has a rating of 4.8 and the average cost for 2 people is 300\nSai Annapurna Pure Veg in Shop 02, Plot 163/02, Kusum Heritage, Sector 12E, Kopar Khairane, Navi Mumbai has a rating of 4.8 and the average cost for 2 people is 300"}
* email
    - utter_goodbye
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mmumbai"}
    - slot{"location": "mmumbai"}
    - action_validate_location
    - slot{"location": ""}
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_validate_location
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"budget": "low"}
    - slot{"budget": "low"}
    - action_search_restaurants
    - slot{"data": "Sai Annapurna Pure Veg in Shop 18, Plot 14/15, Yashodeep Heights, Sector 29C, Ghansoli, Navi Mumbai has a rating of 4.8 and the average cost for 2 people is 300\nSai Annapurna Pure Veg in Shop 02, Plot 163/02, Kusum Heritage, Sector 12E, Kopar Khairane, Navi Mumbai has a rating of 4.8 and the average cost for 2 people is 300"}
* email
    - utter_goodbye

## interactive_story_2
* greet
    - utter_greet
* restaurant_search{"location": "ppune"}
    - slot{"location": "ppune"}
    - action_validate_location
    - slot{"location": ""}
* restaurant_search{"location": "ppune"}
    - slot{"location": "ppune"}
    - action_validate_location
    - slot{"location": ""}
* restaurant_search{"location": "pune"}
    - slot{"location": "pune"}
    - action_validate_location
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"budget": "mid"}
    - slot{"budget": "mid"}
    - action_search_restaurants
    - slot{"data": "Darshan in Amar age cost for 2 people is 700"}
* affirm
    - utter_email
* send_email
    - utter_email
* send_email
    - utter_email
* send_email{"email": "ttt@gmail.com"}
    - slot{"email": "ttt@gmail.com"}
    - action_send_restaurants
    - utter_goodbye


## interactive_story_9
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "indore"}
    - slot{"location": "indore"}
    - action_validate_location
    - utter_ask_budget
* restaurant_search{"budget": "low"}
    - slot{"budget": "low"}
    - action_search_restaurants
    - slot{"data": "fdfdf"}
* email
    - utter_goodbye

## interactive_story_10
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_location
* restaurant_search
    - utter_cityNotSupported
* restaurant_search
* restaurant_search{"location": "lucknow"}
    - slot{"location": "lucknow"}
    - action_validate_location
    - utter_ask_budget
* restaurant_search{"budget": "low"}
    - slot{"budget": "low"}
    - action_search_restaurants
    - slot{"data": ""}
* email
    - utter_goodbye    


## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "bandra"}
    - slot{"location": "bandra"}
    - action_validate_location
    - slot{"location": ""}
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_validate_location
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"budget": "low"}
    - slot{"budget": "low"}
    - action_search_restaurants
    - slot{"data": "Sai Annapurna ai has a rating of 4.8 and the average cost for 2 people is 300"}
* email
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* affirm
    - utter_cityNotSupported
* restaurant_search{"location": "nagpur"}
    - slot{"location": "nagpur"}
    - action_validate_location
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - utter_ask_budget
* restaurant_search{"budget": "high"}
    - slot{"budget": "high"}
    - action_search_restaurants
    - slot{"data": "Bouffage in Wockhart Hospital of 4.5 and the average cost for 2 people is 1100"}
* email
    - utter_goodbye


## interactive_story_10
* greet
    - utter_greet
* restaurant_search{"budget": "low"}
    - slot{"budget": "low"}
    - utter_ask_location
* restaurant_search{"location": "lucknow"}
    - slot{"location": "lucknow"}
    - action_validate_location
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - action_search_restaurants
    - slot{"data": ""}
* email
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "bandra"}
    - slot{"location": "bandra"}
    - action_validate_location
    - slot{"location": ""}
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
<!--
## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "pona"}
    - slot{"location": "pona"}
    - action_validate_location
    - slot{"location": ""}
* restaurant_search{"location": "pune"}
    - slot{"location": "pune"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"budget": "high"}
    - slot{"budget": "high"}
    - action_search_restaurants
    - slot{"data": "Santè Spa Cuisine 1600"}
* restaurant_search
    - utter_email
* send_email{"email": "ttt@gmail.com"}
    - slot{"email": "ttt@gmail.com"}
    - action_send_restaurants
    - utter_goodbye
-->