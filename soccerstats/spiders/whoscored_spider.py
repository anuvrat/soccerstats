# -*- coding: utf-8 -*-

"""
Spider to crawl WhoScored web pages.
"""

import re

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.utils.project import get_project_settings
from soccerstats.spiders.whoscored_linkextractor import WhoScoredLinkExtractor
from soccerstats.items import WhoScoredRatingsItem
import json


class WhoScoredSpider(CrawlSpider):
    """
    Define the crawler to crawwl WhoScored web pages and extract player ratings
    """
    name = 'WhoScored'
    allowed_domains = ['www.whoscored.com']
    rules = (
        Rule(WhoScoredLinkExtractor(), callback='parse_item'),
    )

    def __init__(self, tournament=None, year=None, month=None, *args, **kwargs):
        super(WhoScoredSpider, self).__init__(*args, **kwargs)
        self.start_urls = self.__prepare_seed_list(tournament, year, month)

    def parse_item(self, response):
        """
        Given the match feed page, extract ratings for both the teams
        :param response: The contents of the match page
        :return: The rating items for both the teams.
        """
        
        match_data_element = response.xpath('//script[contains(., "matchCentreData")]/text()').extract()
        if len(match_data_element) == 0:
            return
        
        match_data = match_data_element[0]
        match_center_data = json.loads(re.search("matchCentreData = (.+?);", match_data).group(1))

        item = WhoScoredRatingsItem()

        item['match_id'] = re.search("matchId = (.+?);", match_data).group(1)
        item['venue_name'] = match_center_data['venueName']
        item['referee_name'] = match_center_data['refereeName'] if 'refereeName' in match_center_data else '' 
        item['start_time'] = match_center_data['startTime']
        item['competition'] = response.xpath('//div[@id="breadcrumb-nav"]/a/text()').extract()
        
        for pos in ['home', 'away']:
            team_data = match_center_data[pos]
            item[pos + '_team_id'] = team_data['teamId']
            item[pos + '_team_name'] = team_data['name']
            item[pos + '_team_average_age'] = team_data['averageAge']
            item[pos + '_team_manager'] = team_data['managerName']
            item[pos + '_team_formation'] = team_data['formations'][0]['formationName']
            item[pos + '_team_score_halftime'] = team_data['scores']['halftime']
            item[pos + '_team_score_fulltime'] = team_data['scores']['fulltime']
            
            players = {}
            team_rating = 0.0
            players_involved = 0
            for player in team_data['players']:
                player_id = player['playerId']
                
                ratings_array = player['stats']['ratings'] if 'ratings' in player['stats'] else None
                if ratings_array:
                    rating = ratings_array[max(ratings_array, key = int)]
                    team_rating += rating
                    players_involved += 1
                else: 
                    rating = -1
                
                players[player_id] = {'age': player['age'], 
                                      'height': player['height'], 
                                      'shirt': player['shirtNo'] if 'shirtNo' in player else -1, 
                                      'position': player['position'], 
                                      'name': player['name'], 
                                      'started': 'isFirstEleven' in player and player['isFirstEleven'], 
                                      'rating': rating
                                      }
                
                if player['isManOfTheMatch']:
                    item['man_of_the_match'] = {'id': player_id, 'name': player['name']}
            
            item[pos + '_team_players'] = players
            item[pos + '_team_rating'] = team_rating / players_involved 
        
        return item
        

    def __prepare_seed_list(self, tournament, year, month):
        whoscored_feed_url = get_project_settings().get('WHOSCORED_FEED_URL')

        if tournament and year and month:
            return [whoscored_feed_url % (tournament, year, month.zfill(2))]

        tournaments = get_project_settings().get('TOURNAMENTS')
        years = get_project_settings().get('TOURNAMENT_YEARS')

        dates = [(years[0], month) for month in xrange(06, 12)]
        #dates.extend([(years[1], month) for month in xrange(01, 06)])

        return [whoscored_feed_url % (tournament, year, str(month).zfill(2)) for tournament in tournaments for (year, month) in dates]
