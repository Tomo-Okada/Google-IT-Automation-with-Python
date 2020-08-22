#!/usr/bin/env python3
import os, datetime, reports
import emails
import sys
from datetime import datetime, date

path = "supplier-data/descriptions/"

def main(argv):
    """Process the JSON data and generate a full report out of it."""
    # creating the PDF report
    attachment = "/tmp/processed.pdf"
    today = date.today()
    title = "Processed Update on <"+ today.strftime("%B %d, %Y")+">"

    contents_list = []
    contents_list = reports.read_contents()
    paragraph = ""
    for content in contents_list:
        paragraph += "<br/>"+content["name"]+"<br/>"+content["weight"]+"<br/>"
    reports.generate_report(attachment, title, paragraph)

    # send the email
    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    message = emails.generate_email(sender, receiver, subject, body, attachment)
    emails.send_email(message)

if __name__ == "__main__":
  main(sys.argv)
