## A basic end-to-end test
* greet: hello
   - utter_greet
* restaurant_search: show me [chinese](cuisine) restaurants
   - utter_ask_location
* restaurant_search: in [Delhi](location)
   - action_validate_location
   - utter_ask_budget
* restaurant_search: I will go for [high](budget)
   - action_search_restaurants
* affirm: send me the details
    - utter_email
* send_email: my emails address is dsasadsa.dsdad
    - utter_email
* send_email: my emails address is [fdfd@gmail.com](email)    
    - action_send_restaurants
    - utter_goodbye


