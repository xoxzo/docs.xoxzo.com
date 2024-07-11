import os
import subprocess
import functools

run = functools.partial(subprocess.call, shell=True)

run('pip install virtualenv')

run('virtualenv -p python3 .env')

run('.env/bin/pip install setuptools==51.3.3')

run('.env/bin/pip install --force-reinstall -v "pip==24.0"')

run('.env/bin/pip install zc.buildout')

run('.env/bin/pip install wheel')

if not os.path.exists('buildout.cfg'):
    TPL = """
[buildout]
extends = buildout/development.cfg
"""

    f = open('buildout.cfg', 'w')
    f.write(TPL)

run('.env/bin/buildout bootstrap')
