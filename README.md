## fxideo
Fancy wraper class for ideographic character handling in terminal based displays. Especially so called half-width and full-width Katakana, Hiragana and Romanji characters.

## Installation
Use setup.py
```shell
python3 -m pip install "git+https://git.ars-virtualis.org/yul/fxideo@master"
```

## Usage
```python
from fxideo import FxIdeo


s = "S・H・A・R・E〜愛をふたりで〜ボーナス"
fxd = FxIdeo(s)

# len accounts for displayed size on terminal
>>> len(s)
21
>>> len(fxd)
37

# detection of ideographic characters
if fxd:
    print("this string contains ideographic characters")

# slices based on displayed length
>>> s[:14]
'S・H・A・R・E〜愛をふた'
>>> fxd[:14]
'S・H・A・R・E'

# a call to __str__ returns the original string
>>> len(str(fxd))
21
```

## License
[GPLv2](https://choosealicense.com/licenses/gpl-2.0/)
