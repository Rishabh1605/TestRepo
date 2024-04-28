from fabric.api import *

def pull_code():
    print("pulll_code")

def build():
     print("build")

def restart(service):
    print("restart")

def deploy(sub_dir, service):
     print("deploy")

def deploy_staging():
     print("deploy_staging")

def deploy_prod():
    print("deploy_prod")
