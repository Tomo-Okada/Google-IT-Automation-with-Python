#!/usr/bin/env python3
import os, datetime, reports
path = "/supplier-data/descriptions/"


if __name__ == "__main__":
    attachement = "/tmp/processed.pdf"
    title = "Processed Update on <"+today.strftime("%B %d, %Y")+">"

    contents_list = []
    contents_list = reports.read_contents()
    paragraph = ""
    for content in contents_list:
    paragraph = "<br/>"+content["name"]+"<br/>"+content["weight"]+"<br/>"

    reports.generate_report(attachment, title, paragraph)
