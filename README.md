# brainfuck.py
Brainf*ck implementation in Python

## usage

Write such code:

```python
from interpreter import parse, run

run(parse('your code'))
```

and then

```sh
$ python foo.py

# if you want some input
$ echo 'your input' | python foo.py
```
