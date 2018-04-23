# Helium Application

The helium appcliation is a twisted network application 
that serves different folders of static content on different
ports.

A straightforward example of what we are doing is 
available in the [python-multiport](https://github.com/charlesreid1/python-multiport)
repository at [static_content.py](https://github.com/charlesreid1/python-multiport/blob/master/static_content.py).

The gist of the program is this:

* For each static site:
    * Create a `twisted.File` resource that points to the static directory
    * Create a `twisted.Site` factory that creates an http listener on a port
    * Glue the http listener to a unique TCP port on the host machine
    * Run the `twisted.Site.listen()` method to add the listener to the twisted application
* Run the twisted application

It can be run like any python program,

```
python helium.py
```

