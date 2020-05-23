## A basic end-to-end test
* greet: hello
   - utter_greet
* restaurant_search: find me a [low](budget) budget restaurant
   - utter_ask_location
* restaurant_search: in [Delhi](location)
   - action_validate_location
   - utter_ask_cuisine
* restaurant_search: find  [american](cuisine)
   - action_search_restaurants
* affirm: send me the details
    - utter_email
* send_email: my emails address is [cxc0@gmail.com](email)
    - action_send_restaurants
    - utter_goodbye



