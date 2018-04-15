# Coordinating Subdomains 

The end goal is to have a single Python service
that listens on multiple ports, serving a different
static site on each port, with different static sites
corresponding to different subdomains.


```

                                                      +----------------------------------------+
                                                      |         python helium                  |
                         HTTPS     +----------+       |                                        |
                                   |  nginx   |       | +------------------------------------+ |
pages.charlesreid1.com-----------> |          +-------> | port 7777   pages.charlesreid1.com | |
                                   |          |       | |             static content         | |
                                   |          |       | +------------------------------------+ |
hooks.charlesreid1.com-----------> |          +-------> | port 7778   hooks.charlesreid1.com | |
                                   |          |       | |             static content         | |
                                   |          |       | +------------------------------------+ |
bots.charlesreid1.com------------> |          +-------> | port 7779   bots.charlesreid1.com  | |
                                   |          |       | |             static content         | |
                                   +----------+       | +------------------------------------+ |
                                                      |                                        |
                                                      +----------------------------------------+

```

There are multiple subdomains (bots, hooks, pages),
each with their own cloned copy of the live site, 
run by their own `d-python-helium` container.

So how do we coordinate all of these sites?

## Everything On One Machine

Let's start by explaining how to do it if everything is on 
one machine. 

We have an nginx web server running on the host machine 
as either a host service, or as a container, and it 
reads a configuration file that tells it how to route traffic.

The nginx server will receive a request for a subdomain
(bots.charlesreid1.com), and from the rules in the 
configuration file (which we will cover) it sees it should
forward the request to Python Helium.

If nginx is running as a host service, it will forward 
the request to local port 7777 (or whatever local port 
the Python Helium container is running on). If nginx is 
running in a container, ideally as a container in the same
pod as the Python Helium container, the nginx container 
can set up a route to the Python Helium container 
using the docker virtual network.

In this way, nginx reverse proxies requests for the subdomain
to the Python Helium service.

## Running Nginx and Python Helium on Separate Machines

So you wanna run nginx and Python Helium on separate machines.

The way we do this is nearly identical to the setup 
described above, except we replace the internal 
docker network and/or itra-machine port traffic
with a virtual private network.

Now, we have nginx on one node, and Python Helium on another,
and they can communciate over an encrypted VPN tunnel.

When a subdomain request comes to the nginx server, 
it is now reverse proxied to the VPN IP address 
of the server running Python Helium.

For example, if nginx were running on `10.0.0.1` and 
Python Helium on `10.0.0.2`, the nginx rule would be 
to reverse-proxy all requests for bots.charlesreid1.com
`to 10.0.0.2:7777`.

## Setting Up the VPN

The "easiest" way to get a mesh VPN network going 
is to use tinc. It takes a while, and requires you
read a tutorial step-by-step, but it is powerful
and useful software.

See [https://charlesereid1.com/wiki/Tinc](https://charlesereid1.com/wiki/Tinc)


