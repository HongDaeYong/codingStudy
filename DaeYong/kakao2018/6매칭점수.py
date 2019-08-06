class Parser:
    def __init__(self, html_number, word, html):
        self.number = html_number
        self.word = word
        self.original = html
        self.html_parse = None
        self.link = None

        self.basic_score = 0
        self.num_external_link = 0

        self.indicating_page_links = []
        self.link_score = 0
        self.matching_score = 0

        self.parse()

    def _extract_url(self, keyword, line):
        for piece in line.split():
            if keyword in piece:
                first_ = piece.find("\"")
                second_ = piece.find("\"", first_+1)
                return piece[first_+1:second_]

    def parse(self):
        self.html_parse = self.original.split("\n")

        isBody = False
        for line in self.html_parse:
            # address of link
            if "url" in line:
                self.link = self._extract_url("content", line)

            if line.startswith("</body>"):
                isBody = False
            if isBody:
                if "href" in line:
                    # num external link
                    self.num_external_link += 1
                    # external links
                    self.indicating_page_links.append(self._extract_url("href", line))

                # basic score
                self.basic_score += line.lower().count(word.lower())
            if line.startswith("<body>"):
                isBody = True

        self.matching_score = self.basic_score


def solution(word, pages):
    link_to_address_dict = {}
    parsers = []
    for i, page in enumerate(pages):
        parser = Parser(i, word, page)
        link_to_address_dict[parser.link] = i
        parsers.append(parser)
    for parser in parsers:
        for ipl in parser.indicating_page_links:
            try:
                idx = link_to_address_dict[ipl]
                parsers[idx].link_score += float(parser.basic_score) / parser.num_external_link
            except KeyError:
                print("key error :" + ipl)
    parsers.sort(key=lambda x: x.matching_score, reverse=True)
    return parsers[0].number


# word = 'blind'
# pages = [
#     "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n"
#     "<head>\n"
#     "  <meta charset=\"utf-8\">\n"
#     "  <meta property=\"og:url\" content=\"https://a.com\"/>\n"
#     "</head>  \n"
#     "<body>\n"
#     "Blind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n"
#     "<a href=\"https://b.com\"> Link to b </a>\n"
#     "</body>\n"
#     "</html>",
#
#      "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n"
#      "<head>\n"
#      "  <meta charset=\"utf-8\">\n"
#      "  <meta property=\"og:url\" content=\"https://b.com\"/>\n"
#      "</head>  \n"
#      "<body>\n"
#      "Suspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n"
#      "<a href=\"https://a.com\"> Link to a </a>\n"
#      "blind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n"
#      "<a href=\"https://c.com\"> Link to c </a>\n"
#      "</body>\n"
#      "</html>",
#
#      "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n"
#      "<head>\n"
#      "  <meta charset=\"utf-8\">\n"
#      "  <meta property=\"og:url\" content=\"https://c.com\"/>\n"
#      "</head>  \n"
#      "<body>\n"
#      "Ut condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n"
#      "<a href=\"https://a.com\"> Link to a </a>\n"
#      "</body>\n"
#      "</html>"
#      ]
# print(solution(word, pages))


word = "Muzi"
pages = ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]
print(solution(word, pages))

