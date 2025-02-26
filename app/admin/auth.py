from sqladmin import Admin
from sqladmin.authentication import AuthenticationBackend
from starlette.requests import Request
from starlette.responses import RedirectResponse

from app.users.auth import auth_user, create_access_token
from app.users.dependencies import  get_current_user
from app.config import settings

class AdminAuth(AuthenticationBackend):
    async def login(self, request: Request) -> bool:
        form = await request.form()
        email, password = form["username"], form["password"]
        user = await auth_user(email, password)
        if user:
            cookie = create_access_token({"sub": str(user.id)})
        request.session.update({"token": cookie})

        return True

    async def logout(self, request: Request) -> bool:
        # Usually you'd want to just clear the session
        request.session.clear()
        return True

    async def authenticate(self, request: Request) -> bool:
        token = request.session.get("token")


        if not token:
            return False

        if token:
            user = get_current_user(token)
        else:
            return False
        return True


authentication_backend = AdminAuth(secret_key=settings.SECRET_KEY)
#admin = Admin(app=..., authentication_backend=authentication_backend، ...)
