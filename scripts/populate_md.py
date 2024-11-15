import os


def populate_readme():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_dir = os.path.abspath(os.path.join(script_dir, ".."))
    readme_path = os.path.join(repo_dir, "README.md")

    with open(readme_path, "r") as file:
        lines = file.readlines()

    # Find the index to insert the new lab links
    start_index = next(i for i, line in enumerate(lines) if line.startswith("## Labs"))
    end_index = next(
        (
            i
            for i, line in enumerate(lines[start_index + 1 :], start=start_index + 1)
            if line.startswith("## ")
        ),
        len(lines),
    )

    # Collect existing lab directories
    existing_labs = [
        d
        for d in os.listdir(repo_dir)
        if d.startswith("CI2024_lab") and os.path.isdir(os.path.join(repo_dir, d))
    ]

    # Create lab links
    lab_links = [f"- [{lab}]({lab}/README.md)\n" for lab in existing_labs]

    # Sort the lab links
    lab_links.sort(key=lambda x: int(x.split("CI2024_lab")[1].split("]")[0]))
    
    # Add a new line at the start and two lines at the end of the list
    lab_links.insert(0, "\n")
    lab_links.append("\n")
    lab_links.append("\n")


    # Update the lines with sorted lab links
    lines = lines[: start_index + 1] + lab_links + lines[end_index:]

    with open(readme_path, "w") as file:
        file.writelines(lines)

    print("Updated README.md with lab links")


if __name__ == "__main__":
    populate_readme()
