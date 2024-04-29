import json
import os

from fabric import Connection, task

def read_config():
    path = os.environ['SERVERS_CONFIG']
    f = open(path, 'r')
    obj = json.loads(f.read())
    return obj

@task
def run_docker(ctx):
   config = read_config()
   hosts = config["host_names"]
   for host in hosts:
    c = Connection(host, connect_timeout=60)
