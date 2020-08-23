#!/usr/bin/env python3

# this Python script should send an email if there are problems, such as:
#
# Report an error if available memory is less than 500MB

import shutil
import psutil
import emails
import sys

# Report an error if available disk space is lower than 20%
def check_disk_usage(disk):
    """Verifies that there's enough free space on disk"""
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free > 20

# Report an error if CPU usage is over 80%
def check_cpu_usage():
    """Verifies that there's enough unused CPU"""
    usage = psutil.cpu_percent(1)
    return usage < 80

# Report an error if available memory is less than 500MB
def check_memory_usage():
    """Verifies that there's enough unused memory"""
    mu = psutil.virtual_memory()
    available_memory = mu.available
    # usage = psutil.cpu_percent(1)
    return available_memory < 500*1000000

# Report an error if the hostname "localhost" cannot be resolved to "127.0.0.1"
def check_localhost():
    """Verifies whether the local host is correctly configured"""
    localhost = socket.gethostbyname('localhost')
    return localhost = "127.0.0.1."

def main(argv):
    """Background monitoring system statistics: CPU usage, disk space, available memory and name resolution.
       this Python script should send an email if there are problems"""
    # send the email
    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))
    body = "Please check your system and resolve the issue as soon as possible."

    if not check_disk_usage('/'):
        subject = "Error - Available disk space is less than 20%"
        print(subject)
        message = emails.generate_error_report(sender, receiver, subject, body)
        emails.send(message)
    elif not check_cpu_usage():
        subject = "Error - CPU usage is over 80%"
        print(subject)
        message = emails.generate_error_report(sender, receiver, subject, body)
        emails.send(message)
    elif not check_memory_usage():
        subject = "Error - Available memory is less than 500MB"
        print(subject)
        message = emails.generate_error_report(sender, receiver, subject, body)
        emails.send(message)
    elif not check_localhost():
        subject = "Error - localhost cannot be resolved to 127.0.0.1"
        print(subject)
        message = emails.generate_error_report(sender, receiver, subject, body)
        emails.send(message)

if __name__ == "__main__":
  main(sys.argv)
