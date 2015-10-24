from django.utils.translation import ugettext_lazy as _

import horizon
from openstack_dashboard.dashboards.forum import dashboard

class Post(horizon.Panel):
    name = _("Post")
    slug = "post"


dashboard.Forum.register(Post)
