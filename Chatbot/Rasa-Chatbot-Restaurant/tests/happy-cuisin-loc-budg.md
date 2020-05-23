## A basic end-to-end test
* greet: hello
   - utter_greet
* restaurant_search: show me [chinese](cuisine) restaurants in [mumbai](location) with [mid](budget)
   - action_validate_location
   - action_search_restaurants
* affirm: yes send me the details
    - utter_email
* send_email: my emails address is [g43k4h.fsdf@dsfsdf.co](email)
    - action_send_restaurants
    - utter_goodbye