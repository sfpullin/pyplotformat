'''
Utilities to integrate inkscape modifications into the loop of figure design.
'''

from .write import write_pdf

from pathlib import Path
from pypdf import PdfMerger
import subprocess
from datetime import datetime

def inkscape(figures):

    tmpname = _write_figure_package(figures)

    try:
        subprocess.run(["inkscape", tmpname])
    except Exception as e:
        Path(tmpname).unlink()
        raise

    Path(tmpname).unlink()


def _write_figure_package(figures):

    try:
        iter(figures)
    except:
        figures = [figures]

    tmpname = "." + datetime.now().strftime("%Y%m%d%H%M%S") + "_tmp"

    pdfs = []

    for ii, fig in enumerate(figures):

        fname = tmpname + "_{}.pdf".format(ii)
        pdfs.append(fname)
        write_pdf(fig, fname)

    merger = PdfMerger()

    for pdf in pdfs:
        merger.append(pdf)
        Path(pdf).unlink()

    merger.write(Path(tmpname).with_suffix(".pdf"))
    merger.close()

    return str(Path(tmpname).with_suffix(".pdf"))





