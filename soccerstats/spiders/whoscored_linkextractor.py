# -*- coding: utf-8 -*-

"""
Link extractors for WhoScored web pages.
"""

import ast

from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.link import Link
from scrapy.utils.project import get_project_settings


class WhoScoredLinkExtractor(LinkExtractor):
    """
    Extract links from WhoScored Tournament Feed pages
    """

    def extract_links(self, response):
        """
        Given the response from the tournament feed page, extract all the matches and return URLs to their page.
        :param response: The contents of the tournament feed page
        :return: The list of URL to match pages
        """
        match_page = get_project_settings().get('WHOSCORED_MATCH_FEED')
        
        return [Link(match_page % match[0]) for match in ast.literal_eval(response.body)]
