build/ij-dict.mobi: ij-dict.opf build/ij-dict0.html characters.html
	./kindlegen-wrapper.sh ij-dict.opf -o ij-dict.mobi;
	mv ij-dict.mobi build/;

build/ij-dict0.html:
	python3 ij-scraper.py > build/ij-dict0.html;
