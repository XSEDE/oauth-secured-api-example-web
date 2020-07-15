# oauth-secured-api-example-web
Web API service example using XSEDE/Globus OAuth authentication
Built using the Django Rest Framework

# Example Dictionary Web App

- Welcome, link to add/list/delete, and API docs
<webroot>/dictionary/
<webroot>/dictionary/ui/add
<webroot>/dictionary/ui/list
<webroot>/dictionary/ui/delete
<webroot>/dictionary/api/<word>  # GET, UPDATE, DELETE
<webroot>/dictionary/api/              # POST


# Setup

git clone https://github.com/XSEDE/oauth-secured-api-example-web.git
cd oauth-secured-api-example-web
pipenv --python python3.7 --bare install
pipenv shell
django-admin startproject django_oauth_api
cd django_oauth_api
python manage.py migrate  
