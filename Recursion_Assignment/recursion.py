'''Problem Scenario: Finding a File in a Folder
Imagine you have a file system with folders and files. You want to recursively search for a specific file within a folder structure with the use of recursion.
 '''
def find_file(file_system, file_to_find, current_path=""):
    for key, value in file_system.items():
        new_path = f"{current_path}/{key}"
        if value is None: 
            if key == file_to_find:
                return f"File '{file_to_find}' found at: {new_path}"
        elif isinstance(value, dict): 
            result = find_file(value, file_to_find, new_path)
            if result:  
                return result
    return None  
file_system = {
    "documents": {
        "work": {
            "report.docx": None,
            "summary.xlsx": None,
        },
        "personal": {
            "photos": {
                "vacation.jpg": None,
                "birthday.png": None,
            },
        },
    },
    "downloads": {
        "software": {
            "setup.exe": None,
        },
        "music": {
            "song.mp3": None,
        },
    },
}

file_to_find =input("enter file name:")

result = find_file(file_system, file_to_find)
if result:
    print(result)
else:
    print(f"File '{file_to_find}' not found.")
