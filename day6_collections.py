languages = ["Python", "SQL", "Java"]
print(languages)
print(languages[1])

ai_tools = ["ChatGPT", "Claude", "Gemini", "Codex"]
print(ai_tools[2])

ai_tools[1] = "Claude Code"
print(ai_tools)

ai_tools.append("LangChain")
print(ai_tools)

skills = ["Python", "Git", "GitHub"]

skills.append("SQL")

print(skills)

skills.remove("Git")
print(skills)

number_of_skills = len(skills)
print("Number of Skills:", number_of_skills)

for skill in skills:
    print("Learning:", skill)

project_tools = ["Python", "Git", "Notion"]

project_tools[2] = "GitHub"
print(project_tools)

project_tools.append("SQL")
print(project_tools)

project_tools.remove("Git")
print(project_tools)

tool_count = len(project_tools)
print("Number of Project Tools:", tool_count)

for tool in project_tools:
    print("Project Tool:", tool)


if "Python" in project_tools:
    print("Python is available")
else:
    print("Python is missing")

supported_files = [".pdf", ".txt", ".csv"]

uploaded_file = ".json"

if uploaded_file in supported_files:
    print("File supported")
else:
    print("File not supported")

available_models = ["ChatGPT", "Claude", "Gemini"]

for model in available_models:
    print("Available Model:", model)

selected_model = input("Choose a model: ")

if selected_model in available_models:
    print("Selected:", selected_model)
else:
    print("Model unavailable")
