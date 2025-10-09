def read_and_write_file():
    try:
        # Ask user for the filename to read
        filename = input("Enter the name of the file to read: ")

        # Try opening the file
        with open(filename, 'r') as file:
            content = file.read()

        # Modify the file content (example: convert to uppercase)
        modified_content = content.upper()

        # Ask user for a new file name to save modified content
        new_filename = input("Enter a name for the new file: ")

        with open(new_filename, 'w') as new_file:
            new_file.write(modified_content)

        print(f"\nFile '{filename}' was read successfully!")
        print(f"Modified content saved to '{new_filename}'")

    except FileNotFoundError:
        print("Error: The file you entered does not exist.")
    except PermissionError:
        print("Error: You don't have permission to read this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the function
read_and_write_file()