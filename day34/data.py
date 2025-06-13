import requests
import json
import html

question_data = requests.get("https://opentdb.com/api.php?amount=50&type=boolean").json()['results']
for question in question_data:
    question['question'] = html.unescape(question['question'])
    # print(question['question'])
    # print(question['correct_answer'])