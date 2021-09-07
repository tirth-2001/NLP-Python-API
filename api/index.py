from html.parser import HTMLParser
from http.server import BaseHTTPRequestHandler
from urllib import parse
import json


def getdata():
    parser = HTMLParser()
    parser.feed("""<!DOCTYPE html>
<html>
<head>
<title>HTML Title</title>
</head>
<body>
<h1>Header 1</h1>
<h2>Header 2</h2>
<h3>Header 3</h3>
<p>This is a paragraph.</p>
</body>
</html>""")
    return parser.get_starttag_text()


if __name__ == "__main__":
    print(getdata())

language = "Python"
company = "GeeksForGeeks"
Itemid = 1
price = 0.00

# Create Dictionary
value = {
    "language": language,
    "company": company,
    "Itemid": Itemid,
    "price": price
}


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        s = self.path
        dic = dict(parse.parse_qsl(parse.urlsplit(s).query))
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        tag = getdata()
        print(tag)
        if "name" in dic:
            message = "Hello, " + dic["name"] + "!" + tag
        else:
            message = "Hello, stranger!" + tag
        self.wfile.write(message.encode())
        self.wfile.write(json.dumps(value).encode())
        return
