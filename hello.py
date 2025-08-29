# File Read & Write with Error Handling

def modify_content(content):
    """Example modification: convert text to uppercase"""
    return content.upper()

# Ask the user for the filename
filename = input("Enter the name of the file to read: ")

try:
    # Try opening and reading the file
    with open(filename, "r") as file:
        content = file.read()

    # Modify the content
    modified_content = modify_content(content)

    # Write to a new file
    new_filename = "modified_" + filename
    with open(new_filename, "w") as new_file:
        new_file.write(modified_content)

    print(f"File successfully modified and saved as '{new_filename}'.")

except FileNotFoundError:
    print("Error: The file does not exist. Please check the filename and try again.")

except PermissionError:
    print("Error: You don’t have permission to read this file.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")