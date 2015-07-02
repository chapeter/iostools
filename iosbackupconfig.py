#!/usr/bin/env python

__author__ = 'Chad Peterson'
__email__ = 'chapeter@cisco.com'

import pexpect
import sys
import argparse
import time

##Get arguments##
parser = argparse.ArgumentParser(description="Backup Config")
parser.add_argument('-ip', '--ipaddress', help='IP Address', required=True)
parser.add_argument('-l', '--user', help='username', required=True)
parser.add_argument('-p', '--password', help='password', required=True)
parser.add_argument('-ftpip', '--ftpip', help='ftp server ip', required=True)
parser.add_argument('-ftpuser', '--ftpuser', help='ftp server user', required=True)
parser.add_argument('-ftppass', '--ftppass', help='ftp server password', required=True)
parser.add_argument('-ftpdir', '--ftpdir', help='ftp server directory', required=True)

args = parser.parse_args()

session = pexpect.spawn('telnet ' + args.ipaddress)
session.logfile_read = sys.stdout

session.expect('Password: ')
session.sendline(args.password)

session.expect('.*>')
session.sendline('enable')

session.expect('Password: ')
session.sendline(args.password)

session.expect('.*#')
#session.sendline('copy run ftp://%s:%s@%s/%s%s%s' % (args.ftpuser, args.ftppass, args.ftpip, args.ftpdir, args.ipaddress, time.strftime("%Y-%m-%d %H:%M")))
session.sendline('copy run ftp://' + args.ftpuser + ":" + args.ftppass + "@" + args.ftpip + "/" + args.ftpdir + args.ipaddress + "-" + time.strftime("%Y-%m-%d-%H:%M") + ".txt")

session.expect('.*?')
session.sendline('\n')
session.expect('.*?')
session.sendline('\n')
session.expect('.*#')
