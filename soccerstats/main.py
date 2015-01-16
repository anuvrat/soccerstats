'''
Created on Jan 16, 2015

@author: anuvrat
'''

import scrapy.cmdline

def main():
    scrapy.cmdline.execute(argv=['scrapy', 'crawl', 'WhoScored', '-a', 'tournament=9187', '-a', 'year=2014', '-a', 'month=7'])

if  __name__ =='__main__':
    main()