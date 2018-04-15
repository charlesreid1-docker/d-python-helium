# d-python-helium

Like [d-python-files](https://git.charlesreid1.com/docker/d-python-files), 
but for serving static sites instead of files.

Static files only.

Port and bind address should both be configurable.

## Purpose

We have several subdomains that consist of single static pages:
* [bots.charlesreid1.com](https://git.charlesreid1.com/charlesreid1/bots.charlesreid1.com)
* [hooks.charlesreid1.com](https://git.charlesreid1.com/charlesreid1/hooks.charlesreid1.com)
* [pages.charlesreid1.com](https://git.charlesreid1.com/charlesreid1/pages.charlesreid1.com)
* [api.charlesreid1.com](https://git.charlesreid1.com/charlesreid1/api.charlesreid1.com)

The individual bots also need page upgrades.

To accomplish this, we implement a one-page pelican theme,
[scurvy-knave-theme](https://git.charlesreid1.com/charlesreid1/scurvy-knave-theme).
This page is a dead-simple single page template.

These repos have a source branch (`master`) 
and a live html content branch (`gh-pages`).

The `gh-pages` branch is the only one relevant
to `d-python-helium`. This branch contains
static content to be hosted by `d-python-helium`.

## Helium Application

The helium appcliation is a twisted network application 
that serves different folders of static content on different
ports.

See [Helium.md](/Helium.md).


## Dockerfile and Base Image

The core idea behind python helium is to be as lightweight as possible,
so this is based on the lightweight `jfloff/alpine-python` image.

See [Docker.md](/Docker.md)


## Static Content Layout

Python Helium expects static content to live in `/www` 
inside the container. The document below
details how to bind-mount each subdomain's 
static content/one-pager into the container
for the `helium.py` application.

See [Layout.md](/Layout.md)

## Coordinating Subdomains

The end goal is to have a single Python service
that listens on multiple ports, serving a different
static site on each port, with different static sites
corresponding to different subdomains.

To do this, Python Helium works in coordination with 
the nginx web server. 

See [Subdomains.md](/Subdomains.md)

