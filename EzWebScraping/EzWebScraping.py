#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

""" TODO: desc
"""

import requests
import logging
import warnings
import urllib
from lxml import html


class EzWebScraping:
    def __init__(self):
        self.logger = logging.getLogger()
        self.session = requests.session()
        self.page = None
        self.last_url = None

    # ----
    # Main functions
    # ----

    def connect(self, url, payload=None, auto_session_reset=True):
        if auto_session_reset and self.last_url is not None:
            self.__verify_website_session__(url)

        self.logger.debug('Connecting to %s ...', url)

        if payload is None:
            result = self.session.get(
                url,
                headers=dict(referer=url))
        else:
            result = self.session.post(
                url,
                data=payload,
                headers=dict(referer=url))

        if result.ok:
            self.logger.debug('Connected to %s.', url)
            self.page = result
        else:
            logger.error('Failed to connect to %s.', url)
            self.page = None

    # ----
    # Getters & Setters
    # ----

    def reset_session(self):
        """ It resets the current session.
        """

        self.session = requests.session()

    def get_page(self):
        """ It gets the current page.

        Returns:
        --------
            session -- The current page, or None if unset.
        """

        return self.page

    def get_html_page(self):
        """ It gets the HTML content of the page in bytes.

        Returns:
            bytes -- HTML code of the current page.
        """

        return self.page.content

    def get_session(self):
        """ It gets the current session.

        Returns:
            Session -- The session object (from the "requests" lib), or
                None if unset.
        """

        return self.session

    # ----
    # Private functions
    # ----

    def __verify_website_session__(self, url):
        """ It resets the session if the url given has a different base
        from the last accessed url. It means that it resets the session
        if the user has changed website.

        Arguments:
        ----------
            url {str} -- Website to access
        """

        if self.__get_url_base__(url) != self.__get_url_base__(self.last_url):
            self.logger.warn('You should reset the session when changing ' +
                             'website.')
            self.logger.warn('Use the keywork "auto_session_reset" to ' +
                             'prevent session reset on website change.')
            self.reset_session()

    def __get_url_base__(self, url):
        """ It retrieves the url base :
        For https://google.com/something/ it will get google.com.

        Arguments:
        ----------
            url {str} -- The url which you want the base,

        Returns:
        --------
            str -- The url base.
        """

        if self.__is_url_valid__(url):
            url_base = url.split('//')[-1]
            url_base = url_base.split('/')[0]
            url_base = url_base.split('?')[0]
        else:
            url_base = None

        return url_base

    def __is_url_valid__(self, url, qualifying=('scheme', 'netloc')):
        """ It validates the url.

        Arguments:
        ----------
            url {str} -- The url to validate,

        Keyword Arguments:
        ------------------
            qualifying {tuple of str} -- Min attributes to define the
                url as a valid one (default: ('scheme', 'netloc')),

        Returns:
        --------
            boolean -- True if the url is valid, false otherwise.
        """

        token = urllib.parse.urlparse(url)

        return all([getattr(token, qualifying_attr)
                   for qualifying_attr in qualifying])
