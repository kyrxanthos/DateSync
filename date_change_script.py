import os
import subprocess
import sys

def change_last_modified_date(file_path, new_date):
    # Convert the new date to touch command format
    touch_command = f"touch -t {new_date} '{file_path}'"
    # Use subprocess to execute the touch command
    subprocess.run(touch_command, shell=True)

def main(directories):
    
    for directory in directories:
        print(f'Converting directory {directory}...')
        # Extract the date from the directory name and reformat it
        date_str = directory.split('/')[-1].split()[0]
        formatted_date = f"{date_str[:4]}{date_str[5:7]}{date_str[8:10]}0000"
        # Get the path of the directory
        directory_path = os.path.join(os.getcwd(), directory)
        # Get the list of files in the directory
        files = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]
        # Change the last modified date of each file in the directory
        for file in files:
            file_path = os.path.join(directory_path, file)
            change_last_modified_date(file_path, formatted_date)
            print(f'changed modified date of {file_path} to {formatted_date}')

if __name__ == "__main__":
    # Get directories from command-line arguments excluding the script name
    directories = sys.argv[1:]
    main(directories)
