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
so this uses `jfloff/alpine-python:recent` 
(see [jflof/alpine-python](https://github.com/jfloff/alpine-python)).

See [Docker.md](/Docker.md)


## Static Content Layout

Python Helium expects static content to live in `/www` 
inside the container. The document below
details how to bind-mount each subdomain's 
static content/one-pager into the container
for the `helium.py` application.

See [Layout.md](/Layout.md)


## Note on Future Development

At this point, this repo was abandoned
in favor of [d-nginx-subdomains](https://git.charlesreid1.com/docker/d-nginx-subdomains),
but it is a useful tool that we'll keep around
for a future application.
