"""Rewrite the Latest writing block in README.md from the site's RSS feed."""
import re
import urllib.request
import xml.etree.ElementTree as ET

FEED = 'https://zach-wendt.github.io/rss.xml'
START, END = '<!-- writing:start -->', '<!-- writing:end -->'

items = ET.fromstring(urllib.request.urlopen(FEED, timeout=30).read()).findall('./channel/item')[:5]
lines = [f"- [{i.findtext('title')}]({i.findtext('link')})" for i in items] or ['- First post coming soon.']

readme = open('README.md', encoding='utf8').read()
block = f'{START}\n' + '\n'.join(lines) + f'\n{END}'
open('README.md', 'w', encoding='utf8').write(re.sub(f'{START}.*?{END}', block, readme, flags=re.S))
