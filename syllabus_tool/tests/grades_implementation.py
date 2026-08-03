import yaml
from jinja2 import Environment
from pathlib import Path
import pypandoc  # type: ignore
from pprint import pprint
import matplotlib.pyplot as plt


# open the course information
yaml_path = Path("./ART-2286-S26-31.yml")
with yaml_path.open("r", encoding="utf-8") as f:
    course_info = yaml.safe_load(f)
    grading_type = course_info["course"]["grading_type"]


if grading_type == "weighted_percent":
    assessments = course_info["course"]["assessment_structure"]["components"]
    pprint(assessments)

total = 0
grade_weights = {}

# sanity check for percentages
for item in assessments:
    # make a dict for pie chart
    weight = item["weight_percent"]
    label = item["label"]
    grade_weights[label] = weight
    # sum the weights for sanity check
    total += weight
if total != 100:
    raise ValueError(f"Grading weights must total 100, got {total}")

# create a pie chart
plt_labels = list(grade_weights.keys())
plt_weights = list(grade_weights.values())

# make the figure
plt.figure()
plt.pie(plt_weights, labels=plt_labels, autopct="%1.0f%%", startangle=90)

plt.axis("equal")

# save the chart
plt.savefig("grade_breakdown.png", dpi=150, bbox_inches="tight")
plt.close()


env = Environment(autoescape=False)

template_str = env.from_string("""
## How is my final grade computed?
| Category | Percentage |
|----------| ---------- |
{%- for item in assessments %}
| {{ item.label }} | {{ item.weight_percent }}% |
{%- endfor %}
| **Total** | **{{ total }}%** |

### Can you show me a chart of how my final grade is computed?        
![Pie chart of grade breakdown](grade_breakdown.png)

""")

output = template_str.render(assessments=assessments, total=total)


print("Outputting to Word Document.")
pypandoc.convert_text(output, to="docx", format="md", outputfile="grade_breakdown.docx")
