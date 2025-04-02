# em users/utils.py
def get_real_user(user):
    return user.wrapped_user if hasattr(user, 'wrapped_user') else user
