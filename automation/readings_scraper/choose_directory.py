import os
from tkinter import filedialog
from rich.console import Console


def choose_directory(file_name):
    """
    Prompt the user to choose a directory for the reading assignment file.

    This function asks the user if they want to choose a different folder for the reading assignment file. 
    If the user chooses to select a different folder, it opens a file dialog for the user to choose the folder. 
    If the user chooses not to select a different folder, it places the file in the 'reading_assignments' folder 
    at the same level as the program. If the 'reading_assignments' folder doesn't exist, it creates one.

    Args:
        file_name (str): The name of the reading assignment file.

    Returns:
        str: The file path where the reading assignment file will be saved.
            Returns False if the user chooses not to overwrite an existing file.
    """
    console = Console()
    console.print("\nThis program will create a 'reading_assignments' folder for you at the same level as this program if one doesn't already exist. Would you like to choose a different folder for your reading assignment file instead? (y/n):", style="green3")
    choose_directory = input("> ")

    if choose_directory.lower() in ["y", "yes"]:
        directory = filedialog.askdirectory(title="Choose your folder for your reading assignment file")
        file_path = os.path.join(f'{directory}/{file_name}')
    
    elif choose_directory.lower() in ["n", "no"]:
        console.print(f"Ok! Your file will be placed in the 'reading_assignments' folder.", style="bold yellow")
        directory = os.path.abspath(f'../{os.curdir}')
        folder_path = os.path.join(f'{directory}/reading_assignments')
        file_path = os.path.join(f'{folder_path}/{file_name}')
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
    
    else:
        console.print("Response not recognized. Returning to folder directory prompt.", style="bold red")
        choose_directory()
    
    
    if os.path.exists(file_path):
        console.print("\nThis file already exists.", style="bold red")
        user_input= input("Would you like to overwrite it? (y/n): ")
        
        if user_input.lower() in ["y", "yes"]:
            console.print("Sounds good! Your file will be overwritten.", style="bold yellow")
        
        elif user_input.lower() in ["n", "no"]:
            console.print("Ok! Aborting reading_file mission.", style="bold red")
            return False

        else:
            console.print("Response not recognized. Returning to folder directory prompt.", style="bold red")
            choose_directory()

    return file_path
