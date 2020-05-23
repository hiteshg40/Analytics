## A basic end-to-end test
* greet: hello
   - utter_greet
* restaurant_search: show me  [mexician](cuisine:mexican) restaurants 
   - utter_ask_location
* restaurant_search: in [Delhi](location)
   - action_validate_location
   - utter_ask_budget
* restaurant_search: I will go for [cheap](budget:low)
   - action_search_restaurants
* email: Not needed
    - utter_goodbye