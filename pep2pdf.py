# pep2pdf.py - script for downloading the latest PEPs and converting it to PDF
#
# Copyright 2015 Andriy Korchak <AndriyKorchak at gmail dot com>
#
# This software may be used and distributed according to the terms of the
# GNU General Public License version 2 or any later version.

"""
pep2pdf.py - module for downloading the latest PEPs and converting it to PDF

Usage:
    python pep2pdf.py PEP_number [pdf_filename]

Contains:
    pep2pdf(PEP_number, pdf_file="") - main function. Downloads the PEP with
        number PEP_number and converts it to PDF file named pdf_file
"""

import sys
import urllib2

def pep2pdf(PEP_number, pdf_filename=""):
    """
    Downloads the PEP with given number from the official PEPs Mercurial
    repository and converts it to PDF

    :param PEP_number: (str, int) - number of PEP. For instance: "8", 257
    :param pdf_filename: (str) - full name of generated file. If not specified,
        will be formed like "PEP-0257.pdf".
    :return: None
    """

    source_file = _get_source_file(PEP_number)

def _get_source_file(PEP_number):
    filename = _get_source_filename(PEP_number)
    head = _get_head()
    print head

def _get_source_filename(PEP_number):
    PEP_num_str = str(PEP_number) # Can be int
    PEP_num_str = "0000" + PEP_num_str
    PEP_num_str = "pep-" + PEP_num_str[-4:] + ".txt"
    return PEP_num_str

def _get_head():
    # See https://mercurial.selenic.com/wiki/HttpCommandProtocol
    url = "https://hg.python.org/peps/?cmd=heads"
    try:
        response = urllib2.urlopen(url)
        data = response.read()
    except:
        return None
    heads = data.split(" ")
    if len(heads) > 0:
        return heads[0]
    else:
        return None

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "Not enough arguments"
        print __doc__
    else:
        PEP_number = sys.argv[1]
        pdf_filename = ""
        if len(sys.argv) > 2:
            pdf_filename = sys.argv[2]
        pep2pdf(PEP_number, pdf_filename)