## A basic end-to-end test
* greet: hello
    - utter_greet
* restaurant_search: show me  restaurants
    - utter_ask_location
* restaurant_search: in [bengaluru](location:bangalore)
    - slot{"location": "bangalore"}
    - action_validate_location
    - utter_ask_cuisine   <!-- predicted: action_listen -->
* restaurant_search: in [italian](cuisine)
    - slot{"cuisine": "italian"}
    - utter_ask_budget
* restaurant_search: I will go for [high](budget)
    - slot{"budget": "high"}
    - action_search_restaurants
* email: Not needed
    - utter_goodbye


## A basic end-to-end test
* greet: hello
    - utter_greet
* restaurant_search: find me a restaurant in [bhopal](location)
    - slot{"location": "bhopal"}
    - action_validate_location
    - utter_ask_cuisine   <!-- predicted: action_listen -->
* restaurant_search: find  [mexican](cuisine)
    - slot{"cuisine": "mexican"}
    - utter_ask_budget
* restaurant_search: [expensive](budget:high)
    - slot{"budget": "high"}
    - action_search_restaurants
* affirm: send me the details
    - utter_email
* send_email: my emails address is [hfff@gmail.com](email)
    - slot{"email": "hfff@gmail.com"}
    - action_send_restaurants
    - utter_goodbye


