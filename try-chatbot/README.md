## Scripts for Chatbot's setup 

1. You can run, in the project directory;
### `cd try-chatbot`

<br>

2. To create a virtual environment (Windows)
### `python -m venv venv`
### `venv\Scripts\activate`
### `python -m pip install chatterbot==1.0.4 pytz`

<br>

2. To create a virtual environment (Linux / MacOS)
### `python -m venv venv`
### `source venv/bin/activate`
### `python -m pip install chatterbot==1.0.4 pytz`

<br>

3. To run the chatbot;
### `python bot.py`

<br>

#### gitignore content: venv is the virtual environment and db.sqlite3 is a sql database where it store all your inputs and possible responses.

#### Warning: The 'nltk_data' folder is going to install to default location in your operating system when you run the chatbot because the library might download some data and language models.