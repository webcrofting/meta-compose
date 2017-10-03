import glob
import sys
import os
import yaml
from jinja2 import Environment, FileSystemLoader, StrictUndefined
import argparse
from pprint import pprint

def env_override(value, key):
  print "%s: %s" % ("debug",os.getenv(key, value))
  #pprint (vars(env_override()))    
  return os.getenv(key, value)


def fileglob(pathname):
    print "%s: %s" % ("debug",glob.glob(pathname))
    #pprint (vars(env_override))    
    return glob.glob(pathname)


def parse_args():

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

    return parser.parse_args()

def setup_jinja(template_file_name):

    jinja = Environment(loader=FileSystemLoader("."), undefined=StrictUndefined)
    jinja.filters['env'] = env_override
    jinja.filters['fileglob'] = fileglob
    
    return jinja.get_template(template_file_name)

def collect_data(data_file_names):

    data = {}
    for data_file_name in data_file_names:
        if os.path.isfile(data_file_name):
            with open(data_file_name, "r") as fh:
                data.update(yaml.safe_load(fh))
    return data

def write_compose_file(composition, outputfile):
    print "..."
    with open(outputfile, "w") as fh:
        fh.write(composition)
    print "compose file generated"



def main():

    args = parse_args()
    print "args: "
    print args


    template = setup_jinja(args.template)
    data = collect_data(["meta-compose-data.yml"] + args.datafile)
    print "data: "
    print data

    write_compose_file(template.render(data), args.outputfile)
