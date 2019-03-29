![EzWebScraping](images/EzWebScraping.png)

# EzWebScraping ![version](https://img.shields.io/badge/Version-1-green.svg)

A simple way to retrieve data from websites with or without authentification.

This API is built thanks to those libraries :
- [requests](http://docs.python-requests.org/en/master/)
- [urllib](https://docs.python.org/3/library/urllib.html)
- [lxml](https://lxml.de/)

## How to use it

- Import it
```python
    from EzWebScraping import EzWebScraping
```

- Create an instance & connect to a website (without authentification)
```python
    scraper = EzWebScraping()
    scraper.connect('https://github.com/')
```

- Create an instance & connect to a website (with authentification)
```python
    payload = {
        "login": "YOUR LOGIN",
        "password": "YOUR PASSWORD"
    }
    scraper = EzWebScraping()
    scraper.connect('https://github.com/',
                    payload=payload,
                    auth_token_name="authenticity_token")
```

- Retrieve the content of the website page to scrape it with BeautifulSoup
```python
    bs = BeautifulSoup(web.get_html_page(), "html.parser")
```

## How to use it in your projects

Get the file from the github page and put it in your project directory.

## Documentation

The detailed documentation is available on the [wiki](https://github.com/N3ROO/EzAPI/wiki).

## Contributing

If you want to contribute, make sure to respect PEP8 and python coding conventions. And please remind that the goal of this API is to be very easy to use in a non-object oriented programming context.

## Misc

- See the changelog [here](CHANGELOG.md),
- See the licence [here](../LICENSE).