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
1 words has 11 meanings (total words: 1)
4 words has 7 meanings (total words: 5)
2 words has 6 meanings (total words: 7)
9 words has 5 meanings (total words: 16)
14 words has 4 meanings (total words: 30)
64 words has 3 meanings (total words: 94)
135 words has 2 meanings (total words: 229)
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
