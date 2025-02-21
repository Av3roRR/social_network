from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str
    DB_DRIVER: str
    DATABASE_URL: str
    SECRET_KEY: str
    HASH_ALGO: str
    BROKER: str
    BACKEND: str
    SMTP_SERVER: str
    SMTP_PORT: str
    SMTP_USERNAME: str
    SMTP_PASSWORD: str
    EMAIL_FROM: str
    # Используем model_config для загрузки переменных из .env
    model_config = SettingsConfigDict(env_file=".env")



settings = Settings()