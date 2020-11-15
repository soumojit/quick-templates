# Database Connection Parameters

DATABASE = 'tmp'
USERNAME = 'tmp_user'
PASSWORD = 'tmp_user@1234'
AUTH_DB = 'admin'

## [macOS - db on localhost, app on local]
# HOST = 'localhost' or '127.0.0.1'
## [macOS - db on localhost, app in docker]
HOST = 'docker.for.mac.localhost'

import datetime
from mongoengine import connect, Document, StringField, DateTimeField

connect(DATABASE, host=HOST, username=USERNAME, password=PASSWORD, authentication_source=AUTH_DB)

class Post(Document):
    title = StringField(required=True, max_length=200)
    content = StringField(required=True)
    author = StringField(required=True, max_length=50)
    published = DateTimeField(default=datetime.datetime.now)
