#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from datetime import date

def generate(filename, title, additional_info):
  styles = getSampleStyleSheet()
  report = SimpleDocTemplate(filename)
  report_title = Paragraph(title, styles["h1"])
  report_info = Paragraph(additional_info, styles["BodyText"])
  empty_line = Spacer(1,20)

  report.build([report_title, empty_line, report_info])

def read_contents():
    path = "/supplier-data/descriptions/"
    keys = ["name", "weight", "description"]
    folder = os.listdir(path)
    for file in folder:
        keycount = 0
        fb = {}
        with open(path + file) as fl:
            for line in fl:
                value = line.strip()
                fb[keys[keycount]] = value
                keycount += 1
    contents_list.append(fb)
return contents_list

contents_list = []
contents_list = read_contents()
contents = ""
for content in contents_list:
    contents += "<br/>"+content["name"]+"<br/>"+content["weight"]+"<br/>"
title = "Processed Update on <"+today.strftime("%B %d, %Y")+">"
generate("/tmp/processed.pdf", title, contents)
