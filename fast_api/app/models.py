# Database Connection Parameters

DATABASE = 'tmp'
USERNAME = 'tmp_user'
PASSWORD = 'tmp_user@1234'
AUTH_DB = 'admin'

import datetime
from mongoengine import connect, Document, StringField, DateTimeField

connect(DATABASE, username=USERNAME, password=PASSWORD, authentication_source=AUTH_DB)

class Post(Document):
    title = StringField(required=True, max_length=200)
    content = StringField(required=True)
    author = StringField(required=True, max_length=50)
    published = DateTimeField(default=datetime.datetime.now)
