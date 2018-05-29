#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

""" Run this script to get a preview of EzWebScraping.
"""

import time
import logging

from EzWebScraping import EzWebScraping


def main():
    scraper = EzWebScraping()
    scraper.connect('https://github.com/N3ROO/EzAPI')

if __name__ == '__main__':
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s ' +
                                  '-- %(levelname)s ' +
                                  '-- [%(filename)s:%(lineno)s ' +
                                  '-- %(funcName)s() ] ' +
                                  '-- %(message)s')
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.DEBUG)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    main()
