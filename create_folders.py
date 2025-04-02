import os
import subprocess

# List of team names
team_names = [
    "Koder", "Three musketeers", "SkillForge", "Bug Busters", "Codifo", "NG", "Deep Thinkers", "Code crusaders",
    "Creative souls", "V4", "Syntax squad", "Harshal and team", "Bytebuzz", "Visualizers", "hacknetic",
    "Blueberry", "Code catalyst", "Lucifer", "Quantum", "Hustlers", "X-Factor", "Coffee && Code",
    "Team Techno", "Web Weavers", "The warrior", "Web Wizards", "Tech titans", "System Squad",
    "Code breakers", "TechLog", "Tech Titans", "The code crusaders", "Code Crafters", "Bug Slayers",
    "decoders", "Treasure", "Tech squad", "Shadow coders", "Tanushree", "Blitz", "TachTitans"
]

# Create folders and add a .gitkeep file
for team in team_names:
    folder_name = team.replace(" ", "_")  # Replace spaces with underscores for safer directory names
    os.makedirs(folder_name, exist_ok=True)
    open(os.path.join(folder_name, ".gitkeep"), "w").close()

# Commit and push to GitHub
subprocess.run(["git", "add", "."])
subprocess.run(["git", "commit", "-m", "Added team folders"])
subprocess.run(["git", "push", "origin", "main"])  # Change 'main' if necessary
