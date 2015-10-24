from django.utils.translation import ugettext_lazy as _
 
from horizon import tables
 
from openstack_dashboard.dashboards.forum.post import utils
 
class AddTableData(tables.LinkAction):
    name = "add"
    verbose_name = _("Add Post")
    url = "horizon:forum:post:add"
    classes = ("btn-launch", "ajax-modal")
 
class DeleteTableData(tables.DeleteAction):
    data_type_singular = _("Post")
    data_type_plural = _("Posts")
 
    def delete(self, request, obj_id):
        utils.deletePost(self, obj_id)
 
class FilterAction(tables.FilterAction):
    def filter(self, table, providers, filter_string):
        filterString = filter_string.lower()
        return [provider for provider in providers
                if filterString in provider.title.lower()]
 
class UpdateRow(tables.Row):
    ajax = True
 
    def get_data(self, request, post_id):
        pass
 
class PostTable(tables.DataTable):
    id = tables.Column("id",
                          verbose_name=_("Id"))
 
    title = tables.Column("title",
			 link="horizon:forum:post:view",
                          verbose_name=_("Title"))

    content = tables.Column("content",
                          verbose_name=_("Content"))

    owner = tables.Column("owner",
                          verbose_name=_("Owner"))

    created_at = tables.Column("created_at",
                          verbose_name=_("Create at"))

 
    class Meta:
        name = "forum"
        verbose_name = _("Posts")
        row_class = UpdateRow
        table_actions = (AddTableData,
                         FilterAction)
        row_actions = (DeleteTableData,)
