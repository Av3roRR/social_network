from sqladmin import ModelView
from app.models import User, Post, Like, Follow, Comment



class UserAdmin(ModelView, model=User):
    #column_list = "__all__"
    can_delete = False
    name = "Пользователь"
    name_plural = "Пользователи"
    icon = "fa-solid fa-user"
    column_details_exclude_list = [User.hashed_password]
    column_exclude_list = [User.hashed_password]

class PostAdmin(ModelView, model=Post):
    column_list = "__all__"
    can_delete = False
    name = "Пост"
    name_plural = "Посты"
    icon = "fa-solid fa-user"
    #column_exclude_list = []

class LikeAdmin(ModelView, model=Like):
    column_list = "__all__"
    can_delete = False
    name = "Лайк"
    name_plural = "Лайки"
    icon = "fa-solid fa-user"
    #column_exclude_list = []

class FollowAdmin(ModelView, model=Follow):
    column_list = "__all__"
    can_delete = False
    name = "Подписка"
    name_plural = "Подписки"
    icon = "fa-solid fa-user"
    #column_exclude_list = []

class CommentAdmin(ModelView, model=Comment):
    column_list = "__all__"
    can_delete = False
    name = "Комментарий"
    name_plural = "Комментарии"
    icon = "fa-solid fa-user"
    #column_exclude_list = []
