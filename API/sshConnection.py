import paramiko
from utilities.configuration import *

host = get_config()['Server']['host']
port = get_config()['Server']['port']
username = get_config()['Server']['username']
password = get_config()['Server']['password']
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port, username, password)

