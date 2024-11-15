import os
import subprocess

def add_submodule(lab_number):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_dir = os.path.abspath(os.path.join(script_dir, ".."))
    lab_name = f"CI2024_lab{lab_number}"
    lab_url = f"https://github.com/CodeClimberNT/{lab_name}"
    lab_path = os.path.join(repo_dir, lab_name)

    # Check if the submodule already exists
    if os.path.exists(lab_path):
        print(f"Submodule {lab_name} already exists.")
        return False

    try:
        # Add the submodule
        subprocess.run(["git", "submodule", "add", lab_url, lab_path], check=True)
    except subprocess.CalledProcessError:
        print(f"Failed to add submodule {lab_name}. Repository may not exist.")
        return False

    print(f"Added submodule {lab_name}")
    return True

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_dir = os.path.abspath(os.path.join(script_dir, ".."))
    
    # Determine the next lab number
    existing_labs = [d for d in os.listdir(repo_dir) if d.startswith("CI2024_lab")]
    existing_lab_numbers = [
        int(lab.split("CI2024_lab")[1])
        for lab in existing_labs
        if lab.split("CI2024_lab")[1].isdigit()
    ]
    next_lab_number = max(existing_lab_numbers) + 1 if existing_lab_numbers else 1

    if add_submodule(next_lab_number):
        print(f"Successfully added CI2024_lab{next_lab_number}")
    else:
        print(f"Failed to add CI2024_lab{next_lab_number}")
        exit(1)