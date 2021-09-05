import subprocess


def test():
    print("Hello")


def build():
    val = subprocess.check_call("python setup.py sdist", shell=True)
