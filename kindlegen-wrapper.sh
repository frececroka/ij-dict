#!/usr/bin/env bash

./kindlegen "$@"; EC=$?;
if [ $EC -eq 1 ]; then
	exit 0;
else
	exit $EC;
fi
