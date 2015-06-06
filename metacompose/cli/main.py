import sys
import os
import yaml
from jinja2 import Environment, FileSystemLoader

def env_override(value, key):
  return os.getenv(key, value)

def main():
    jinja = Environment(loader=FileSystemLoader("."))
    jinja.filters['env'] = env_override

    template = jinja.get_template("meta-compose.yml")

    with open("meta-compose-data.yml", "r") as fh:
        data = yaml.safe_load(fh)

    composition = template.render(data)

    with open("docker-compose.yml", "w") as fh:
        fh.write(composition)
