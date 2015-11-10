# Videoscene
![downloads](https://img.shields.io/pypi/dm/videoscene.svg)
![license](https://img.shields.io/pypi/l/videoscene.svg)
![version](https://img.shields.io/pypi/v/videoscene.svg)

A parser for scene release tags

## Install (automatic)
```
$ pip install videoscene
```
## Install (manual)
```
$ git clone git@github.com:walidsa3d/videoscene.git
$ cd videoscene
$ python setup.py install
```
## Usage
```python
>>> from videoscene.core import parse
>>> parse('Game.of.Werewolves.2011.SPANiSH.HDRip.x264-iLU')
{'title': 'Game of Werewolves', 'source': 'HDRip', 'video': 'x264', 'subtitles': 'SPANiSH', 'year': '2011', 'release_group': 'iLU'}
>>> parse('Jumanji.1995.FRENCH.720p.HDRip.XviD.AC3-CiNEFOX')
{'language': 'FRENCH', 'title': 'Jumanji', 'source': 'HDRip', 'video': 'XviD', 'screenSize': '720p', 'year': '1995', 'audio': 'AC3', 'release_group': 'CiNEFOX'}
>>> parse('Rush.Hour.2.2001.720p.FRENCH.HDRiP.x264.AC3-KLiT')
{'language': 'FRENCH', 'title': 'Rush Hour 2', 'source': 'HDRiP', 'video': 'x264', 'screenSize': '720p', 'year': '2001', 'audio': 'AC3', 'release_group': 'KLiT'}
>>> 
```
## License
```
The MIT License (MIT)
Copyright (c) 2015 Walid Saad

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE
OR OTHER DEALINGS IN THE SOFTWARE.
```