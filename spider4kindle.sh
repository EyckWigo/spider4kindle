#!/bin/bash 

scrapy crawl news

ebook-convert result.html cnbeta.mobi --output-profile kindle --no-inline-toc --title "news" --publisher 'anoy' --language en --authors 'spider4kindle'

rm -f result.html
