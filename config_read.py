from pydantic_settings import BaseSettings
from pydantic import SecretStr


class Settings(BaseSettings):
    bot_token: SecretStr
    admin_id: SecretStr

    class Config:
        env_file = ".env"
        env_file_encoding = "UTF-8"


config = Settings()