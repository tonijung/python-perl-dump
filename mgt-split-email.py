#!/usr/bin/env python

'''
Author: Toni Jung
Date: March 12, 2015 - 10:44am
Goal: email out to each individual students a PDF grade report.. should be doing this in R but I'm lazy and Python is awesome.

'''

from PyPDF2 import PdfFileWriter, PdfFileReader
import os, sys
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage

# [1] split pdf from RNW
inputpdf = PdfFileReader(open("grades-main.pdf", "rb"))

for i in xrange(inputpdf.numPages):
    output = PdfFileWriter()
    output.addPage(inputpdf.getPage(i))
    with open("grade-%s.pdf" % i, "wb") as outputStream:
        output.write(outputStream)
        
# [2] rename files
students = ["ROSTER HERE"] #import from CSV
numstudent = range(1,37)
for student, i in zip(students, numstudent):
        os.rename("grade-%s.pdf" % i, "%s.pdf" % student)

# [3] send out emails
stuemails = ["LIST HERE"]
msg = MIMEMultipart()
#msg.attach(MIMEText(file("/home/myuser/sample.pdf").read())
msg.attach(MIMEText(file("C:/test/Choice.pdf").read())

mailer = smtplib.SMTP()
mailer.connect()
mailer.sendmail(from_, to, msg.as_string())
mailer.close()
