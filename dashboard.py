from django.utils.translation import ugettext_lazy as _

import horizon

class Post(horizon.PanelGroup):
    slug = "post"
    name = _("Post")
    panels = ('post',)

class Forum(horizon.Dashboard):
    name = _("Forum")
    slug = "forum"
    panels = (Post,)  # Add your panels here.
    default_panel = 'post'  # Specify the slug of the dashboard's default panel.

horizon.register(Forum)