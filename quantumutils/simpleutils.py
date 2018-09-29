"""
Some very simple utility methods, that do not require extensive coding
"""
import aiohttp

def partition(text: str, length: int)->list:
    """
    split a text according to its length
    :param text: input text
    :param length: maximum length of each substring
    :return: a list of substrings
    """
    res=[]
    while len(text)>0:
        res.append(text[:length])
        text=text[length:]
    return res

def tdm(td):
    """
    converting a datetime.datetime object to a timestamp
    :param td: A datetime.datetime instance
    :return: time in milliseconds
    """
    return ((td.days * 86400000) + (td.seconds * 1000)) + (td.microseconds / 1000)


def find(substring, string):
    """
    gets the occurrences of the substring in the main string
    :param substring: the text to find
    :param string: the main search string
    :return: the indices of occurrence
    """
    last_found = -1  # Begin at -1 so the next position to search from is 0
    while True:
        # Find next index of substring, by starting after its last known position
        last_found = string.find(substring, last_found + 1)
        if last_found == -1:
            break  # All occurrences have been found
        yield last_found


async def getjson(url):
    """
    gets json content from url if supported
    :param url: the url used
    :return: the json output
    """
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            f = await response.json(encoding='utf8')
    return f
