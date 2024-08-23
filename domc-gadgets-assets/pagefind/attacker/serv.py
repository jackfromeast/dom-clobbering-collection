#!/usr/bin/env python
from http import server

class MyHTTPRequestHandler(server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        server.SimpleHTTPRequestHandler.end_headers(self)


if __name__ == '__main__':
    server.test(HandlerClass=MyHTTPRequestHandler)