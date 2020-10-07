fp=open("index.html", "w")
print("<h1>Заголовок</h1>", file=fp)
fp.close()
def generate_body(header, paragraphs):
    body = "<h1>" + header + "</h1>"
    for p in paragraphs:
        body +="<p>"+p+"</p>"
    return "<body>" + body + "</body>"
