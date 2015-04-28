from tastypie.authorization import Authorization
from tastypie.exceptions import Unauthorized
from tastypie.resources import ModelResource
from Alexandra.models import Post, User

class UserObjectsAuthorization(Authorization):
    def read_list(self, object_list, bundle):
        return []
#        return object_list
    def read_detail(self, object_list, bundle):
        return False
#        return True
    def create_list(self, object_list, bundle):
        return object_list
    def create_detail(self, object_list, bundle):
        return True
    def update_list(self, object_list, bundle):
        return []
    def update_detail(self, object_list, bundle):
        return False
    def delete_list(self, object_list, bundle):
        raise Unauthorized("Users cannot be deleted")
    def delete_detail(self, object_list, bundle):
        raise Unauthorized("Users cannot be deleted")

class PostObjectsAuthorization(Authorization):
    def read_list(self, object_list, bundle):
        return object_list
    def read_detail(self, object_list, bundle):
        return True
    def create_list(self, object_list, bundle):
        return object_list
    def create_detail(self, object_list, bundle):
        return True
    def update_list(self, object_list, bundle):
        return []
    def update_detail(self, object_list, bundle):
        return False
    def delete_list(self, object_list, bundle):
        return []
    def delete_detail(self, object_list, bundle):
        return False


class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        authorization = UserObjectsAuthorization()
# excludes = ['password']

class PostResource(ModelResource):
    class Meta:
        queryset = Post.objects.all()
        resource_name = 'post'
        authorization = PostObjectsAuthorization()
