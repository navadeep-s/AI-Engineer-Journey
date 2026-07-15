ai_providers = ("OpenAI", "Anthropic", "Google")
print(ai_providers)

print(ai_providers[1])


for provider in ai_providers:
    print("Provider:", provider)

ai_skills = {"Python", "RAG", "Python", "APIs"}
print(ai_skills)

ai_skills.add("Agents")

print(ai_skills)

ai_skills.add("Python")

print(ai_skills)

ai_skills.remove("RAG")

print(ai_skills)

ai_skills.discard("RAG")

print(ai_skills)

if "Python" in ai_skills:
    print("Python skill available")
else:
    print("Python skill missing")

required_skills = {"Python", "SQL", "Git"}
navi_skills = {"Python", "SQL", "GitHub"}

matching_skills = required_skills.intersection(navi_skills)

print(matching_skills)

missing_skills = required_skills.difference(navi_skills)

print(missing_skills)

extra_skills = navi_skills.difference(required_skills)

print(extra_skills)

all_skills = required_skills.union(navi_skills)

print(all_skills)

job_requirements = {"Python", "SQL", "APIs", "Git"}
current_skills = {"Python", "SQL", "GitHub", "Excel"}

matching_requirements = job_requirements.intersection(current_skills)

print(matching_requirements)

missing_requirements = job_requirements.difference(current_skills)

print(missing_requirements)

extra_requirements = current_skills.difference(job_requirements)

print(extra_requirements)

all_requirements = job_requirements.union(current_skills)

print(all_requirements)
