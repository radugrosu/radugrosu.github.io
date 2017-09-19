#!/usr/bin/env python
# -*- coding: utf-8 -*- #
PATH = 'content'

AUTHOR = 'Radu Grosu'
SITENAME = 'First Day of Autumn'
SITEURL = 'http://localhost:8000'
SITETITLE = AUTHOR
SITESUBTITLE = ''
SITELOGO = SITEURL + '/images/rg1.jpg'
FAVICON = SITEURL + '/images/favicon.ico'

THEME = "/home/radu/blog/pelican-themes/Flex"
ROBOTS = 'index, follow'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

HOME_HIDE_TAGS = True

# Blogroll
LINKS = (
         ('home', 'http://radugrosu.com'),
        )

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/orgrosu'),
          ('github', 'https://github.com/radugrosu/'),
          ('linkedin', 'https://www.linkedin.com/in/radu-grosu-26b86214a/'),
         )

DEFAULT_PAGINATION = 6

STATIC_PATHS = ['images', 'extra']

JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
MARKUP = ('md', 'ipynb')
PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup', 'render_math']

CC_LICENSE = {
    'name': 'Creative Commons Attribution-ShareAlike',
    'version': '4.0',
    'slug': 'by-sa'
}
