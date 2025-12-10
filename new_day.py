import argparse
import os
import datetime

today = datetime.datetime.now()
year = today.year
day = today.day

parser = argparse.ArgumentParser()
parser.add_argument("--year", type=int, default=year)
parser.add_argument("--day", type=int, default=day)
args = parser.parse_args()

year = args.year
day = args.day

print(f"Year {year} Day {day}")

# create the day directory
os.makedirs(f"{year}/d{day}", exist_ok=True)

# create the day.py file
if not os.path.exists(f"{year}/d{day}/d{day}.py"):
    with open(f"{year}/d{day}/d{day}.py", "w") as f:
        f.write("")
if not os.path.exists(f"{year}/d{day}/d{day}-t.txt"):
    with open(f"{year}/d{day}/d{day}-t.txt", "w") as f:
        f.write("")
if not os.path.exists(f"{year}/d{day}/d{day}.txt"):
    with open(f"{year}/d{day}/d{day}.txt", "w") as f:
        f.write("")
