 

This repository contains the work that has been done so far on the chess tournament program.

### Data files

There are data files provided:
- JSON files for the chess clubs of Springfield and Cornville
- JSON files for two tournaments: one completed, and one in progress

### Models

This package contains the models already defined by the application:
* `Player` is a class that represents a chess player
* `Club` is a class that represents a chess club (including `Player`s)
* `ClubManager` is a manager class that allows to manage all clubs (and create new ones)

### Screens

This package contains classes that are used by the application to display information from the models on the screen.
Each screen returns a Command instance (= the action to be carried on).

### Commands

This package contains "commands" - instances of classes that are used to perform operations from the program.
Commands follow a *template pattern*. They **must** define the `execute` method.
When executed, a command returns a context.

### Main application

The main application is controlled by `manage_clubs.py`. Based on the current Context instance, it instantiates the screens and run them. The command returned by the screen is then executed to obtain the next context.

The main application is an infinite loop and stops when a context has the attribute `run` set to False.


## Setting Up the Environment

To set up the project environment, follow these steps:

1. Ensure you have Python installed on your system. This project is tested with Python 3.8+.

2. Clone this repository to your local machine: 

    git clone https://github.com/OpenClassrooms-Student-Center/P3-Application-Developer-Skills-Bootcamp.git

    cd your-repository-directory

3. Create a virtual environment: python -m venv venv

4. Activate the virtual environment:

   - On Windows:
     ```
     .\venv\Scripts\activate
     ```
   - On Unix or MacOS:
     ```
     source venv/bin/activate
  
5. Install the required packages: pip install -r requirements.txt

6. ## Running the Program
    * python3  manage_clubs.py: to create a club json file
    * python3 create-tournament.py: to create an initial tournament json file 
    * python3 tournament_manager.py: to make updates to the tournament JSON file and also create a new JSON file 
      for the point system of the tournament.

## Generating a Flake8 Report

To lint the code and generate a new `flake8` report:

1. Install flake8 and flake8-html: pip install flake8 flake8-html
2. Run flake8 with the max-line-length option: To lint your code with a specific max line length of 119 characters, 
   you can use the --max-line-length option. Navigate to your project directory in the terminal and run:
   flake8 --max-line-length=119 . (The . at the end specifies that flake8 should lint all .py files in 
   the current directory and its subdirectories.)
3. Generate the flake8 HTML report: To generate an HTML report using flake8-html, you can use the --format=html 
   option followed by --htmldir to specify the directory where the report should be saved. If you want the report 
   in a directory called “flake8_report” as mentioned, you would run:
   flake8 --max-line-length=119 --format=html --htmldir=flake8_report . (This command tells flake8 to lint your code 
   according to PEP 8 guidelines with a maximum line length of 119 characters, format the output as HTML, 
   and save the report in a directory named “flake8_report” in your current working directory.)
4. Check for No Errors: After generating the report, open the flake8_report/index.html file in a web browser 
   to view the linting results. If your code adheres to PEP 8 guidelines with the specified configurations, 
   you should see no errors listed in the report. If there are any issues, the HTML report will detail them, 
   allowing you to make the necessary adjustments to your code. Keep modifying your code and regenerating 
   the report until no errors are displayed.)

