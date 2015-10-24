import traceback
 
from horizon import workflows, forms, exceptions
from django.utils.translation import ugettext_lazy as _
 
from openstack_dashboard.dashboards.forum.post import utils
 
class SetAddPostDetailsAction(workflows.Action):
 
    title = forms.CharField(
        label=_("Title"),
        required=True,
        max_length=80,
        help_text=_("Title"))
 
    content = forms.CharField(
        label=_("Description"),
        required=True,
        max_length=120,
        help_text=_("Description"))

    status = forms.ChoiceField (
        label=_("Status"),
        required=True,
        widget=forms.Select(),
        choices=(
            (1, _("Active")),
            (2, _("Lock"))
        ),
        help_text=_("Status post"))


    class Meta:
        name = _("New")
 
    def __init__(self, request, context, *args, **kwargs):
        self.request = request
        self.context = context
        super(SetAddPostDetailsAction, self).__init__(
            request, context, *args, **kwargs)

        # Set our user options
        # self.fields['owner'].default = request.user.id
 
class SetAddPostDetails(workflows.Step):
    action_class = SetAddPostDetailsAction
    contributes = ("title", "content", "status")
 
    def contribute(self, data, context):
        if data:
            context['title'] = data.get("title", "")
            context['content'] = data.get("content", "")
            context['status'] = data.get("status", "")
        return context
 
class AddPost(workflows.Workflow):
    slug = "add"
    name = _("Add new post")
    finalize_button_name = _("Add")
    success_message = _('Added provider "%s".')
    failure_message = _('Unable to add post "%s".')
    success_url = "horizon:forum:post:index"
    failure_url = "horizon:forum:post:index"
    default_steps = (SetAddPostDetails,)
 
    def format_status_message(self, message):
         return message % self.context.get('title', 'unknown')
 
    def handle(self, request, context):
        try:
            utils.addPost(self, request, context)
            return True
        except Exception:
            print traceback.format_exc()
            exceptions.handle(request, _("Unable to add provider"))
            return False