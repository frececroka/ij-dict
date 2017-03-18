#!/usr/bin/env bash

KINDLEGEN_DIR=".kindlegen"

if [ ! -d $KINDLEGEN_DIR ]; then
	curl 'http://kindlegen.s3.amazonaws.com/kindlegen_linux_2.6_i386_v2_9.tar.gz' > kindlegen.tar.gz;
	mkdir $KINDLEGEN_DIR;
	tar xzf kindlegen.tar.gz -C $KINDLEGEN_DIR;
	rm kindlegen.tar.gz;
fi

./$KINDLEGEN_DIR/kindlegen "$@"; EC=$?;
if [ $EC -eq 1 ]; then
	exit 0;
else
	exit $EC;
fi
