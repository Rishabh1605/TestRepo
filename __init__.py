import json
import os

from fabric import Connection, task

@task
def deploy_prod(ctx):
   print("deploy_prod")

@task
def deploy_staging(ctx):
   print("deploy_staging")