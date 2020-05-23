## A basic end-to-end test
* greet: hello
    - utter_greet
* restaurant_search: show me  restaurants
    - utter_ask_location
* restaurant_search: in [bengaluru](location:bangalore)
    - action_validate_location
    - utter_ask_cuisine
* restaurant_search: in [italian](cuisine)
    - utter_ask_budget
* restaurant_search: I will go for [high](budget)
    - action_search_restaurants
* email: Not needed
    - utter_goodbye