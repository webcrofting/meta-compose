# meta-compose

This package aims to solve the problem of variable substitution in
docker-compose files by parsing them as [Jinja2](http://jinja.pocoo.org/)
template.

It was inspired by the discussion [here](https://github.com/docker/compose/issues/1377)

It supports variable declaration in a separate YAML file as well as
access to environment variables.

## Usage:

- Install with `pip install meta-compose`

- Create a file `meta-compose.yml` that is a [Jinja2](http://jinja.pocoo.org/)
  template for a docker compose file.

- [Optional] Create a file `meta-compose-data.yml` that contains the variables
  used in the template that are not environment variables.

- Call `meta-compose` and it will create a docker-compose.yml in the current
  directory

```
usage: meta-compose [-h] [-d DATAFILE]

optional arguments:
  -h, --help            show this help message and exit
  -d DATAFILE, --datafile DATAFILE
                        Use to specify data files in addition to meta-compose-
                        data.yml. They must be JSON or YAML files.
```

## Syntax of meta-compose.yml

- Everything in basic [Jinja2](http://jinja.pocoo.org/) is allowed.

- To access environment variables use `{{'default'| env('VARIABLE_NAME')}}`
  where `VARIABLE_NAME` is the name of your environment variable and `default`
  is the default value you want it to be if the environment variable is not set.
