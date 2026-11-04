#!/usr/bin/env python3
"""Check all local page/asset links and fragment targets without a web framework."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote

ROOT = Path(__file__).resolve().parents[1]

class Page(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.path, self.links, self.ids = path, [], set()
        self.lang = None
        self.title = False
    def handle_starttag(self, tag, attributes):
        attrs = dict(attributes)
        if 'id' in attrs:
            assert attrs['id'] not in self.ids, f'{self.path}: duplicate id {attrs["id"]}'
            self.ids.add(attrs['id'])
        if tag == 'html': self.lang = attrs.get('lang')
        if tag == 'title': self.title = True
        for name in ['href', 'src']:
            if attrs.get(name): self.links.append(attrs[name])
        if tag == 'img': assert 'alt' in attrs, f'{self.path}: image needs alt text'

pages = {}
for path in ROOT.rglob('*.html'):
    page = Page(path)
    page.feed(path.read_text())
    assert page.lang == 'en-US' and page.title, f'{path}: expected English (US) language and title'
    assert not any('\u4e00' <= c <= '\u9fff' for c in path.read_text()), f'{path}: unexpected Chinese text'
    pages[path.resolve()] = page
for path, page in pages.items():
    for link in page.links:
        url = urlsplit(link)
        if url.scheme or url.netloc: continue
        target = (path.parent / unquote(url.path)).resolve() if url.path else path
        assert target.is_relative_to(ROOT), f'{path}: link escapes site {link}'
        assert target.exists(), f'{path}: missing {link}'
        if url.fragment and target in pages:
            assert unquote(url.fragment) in pages[target].ids, f'{path}: missing fragment {link}'
assert len(pages) == 6, f'Expected three English pages and three legacy English aliases, got {len(pages)}'
print(f'Checked {len(pages)} pages: local links, assets, fragment targets, language and image alt text OK')
