# pyPublisher
use zeromq and the linux pipe

usage:

```(bash)
python publisher.py --host [localhost|other] --port[port to make data available on] --verbose
```


The publisher script takes a file or stdin(default) as the input and makes that available on a port of your choice using ZeroMQ
So you can do things like:
```
echo "this is a test" | python publisher.py [options]
```
The two client scripts one in Lua and the other in python are just there as an example.
