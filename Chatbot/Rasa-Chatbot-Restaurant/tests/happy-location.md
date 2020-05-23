## A basic end-to-end test
* greet: hello
   - utter_greet
* restaurant_search: find me a restaurant in [bhopal](location)
   - action_validate_location
   - utter_ask_cuisine
* restaurant_search: find  [mexican](cuisine)
   - utter_ask_budget
* restaurant_search: [expensive](budget:high)
   - action_search_restaurants
* affirm: send me the details
    - utter_email
* send_email: my emails address is [hfff@gmail.com](email)
    - action_send_restaurants
    - utter_goodbye



