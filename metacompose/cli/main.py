import sys
import os
import yaml
from jinja2 import Environment, FileSystemLoader, StrictUndefined

def env_override(value, key):
  return os.getenv(key, value)

def main():

    template_file_name = "meta-compose.yml"
    data_file_name = "meta-compose-data.yml"

    jinja = Environment(loader=FileSystemLoader("."), undefined=StrictUndefined)

    jinja.filters['env'] = env_override

    template = jinja.get_template(template_file_name)


    if os.path.isfile(data_file_name):
        with open(data_file_name, "r") as fh:
            data = yaml.safe_load(fh)
    else:
        data = {}

    composition = template.render(data)

    with open("docker-compose.yml", "w") as fh:
        fh.write(composition)
