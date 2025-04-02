from django.utils.deprecation import MiddlewareMixin
from users.models import CustomUser
from users.wrappers import AuthenticatedUserWrapper

class AnonymousUser:
    @property
    def is_authenticated(self):
        return False

    @property
    def is_anonymous(self):
        return True

class CustomAuthMiddleware(MiddlewareMixin):
    def __call__(self, request):
        user_id = request.session.get("user_id")
        if user_id:
            try:
                user = CustomUser.objects.get(id=user_id)
                request.user = AuthenticatedUserWrapper(user)
            except CustomUser.DoesNotExist:
                request.user = AnonymousUser()
        else:
            request.user = AnonymousUser()

        return self.get_response(request)
