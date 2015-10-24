from django.utils.translation import ugettext_lazy as _

import horizon
from openstack_dashboard.dashboards.forum import dashboard

class Comment(horizon.Panel):
    name = _("Comment")
    slug = "comment"


dashboard.Forum.register(Comment)
