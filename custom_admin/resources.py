from import_export import resources

from custom_admin.models import Comment


class CommentResource(resources.ModelResource):
    class Meta:
        model = Comment
