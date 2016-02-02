# -*- coding: utf-8 -*-
import click


@click.command()
@click.option('--url', default='', help='base url')
def main(url):
    click.echo('open url %s' % url)


if __name__ == '__main__':
    main()
