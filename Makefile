build/ij-dict.mobi: ij-dict.opf ij-dict0.html characters.html
	mkdir -p build;
	./kindlegen-wrapper.sh ij-dict.opf -o ij-dict.mobi;
	mv ij-dict.mobi build/;
