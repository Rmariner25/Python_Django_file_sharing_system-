# Ushare - Django study resources sharing system

[![CodeQL](https://github.com/Rmariner25/django_web_app/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/Rmariner25/django_web_app/actions/workflows/codeql-analysis.yml)
[![Django CI](https://github.com/Rmariner25/django_web_app/actions/workflows/django.yml/badge.svg)](https://github.com/Rmariner25/django_web_app/actions/workflows/django.yml)
[![MIT License](https://img.shields.io/github/license/Rmariner25/Django_web_app)](https://github.com/Rmariner25/django_web_app/blob/main/LICENSE)

A Django web application that allows users to view, share and manage study resources. 

## Current features

* Users can share files (provided they are logged in) and download files uploaded by other users.
* Users can search in the uploaded content.
* The allowed files types include files with extension .pdf, .doc, .docx, .ppt, .pptx and .txt.
* A user is required to submit title and description of the file to be uploaded.
* The file to be uploaded should be <= 15 MB (all this is configurable within the code).
* Users can manage i.e edit and delete their uploads.
* User can edit their profile.
* Admin pages to regulate the content and manage users and their roles.
* The web-pages are responsive, clean and clutter-free.

## Running the project locally

### Pre-requisites:

* Make sure you have [Python 3](https://www.python.org/downloads/) and pip installed on your system.

### Steps:

1. First, clone the repository to your local machine: 
  
   ```bash
   git clone https://github.com/Rmariner25/django_web_app.git
   ```
  
2. Then cd into the folder base directory `django_web_app`:

   ```bash
   cd django_web_app
   ```

3. Install virtual environment and activate it:
* For Windows:
   ```bash
   pip install virtualenv
   ```
   ```bash
   virtualenv venv
   ```
   ```bash 
   venv\Scripts\activate
   ```
* For Ubuntu Linux:
   ```bash
   sudo apt install virtualenv
   ```
   ```bash
   virtualenv -p python3 venv
   ```
   ```bash
   source venv/bin/activate
   ```
  
4. Install the dependencies as in `requirements.txt`:
  
   ```bash
   pip install -r requirements.txt
   ```
  
5. Run the development server:</li>

   ```bash
   python manage.py runserver
   ```

6. Now, copy the url http://127.0.0.1:8000 and paste it in your web browser's address bar. 

### Superuser:

7. To log into admin at http://127.0.0.1:8000/admin create a super user:

   ```bash
   python manage.py createsuperuser
   ```

## Screenshots

Home page (logged in):

![Home page](https://github.com/Rmariner25/django_web_app/blob/main/Screenshots/home_page.jpg) 
<br>

New upload (logged in):

![New upload](https://github.com/Rmariner25/django_web_app/blob/main/Screenshots/new_upld.jpg) 
<br>
