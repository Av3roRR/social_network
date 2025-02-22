# 🌐 EchoHub – Социальная сеть нового поколения 🚀

![EchoHub](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNzExNzMzZjFkNTdkZTY0ZTk5MGM0NjdiNTJhOWU3NzEyM2ZiNjA0NCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/WFZvB7VIXBgiz3oDXE/giphy.gif)

EchoHub – это современная, быстрая и безопасная социальная сеть, разработанная на базе **FastAPI**, **OAuth2** и **SQLAlchemy**.  
Наш сервис позволяет пользователям создавать и публиковать посты, комментировать, ставить лайки, подписываться на интересных людей и управлять своим профилем.

## ⚙️ Технологии

- **Backend**: FastAPI, SQLAlchemy, Alembic
- **Аутентификация**: OAuth2, JWT-токены
- **База данных**: PostgreSQL
- **ORM**: SQLAlchemy + Pydantic
- **Кэширование**: Redis
- **Фоновые задачи**: Celery + Redis
- **Уведомления в реальном времени**: WebSockets  

## 🔥 Функционал

✅ Регистрация и авторизация (OAuth2, JWT)  
✅ Управление профилем (аватар, описание, настройки)  
✅ Создание, редактирование и удаление постов  
✅ Лайки и комментарии к постам  
✅ Система подписок и подписчиков  
✅ WebSockets – уведомления в реальном времени  
✅ Асинхронные фоновые задачи (например, отправка email-уведомлений через **Celery**)  

## 🚀 Установка и запуск

```sh
git clone https://github.com/Av3roRR/social_network.git
uv sync 
uvicorn app.main:app --reload
celery -A app.tasks worker --loglevel=info
```

## 🎯 Контакты и участие
Если у вас есть идеи или вопросы, создавайте **issues** или **pull requests**!

💡 _С уважением, команда EchoHub_ 🎉


