from fabric.api import task, run, sudo, env, get, hide, prompt, local, put, get
from fabric.context_managers import cd
from fabric.contrib.files import upload_template, exists
from fabric.utils import abort, puts
from fabric.contrib.console import confirm
import os
import warnings

warnings.filterwarnings(action='ignore',module='.*paramiko.*')

env.hosts = ['52.19.58.78']
#env.port = 2232
env.user = "ubuntu"
env.key_filename = "cursopy.pem"


@task()
def status():
    out = run('pip3 freeze |grep checkurl')
    puts(out)

@task()
def deps():
    sudo("apt install python3-pip")
    sudo("apt install python3-requests")
    sudo("apt install python3-click")

@task()
def build():
    local("pip wheel -w wheels .")

@task()
def version():
     run("checkurl -v")

@task()
def deploy(version="0.0.1"):
     build()
     put("wheels/checkurl-{}-py3-none-any.whl".format(version))
     sudo("pip3 install checkurl-{}-py3-none-any.whl".format(version))
     version()

# ej: fab config:"http://ono.com","WEB-ono"
@task()
def config(url="https://www.apsl.net/", name="WEB-apsl"):
    # Reconfiguramos check-mk NRPE
    filename = 'crontab'
    fab_dir = os.path.dirname(env.real_fabfile)
    template_path = os.path.join(fab_dir, "..",  'templates')
    puts("Aplicando el nuevo mrpe")
    if not exists("/etc/check-mk"):
        sudo("mkdir -p /etc/check-mk")
    env.check_url = url 
    env.check_name = name 
    upload_template(filename="mrpe.cfg.jinja", destination='/etc/check-mk/mrpe2.cfg', context=env,
                    use_sudo=True, backup=False, use_jinja=True, template_dir=template_path)
    run("cat /etc/check-mk/mrpe2.cfg")