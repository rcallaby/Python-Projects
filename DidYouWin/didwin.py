#import the necessary libraries
import json
import requests

#open the first json file and store the numbers in a list
with open('powerball_numbers.json') as f:
    data1 = json.load(f)
    powerball_nums = data1['numbers']

#access the lottery api and store the numbers in a separate json file
response = requests.get('http://www.lotteryapi.com/api/numbers')
if response.status_code == 200:
    powerball_nums_json = response.json()
    with open('powerball_numbers_api.json', 'w') as f:
        json.dump(powerball_nums_json, f)

#compare the first json file with the second json file
with open('powerball_numbers_api.json') as f:
    data2 = json.load(f)
    powerball_nums_api = data2['numbers']

#if any numbers match print them out on the screen
matches = []
for num in powerball_nums:
    if in powerball_nums_api:
        matches.append(num)

if matches:
    print("The numbers that match are:")
    for num in matches:
        print(num)
else:
    print("No numbers matched.")
