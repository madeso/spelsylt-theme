# gamejam theme generator

Generate a theme for a gamejam


```sh
# generate a 'word' with at least 5 definitions
./sylt.py theme --min 5
spel
- bollspel, dataspel, schackspel, etc.
- framförande av musik eller sceniskt verk
- hasardspel d.v.s. spel om pengar
- oberäknelig rörelse fram och tillbaka eller bli tillfälligt tokig/galen
- parningslek hos fåglar
- större festligt arrangemang t.ex. olympiska spelen
- vinda, vinsch
```

```sh
# display all words
./sylt.py stat
11 has 1 words (total: 1)
7 has 4 words (total: 5)
6 has 2 words (total: 7)
5 has 9 words (total: 16)
4 has 14 words (total: 30)
3 has 64 words (total: 94)
2 has 135 words (total: 229)
```


```sh
./sylt.py -h           
usage: sylt.py [-h] {theme,ls,stat} ...

Sylt tools

options:
  -h, --help       show this help message and exit

Commands:
  {theme,ls,stat}
    theme          Generate a theme
    ls             List all words
    stat           List word stats
```
