class AuthenticatedUserWrapper:
    def __init__(self, user):
        self.user = user

    @property
    def is_authenticated(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def __getattr__(self, attr):
        return getattr(self.user, attr)
