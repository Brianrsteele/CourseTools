import yaml
from pathlib import Path
from pprint import pprint
from datetime import date, timedelta
import pypandoc  # type: ignore

yaml_path = Path("./sundays implementation test/test.yml")

with yaml_path.open("r", encoding="utf-8") as f:
    course = yaml.safe_load(f)
    pprint(course)


start = date.fromisoformat(str(course["start_date"]))
end = date.fromisoformat(str(course["end_date"]))


def find_sundays(start, end):
    first_sunday_delta = 6 - start.weekday()
    delta = timedelta(days=first_sunday_delta)
    first_sunday = start + delta
    sundays = []
    date = first_sunday
    while date <= end:
        sundays.append(date)
        date += timedelta(days=7)

    return sundays


sunday_list = find_sundays(start, end)


weeks = course["important_dates"]


for week, the_date in zip(weeks, sunday_list):
    week["due_date"] = the_date

pprint(weeks)

important_dates = """
## Important Dates
| Week | Topic | Due Date |"""
important_dates += """
|----|------|------|\n"""


for week in weeks:
    important_dates += (
        "| "
        + str(week["week"])
        + " | "
        + week["title"]
        + " | "
        + week["due_date"].strftime("%-m/%-d/%-Y")
        + " at 11:59 p.m. |\n"
    )

print(important_dates)

pypandoc.convert_text(
    important_dates, to="docx", format="md", outputfile="important_dates.docx"
)
