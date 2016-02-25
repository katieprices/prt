# -*- coding: utf-8 -*-
import click
import requests
import yaml


@click.command()
@click.option('--url', default='', help='base test url')
@click.option('--f', default='', help='test *.yaml file')
def main(url, f):
    file_name = f
    try:
        requests.head(url)
    except requests.exceptions.RequestException as e:
        click.echo('open url %s failed: %r' % (url, e))

    with open(file_name, 'r') as f:
        y = yaml.load(f.read())
        print y['name']


if __name__ == '__main__':
    main()
