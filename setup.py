from distutils.core import setup
import py2exe

setup(
    windows=[{"script":"main.py",
	      "icon_resources": [(1, "ico.ico")]}],
    options={"py2exe": {"dll_excludes": ["MSVCP90.dll"],"includes":["PyQt4","sip","sys", "PyQt4.QtSvg","PyQt4.QtCore","PyQt4.QtGui",
                        "PyQt4.QtNetwork","PyQt4.QtWebKit","shutil", "xlrd", "xlwt", "logging", "wstools","defusedxml", "_xmlplus.sax.drivers2.*", "os"]}},
    zipfile=None

)