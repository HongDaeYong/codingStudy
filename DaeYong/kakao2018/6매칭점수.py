from html.parser import HTMLParser

import re
class Parser(HTMLParser):
    def __init__(self, number, word):
        super().__init__()
        self.number = number
        self.word = word

        self.isBody = False
        self.isA = False

        self.link = None
        self.basic_score = 0
        self.external_links = []
        self.link_score = 0
        self.matching_score = 0

    def handle_starttag(self, tag, attrs):
        if tag == "meta" and len(attrs) > 1:
            self.link = attrs[1][1]
        elif tag == "body":
            self.isBody = True
        elif tag == "a":
            self.isA = True
            if attrs[0][0] == "href":
                self.external_links.append(attrs[0][1])

    def handle_endtag(self, tag):
        if tag == "body":
            self.isBody = False
        elif tag == "a":
            self.isA = False

    def handle_data(self, data):
        if self.isBody and not self.isA:
            print("curr data:", data)
            data_list = re.compile("[^a-zA-Z]+").split(data)
            print(data_list)
            for d in data_list:
                if d.lower() == self.word.lower():
                    self.basic_score += 1
                    print()


def solution(word, pages):
    parsers = []
    parser_dict = {}
    # feed to get own link, basic score and external links
    for i, page in enumerate(pages):
        parser = Parser(i, word)
        parser.feed(page)
        parsers.append(parser)
        parser_dict[parser.link] = i
    # get link scores
    for parser in parsers:
        for exLink in parser.external_links:
            try:
                tmp_link_score = float(parser.basic_score) / len(parser.external_links)
                parsers[parser_dict[exLink]].link_score += tmp_link_score
            except KeyError:
                pass
    # get matching scores
    max_score = -1
    answer = 0
    for i, parser in enumerate(parsers):
        parser.matching_score = parser.basic_score + parser.link_score
        if max_score < parser.matching_score:
            max_score = parser.matching_score
            answer = i
    return answer


# word = 'blind'
# pages = ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]
# print(solution(word, pages))


word = "Muzi"
pages = ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]
print(solution(word, pages))

# 40 점
# class Parser:
#     def __init__(self, html_number, word, html):
#         self.number = html_number
#         self.word = word
#         self.original = html
#         self.html_parse = None
#         self.link = None
#
#         self.basic_score = 0
#         self.num_external_link = 0
#
#         self.indicating_page_links = []
#         self.link_score = 0
#         self.matching_score = 0
#
#         self.parse()
#
#     def _extract_url(self, keyword, line):
#         for piece in line.split():
#             if keyword in piece:
#                 first_ = piece.find("\"")
#                 second_ = piece.find("\"", first_+1)
#                 return piece[first_+1:second_]
#
#     def parse(self):
#         self.html_parse = self.original.split("\n")
#
#         isBody = False
#         for line in self.html_parse:
#             # address of link
#             if "url" in line:
#                 self.link = self._extract_url("content", line)
#
#             if line.startswith("</body>"):
#                 isBody = False
#             if isBody:
#                 if "href" in line:
#                     # num external link
#                     self.num_external_link += 1
#                     # external links
#                     self.indicating_page_links.append(self._extract_url("href", line))
#
#                 # basic score
#                 idx = line.find("<a")
#                 outofa = line[:idx] if idx != -1 else line
#                 cnt = outofa.lower().count(self.word.lower())
#                 self.basic_score += cnt if cnt != -1 else 0
#             if line.startswith("<body>"):
#                 isBody = True
#
#         self.matching_score = self.basic_score
#
#
# def solution(word, pages):
#     link_to_address_dict = {}
#     parsers = []
#     for i, page in enumerate(pages):
#         parser = Parser(i, word, page)
#         link_to_address_dict[parser.link] = i
#         parsers.append(parser)
#     for parser in parsers:
#         for ipl in parser.indicating_page_links:
#             try:
#                 idx = link_to_address_dict[ipl]
#                 parsers[idx].link_score += float(parser.basic_score) / parser.num_external_link
#                 parsers[idx].matching_score += float(parser.basic_score) / parser.num_external_link
#             except KeyError:
#                 pass
#     maximum = -1
#     answer = 0
#     for i, parser in enumerate(parsers):
#         if parser.matching_score > maximum:
#             maximum = parser.matching_score
#             answer = i
#     return answer
