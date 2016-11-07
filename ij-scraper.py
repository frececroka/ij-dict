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
		cnt = [t for t in p.contents if t.name != 'br' and (type(t) != bs4.element.NavigableString or t.strip() != '')]
		if not cnt: continue
		if cnt[0].name == 'b':
			if key is not None: yield (key, text)
			key = extract_text(cnt[0])
			text = extract_text_arr(cnt[1:])
		else:
			if key is None: continue
			text += ' ' + extract_text_arr(cnt)

	if key is not None:
		yield (key, text)

def extract_text_arr(tags):
	return ''.join(map(extract_text, tags)).strip()

def extract_text(tag):
	if 'text' in dir(tag):
		return tag.text.strip()
	else:
		return tag.string.strip()

urls = [
	'/david-foster-wallace/index.php?title=Pages_3-27',
	'/david-foster-wallace/index.php?title=Pages_27-63',
	'/david-foster-wallace/index.php?title=Pages_63-87',
	'/david-foster-wallace/index.php?title=Pages_87-127',
	'/david-foster-wallace/index.php?title=Pages_127-156',
	'/david-foster-wallace/index.php?title=Pages_157-181',
	'/david-foster-wallace/index.php?title=Pages_181-198',
	'/david-foster-wallace/index.php?title=Pages_198-219',
	'/david-foster-wallace/index.php?title=Pages_219-258',
	'/david-foster-wallace/index.php?title=Pages_258-283',
	'/david-foster-wallace/index.php?title=Pages_283-306',
	'/david-foster-wallace/index.php?title=Pages_306-321',
	'/david-foster-wallace/index.php?title=Pages_321-342',
	'/david-foster-wallace/index.php?title=Pages_343-379',
	'/david-foster-wallace/index.php?title=Pages_380-398',
	'/david-foster-wallace/index.php?title=Pages_398-418',
	'/david-foster-wallace/index.php?title=Pages_418-442',
	'/david-foster-wallace/index.php?title=Pages_442-469',
	'/david-foster-wallace/index.php?title=Pages_470-489',
	'/david-foster-wallace/index.php?title=Pages_489-508',
	'/david-foster-wallace/index.php?title=Pages_508-530',
	'/david-foster-wallace/index.php?title=Pages_531-562',
	'/david-foster-wallace/index.php?title=Pages_563-588',
	'/david-foster-wallace/index.php?title=Pages_589-619',
	'/david-foster-wallace/index.php?title=Pages_620-651',
	'/david-foster-wallace/index.php?title=Pages_651-662',
	'/david-foster-wallace/index.php?title=Pages_663-686',
	'/david-foster-wallace/index.php?title=Pages_686-698',
	'/david-foster-wallace/index.php?title=Pages_698-716',
	'/david-foster-wallace/index.php?title=Pages_716-735',
	'/david-foster-wallace/index.php?title=Pages_736-755',
	'/david-foster-wallace/index.php?title=Pages_755-785',
	'/david-foster-wallace/index.php?title=Pages_785-808',
	'/david-foster-wallace/index.php?title=Pages_809-827',
	'/david-foster-wallace/index.php?title=Pages_827-845',
	'/david-foster-wallace/index.php?title=Pages_845-876',
	'/david-foster-wallace/index.php?title=Pages_876-883',
	'/david-foster-wallace/index.php?title=Pages_883-902',
	'/david-foster-wallace/index.php?title=Pages_902-916',
	'/david-foster-wallace/index.php?title=Pages_916-934',
	'/david-foster-wallace/index.php?title=Pages_934-964',
	'/david-foster-wallace/index.php?title=Pages_964-981',
	'/david-foster-wallace/index.php?title=Notes_and_Errata_-_Pages_983-1079']

html = Element('html', {
	'xmlns:idx': 'www.mobipocket.com',
	'xmlns:mbp': 'www.mobipocket.com',
	'xmlns:xlink': 'http://www.w3.org/1999/xlink'
})

body = Element('body')
html.append(body)

for url in urls:
	for d in process_page('http://infinitejest.wallacewiki.com' + url):
		idx_el = SubElement(body, 'idx:entry', { 'name': 'word', 'scriptable': 'yes' })
		orth_el = SubElement(idx_el, 'idx:orth', { 'value': d[0] })
		key_el = SubElement(idx_el, 'h2')
		key_el.text = d[0]
		desc_el = SubElement(idx_el, 'span')
		desc_el.text = d[1]
		infl_el = SubElement(orth_el, 'idx:infl')
		for infl in re.split(r'\W+', d[0]):
			if infl == '': continue
			SubElement(infl_el, 'idx:iform', { 'value': infl })

print(xml.dom.minidom.parseString(tostring(html, 'utf-8')).toprettyxml())
