from fabric.api import task, run, sudo, env, get, hide, prompt, put, get
from fabric.context_managers import cd
from fabric.contrib.files import upload_template, exists
from fabric.utils import abort, puts
from fabric.contrib.console import confirm

import warnings
warnings.filterwarnings(action='ignore',module='.*paramiko.*')

env.hosts = ['curso0']
#env.port = 2232
env.user = "ubuntu"
env.key_filename = "../../cursopy.pem"


@task()
def uname():
    out = run('uname -a')
    puts(out)

# podemos silenciar salida
@task()
def hostname():
    with hide('running', 'stdout', 'stderr'):
        hostname = run('hostname')
        puts(hostname)

# ejecutamos como sudo
@task()
def id():
    sudo('id')

# Cambiamos hostname al nodo, con parametro
# ej: fab sethostname:curso3
@task()
def sethostname(name="curso1"):
    sudo("echo 127.0.1.0 {}.localdomain >> /etc/hosts".format(name))
    sudo('hostnamectl set-hostname {}.localdomain'.format(name))


# cd contextmanager
@task()
def lstmp():
    with cd("/tmp"):
        run("ls -l")
