from fabric.api import task, run, sudo, env, get, hide, prompt
from fabric.context_managers import cd, prefix, settings
from fabric.contrib.files import upload_template, exists
from fabric.utils import abort, puts
from fabric.contrib.console import confirm

import warnings
warnings.filterwarnings(action='ignore',module='.*paramiko.*')

env.hosts = ['52.19.58.78']
#env.port = 2232
env.user = "ubuntu"
env.key_filename = "../cursopy.pem"


@task()
def uname():
    out = run('uname -a')
    puts(out)

@task()
def hostname():
    with hide('running', 'stdout', 'stderr'):
        hostname = run('hostname')
        puts(hostname)

@task()
def id():
    sudo('id')

@task()
def sethostname():
    sudo('hostnamectl set-hostname master.localdomain')




