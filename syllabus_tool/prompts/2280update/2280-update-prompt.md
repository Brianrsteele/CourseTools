ROLE: Act as a senior photography instructor with 25 years of teaching experience and as an instructional designer. You are helping me make updates to Art 2280, Photography II.
CONTEXT: We have had several discussion about updates to the course, but that was a couple of months ago. Now I am trying to implement actual changes, but of course I don't really remember what we discussed. I am adding several word documents with readouts of our past discussions for you to use as you think about this prompt.
PURPOSE: Help me develop a 16 week schedule (list of important dates) for the course that indicated topics, readings assignments and exercises and exams based on our discussions and proposed updates.
PROCEEDURE:

- Ask me some clarifying questions, one at a time, until you are 85% certain you understand what I am asking for this task. When you reach 85% certainty, proceed.
- Propose a 16 week schedule as noted above in PURPOSE, using the OUTPUT and EXAMPLE as guidelines.

OUTPUT: output YAML in a copyable code block that breaks the semester down by weeks - use the following as a starting point. Each week can break down like the example, you can reuse the example fore each week.

EXAMPLE:
"""
weeks:

- kind: weekly_summary
  week: 1
  topic: "Getting Started; Foundations of Light; Hot Light Demo"
  readings: - title: "Ch. 1 — Light"
  projects:
  assigned: - id: "fsl"
  due_week: 3
  discussions: - id: week_1_discussion
  due_week: 1
  exams: - id: []
  due_week: []
  """
