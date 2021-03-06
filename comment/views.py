from horizon import views


from horizon import exceptions, tables, workflows, forms, tabs
 
from openstack_dashboard.dashboards.forum.comment.tables import PostTable
from openstack_dashboard.dashboards.forum.comment import utils
from openstack_dashboard.dashboards.forum.comment.add_comment import AddPost
 
class PostsIndexView(tables.DataTableView):
    table_class = PostTable
    template_name = 'forum/comment/index.html'
 
    def get_data(self):
        return utils.getPosts(self)
 
class AddPostView(workflows.WorkflowView):
    workflow_class = AddPost
 
    def get_initial(self):
        initial = super(AddPostView, self).get_initial()
        return initial

class IndexView(views.APIView):
    # A very simple class-based view...
    template_name = 'forum/comment/index.html'

    def get_data(self, request, context, *args, **kwargs):
        # Add data to the context here...
        return context


