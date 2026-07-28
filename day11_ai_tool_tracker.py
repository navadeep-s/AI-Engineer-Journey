ai_tools = [
    {"name": "ChatGPT", "company": "OpenAI"},
    {"name": "Claude", "company": "Anthropic"},
    {"name": "Gemini", "company": "Google"}
]


def display_tools(tools):
    for tool in tools:
        print(tool["name"], "-", tool["company"])


def save_tool(tool):
    with open("ai_tool.txt", "a") as file:
        file.write(tool["name"] + "," + tool["company"] + "\n")


def load_saved_tools(tools):
    try:
        with open("ai_tool.txt", "r") as file:
            for line in file:
                parts = line.strip().split(",")

                saved_tool = {
                    "name": parts[0],
                    "company": parts[1]
                }

                tools.append(saved_tool)

    except FileNotFoundError:
        print("No saved tools found.")


load_saved_tools(ai_tools)

print("Current AI tools:")
display_tools(ai_tools)

new_name = input("\nEnter AI tool name: ")
new_company = input("Enter company: ")

tool_exists = False

for tool in ai_tools:
    if tool["name"] == new_name:
        tool_exists = True

if tool_exists:
    print("\nTool already exists.")

else:
    new_tool = {
        "name": new_name,
        "company": new_company
    }

    ai_tools.append(new_tool)
    save_tool(new_tool)

    print("\nTool added successfully.")

print("\nUpdated AI tools:")
display_tools(ai_tools)

tool_count = len(ai_tools)
print("Total tools:", tool_count)