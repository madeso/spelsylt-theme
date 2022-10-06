#!/usr/bin/env python3

import argparse
import os
import urllib
import urllib.parse
import urllib.error
import urllib.request
import typing
import random
import itertools
import collections

from bs4 import BeautifulSoup


###################################################################################################

# https://letsmakeagame.net/game-jam-theme-generator/
# https://homonym.se/homonymer

###################################################################################################


def download_url(link: str, status: str) -> str:
    status_text = '' if len(status)==0 else '({})'.format(status)
    print('Requesting url{}: {}'.format(status_text, link))
    try:
        with urllib.request.urlopen(link) as url_handle:
            data = url_handle.read()
            return data.decode('utf-8')
    except urllib.error.HTTPError as http_error:
        if http_error.code == 404:
            print('404 error')
            return ''
        else:
            raise http_error


def get_cachedir() -> str:
    filedir = os.path.join(os.getcwd(), 'cache')
    os.makedirs(filedir, exist_ok=True)
    return filedir


def local_filename(link: str) -> str:
    filedir = get_cachedir()
    filename = urllib.parse.quote(link, '')
    path = os.path.join(filedir, filename)
    return path


def get_url_or_cache(link: str, status: str) -> str:
    path = local_filename(link)
    if os.path.exists(path):
        with open(path, 'rb') as file_handle:
            return file_handle.read().decode('utf-8')
    else:
        data = download_url(link, status)
        with open(path, 'wb') as file_handle:
            file_handle.write(data.encode('utf-8'))
        return data


class Homonym:
    def __init__(self, base, data):
        self.url = base + data.get('href')
        self.word = data.get_text()

        data = get_url_or_cache(self.url, self.word)
        soup = BeautifulSoup(data, 'html.parser')
        defs = soup.find_all('td')
        self.defs = [d.get_text().split(' ', maxsplit=2)[2].strip() for d in defs]
    
    def __str__(self):
        return f'{self.url}: {self.word}'
    
    def __repr__(self):
        return f'{self.word}: {len(self.defs)}'


def collect_homonym() -> typing.List[Homonym]:
    base = 'https://homonym.se'
    data = get_url_or_cache(base + '/homonymer', '')
    soup = BeautifulSoup(data, 'html.parser')
    links = soup.find_all('a')
    links = [Homonym(base, link) for link in links if link.get('href').startswith('/homonymer/')]
    return links


def grouped_homonym():
    hs = collect_homonym()
    keyfunc = lambda h: len(h.defs)
    hs = sorted(hs, key=keyfunc, reverse=True)
    return itertools.groupby(hs, keyfunc)


###################################################################################################

def handle_theme(args):
    hs = collect_homonym()
    if args.min > 0:
        hs = [h for h in hs if len(h.defs) >= args.min]
    if len(hs) == 0:
        print('no themes :(')
        print()
        return
    theme = random.choice(hs)
    print(theme.word)
    for d in theme.defs:
        print(f'- {d}')
    print()


def handle_ls(args):
    for count, hss in grouped_homonym():
        print(count)
        for h in hss:
            print(f' - {h.word}')
    print()


def handle_stat(args):
    tot = 0
    for count, hss in grouped_homonym():
        hss = list(hss)
        c = len(hss)
        tot += c
        print(f'{c} words has {count} meanings (total words: {tot})')
    print()


###################################################################################################


def main():
    parser = argparse.ArgumentParser(description='Sylt tools')
    sub_parsers = parser.add_subparsers(dest='command_name', title='Commands')

    sub = sub_parsers.add_parser("theme", help="Generate a theme")
    sub.add_argument('--min', metavar='N', type=int, default=0)
    sub.set_defaults(func=handle_theme)

    sub = sub_parsers.add_parser("ls", help="List all words")
    sub.set_defaults(func=handle_ls)

    sub = sub_parsers.add_parser("stat", help="List word stats")
    sub.set_defaults(func=handle_stat)

    args = parser.parse_args()
    args = parser.parse_args()
    if args.command_name is not None:
        args.func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
