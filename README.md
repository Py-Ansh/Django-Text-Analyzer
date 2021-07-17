# Text Utilizers

A simple tool to analyze text written in python's django backend web frame work

## What Can you do with this website?
Remove Punctuations in the text

Remove Numbers in the text

Remove New Lines in the text

Remove Extra Spaces in the text

Change text to Upper and Lower case

Count Only Characters present in the text

(Includes a contact page also to send contact messages to the database)

## Usage
After you cloned this repository install the dependencies

```bash
pip3 install -r requirements.txt
```
After that makemigrations and migrate
```bash
python3 manage.py makemigrations
```

```bash
python3 manage.py migrate
```
Create a superuser

```bash
python3 manage.py createsuperuser
```
At last
```bash
python3 manage.py runserver
```
To start this webapp

## what After That?

Enter the text to analyze in the textbox select operations and click on Analyze Button and see the output according to the operators you selected.

For example if you have entered "python" in the textbox and selected UPPER CASE operator and clicked on analyze button then it will change "python" which is in lower case to "PYTHON" which is in upper case now.

## Dependencies
Python3

Django
