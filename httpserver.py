# File: main.py
# Aim: Start Simple HTTP server

import http.server
import socketserver
import webbrowser
import threading


class HTTPServer(object):
    # HTTP Server
    def __init__(self, PORT=8000):
        # Init parameters
        self.PORT = PORT
        self.Handler = http.server.SimpleHTTPRequestHandler
        self.httpd = socketserver.TCPServer(('', self.PORT), self.Handler)

    def _serve_forever(self):
        # Built-in function,
        # start serving
        print('Backend is serving at port', self.PORT)
        self.httpd.serve_forever()

    def start(self):
        # Start serving and handle the server in a thread
        t = threading.Thread(target=self._serve_forever)
        # Set the thread Deamon to make sure it can be stopped when closed
        t.setDaemon(True)
        # Start the thread
        t.start()


# Set up HOMEPAGE
HOMEPAGE = 'http://localhost:8000/src/index.html'
HOMEPAGE = 'http://localhost:8000/src/img_resize.html'

# Define FUNCTIONS dict,
# key is the hot key,
# value is the description
FUNCTIONS = dict(
    q='close the backend',
    n='open a new HOMEPAGE',
    h='show the URL of HOMEPAGE'
)


def get_help(functions=FUNCTIONS):
    # Print help session
    print('-' * 80)
    print('Welcome to HELP session')
    for key in functions:
        print(f'Enter "{key}" to {functions[key]}')
    print('')


if __name__ == '__main__':
    # Init server
    server = HTTPServer()
    # Start server
    server.start()

    # Provide a very simple manager,
    # press 'h' to get help

    # Print help session first
    get_help()

    # Start manage loop
    while True:
        # Wait for input
        inp = input('>> ')

        if not inp in FUNCTIONS:
            # Get illegal input,
            # print help session
            get_help()

        if inp == 'q':
            # Get 'q', break the loop
            break

        if inp == 'n':
            # Get 'n', start a new homepage
            webbrowser.open(HOMEPAGE)

        if inp == 'h':
            # Get 'h', show the url of homepage
            print(f'Homepage URL is "{HOMEPAGE}"')

    # Closing the backend,
    # say good-byd
    print('The backend has been closed, bye!')
