import json
import os

from fabric import Connection, task

@task
def deploy_prod():
   print("deploy_prod")

@task
def deploy_staging():
   print("deploy_staging")