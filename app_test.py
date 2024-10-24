import requests

base_url = "http://127.0.0.1:5000/predict/"

# test cases (two fake news and two real news)
test_cases = {
    "1": "The Earth is the largest planet in the solar system",
    "2": "Thomas Edison invented the iPhone",
    "3": "Christmas is in December",
    "4": "There are 24 hours in a day"
}

# expected results
expected_results = {
    "1": "FAKE",
    "2": "FAKE",
    "3": "REAL",
    "4": "REAL"
}

# Run tests
for case, test in test_cases.items():
    response = requests.get(base_url + test)
    result = response.text
    expected = expected_results[case]
    
    print(f"Test case: {case}")
    print(f"Input: {test}")
    print(f"Expected: {expected}")
    print(f"Test {'Passed' if result == expected else 'Failed'}\n")
