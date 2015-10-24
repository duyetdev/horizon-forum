import traceback
import time
from time import mktime
from datetime import datetime
from requests.auth import HTTPBasicAuth
 
from django.template.defaultfilters import register
from django.utils.translation import ugettext_lazy as _
import requests
 
from horizon import exceptions
 
requests.packages.urllib3.disable_warnings()
 
forum_url = "https://localhost:8443/rest"
json_headers = {'Accept': 'application/json'}
 
class Post:
    """
    Post data
    """
 
    def __init__(self, id, title, content):
        self.id = id
        self.title = title
        self.content = content
 
def getPosts(self):
    try:
        r = requests.get(forum_url + "/post", verify=False, auth=HTTPBasicAuth('admin', 'forum'), headers=json_headers)
 
        post = []
        for post in r.json()['post']:
            post.append(Post(post[u'id'], post[u'title'], post[u'content']))
 
        return post
 
    except:
        exceptions.handle(self.request,
                          _('Unable to get post'))
        return []
 
# request - horizon environment settings
# context - user inputs from form
def addPost(self, request, context):
    try:
 
        title = context.get('title')
        content = context.get('content')
 
        payload = {'title': title, 'content': content}
        requests.post(forum_url + "/post", json=payload, verify=False, auth=HTTPBasicAuth('admin', 'forum'), headers=json_headers)
 
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