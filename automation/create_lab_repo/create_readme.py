def create_readme(directory):
    """
    Function to create a README.md file with a standard template in the specified directory.

    Args:
        directory (str): The directory path where the README.md file will be created.

    Returns:
        bool: True if the README.md file is successfully created, False otherwise.
    """
    import os
    readme_template = """
# LAB - Class xx

## Project: Project Name Here

### Author: Student/Group Name

### Links and Resources

- [Back-end Server URL] # Fill in when applicable
- [Front-end Application URL] # Fill in when applicable
- [CodeFellows Python Lab Instructions](https://codefellows.github.io/code-401-python-guide/reference/submission-instructions/labs/)
- [CodeFellows README template](https://codefellows.github.io/code-401-python-guide/reference/submission-instructions/labs/README-template.html)
- lecture demo code used for reference
- [ChatGPT chat]() # Fill in when applicable
- GitHub CoPilot used for... #Fill in when applicable

### Setup
- Create a `.env` file with the following requirements:
  - PORT - Port Number
  - DATABASE_URL - URL to the running Postgres instance/db
- OR *.env requirements: n/a*

### How to Initialize/Run Your Application

- Install requirements.txt
- Example: Enter CLI command "python manage.py runserver"

### How to Use Your Library
- Provide instructions here if applicable

### Tests
#### How to Run Tests
- Describe how to run tests

#### Tests of Note
- Any noteworthy information about the tests

#### Incomplete Tests
- Describe any tests that were not completed or skipped
"""

    with open(f'{directory}/README.md', 'w') as readme:
        readme.write(readme_template)

    return os.path.exists(f'{directory}/README.md')
