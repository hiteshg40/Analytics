## A basic end-to-end test
* greet: hello
   - utter_greet
* restaurant_search: show me [italian](cuisine) restaurants in [chennai](location)
   - action_validate_location
   - utter_ask_budget
* restaurant_search: I will go for [high](budget)
   - action_search_restaurants
* email: Not needed
    - utter_goodbye