# Weather Application
### CI/CD flows
- change in weatherapp/models.py - database update using "python3 manage.py makemigrations && python3 manage.py migrate"
- change in weatherapp/static folder - frontend update using "python3 manage.py collectstatic": all static files (including weatherapp/static) will be copied into separate directory staticfiles/ which should be deployed to nginx
- anything else - backend redeploy