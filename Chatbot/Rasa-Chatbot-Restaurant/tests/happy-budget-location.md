## A basic end-to-end test
* greet: hello
   - utter_greet
* restaurant_search: show me [mid](budget) restaurants in [chennai](location)
   - action_validate_location
   - utter_ask_cuisine
* restaurant_search: I will go for [italian](cuisine)
   - action_search_restaurants
* email: Not needed
    - utter_goodbye