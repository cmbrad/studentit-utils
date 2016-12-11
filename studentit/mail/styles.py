TEMPLATE = \
"""
<html>
<head>
{head}
</head>
<body>
{body}
</body>
</html>
"""

HEAD = \
"""
<style>
{styles}
</style>
"""

STYLES = \
"""

"""

BODY = \
"""
"""

HEAD = HEAD.format(styles=STYLES)
TEMPLATE = TEMPLATE.format(head=HEAD, body=BODY)


def with_header(body):
	pass


def _element(tag, content):
	return '<{tag}>{content}</{tag}>'.format(tag=tag, content=content)


def table(content):
	return _element('table', content)


def tr(content):
	return _element('tr', content)


def td(content):
	return _element('td', content)

