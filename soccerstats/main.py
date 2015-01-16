'''
Created on Jan 16, 2015

@author: anuvrat
'''

import scrapy.cmdline

def main():
    scrapy.cmdline.execute(argv=['scrapy', 'crawl', 'WhoScored', '-a', 'tournament=9155', '-a', 'year=2015', '-a', 'month=1'])

if  __name__ =='__main__':
    main()