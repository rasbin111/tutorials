First, perfrom migrations and migrate changes to database 
```bash
python manage.py makemigrations
python manage.py migrate
```
Add some data to course models.

Now, run you project:
```bash
python manage.py runserver
```
Open browser, and go to http://localhost:8000/graphql and play around with queries and mutations. 

