# snwy.me
this is my site

i wrote a simple static site generator, `gen.py`. you can use it on your own site. the syntax is:
```
~title[<name here without arrows>] : the title of the document
~template[<name here without arrows>] : the template html page
~replace[<name here without arrows>] : the string to replace with the output in the template

<any html tag>[<content>] : for example: p[hello world] will create <p>hello world</p> in the output. these do not support multiline because the generator is extremely basic.
```
