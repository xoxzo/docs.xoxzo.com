import os
import sys
import subprocess
import functools

run = functools.partial(subprocess.call, shell=True)

run('python3.6 -mvenv .env')

run('.env/bin/pip install setuptools==51.3.3')

run('.env/bin/pip install --upgrade pip')

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
