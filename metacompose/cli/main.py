import sys
import os
import yaml
from jinja2 import Environment, FileSystemLoader, StrictUndefined
import argparse

def env_override(value, key):
  return os.getenv(key, value)

def main():

    parser = argparse.ArgumentParser()

    parser.add_argument(
      "-d", "--datafile", action='append',
      default=[],
      help="Use to specify data files in addition to meta-compose-data.yml. "
           "They must be JSON or YAML files.")

    parser.add_argument(
      "-t", "--template",
      default="./meta-compose.yml",
      help="Use to specify the template file to use. "
           "Defaults to ./meta-compose.yml")

    parser.add_argument(
      "-o", "--outputfile",
      default="./docker-compose.yml",
      help="Use to specify the output file to create. "
           "Defaults to ./docker-compose.yml")

    args = parser.parse_args()


    template_file_name = args.template
    output_file_name = args.outputfile
    data_file_names = ["meta-compose-data.yml"] + args.datafile



    jinja = Environment(loader=FileSystemLoader("."), undefined=StrictUndefined)
    jinja.filters['env'] = env_override
    template = jinja.get_template(template_file_name)

    data = {}
    for data_file_name in data_file_names:
        if os.path.isfile(data_file_name):
            with open(data_file_name, "r") as fh:
                data.update(yaml.safe_load(fh))


    composition = template.render(data)

    with open(output_file_name, "w") as fh:
        fh.write(composition)
