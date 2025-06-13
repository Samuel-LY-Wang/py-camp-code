import requests
import json
import html

def get_questions(max_qs):
    question_data = requests.get(f"https://opentdb.com/api.php?amount={max_qs}&type=boolean").json()['results']
    for question in question_data:
        question['question'] = html.unescape(question['question'])
        # print(question['question'])
        # print(question['correct_answer'])
    return question_data