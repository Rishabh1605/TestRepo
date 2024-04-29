import json
import os

from fabric import Connection, task

@task
def run_docker(ctx):
   print("deploy_prod")
