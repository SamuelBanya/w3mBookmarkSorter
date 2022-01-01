# w3mBookmarkSorter

## GIT CLONE INSTRUCTIONS
You can 'git clone' the repo with the following command so you can use the utility locally on your Linux machine:
`git clone https://git.musimatic.net/w3mBookmarkSorter`

## SETTING UP 'pip3' DEPENDENCIES WITH 'venv':
You need to then create a virtual environment called 'venv' to house the project itself so that you can pull in dependencies in the
same directory without potentially interfering with your user's already-installed pip3 based Python 3 packages:
`python3 -m venv venv`

Once you've cloned the repository, you need to then run:
`source venv/bin/activate`

Then, once your terminal has (venv) present near your name, you need to then pull in dependencies with 'pip3':
`pip3 install -r requirements.txt`

This will then pull down the dependencies you need to run the "w3mBookmarkSorter.py" utility.

## ADJUSTING THE 'config' FILE:
The only thing you need to adjust is the "w3m_directory" variable in the "config" file in the directory you placed the 'w3mBookmarkSorter' project in. 

The value of the "w3m_directory" variable will be the directory where your ".w3m" directory resides on your machine (typically "~/(username)/.w3m", ex: "~/joe/.w3m"

If this is left blank, the 'main.py' script will prompt you for it upon the first run of the program, and then write it to the file after you've been prompted for this directory.

This is to allow for an easy process of re-running the program later on, especially if you plan on adding the 'w3mBookmarkSorter/main.py' script to your ~/.bashrc via a Bash alias for ease of use after adding bookmarks to w3m after a given surfing session.

## RUNNING THE UTILITY
Make sure you've followed the "SETTING UP 'pip3' DEPENDENCIES WITH 'venv':" section above, as you will need to run a 'venv' virtual environment to utilize the correct dependencies.

You can run the utility by using the following command:
`python3 main.py`

This will sort your bookmarks in terms of their overarching sections from 'A' to 'Z', and will make your bookmarks file look much nicer as a result.

Enjoy, pay it forward, and keep it FOSS! :)
