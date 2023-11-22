
## _Setup project_
### Clone the project in your system
install python 3.9 in your system by follwoing link
[python: 3.9](https://www.python.org/downloads/release/python-39/)
- Create virtual environment and activate it
    - To create virtual env: `python -m venv env`
    - To activate virtual env: `.\env\Scripts\activate`
- Now go to project directory and install all dependencies from requirement.txt
    - To install dependencies: `pip install -r .\requirements.txt`
- Setup database(SQLite)
    - `python manage.py migrate`
- Create super user
    - To create super user: `python manage.py createsuperuser`  
- Project is setup now, you can run the project by following command
    - `python manage.py runserver`
 

## Admin page
Login admin page
-- Go to http://localhost:8000/admin and login by user credentials

## Models/ Features

| Models/Feature | README/URLs | Local |
| ------ | ------ |------|
| Blog Article | http://3.110.169.115:8000/admin/article/blogarticle/  |http://localhost:8000/admin/article/blogarticle/ (For local)|
| Contact Requests | http://3.110.169.115:8000/admin/article/contactrequest/|  http://localhost:8000/admin/article/contactrequest/ (For local)|
| Home page | http://3.110.169.115:8000/  | http://localhost:8000/ (For local)|
| Article list | http://3.110.169.115:8000/articles/ | http://localhost:8000/articles (For local) |
| Medium |http://3.110.169.115:8000/contact/ |  http://localhost:8000/contact (For local)|