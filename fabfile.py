import sys
import os
import json

from fabric import task

@task
def pull_code(c):
    print("pulll_code")

@task
def build(c):
    print("build")

@task
def restart(c, service):
    print("restart")

@task
def deploy(c, sub_dir, service):
    print("deploy")

@task
def deploy_staging(c):
    print("deploy_staging")

@task
def deploy_prod(c):
    print("deploy_prod")