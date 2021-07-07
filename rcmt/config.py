import os.path
import tempfile
from typing import Optional

import pydantic
import yaml
from pydantic.fields import Field


class Run(pydantic.BaseModel):
    name: str
    packages: list[str] = []
    match: str


class Git(pydantic.BaseModel):
    branch_name: str = "rcmt"
    data_dir: str = os.path.join(tempfile.gettempdir(), "rcmt", "data")


class Github(pydantic.BaseModel):
    access_token: str = os.getenv("GITHUB_ACCESS_TOKEN")


class Json(pydantic.BaseModel):
    indent: int = 2
    extensions: list[str] = [".json"]


class Toml(pydantic.BaseModel):
    extensions: list[str] = [".toml"]


class Yaml(pydantic.BaseModel):
    explicit_start: Optional[bool] = False
    extensions: list[str] = [".yaml", ".yml"]


class Config(pydantic.BaseModel):
    auto_merge: bool = False
    dry_run: bool = False
    git: Git
    github: Github
    # Add _ because json is a reserved field of pydantic
    json_: Json = Field(alias="json", default=Json())
    log_level: str
    packages_path: str
    run_path: str
    toml: Toml = Toml()
    yaml: Yaml = Yaml()


def read_config_from_file(path: str) -> Config:
    data = {}
    if path != "":
        with open(path, "r") as f:
            data = yaml.load(f, Loader=yaml.FullLoader)

    return Config(**data)
