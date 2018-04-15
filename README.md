# d-python-helium

Like [d-python-files](https://git.charlesreid1.com/docker/d-python-files), 
but for serving static sites instead of files.

Static files only.

Port and bind address should both be configurable.

## Purpose

The purpose of Python Helium is to host
multiple one-page static sites for a 
series of subdomains of charlesreid1.com.

See [Subdomains.md](/Subdomains.md)

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

