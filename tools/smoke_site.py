#!/usr/bin/env python3
"""Load the production site over HTTP and assert its routes and local assets."""
from http.client import HTTPConnection


def get(path):
    connection = HTTPConnection('127.0.0.1', 4321, timeout=10)
    try:
        connection.request('GET', path)
        response = connection.getresponse()
        if response.status != 200:
            raise SystemExit(f'{path}: HTTP {response.status}')
        content = response.read().decode('utf-8')
        if not content.strip():
            raise SystemExit(f'{path}: empty response')
        return content
    finally:
        connection.close()


home = get('/')
for text in ['Container Registry', 'Docker containers for the media server enthusiast', 'web.edb.fi']:
    if text not in home:
        raise SystemExit('Home page missing ' + text)
for name in ['base-image', 'caddy', 'obzorarr', 'otpravkarr', 'qbittorrent', 'qflood', 'sabnzbd', 'zondarr']:
    path = f'/containers/{name}/'
    page = get(path)
    if f'https://web.edb.fi{path}' not in page or 'ghcr.io/edbfi/' + name not in page:
        raise SystemExit('Incorrect served container page: ' + name)
for asset in ['/img/edbfi.svg', '/javascripts/tagcopy.js', '/javascripts/tablesort.js', '/stylesheets/extra-custom.css']:
    get(asset)
print('Served home, eight container routes and application assets passed semantic HTTP assertions')
