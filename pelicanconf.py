#!/usr/bin/env python
# -*- coding: utf-8 -*- #
PATH = 'content'

AUTHOR = 'Radu Grosu'
SITENAME = 'Tame AI, Slow ML'
SITEURL = 'http://localhost:8000'
SITETITLE = AUTHOR
SITESUBTITLE = ''
SITELOGO = '/images/rg1.jpg'
FAVICON = '/images/favicon.ico'

THEME = "../pelican-themes/Flex"
ROBOTS = 'index, follow'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
# HOME_HIDE_TAGS = True

MAIN_MENU = True
STATIC_PATHS = ['images', 'extras']
DISQUS_SITENAME = 'radugrosu-com'
# Blogroll
uri = 'https://radugrosu.github.io'
# LINKS = (
#          ('blog', f'{uri}/'),
#         )

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/orgrosu'),
          ('github', 'https://github.com/radugrosu/'),
          ('linkedin', 'https://www.linkedin.com/in/radu-grosu-26b86214a/'),
         )

# MENUITEMS = (('Archives', '/archives.html'),
#              ('Categories', '/categories.html'),
#              ('Tags', '/tags.html'),
# )

MENUITEMS = [('Blog', '%s' % uri),
             ('Archives', '%s/archives.html' % uri),
]
DEFAULT_PAGINATION = 6

STATIC_PATHS = ['images', 'extra']

# JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

MARKUP = ('md', 'ipynb')
PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup', 'render_math']
TWITTER_FOLLOW_BUTTON = True
CC_LICENSE = {
    'name': 'Creative Commons Attribution-ShareAlike',
    'version': '4.0',
    'slug': 'by-sa'
}
