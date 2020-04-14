import click

def info():
  return {
    "name":"ip manager",
    "author":"Mac New", #author of this module
    "email":"newmac1000@gmal.com", #email to notify about the status of module
    "dependencies":["click", "requests"], #dependencies this module depends upon
    "alias":"ipmanager", #alias which detects this module
    "description":"This is simple Ip address manager", #description
    "version":1
  }

@click.group()
def run():
  """This is simple Ip address manager"""
  pass

@run.command()
def m():
  pass