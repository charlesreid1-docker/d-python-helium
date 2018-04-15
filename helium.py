import os

"""
Python Helium Application

This is a multiport example that uses twisted
to serve up different static content 
on different ports.

See https://twistedmatrix.com/documents/current/web/howto/web-in-60/static-content.html
"""

from twisted.web.server import Site
from twisted.web.static import File
from twisted.internet import reactor
from twisted.internet import endpoints

info = {
        7777: 'pages',
        7778: 'hooks',
        7779: 'bots'
}

for port in info.keys():
    sub = info[port]
    subdomain = sub+".charlesreid1.com"

    # create server, glue to port, listen
    resource = File(os.path.join('/www',subdomain,'htdocs'))
    factory = Site(resource)
    endpoint = endpoints.TCP4ServerEndpoint(reactor,port)
    endpoint.listen(factory)

reactor.run()

