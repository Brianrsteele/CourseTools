import yaml
from pprint import pprint
from datetime import date, datetime, timedelta

# open the institutional dates file -------------------------------------------->

with open("05_instutional_S26.yml", "r") as file:
    # load yaml content
    institutional_calendar = yaml.safe_load(file)


semester_start = institutional_calendar["institutional_dates"]["start_date"]
semester_end = institutional_calendar["institutional_dates"]["end_date"]


# open course dates file -------------------------------------------->

with open("ART-2286-importand-dates.yml", "r") as file:
    # load yaml content
    course_calendar = yaml.safe_load(file)


# find the first sunday after a date object ------------------------>
def first_sunday_after(start_date):
    first_sunday_delta = 6 - start_date.weekday()
    delta = timedelta(first_sunday_delta)
    first_sunday_after = start_date + delta
    return first_sunday_after


# generate a list of sundays between a start and end dates
def generate_sunday_list(start_date, end_date, week_day_integer):
    semester_dates_list = []
    date_pointer = first_sunday_after(start_date)
    one_week = timedelta(weeks=1)
    while date_pointer <= end_date:
        semester_dates_list.append(date_pointer)
        date_pointer += one_week
    return semester_dates_list


# sort holidays and week
def sort_key(item):
    if "kind" in item and item["kind"] == "institutional_event":
        if "subkind" in item:
            if item["subkind"] == "spring_break":
                return item["date_range"]["start"]
        return item["date"]
    return item["due_date"]


# need a list of sundays
date_list = generate_sunday_list(semester_start, semester_end, 6)

# TODO - This needs to be worked on in the fall!
# find spring break in the institutional calendar yaml data
spring_break = [
    h
    for h in institutional_calendar["institutional_dates"]["holidays_and_closures"]
    if h["label"] == "Spring Break - No Classes"
]

# figure out which sunday is after spring break
spring_break_sunday = first_sunday_after(spring_break[0]["date_range"]["end"])
# remove spring break sunday from list of dates
date_list.remove(spring_break_sunday)

# assign a variable to the list of weeks for ease of use
weekly_schedule = course_calendar["weeks"]
# assign a variable to the list of holidays for eas of use.
holidays = institutional_calendar["institutional_dates"]["holidays_and_closures"]

for week, due_date in zip(weekly_schedule, date_list):
    week["due_date"] = due_date

weekly_schedule = weekly_schedule + holidays

weekly_schedule.sort(key=sort_key)


# double check that the dates and sessions match up
if len(date_list) == len(course_calendar["weeks"]):
    print("\n\n\n***********************")
    # print("start", semester_start)
    # print("end", semester_end)
    # pprint(date_list)
    # print("dates:", len(date_list), "course weeks:", len(weekly_schedule))
    # pprint(spring_break_sunday)
    pprint(weekly_schedule)
    print("***********************\n\n\n")
