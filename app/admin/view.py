from sqladmin import ModelView
from app.models import User



class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.username, User.email, User.created_at, User.is_active]
    can_delete = False
    name = "Пользователь"
    name_plural = "Пользователи"
    icon = "fa-solid fa-user"
    column_details_exclude_list = [User.hashed_password,User.posts, User.likes, User.comments, User.followers, User.following]
