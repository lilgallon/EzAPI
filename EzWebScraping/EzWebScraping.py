#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

"""It makes the complicated part of web scraping easy. Everything related to
the requests and sessions are handled in this class. Here is a small example on
how to use it:

0. Import
    from EzWebScraping import EzWebScraping

1.1 Create an instance & connect to a website (without authentification)
    scraper = EzWebScraping()
    scraper.connect('https://github.com/')

1.2 Create an instance & connect to a website (with authentification)
    payload = {
        "login": "YOUR LOGIN",
        "password": "YOUR PASSWORD"
    }
    scraper = EzWebScraping()
    scraper.connect('https://github.com/',
                    payload=payload,
                    auth_token_name="authenticity_token")

2. Retrieve the content of the website page to scrape it through BeautifulSoup
    bs = BeautifulSoup(web.get_html_page(), "html.parser")

Note: It uses "logging" from python. If you want to see the logs, you have to
set up your logger.

This API is built thanks to those libraries :
- requests: http://docs.python-requests.org/en/master/
- urllib: https://docs.python.org/3/library/urllib.html
- lxml: https://lxml.de/

Author: Lilian Gallon (N3ROO)
Version: 1.0
"""

import requests
import logging
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

    def connect(self, url, payload=None, auth_token_name=None,
                postRequest=True, session_reset=False):
        """It connects to the specified URL. If you want to perform a
        login (that requires login information), you need to specify
        payload and probably auth_token_name (some websites do not
        want this information). Each website login implementation is
        different, so you will have to find the right values for your
        website. Here is an explanation: (screenshot guide available on
        github)
        Inspect the <form> content in the specified website. Look for
        the username input, and write the content of its name somewhere.
        Then, do the samething for the password field. Once it is done,
        the payload variable should look like this:
        payload = {
            <username-input-name>: <your-username>,
            <password-input-name>: <your-password>
        }
        (friendly remember: do not push to git your personal info).
        Now, we will take a look to the "authentification token name".
        Some websites require it. Look for an input which name is
        something like "csrfmiddlewaretoken" or "csrf_token", or
        "authenticity_token" or ... . Once you found it, copy its name
        attribute, and pass it in this function:
        auth_token_name = <authen-token-name-that-you-found>.
        Okay, just few things left. Now, take a look at the <form> tag,
        and if "method" attribute value is "get", change postRequest to
        false. Otherwise postRequest is already true, so it's fine!
        You are almost done! The last thing to check is the url.
        Sometimes, you write your personal information on a page, and
        the login is performed on a different page. To know that, take
        a look to the <form> tag. There should be an "action" attribute.
        It indicates where the login will be performed. If the website
        is https://github.com/, and the action is "/session", you need
        to put https://github.com/session, for the url (instead of
        https://github.com/login in this case).

        Arguments:
            url {str} -- The url where the login is performed (take a
            look at the "action" attribute of the <form> tag)

        Keyword Arguments:
            payload {dict} -- It contains your personal information if
                you want to perform a login (default: {None}),
            auth_token_name {[type]} -- It contains the name of the
            authentification token input (default: {None}),
            session_reset {bool} -- Change it to true if you want to
                reset your browsing session (it will forget everything)
                (default: {False}).
        """

        if session_reset and self.last_url is not None:
            self.__verify_website_session__(url)

        self.logger.debug('Connecting to %s ...', url)

        if payload is None:
            result = self.session.get(
                url,
                headers=dict(referer=url))
        else:
            if auth_token_name is not None:
                # We need the authentification token, and add it to the
                # payload dict
                result = self.session.get(url)

                tree = html.fromstring(result.text)
                payload[auth_token_name] = list(
                    set(
                        tree.xpath("//input[@name='" +
                                   auth_token_name +
                                   "']/@value")
                        )
                    )[0]

            if postRequest:
                result = self.session.post(
                    url,
                    data=payload,
                    headers=dict(referer=url))
            else:
                # If we want to use a getRequest, we need to put the
                # information after the url : url?p1=v1&p2=v2 and so on
                getParameters = "?"
                for key, value in payload.items():
                    getParameters += key + "=" + value + "&"
                url += getParameters

                result = self.session.get(
                    url,
                    headers=dict(referer=url))

        if result.ok:
            self.logger.debug('Connected to %s.', url)
            self.page = result
        else:
            self.logger.error('Failed to connect to %s.', url)
            self.page = None

    # ----
    # Getters & Setters
    # ----

    def reset_session(self):
        """ It resets the current session.
        """

        self.session = requests.session()

    def get_response(self):
        """ It gets the response of the current page. Here is some
        documentation:
        docs.python-requests.org/en/master/user/advanced/#session-objects

        Returns:
        --------
            session -- The current page response, or None if unset.
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

    def get_url(self):
        """ It gets the url of the current page.

        Returns:
            string -- The current page URL.
        """

        return self.page.url

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
