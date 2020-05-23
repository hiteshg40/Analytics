## Steps to Use the code -
1- Create the Zomato api key and update the same in the actions.py file as mentioned in the code
2- Update the Email id and credentials in the actions.py file to ensiure that an email is sent.
3- Also follow the instruction to remove 2 - factor authentication and access insecure applications to the gmail server.
4- Update the appropriate smtp path for the mail client used. Currently it is setup to use a gmial account.

## Updated Version used for this project -

# Name                    Version                
rasa                      1.9.6                  
rasa-core                 0.10.1                   
rasa-nlu                  0.12.3                   
rasa-sdk                  1.9.0                    
rasa-x                    0.27.5
spacy                     2.1.9
tensorflow                2.1.0
Python                    3.6.5                   

## Test setup
13 test cases have been created in the tests folder.The results of the same is updated in the file /results/failed_stories.md. 
Overall there is a score of 0.99 for prescision , recall and f1-score on the test set.



## Key functionality in the code
1- ActionSearchRestaurants class in Actions.py file uses the Restaurant_serach function in the zomato.py file to get the restaurant list.
2- Restaurant_serach function gets the list based on the city, cuisine and sorts the list by the average rating in the descending order.
3- This list is then filtered in the ActionSearchRestaurants function to get the list with the appropriate budget category.
4- Top 5 list is provided as a nessage to the user and Top 10 list is provided as an option for the email.
5- Actionsendemail class provides for the functionality of sending the email using a gmail client.
6- This class uses the simpleemail.py file for the setup and sending the email.
7- location.txt contains the list of tier 1 and tier 2 cities
8- ActionvalidateLocation class is used to validate the city provided by the user from the locations.txt file.This file contains the Tier 1 and tier 2 cities.
9- This file is also used in the NLU.md file to identify the correct cities to be used for entity recogonition.
10- NLU.md , domain.yml and stories.md is used for training the model.
11- /Tests - Around 10 scenarios have been created in the 'tests' folder, which can be used to test this model.
12- /Result folder  holds the result of the test scenarios.