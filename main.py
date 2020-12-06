import os
import subprocess
import numpy as np
import datetime
from email.utils import formatdate
from utils.char_to_date import convert_words_to_dates


def create_new_orphan(name):
    subprocess.call(["git", "checkout", "latest"])
    subprocess.call(["git", "branch", "-d", name])
    subprocess.call(["git", "push", "origin", "--delete", name])
    subprocess.call(["git", "checkout", "--orphan", name])
    subprocess.call(["git", "add", "."])
    subprocess.call(["git", "commit", "-m", "new repo"])
    subprocess.call(["git", "push", "origin", name])


def create_fake_commit_in_past(dates, branch_name, number_of_commits=50):
    for i_commit in range(number_of_commits):
        for i_date, date in enumerate(dates):
            # make random update
            opened_file = open("random/random_file.txt", "w")
            opened_file.write(str(np.random.randint(5000, size=(100))))
            opened_file.close()
            # stage and commit
            subprocess.call(["git", "add", "."])
            # set environment date
            my_env = os.environ.copy()
            my_env["GIT_AUTHOR_DATE"] = date
            my_env["GIT_COMMITTER_DATE"] = date
            fake_commit_msg = f"'fake commit {(i_commit+1)*(i_date+1)}'"
            # make commit on date
            subprocess.Popen(["git", "commit", "-m", fake_commit_msg], env=my_env)
    # push
    subprocess.call(["git", "push", "-f", "origin", branch_name])


if __name__ == "__main__":
    # find first monday
    today = datetime.date.today()
    next_monday = today + datetime.timedelta(days=-today.weekday(), weeks=1)
    start_date = next_monday - datetime.timedelta(356)
    word = "HELLO WORLD"
    branch_name = "new_branch"
    all_dates = convert_words_to_dates(word, start_date)
    # create new branch (afterwards set manually to default branch)
    create_new_orphan(branch_name)
    # fake commits in the shape of word
    # create_fake_commit_in_past(all_dates, branch_name)
