from pydantic import BaseSettings, Field, HttpUrl


class Settings(BaseSettings):
    env: str = Field("production", env="ENV")
    pubchem_url: HttpUrl = Field("https://pubchem.ncbi.nlm.nih.gov/rest/pug/", env="PUBCHEM_URL")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
