# -*- coding: utf-8 -*-

# Scrapy settings for soccerstats project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'soccerstats'

SPIDER_MODULES = ['soccerstats.spiders']
NEWSPIDER_MODULE = 'soccerstats.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Anuvrat Singh (+http://singhanuvrat.com)'

# WhoScored settings
WHOSCORED_MATCH_FEED = 'http://www.whoscored.com/Matches/%s/Live'
WHOSCORED_FEED_URL = 'http://www.whoscored.com/tournamentsfeed/%s/Fixtures/?d=%s%s&isAggregate=false'
TOURNAMENTS = [9155,    # England-Premier-League-2014-2015
               11369,   # Italy-Serie-A-2014-2015
               11363,   # Spain-La-Liga-2014-2015
               9192,    # Germany-Bundesliga-2014-2015
               9105,    # France-Ligue-1-2014-2015
               9121,    # Netherlands-Eredivisie-2014-2015
               9145,    # Russia-Premier-League-2014-2015
               4185,    # Fixtures/Brazil-Brasileiro-2014
               8358,    # USA-Major-League-Soccer-2014
               11306,   # Turkey-Super-Lig-2014-2015
               9156,    # England-Championship-2014-2015
               9189,    # Europe-UEFA-Champions-League-2014-2015
               9187,    # Europe-UEFA-Europa-League-2014-2015
               10274    # International-FIFA-World-Cup-2014
               ]
TOURNAMENT_YEARS = [2014, 2015]    # Years for the current season
