# -*- coding: utf-8 -*-
import click
import requests


@click.command()
@click.option('--url', default='', help='base test url')
def main(url):
    try:
        requests.head(url)
    except:
        click.echo('open url %s faild' % url)


if __name__ == '__main__':
    main()
