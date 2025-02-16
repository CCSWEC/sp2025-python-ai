![Static Badge](https://img.shields.io/badge/build-passing-brightgreen) ![Static Badge](https://img.shields.io/badge/python-3.8+-nextpart?logo=python)

# Python-AI Project

---

This repository is one of Collin College's SWE club projects during the Spring 2025 semester.

# Getting started

---

Follow these instructions to set up the project properly:

#### Install Git

Git is required to run this project.

This is the version control and the tool we will be using to update and upload our progress.

You can find the link to install it here: [Git website](https://git-scm.com/)

In the installation manager, you should go with the default options. If it asks you for a text editor, nano is highly recommended.

#### Install Python

Python is needed to run the dependencies here.

The latest version is consistently posted on python's website:

[Python download page](https://www.python.org/downloads/)

#### Which Editor to use?

Here are my recommendations:

- **VSCode:**
    - Lightweight text editor which is good for general purpose projects. Additional set up is required but it's more adaptable and extensive to other features. 
    - Set up: Open the extensions sidebar by clicking the puzzle piece on the lefthand screen. Then search for the following and enable them:
        - Python
        - Pylance
        - Python Debugger
    - Download can be found here: [VSCode website](https://code.visualstudio.com/)

- **PyCharm:**
    - A JetBrains IDE, which is useful for python projects without requiring additional set up and plugins. It is also a good option to install the JetBrains manager to use its other environments for other languages.
    - You can find the link here: [Pycharm page](https://www.jetbrains.com/pycharm/)

### Further Steps


#### I don't see the project

If the CCSWEC projects are not shown, that probably means you haven't yet been added to our GitHub organization, in which case you should post your GitHub username in the `#orginv` channel on the SWE Club Discord.
#### Cloning the project

In order to begin contributing, you will have to clone the project from GitHub using your editor. You can find the info by simply clicking the green "code" button.
#### Using VSCode

In VSCode, open the explorer sidebar by pressing the explorer (overlapping pages) icon on the sidebar. (If it was already open, it will close. Press again to reopen it.)

If you don't see a "Clone Repository" button in the sidebar, use File -> Close Folder, and then "Clone Repository" should appear in the explorer sidebar.

Press "Clone Repository," then select "Clone from GitHub" in the dialog. Sign in to GitHub if necessary. Search the list and select "CCSWEC/sp2025-python-ai".
Then choose a folder to store your copy, and, if asked, select the option to open the repository in the current window.
If prompted, select the option to trust this repository.

Once the project is loaded in VSCode (which may take a couple of minutes because of the build process), press the elephant icon in the sidebar to open the Gradle panel.
Expand the "Tasks" menu, and then the "application" section.

#### Using PyCharm

Find the configuration dropdown in the top bar (it's just left of the green run arrow icon).
Expand the dropdown and press "Edit Configurations."

In the dialog, press the plus icon near the top left and select Gradle.
Then, with the new Gradle task selected in the sidebar, change the name field to "PythonAI" and the "Run" field to "run".
Close the dialog. Then make sure your new PythonAI target is selected in the configuration dropdown.

After this, you can run the project by pressing the green run arrow icon.
#### Setting up dependencies

- When you have the file installed, to ensure you have the correct libraries, run the following command in your project directory:

```
pip install -r requirements.txt
```

#### API token

- This is just a fancy term for a protected code that is used for the user to gain access to the AI services.
- It's very important to add your own key to the .env file so that personal data isn't stolen (Data leaks are very bad).
- You can create an OPENAI token here if the current code fails: [openai keys](https://platform.openai.com/settings/organization/api-keys)

#### Project Objectives:


- **Input**: User submits input to the system.

- **Response Generation**: The input is sent to three separate chatbots for individual responses.

- **Summary**: Each response is combined and sent to a fourth chatbot for processing.

- **Output**: The summary created by the fourth chatbot is collected and sent to the user.
