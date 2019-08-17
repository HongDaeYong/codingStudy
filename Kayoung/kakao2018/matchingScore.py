from html.parser import HTMLParser
import re
import operator

class KakaoHTMLParser(HTMLParser):
    url = ""
    isBody = False
    word = ""
    # links = []

    basicScore = 0

    def __init__(self, word):
        super().__init__()
        self.word = word.lower()
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag == "body":
            self.isBody = True

        if tag == "meta":
            for attr in attrs:
                if attr[0] == "content":
                    self.url = attr[1]

        if tag == "a":
            for attr in attrs:
                if attr[0] == "href":
                    self.links.append(attr[1])

    def handle_endtag(self, tag):
        if tag == "body":
            self.isBody = False

    def handle_data(self, data):
        if self.isBody:
            p = re.compile("[^a-z]+")
            words = p.split(data.lower())
            self.basicScore += words.count(self.word)


def solution(word, pages):
    parsers = []
    for page in pages:
        parser = KakaoHTMLParser(word)
        parser.feed(page)
        parsers.append(parser)


    matchingScores = {i: i for i in range(0, len(pages))}

    for i, p in enumerate(parsers):
        linkScore = 0
        for ps in parsers:
            for link in ps.links:
                if p.url == link:
                    linkScore += ps.basicScore / len(ps.links)
        matchingScores[i] = linkScore + p.basicScore

    return max(matchingScores.items(), key=operator.itemgetter(1))[0]



print(solution("blind",
["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]
         ))