import traceback
import time
from time import mktime
from datetime import datetime
from requests.auth import HTTPBasicAuth
 
from django.template.defaultfilters import register
from django.utils.translation import ugettext_lazy as _
import requests
import time
from random import randint
 
from horizon import exceptions
 
requests.packages.urllib3.disable_warnings()
 
forum_url = "http://188.166.237.75/api"
json_headers = {'Accept': 'application/json'}
 
class Post:
    """
    Post data
    """
 
    def __init__(self, id, title, content, created_at, owner):
        self.id = id
        self.title = title
        self.content = content
        self.created_at = created_at
        self.owner = owner
	self.active = True
 
def getPosts(self):
    try:
        r = requests.get(forum_url + "/post", verify=False, auth=HTTPBasicAuth('admin', 'forum'), headers=json_headers)
 
        print (r.json())

        posts = []
        for post in r.json():
            posts.append(Post(post[u'id'], post[u'title'], post[u'content'], post[u'created_at'], post[u'owner']))
 
        return posts
 
    except:
        exceptions.handle(self.request,
                          _('Unable to get post'))
        return []
 
# request - horizon environment settings
# context - user inputs from form
def addPost(self, request, context):
    try:
        _id = randint(0,999)
        title = context.get('title')
        content = context.get('content')
        owner = request.user.username
        created_at = time.strftime("%c")
 
        payload = {'id': _id,  'title': title, 'content': content, 'owner': owner, 'created_at': created_at}
        requests.post(forum_url + "/post", json=payload, verify=False, headers=json_headers)
 
    except:
        print "Exception inside utils.addPost"
        print traceback.format_exc()
        exceptions.handle(self.request,
                          _('Unable to add post'))
        return []
 
# id is required for table
def deletePost(self, id):
    try:
 
        requests.delete(forum_url + "/post/" + id, verify=False, auth=HTTPBasicAuth('admin', 'forum'), headers=json_headers)
 
    except:
        print "Exception inside utils.deletePost"
        print traceback.format_exc()
        exceptions.handle(self.request,
                          _('Unable to delete post'))
        return False
