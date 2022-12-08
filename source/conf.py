#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import pygments

# The parent directory has to be included for 'sphinx-autobuild' to work.
sys.path.insert(0, os.path.abspath("../"))
sys.path.insert(0, os.path.abspath("extensions"))

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'mollie.setup',
    'cloud_sptheme.ext.table_styling',
    'sphinx_reredirects_fork'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = []

# The suffix(es) of source filenames.
source_suffix = '.rst'

# The master toctree document.
master_doc = 'contents'

# General information about the project.
project = 'Mollie API'
copyright = '2021, Mollie B.V. <info@mollie.com>'
author = 'Mollie B.V. <info@mollie.com>'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '1.0'
# The full version, including alpha/beta/rc tags.
release = '1.0'

# Hide .txt extension for source links
html_sourcelink_suffix = ''

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

root_url = os.environ['MOLLIE_DOCS_URL']

html_file_suffix = os.environ['MOLLIE_FILE_SUFFIX']

def to_url(path):
    return root_url + path + html_file_suffix

# -- SEO stuff ------------------------------------------------------------
redirects = {
    'guides/applepay-direct-integration': to_url('/wallets/applepay-direct-integration'),
    'guides/authentication': to_url('/overview/authentication'),
    'guides/checkout': to_url('/payments/hosted-checkout'),
    'guides/common-data-types': to_url('/overview/common-data-types'),
    'guides/gift-cards': to_url('/payments/gift-cards'),
    'guides/handling-errors': to_url('/overview/handling-errors'),
    'guides/mollie-components/handling-errors': to_url('/components/handling-errors'),
    'guides/mollie-components/overview': to_url('/components/overview'),
    'guides/mollie-components/reference': to_url('/reference/mollie-js/overview'),
    'guides/mollie-components/styling': to_url('/components/styling'),
    'guides/mollie-components/testing': to_url('/components/testing'),
    'guides/pagination': to_url('/overview/pagination'),
    'guides/qr-codes': to_url('/payments/qr-codes'),
    'guides/security': to_url('/overview/security'),
    'guides/testing': to_url('/overview/testing'),
    'guides/webhooks': to_url('/overview/webhooks'),
    'oauth/application-fees': to_url('/connect/application-fees'),
    'oauth/getting-started': to_url('/connect/getting-started'),
    'oauth/onboarding': to_url('/connect/onboarding'),
    'oauth/overview': to_url('/connect/overview'),
    'oauth/permissions': to_url('/connect/permissions'),
    'oauth/splitting-payments': to_url('/connect/splitting-payments'),
    'payments/overview': to_url('/payments/accepting-payments'),
    'reference/v1/settlements-api/get-open-settlement': to_url('/reference/v1/settlements-api/get-settlement'),
    'reference/v2/chargebacks-api/get-chargeback': to_url('/reference/v2/chargebacks-api/get-payment-chargeback'),
    'reference/v2/orders-api/create-order-refund': to_url('/reference/v2/refunds-api/create-order-refund'),
    'reference/v2/orders-api/list-order-refunds': to_url('/reference/v2/refunds-api/list-order-refunds'),
    'reference/v2/orders-api/update-orderline': to_url('/reference/v2/orders-api/update-order-line'),
    'reference/v2/organizations-api/me': to_url('/reference/v2/organizations-api/current-organization'),
    'reference/v2/partners-api/get-partner': to_url('/reference/v2/organizations-api/get-partner'),
    'reference/v2/partners-api/get-client': to_url('/reference/v2/clients-api/get-client'),
    'reference/v2/partners-api/list-clients': to_url('/reference/v2/clients-api/list-clients'),
    'reference/v2/profiles-api/enable-giftcard-issuer': to_url('/reference/v2/profiles-api/enable-gift-card-issuer'),
    'reference/v2/refunds-api/cancel-refund': to_url('/reference/v2/refunds-api/cancel-payment-refund'),
    'reference/v2/refunds-api/create-refund': to_url('/reference/v2/refunds-api/create-payment-refund'),
    'reference/v2/refunds-api/get-refund': to_url('/reference/v2/refunds-api/get-payment-refund'),
    'reference/v2/subscriptions-api/list-subscriptions-payments': to_url('/reference/v2/subscriptions-api/list-subscription-payments')
}

# -- Options for HTML output ----------------------------------------------

# Add the pathname of pages you want to prevent from being indexed by search engines here.

# The theme to use for HTML and HTML Help pages. See the documentation for
# a list of builtin themes.
#
html_theme_path = ["./"]
html_theme = 'theme'

html_context = {
    'display_github': True,
    'github_user': 'mollie',
    'github_repo': 'api-documentation',
    'github_version': 'master/source/',
    'do_not_index': [],
}

html_logo = '_static/img/mollie-logo.png'

html_favicon = '_static/img/favicon.ico'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Add custom CSS overrides of the theme.
def setup(app):
    # enable Pygments json lexer
    try:
        if pygments.__version__ >= '1.5':
            # use JSON lexer included in recent versions of Pygments
            from pygments.lexers import JsonLexer
        else:
            # use JSON lexer from pygments-json if installed
            from pygson.json_lexer import JSONLexer as JsonLexer
    except ImportError:
        pass  # not fatal if we have old (or no) Pygments and no pygments-json
    else:
        app.add_lexer('json', JsonLexer())
