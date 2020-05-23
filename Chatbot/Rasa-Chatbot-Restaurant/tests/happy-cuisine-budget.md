## A basic end-to-end test
* greet: hello
   - utter_greet
* restaurant_search: show me [high](budget) [italian](cuisine) restaurants
   - utter_ask_location
* restaurant_search: in [Delhi](location)
   - action_validate_location
   - action_search_restaurants
* email: Not needed
    - utter_goodbye