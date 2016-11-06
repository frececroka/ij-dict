import bs4
import urllib.request

def process_page(url):
	with urllib.request.urlopen(url) as response:
		soup = bs4.BeautifulSoup(response.read(), 'html.parser')
		for d in extract_definitions(soup):
			yield d

def extract_definitions(soup):
	ps = soup.find(id='mw-content-text').find_all('p')
	for p in ps:
		if len(p.contents) < 2: continue
		if p.contents[0].name != 'b': continue
		key = extract_text(p.contents[0])
		description = ' '.join(map(extract_text, p.contents[1:])).strip()
		yield (key, description)

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

for url in urls:
	for d in process_page('http://infinitejest.wallacewiki.com' + url):
		print(d[0] + '\t' + d[1])
