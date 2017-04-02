# coding=utf-8

import ftplib
import sys

def get_text(ftp, filename, outfile=None):
    # fetch a text file
    if outfile is None:
        outfile = sys.stdout
    # use a lambda to add newlines to the lines read from the server
    ftp.retrlines("RETR" + filename, lambda s, w=outfile.write: w(s+"\n"))

