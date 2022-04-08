#!/usr/bin/python3
# Fabfile to delete out-of-date archives
import os

from fabric.api import *

env.hosts = ["3.235.21.36", "3.83.35.54"]


def do_clean(number=0):
    """
    Delete all archives older than number days
    """

    if (int(number) == 0) :
        number = 1
    else: int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]
