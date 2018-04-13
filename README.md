# d-python-helium

Like [d-python-onepagers](https://git.charlesreid1.com/docker/d-python-files), 
but more general.

Useful for static one-pagers:
* [bots.charlesreid1.com](https://git.charlesreid1.com/charlesreid1/bots.charlesreid1.com)
* [hooks.charlesreid1.com](https://git.charlesreid1.com/charlesreid1/hooks.charlesreid1.com)
* [pages.charlesreid1.com](https://git.charlesreid1.com/charlesreid1/pages.charlesreid1.com)

Runs either a file server (for files.charlesreid1.com) or a web server (for above).

Static files only.

Port and bind address should both be configurable.

## files.charlesreid1.com

This container will run a static files server in a given directory.

Currently, [d-python-files](https://git.charlesreid1.com/docker/d-python-files)
fills this role. It is a static server that runs in the 
[pod-charlesreid1](https://git.charlesreid1.com/charlesreid1/pod-charlesreid1.git)
so the bind address is `127.0.0.1` and the bind port is 8081.
This server is then reverse-proxied by nginx, so that nginx can handle
the subdomain and the HTTPS sessions, and Python can remain purely HTTP.


## static one-pagers

We have some additions to the charlesreid1 site,
now that blackbeard has been onboarded:
* [bots.charlesreid1.com](https://git.charlesreid1.com/charlesreid1/bots.charlesreid1.com)
* [hooks.charlesreid1.com](https://git.charlesreid1.com/charlesreid1/hooks.charlesreid1.com)
* [pages.charlesreid1.com](https://git.charlesreid1.com/charlesreid1/pages.charlesreid1.com)

The individual bots also need page upgrades.

To accomplish this, we implement a one-page pelican theme
called [scurvy-knave-theme](https://git.charlesreid1.com/charlesreid1/scurvy-knave-theme).
This page is a dead-simple single page template.

These repos have a source branch (`master`) 
and a live html content branch (`gh-pages`).
The `gh-pages` branch is the only one relevant
to `d-python-helium`.

### helium container

The `d-python-helium` container provides a super lightweight web server,
using Python's built-in webserver.

The static content for site `site.com` consists of html, images, 
css, js, and other files in the live `gh-pages` branch.
A copy of `gh-pages` for each subdomain is cloned on the host
machine (blackbeard) at `/www/site.com/htdocs/`:

```
mkdir -p /www/bots.charlesreid1.com/htdocs
git clone -b gh-pages https://git.charlesreid1.com/charlesreid1/bots.charlesreid1.com /www/bots.charlesreid1.com/htdocs
```

Now, each site is hosted by a `d-python-helium` container 
that mounts the `htdocs` directory inside the container
and serves it up on a particular port.

### coordinating multiple subdomains

There are multiple subdomains (bots, hooks, pages),
each with their own cloned copy of the live site, 
run by their own `d-python-helium` container.

So how do we coordinate all of these sites?

On blackbeard, we run one helium container per subdomain site,
and we set each helium container to listen on a different port 
(7777, 7778, 7779, 7780, 7781, etc.).

To serve this up, you set up a reverse proxy listener 
on the frontend (krash). Every domain and subdomain request
is directed to krash, and krash directs the traffic 
to the correct IP address.

Furthermore, you create a VPN between krash and blackbeard
so that they can communicate securely. All of the helium
servers are either running on krash with the `pod-charlesreid1` 
pod running the nginx frontend, or they listen on the 
private network connecting them to krash.

Reverse proxy setup for helium servers 
(assuming krash is at 10.0.0.1, blackbeard is at 10.0.0.2):

* Requests for `files.charlesreid1.com` are reverse-proxied to `127.0.0.1:8081`. 

* Requests for `bots.charlesreid1.com` are reverse-proxied to `10.0.0.2:7777`

* Requests for `hooks.charlesreid1.com` are reverse-proxied to `10.0.0.2:7778`

* Requests for `pages.charlesreid1.com` are reverse-proxied to `10.0.0.2:7779`

