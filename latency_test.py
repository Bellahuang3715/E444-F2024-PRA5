import requests
import time
import csv

# base_url = "http://127.0.0.1:5000/predict/"
base_url = "http://server-sentiment-1-env.eba-rj25pess.us-east-2.elasticbeanstalk.com/predict/"

# test cases
test_cases = {
    "1": "The Earth is the largest planet in the solar system",
    "2": "Thomas Edison invented the iPhone",
    "3": "Christmas is in December",
    "4": "There are 24 hours in a day"
}

iterations = 100

with open("latency_results.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Test Case", "Input", "Start Time", "End Time", "Latency (s)"])

    for case, test in test_cases.items():
        for i in range(iterations):
            start_time = time.time()
            response = requests.get(base_url + test)
            end_time = time.time()
            latency = end_time - start_time

            writer.writerow([case, test, start_time, end_time, latency])
