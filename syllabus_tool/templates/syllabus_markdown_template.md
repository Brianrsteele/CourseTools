# {{ dept }} {{ course_number }}–{{ section }}, {{ course_title }} Syllabus, {{ semester }}, {{ year }}

## Course Information

- **Semester:** {{ semester }}, {{ year }}
- **Course Number/Section:** {{ dept }} {{ course_number }}–{{ section }}
- **Credits:** {{ credits }}
- **Hours per week:** {{ hours }}
- **Delivery Method:** {{ delivery }}
- **Prerequisites:** {%- if prereqs %} {{ prereqs }}.{%- else %} None{%- endif %}
{% if meeting_times_days and meeting_times_time %}
- **Meeting Times:** {{ meeting_times_days }}, {{ meeting_times_time }}
{% else %}
- **Meeting Times:** Online asynchronous. There are no scheduled meeting times.
{% endif %}
{% if classroom %}
- **Classroom:** {{ classroom }}
{% else %}
- **Classroom:** Online course. There is no classroom.
{% endif %}
- **Instructor:** {{ instructor }}, {{ instructor_email }}
- **Office Phone:** {{ office_phone }}
- **Student Meeting Hours:** I meet with students in my office during the following hours:
  - **Monday:** {{ monday_office_hours }}
  - **Tuesday:** {{ tuesday_office_hours }}
  - **Wednesday:** {{ wednesday_office_hours }}
  - **Thursday:** {{ thursday_office_hours }}
  - **Friday:** {{ friday_office_hours }}
  - **Note:** {{ office_hours_note }}
- **Office location:** {{ office_location}}

### I have a question or an issue. How can I reach you?

{{ instructor_contact_notes }}

### Am I ready to take this course?

{{ am_i_ready }}

### What is this course about (Catalog Description)?

{{ catalog_description }}

### How does this course work?

{{ how_course_works }}

### What is this course going to cover (Outline of Specific Content)?

{{ outline_specific_content }}

### Course Learning Outcomes and Competencies

{{ course_learning_outcomes }}

### What transfer goals does this course satisfy (MnTC Goals)?

{{ mntc_goals }}

### This course contributes to meeting the following RCTC Core Learning Outcome(s):

{% for outcome in rctc_core_outcomes %} - {{ outcome }}
{% endfor %}

## Course Materials

### What textbook will I need for this course (Readings/Required Textbooks)?

{% for textbook in textbooks %} - {{ textbook }}
{% endfor %}

{% if camera %}
### Do I need a camera for this class?

**REQUIRED - Necessary Equipment**

{% for c in camera %} - {{ c }}
{% endfor %}

{% endif %}

### What software do I need for this class?

{% for s in software %} - {{ s }}
{% endfor %}

### Are there any special fees associated with this class?

{% for f in fees %} - {{ f }}
{% endfor %}

### Can I check out a camera from the Art Department?

{{ camera_checkout }}

### Computer

{{ computer }}

### Will I need internet access at home?

{{ internet}}

### Is there anything else I will need for this class?

{% for o in other %} - {{ o }}
{% endfor %}

## Course Policies

### Preferred names and pronouns

{{ names_pronouns }}

### What is the attendance policy for this course?

**REFERENCE INFORMATION - You don't need to read this now**

{% if attendance_variant == "in-person" -%}
{{attendance_in_person}}
{%- endif -%}
{% if attendance_variant == "online" -%}
{{attendance_online}}
{%- endif %}
{% if attendance_variant == "hybrid" -%}
{{attendance_hybrid}}
{%- endif %}

{% if delivery == "in-person" %}
### Will I have to work outside of class to complete my projects?
{% else %}
### Will I have to work beyond reading/watching material on D2L/Brightspace to complete my projects?
{% endif %}

{{ work_outside_class }}

### What is the policy for late work?

**REFERENCE INFORMATION - You don't need to read this now**

{{ late_work }}

### Can I work in the lab/classroom outside of class time?

**IMPORTANT**

{{ lab_use }}

## Grading

### What matters most for my course grade?

{{ what_matters_grade }}

### How will this class be graded?

{{ course_grading }}

### How will you compute our final grades for the course?

{{ final_grade_calculation }}

### How does the final grade break down?

**IMPORTANT INFORMATION - Return to as needed**

{%- if grading_type == "points"%}
**Assignments by Points Value**

| Category | Points |
| -------- | :----: |

{%- for item in assessments %}
| {{ item.label }} | {{ item.points }} |
{%- endfor %}
| **Total** | **{{ total }}** |

**Categories of Assignments by Percentage of Final Grade**

| Category | Percentage |
| -------- | :--------: |

{%- for kind in grade_weights %}
| {{ kind }} | {{ grade_weights[kind] }} |
{%- endfor %}
| **Total** | **{{ percent_total }}%** |

{% endif -%}

{% if grading_type == "weighted_percent"%}

**Assignments by Points Value**

| Category | Points |
| -------- | :----: |

{%- for item in assessments %}
| {{ item.label }} | {{ item.points }} |
{%- endfor %}
| **Total** | **{{ total }}** |

**Categories of Assignments by Percentage of Final Grade**

| Category | Percentage |
| -------- | ---------- |

{%- for item in components %}
| {{ item.label }} | {{ item.weight_percent }}% |
{%- endfor %}
| **Total** | **{{ total }}%** |
{% endif %}

### Can you show me a chart of how my final grade is computed?

![Pie chart of grade breakdown]({{ chart_title }})

### How are the assignments graded?

{{ assignment_grading }}

### How soon will grades be posted on D2L/Brightspace?

{{ grade_turnaround }}

## Request for alternative feedback.

{{ feedback_format }}

## AI and Academic Integrity

### What happens if I cheat in this course (Academic Integrity)?

{{ academic_integrity }}

### May I use ChatGPT or other generative A.I. tools in this course?

{{ ai_usage }}

## RCTC Policies

### I have a health or learning difference that will require some accommodations. How do I set those up (Americans with Disability Act)?

{{ ada }}

### I am a military veteran, are there services available on campus (Military Friendly Statement)?

{{ veterans }}

### What are the campus policies about sexual harassment, misconduct, or violence (Title IX Statement)?

{{ title_ix }}

## Course Schedule Overview

**REFERENCE INFORMATION - You don't need to read this now**

| Week | Topic | Readings | Projects | Discussions | Exams | Due Date |
| ---- | ----- | -------- | -------- | ----------- | ----- | -------- |

{%- for week in weeks %}
| {{ week.week }} | {{ week.topic }} | {%- for reading in week.readings %} · {{ reading.title }} {%- endfor %} | {%- for project in week.projects.assigned %} {%- if project['code'] %} · **{{ project['code'] }}**: {%- endif %} {{ project.label }}{%- if project['due_date'] %} **(due {{ project['due_date'] }})** {% endif %} {%- endfor %} | {%- for discussion in week.discussions %} · **{{ discussion['code']}}**: {{ discussion['label']}} {% endfor %} | {%- for exam in week.exams %} {% if exam['code'] %} · **{{ exam['code'] }}**:{% endif %} {{ exam['label'] }} {% endfor %} | {{ week.due_date }} |
{%- endfor %}
