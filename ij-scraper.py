import bs4
import urllib.request
import xml.dom.minidom
import re

from xml.etree.ElementTree import Element, SubElement, tostring

def process_page(url):
	with urllib.request.urlopen(url) as response:
		soup = bs4.BeautifulSoup(response.read(), 'html.parser')
		for d in extract_definitions(soup):
			yield d

def extract_definitions(soup):
	ps = soup.find(id='mw-content-text').find_all('p')

	key = None
	text = None

	for p in ps:
		nkey = extract_key(p)
		if nkey is not None:
			if key is not None:
				yield (key, text)
			key = nkey.strip()
			text = p.text[len(nkey):].strip()
		else:
			if key is None: continue
			text += ' ' + p.text.strip()

	if key is not None:
		yield (key, text)

def extract_key(p):
	prefix = ''
	for c in p.contents:
		if type(c) == bs4.element.NavigableString:
			if re.match(r'[\'"]*', c.strip()):
				prefix += c
				continue
			else:
				return None
		elif c.text == '':
			continue
		elif c.name == 'b' or c.name == 'i':
			return prefix + c.text
		else:
			return None
	return None

pages = [
	'Pages_3-27',
	'Pages_27-63',
	'Pages_63-87',
	'Pages_87-127',
	'Pages_127-156',
	'Pages_157-181',
	'Pages_181-198',
	'Pages_198-219',
	'Pages_219-258',
	'Pages_258-283',
	'Pages_283-306',
	'Pages_306-321',
	'Pages_321-342',
	'Pages_343-379',
	'Pages_380-398',
	'Pages_398-418',
	'Pages_418-442',
	'Pages_442-469',
	'Pages_470-489',
	'Pages_489-508',
	'Pages_508-530',
	'Pages_531-562',
	'Pages_563-588',
	'Pages_589-619',
	'Pages_620-651',
	'Pages_651-662',
	'Pages_663-686',
	'Pages_686-698',
	'Pages_698-716',
	'Pages_716-735',
	'Pages_736-755',
	'Pages_755-785',
	'Pages_785-808',
	'Pages_809-827',
	'Pages_827-845',
	'Pages_845-876',
	'Pages_876-883',
	'Pages_883-902',
	'Pages_902-916',
	'Pages_916-934',
	'Pages_934-964',
	'Pages_964-981',
	'Notes_and_Errata_-_Pages_983-1079']

html = Element('html', {
	'xmlns:idx': 'www.mobipocket.com',
	'xmlns:mbp': 'www.mobipocket.com',
	'xmlns:xlink': 'http://www.w3.org/1999/xlink'
})

body = Element('body')
html.append(body)

for page in pages:
	for d in process_page('http://infinitejest.wallacewiki.com/david-foster-wallace/index.php?title=' + page):
		idx_el = SubElement(body, 'idx:entry', { 'name': 'word', 'scriptable': 'yes' })
		SubElement(idx_el, 'idx:orth', { 'value': d[0] })
		for part in re.split(r'\W+', d[0]):
			if part == '' or part == d[0]: continue
			SubElement(idx_el, 'idx:orth', { 'value': part })
		key_el = SubElement(idx_el, 'h2')
		key_el.text = d[0]
		desc_el = SubElement(idx_el, 'span')
		desc_el.text = d[1]

print(xml.dom.minidom.parseString(tostring(html, 'utf-8')).toprettyxml())
