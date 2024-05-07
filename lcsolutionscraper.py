import os
import time
import json
import requests
from bs4 import BeautifulSoup

"""
Logic:
1. 3 folders with 3 folders, Difficulty -> Language
2. For each submission, check if submission is accepted
3. If accepted, note language and submission date
4. Check current folders for a matching submission
5. If no matching submission, create a new file
6. If matching submission, compare submission dates and replace with newest
7. Designate number of pages to search through based off most recent date?
8. Maybe automate github push
https://leetcode.com/api/submissions/?offset=0

"""
timestamps = {}
mostrecent = 0

file_extension_mapping = {
    "python" : ".py",
    "java" : ".java",
    "c++" : ".c++"
}

def export_submission(submission):
    global timestamps
    name = submission['title_slug']
    time = submission['timestamp']
    language = submission['lang']

    if language == 'python3': language = 'python'

    if not os.path.exists(f'./solutions/{file_extension_mapping[language]}'):
        os.makedirs(f'./solutions/{file_extension_mapping[language]}')

    file_name = f'{name}{file_extension_mapping[language]}'
    if (file_name in timestamps and time > timestamps[file_name]) or file_name not in timestamps:

        code = submission['code']
        file_path = f'./solutions/{file_extension_mapping[language]}/{file_name}'

        with open(file_path, 'w+') as file:
            file.write(code)

        timestamps[file_name] = time


def main():

    headers = {
        "Priority" : "",
        "Sec-Ch-Ua" : '',
        "Sec-Ch-Ua-Mobile" : "",
        "Sec-Ch-Ua-Platform" : '',
        "Sec-Fetch-Dest" : "",
        "Sec-Fetch-Mode" : "",
        "Sec-Fetch-Site" : "",
        "Sec-Fetch-User" : "",
        "Upgrade-Insecure-Requests" : "",
        "User-Agent" : ""
    }
    cookies = ""

    leetcode_session = requests.Session()

    leetcode_session.headers.update(headers)

    for cookie in cookies.split(";"):
        cookie_split = [el.strip() for el in cookie.split("=", 1)]
        leetcode_session.cookies.set(cookie_split[0], cookie_split[1])

    offset = 0

    with open('timestamps.json', 'r') as file:
            global timestamps
            timestamps = json.load(file)

    global mostrecent
    for submission_time in timestamps.values():
        mostrecent = max(submission_time, mostrecent)

    while True:
        submissions_page = leetcode_session.get(f"https://leetcode.com/api/submissions/?offset={offset}")
        page_data = submissions_page.json()

        submissions = page_data['submissions_dump']
        has_next = page_data['has_next']

        if not os.path.exists('./solutions'):
            os.makedirs('./solutions')
            
        for submission in submissions:
            if submission['status_display'] != 'Accepted':
                continue

            if submission['timestamp'] <= mostrecent:
                has_next = False
                break
            export_submission(submission)

        if not has_next:
            break

        offset+=20
        time.sleep(5)

    with open('timestamps.json', 'w') as file:
        json.dump(timestamps, file, indent=4)




if __name__ == "__main__":
    main()