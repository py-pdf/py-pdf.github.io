import logging

logging.root.setLevel(logging.INFO)
logging.getLogger('pelican.utils').setLevel(logging.WARN)  # avoids verbose "-> Copying ..." logs
logging.getLogger('tornado.access').setLevel(logging.WARN)  # avoids verbose HTTP logs from livereload server
# Configure LOG_FORMAT to prefix it with "%(asctime)s [%(module)s]":
if logging.root.handlers:  # handlers are only set the 2nd time this file is evaluated by Pelican
    formatter = logging.root.handlers[0].formatter
    formatter._fmt = formatter._style._fmt = "%(asctime)s [%(name)s] %(levelname)s %(message)s"

AUTHOR = "The py-pdf owners"
SITENAME = "The py-pdf organization"

TIMEZONE = "Europe/Berlin"
DEFAULT_LANG = "en"

PATH = './content'
OUTPUT_PATH = './output'

# Blogroll
LINKS = (
    ("Github", "https://github.com/py-pdf"),
    # Order the following by Github stars:
    # Either link to GitHub or to PyPI
    ("pypdf and PyPDF2", "https://github.com/py-pdf/pypdf"),
    ("fpdf2", "https://github.com/py-pdf/fpdf2"),
    ("PyPDF-Builder", "https://github.com/py-pdf/PyPDF-Builder"),
    ("pdfly", "https://github.com/py-pdf/pdfly"),
)

# Social widget
SOCIAL = (  # ('You can add links in your config file', '#'),
    ("py_pdf", "https://twitter.com/py_pdf"),
)

DEFAULT_PAGINATION = 10


#######################################
# Config options specific to dev-mode:
#######################################

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
