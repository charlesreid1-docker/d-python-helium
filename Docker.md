# Dockerfile and Base Image

The core idea behind python helium is to be as lightweight as possible,
so this is based on the lightweight `jfloff/alpine-python` image.

The Dockerfile extends `jfloff/alpine-python:recent-slim` 
and installs twisted into the container on first run.

## Network

This requires the container to listen for requests 
on multiple ports. The container should be bound 
to the correct address.

If Python Helium is listening for requests from an nginx 
container in the same pod, you can listen for any incoming
request (no need to bind to a particular address).
In this case the container will not have any external
interface.

If Python Helium is listening for requests over a VPN, 
the service should be bound to the VPN IP address of
the machine. This will ensure that the server only
responds to (encrypted) requests from machines on the VPN.

## Volumes and Bind Mounting

The Dockerfile expects the application to be at:

```
/app/helium.py
```

so bind mount the `helium.py` application to `/app/helium.py`
when you run this container.

