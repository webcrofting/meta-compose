import sys
import os
import yaml
from jinja2 import Environment, FileSystemLoader, StrictUndefined
import argparse

def env_override(value, key):
  return os.getenv(key, value)

def main():

    parser = argparse.ArgumentParser()

    template_file_name = "meta-compose.yml"
    data_file_names = ["meta-compose-data.yml"]

    parser.add_argument(
      "-d", "--datafile", action='append',
      help="Use to specify data files in addition to meta-compose-data.yml."
           " They must be JSON or YAML files.")

    args = parser.parse_args()

    data_file_names += args.datafile

    jinja = Environment(loader=FileSystemLoader("."), undefined=StrictUndefined)
    jinja.filters['env'] = env_override
    template = jinja.get_template(template_file_name)

    data = {}
    for data_file_name in data_file_names:
        if os.path.isfile(data_file_name):
            with open(data_file_name, "r") as fh:
                data.update(yaml.safe_load(fh))


    composition = template.render(data)

    with open("docker-compose.yml", "w") as fh:
        fh.write(composition)
