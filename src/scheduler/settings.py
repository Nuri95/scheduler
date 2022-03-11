from pydantic import BaseSettings


class Settings(BaseSettings):
    server_host: str = '127.0.0.1'
    server_port: int = 8000
    database_url: str = 'sqlite:///./sql_app.db'

    jwt_secret: str = 'Sqmn683cM5-sGzB3ORMkoBSDsJgw1pWIUl0SbtlVjqw'
    jwt_algorithm: str = 'HS256'
    jwt_expiration: int = 3600


settings = Settings(
    _env_file='.env',
    _env_file_encoding='utf-8',
)
