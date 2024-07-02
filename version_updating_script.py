import os

def read_elements_from_file(file_path):
    with open(file_path, 'r') as file:
        elements = [line.strip() for line in file if line.strip()]
    print(elements)
    return elements

def search_and_replace_in_repository(repo_path, elements):
    for root, dirs, files in os.walk(repo_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            with open(file_path, 'r') as file:
                lines = file.readlines()

            new_lines = []
            element_found = False
            version_found = False
            for line in lines:
                for element in elements:
                    if f"name = {element}" in line:
                        element_found = True
                if "version = 10" in line:
                    version_found = True
                    line = line.replace("version = 10", "version = 11")
                new_lines.append(line)

            if element_found and version_found:
                with open(file_path, 'w') as file:
                    file.writelines(new_lines)
                print(f"Updated version in {file_path}")

if __name__ == "__main__":
    elements_file = r"C:\Users\js105\Documents\git\version_updating\bq_names.txt"  # Change this to the path of your file containing elements
    repository_path = r"C:\Users\js105\Documents\git\repo_name"  # Change this to your desired repository path

    elements = read_elements_from_file(elements_file)
    if elements:
        search_and_replace_in_repository(repository_path, elements)
