ai_tool = {
    "name": "ChatGPT",
    "company": "OpenAI"
}

print(ai_tool)

print(ai_tool["name"])


ai_tool["company"] = "OpenAI Inc."

print(ai_tool["company"])

print(ai_tool)

ai_tool["category"] = "AI Assistant"
print(ai_tool)

del ai_tool["category"]

print(ai_tool)


for key in ai_tool:
    print(key, ":", ai_tool[key])


for key, value in ai_tool.items():
    print(key, ":", value)

ai_model = {
    "name":"Gemini", 
    "company":"Google", 
    "status":"Available"    
}

print(ai_model)

ai_model["status"] = "Selected"

print(ai_model)

for key, value in ai_model.items():
    print(key, ":", value)

if ai_model["status"] == "Selected":
    print("Model is ready")
else:
    print("Select a model")

ai_model["version"] = "2.5"

print(ai_model)

print(ai_model.get("version", "Not provided"))

del ai_model["version"]

print(ai_model)

if "version" in ai_model:
    print("Version is available")
else:
    print("version is missing")


job_posting = {
    "title": "Junior AI Engineer",
    "company": "TechNova",
    "status": "Open"
}

print(job_posting["company"])

job_posting["status"] = "Closed"

print(job_posting)

job_posting["location"] = "Cleveland"

print(job_posting)

for key, value in job_posting.items():
    print(key, ":", value)

