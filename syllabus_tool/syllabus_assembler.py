#!/usr/bin/env python3
"""Syllabus assembler script."""

from datetime import date, timedelta
from pathlib import Path

import matplotlib.pyplot as plt
import pypandoc  # type: ignore
import yaml
from jinja2 import Environment, FileSystemLoader

# Wow, does this script need some refactoring!
# This script loads course data and important dates from yaml files
# and course polices from markdown files and combines
# them into a markdown syllabus and then uses pandocs to
# convert that to a word document.

# Some constants to make life easier later ---------------------------->

# TODO - need to be updated each semester
INSTRUCTOR_YML_FILE = Path("syllabus_tool/instructor_info/instructor-F26.yml")
INSTITUTIONAL_DATES_YML_FILE = Path(
    "syllabus_tool/institutional_dates/institutional_F26.yml"
)

COURSE_POLICIES_FOLDER = Path("syllabus_tool/course_policies/")
RCTC_POLICIES_FOLDER = Path("syllabus_tool/rctc_policies")
TEMPLATES_FOLDER = Path("syllabus_tool/templates")
OUTPUT_FOLDER = Path("syllabus_tool/output")


# COURSE_YML_FILE = "ART-2286-S26-31.yml"
# COURSE_YML_DATES_FILE = "ART-2286-important-dates.yml"

# COURSE_YML_FILE = Path("syllabus_tool/courses/art-1184/Art-1184-F26-01.yml")
# COURSE_YML_DATES_FILE = Path(
#     "syllabus_tool/courses/art-1184/ART-1184-important-dates.yml"
# )

COURSE_YML_FILE = Path("syllabus_tool/courses/art-1184/Art-1184-F26-31.yml")
COURSE_YML_DATES_FILE = Path(
    "syllabus_tool/courses/art-1184/ART-1184-important-dates.yml"
)


# COURSE_YML_FILE = "ART-2280-S26-31.yml"
# COURSE_YML_DATES_FILE = "ART-2280-important-dates.yml"

# COURSE_YML_FILE = "ART-2281-S26-31.yml"
# COURSE_YML_DATES_FILE = "ART-2281-important-dates.yml"

# COURSE_YML_FILE = "COMP-1741-S26-31.yml"
# COURSE_YML_DATES_FILE = "COMP-1741-important-dates.yml"

# create an output folder --------------------------------------------->

print(Path.cwd())

output_path = Path(OUTPUT_FOLDER / "output")
output_path.mkdir(parents=True, exist_ok=True)

# open the course yaml file -------------------------------------------->

with COURSE_YML_FILE.open("r", encoding="utf-8") as file:
    # load yaml content
    course_info = yaml.safe_load(file)


# open the instructor yaml file ---------------------------------------->
with INSTRUCTOR_YML_FILE.open("r", encoding="utf-8") as file:
    # load yaml content
    instructor = yaml.safe_load(file)

# deal with grading --------------------------------------------------->
grading_type = course_info["course"]["grading_type"]

assessments: list[dict] = []
components: list[dict] = []

if grading_type == "weighted_percent":
    components = course_info["course"]["assessment_structure"]["components"]
    total = 0
    grade_weights = {}
    # sanity check for percentages
    for item in components:
        # make a dict for pie chart
        weight = item["weight_percent"]
        label = item["label"].capitalize()
        grade_weights[label] = weight
        # sum the weights for sanity check
        total += weight
    if abs(total - 100) > 1e-6:
        raise ValueError(f"Grading weights must total 100, got {total}")
    if len(components) > 0:
        # create a pie chart
        plt_labels = list(grade_weights.keys())
        plt_weights = list(grade_weights.values())
        # make the figure
        plt.figure()
        plt.pie(plt_weights, labels=plt_labels, autopct="%1.0f%%", startangle=90)
        plt.axis("equal")
        # chart is exported at the end of the script to assist with file naming
        created_chart = True
    assessments = course_info["course"]["assessment_structure"]["assessments"]
elif grading_type == "points":
    assessments = course_info["course"]["assessment_structure"]["assessments"]
    total = 0
    # make a dict for pie chart
    grade_weights = {}
    for item in assessments:
        points = item["points"]
        kind = item["kind"].capitalize()
        if kind not in grade_weights:
            grade_weights[kind] = 0
        grade_weights[kind] += points
        total += item["points"]
    # turn grade weights into percentages not points
    percent_total = 0
    for item in grade_weights:
        value = grade_weights[item]
        grade_weights[item] = round((value / total) * 100, 2)
        # add the percents to help check for accuracy
        percent_total += grade_weights[item]
    # check that the total percentage is accurately 100
    if abs(percent_total - 100) > 1e-6:
        raise ValueError(f"Grading weights must total 100, got {total}")
    if len(assessments) > 0:
        # create a pie chart
        plt_labels = list(grade_weights.keys())
        plt_weights = list(grade_weights.values())
        # make the figure
        plt.figure()
        plt.pie(plt_weights, labels=plt_labels, autopct="%1.0f%%", startangle=90)
        plt.axis("equal")
        # chart is exported at the end of the script to assist with file naming
        created_chart = True
else:
    pass


# deal with important dates ------------------------------------------>

# open the institutional dates
with open(INSTITUTIONAL_DATES_YML_FILE, "r") as file:
    # load yaml content
    institutional_dates = yaml.safe_load(file)
start_date = date.fromisoformat(
    str(institutional_dates["institutional_dates"]["start_date"])
)
end_date = date.fromisoformat(
    str(institutional_dates["institutional_dates"]["end_date"])
)

# open the course session information
yaml_path = Path(COURSE_YML_DATES_FILE)
with yaml_path.open("r", encoding="utf-8") as f:
    sessions = yaml.safe_load(f)
weeks = sessions["weeks"]

# join assignment ids with titles, discussion ids with discussion titles -------------------------------->
assessments_list = course_info["course"]["assessment_structure"]["assessments"]
for week in weeks:
    if week["projects"]["assigned"]:
        for assignment in week["projects"]["assigned"]:
            assignment_id = assignment["id"]
            for item in assessments_list:
                if item.get("id") == assignment_id:
                    assignment["label"] = item["label"]
                    assignment["code"] = item["code"]
    for discussion in week["discussions"]:
        discussion_id = discussion["id"]
        for item in assessments_list:
            if item["id"] == discussion_id:
                discussion["label"] = item["label"]
                discussion["code"] = item["code"]
    for quiz in week["exams"]:
        quiz_id = quiz["id"]
        for item in assessments_list:
            if item["id"] == quiz_id:
                quiz["label"] = item["label"]
                quiz["code"] = item["code"]


# find the first sunday after a date object
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
        if "subkind" in item and (
            item["subkind"] == "spring_break"
            or item["subkind"] == "educatation_minnesota"
            or item["subkind"] == "thanksgiving_break"
        ):
            return item["date_range"]["start"]
        return item["date"]
    return item["due_date"]


# need a list of sundays
date_list = generate_sunday_list(start_date, end_date, 6)

# TODO - This needs to be worked on in the fall!
# find spring break in the institutional calendar yaml data
spring_break = [
    h
    for h in institutional_dates["institutional_dates"]["holidays_and_closures"]
    if h["label"] == "Spring Break - No Classes"
]

# figure out which sunday is after spring break
if spring_break:
    spring_break_sunday = first_sunday_after(spring_break[0]["date_range"]["end"])
    # remove spring break sunday from list of dates
    if spring_break_sunday in date_list:
        date_list.remove(spring_break_sunday)

# assign a variable to the list of weeks for ease of use
weekly_schedule = weeks

# assign a variable to the list of holidays for eas of use.
holidays = institutional_dates["institutional_dates"]["holidays_and_closures"]

for week, due_date in zip(weekly_schedule, date_list):
    week["due_date"] = due_date

weekly_schedule = weekly_schedule + holidays

weekly_schedule.sort(key=sort_key)

if len(weeks) != len(date_list):
    raise ValueError(f"weeks ({len(weeks)}) != date_list ({len(date_list)})")

for week, the_date in zip(weeks, date_list):
    week["due_date"] = the_date.strftime("%m/%d/%y")


def find_due_date_by_week(week_num):
    for week in weeks:
        if week["week"] == week_num:
            return week["due_date"]


for week in weeks:
    for assignment in week["projects"]["assigned"]:
        if assignment["due_week"] != week["week"]:
            assignment["due_date"] = find_due_date_by_week(assignment["due_week"])

# open the course policies markdown files ------------------------------>

with open(COURSE_POLICIES_FOLDER / "assignment_grading.md", "r") as file:
    # read the content
    assignment_grading = file.read()

with open(COURSE_POLICIES_FOLDER / "attendance_hybrid.md", "r") as file:
    # read the content
    attendance_hybrid = file.read()

with open(COURSE_POLICIES_FOLDER / "attendance_in_person.md", "r") as file:
    # read the content
    attendance_in_person = file.read()

with open(COURSE_POLICIES_FOLDER / "attendance_online.md", "r") as file:
    # read the content
    attendance_online = file.read()

with open(COURSE_POLICIES_FOLDER / "camera_checkout.md", "r") as file:
    # read the content
    camera_checkout = file.read()

with open(COURSE_POLICIES_FOLDER / "computer.md", "r") as file:
    # read the content
    computer = file.read()

with open(COURSE_POLICIES_FOLDER / "course_grading.md", "r") as file:
    # read the content
    course_grading = file.read()

with open(COURSE_POLICIES_FOLDER / "feedback_format.md", "r") as file:
    # read the content
    feedback_format = file.read()

with open(COURSE_POLICIES_FOLDER / "final_grade_calculation.md", "r") as file:
    # read the content
    final_grade_calculation = file.read()

with open(COURSE_POLICIES_FOLDER / "grade_turnaround.md", "r") as file:
    # read the content
    grade_turnaround = file.read()

with open(COURSE_POLICIES_FOLDER / "internet.md", "r") as file:
    # read the content
    internet = file.read()

with open(COURSE_POLICIES_FOLDER / "lab_use.md", "r") as file:
    # read the content
    lab_use = file.read()

with open(COURSE_POLICIES_FOLDER / "late_work.md", "r") as file:
    # read the content
    late_work = file.read()

with open(COURSE_POLICIES_FOLDER / "names_pronouns.md", "r") as file:
    # read the content
    names_pronouns = file.read()

with open(COURSE_POLICIES_FOLDER / "required_computer.md", "r") as file:
    # read the content
    required_computer = file.read()

with open(COURSE_POLICIES_FOLDER / "work_outside_class.md", "r") as file:
    # read the content
    work_outside_class = file.read()

# open the rctc_polices markdown file ---------------------------------->

with open(RCTC_POLICIES_FOLDER / "academic_integrity.md", "r") as file:
    # read the content
    academic_integrity = file.read()

with open(RCTC_POLICIES_FOLDER / "ada.md", "r") as file:
    # read the content
    ada = file.read()

with open(RCTC_POLICIES_FOLDER / "ai_usage.md", "r") as file:
    # read the content
    ai_usage = file.read()

with open(RCTC_POLICIES_FOLDER / "title_ix.md", "r") as file:
    # read the content
    title_ix = file.read()

with open(RCTC_POLICIES_FOLDER / "veterans.md", "r") as file:
    # read the content
    veterans = file.read()

# create the template -------------------------------------------------->

# set up jinja2 environment
file_loader = FileSystemLoader(TEMPLATES_FOLDER)  # folder for templates
env = Environment(loader=file_loader)

# load the template --------------------------------------------------->
syllabus_template = env.get_template("syllabus_markdown_template.md")

# render the template as a string ----------------------------------->
syllabus_template_output = syllabus_template.render(
    # course and section information -------------------------------->
    am_i_ready=course_info["course"]["am_i_ready"],
    dept=course_info["course"]["department"],
    course_number=course_info["course"]["course_number"],
    section=course_info["course"]["section"],
    course_title=course_info["course"]["course_title"],
    semester=course_info["course"]["semester"],
    year=course_info["course"]["year"],
    credits=course_info["course"]["credits"],
    hours=course_info["course"]["hours"],
    how_course_works=course_info["course"]["how_course_works"],
    prereqs=course_info["course"]["prerequisites"],
    delivery=course_info["course"]["modality"],
    attendance_variant=course_info["course"]["attendance_variant"],
    meeting_times_days=course_info["course"]["meeting_times"]["days"],
    meeting_times_time=course_info["course"]["meeting_times"]["time"],
    classroom=course_info["course"]["classroom"],
    instructor=instructor["instructor"]["name"],
    office_phone=instructor["instructor"]["phone"],
    instructor_email=instructor["instructor"]["email"],
    instructor_contact_notes=instructor["instructor"]["contact_notes"],
    monday_office_hours=instructor["instructor"]["office_hours"]["monday"],
    tuesday_office_hours=instructor["instructor"]["office_hours"]["tuesday"],
    wednesday_office_hours=instructor["instructor"]["office_hours"]["wednesday"],
    thursday_office_hours=instructor["instructor"]["office_hours"]["thursday"],
    friday_office_hours=instructor["instructor"]["office_hours"]["friday"],
    office_hours_note=instructor["instructor"]["office_hours"]["note"],
    office_location=instructor["instructor"]["office"],
    catalog_description=course_info["course"]["catalog_description"],
    outline_specific_content=course_info["course"]["major_content_outline"],
    course_learning_outcomes=course_info["course"]["course_learning_outcomes"],
    mntc_goals=course_info["course"]["mntc_goals"],
    rctc_core_outcomes=course_info["course"]["rctc_core_outcomes"],
    textbooks=course_info["course"]["required_materials"]["textbooks"],
    camera=course_info["course"]["required_materials"]["camera"],
    software=course_info["course"]["required_materials"]["software"],
    computer=course_info["course"]["required_materials"]["computer"],
    fees=course_info["course"]["required_materials"]["fees"],
    other=course_info["course"]["required_materials"]["other"],
    what_matters_grade=course_info["course"]["what_matters_grade"],
    # policies and boiler plate from admin -------------------------------->
    assignment_grading=assignment_grading,
    attendance_in_person=attendance_in_person,
    attendance_hybrid=attendance_hybrid,
    attendance_online=attendance_online,
    camera_checkout=camera_checkout,
    course_grading=course_grading,
    feedback_format=feedback_format,
    final_grade_calculation=final_grade_calculation,
    grade_turnaround=grade_turnaround,
    internet=internet,
    lab_use=lab_use,
    late_work=late_work,
    names_pronouns=names_pronouns,
    required_computer=required_computer,
    work_outside_class=work_outside_class,
    academic_integrity=academic_integrity,
    ada=ada,
    ai_usage=ai_usage,
    title_ix=title_ix,
    veterans=veterans,
    # grading ---------------------------------------------------------->
    grading_type=grading_type,
    grade_weights=grade_weights,
    assessments=assessments,
    components=components,
    total=total,
    percent_total=percent_total,
    # important dates -------------------------------------------------->
    weeks=weeks,
    # file name for grade chart --------------------------------------->
    chart_title=f"{course_info['course']['department']}-{course_info['course']['course_number']}-{course_info['course']['section']}-{course_info['course']['semester']}-{course_info['course']['year']}.png",
)

dept = course_info["course"]["department"]
course_number = course_info["course"]["course_number"]
section = course_info["course"]["section"]
semester = course_info["course"]["semester"]
year = course_info["course"]["year"]
title = f"{dept}-{course_number}-{section}-{semester}-{year}"

print("Syllabus saved as " + title)

if created_chart:
    # save the chart
    chart_title = title + ".png"
    chart_path = Path(output_path / chart_title)
    plt.savefig(chart_path, dpi=150, bbox_inches="tight")
    plt.close()

markdown_title = title + ".md"
markdown_path = Path(output_path / markdown_title)

with open(markdown_path, "w") as file:
    file.write(syllabus_template_output)

word_title = title + ".docx"
word_path = Path(output_path / word_title)

pypandoc.convert_text(
    syllabus_template_output,
    to="docx",
    format="md",
    outputfile=word_path,
    extra_args=[f"--resource-path={output_path}"],
)
