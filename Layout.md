# Static Content Layout: Inside Container

Insie of the container, Python Helium expects
static content to be present in `/www`.

Each site should follow the schema of:

```
/www/<subdomain-url>/htdocs
```

where `htdocs` is a cloned copy of the `gh-pages` 
branch of the repository for that subdomain's 
one pager.

For example, the bots subdomain bots.charlesreid1.com
has the layout:

```
/www
    bots.charlesreid1.com/
        htdocs/
            index.html
            css/
            js/
            ...
    pages.charlesreid1.com
    hooks.charlesreid1.com
    api.charlesreid1.com
```

and htdocs is the repo at
[https://git.charlesreid1.com/charlesreid1/bots.charlesreid1.com](https://git.charlesreid1.com/charlesreid1/bots.charlesreid1.com).


