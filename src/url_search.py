#!/usr/bin/python

from Alfred import Items, Tools
from MyNotes import Search

query = Tools.getArgv(1)
bookmark_tag = '#' + Tools.getEnv('bookmark_tag')

search_terms = [bookmark_tag, query] if query else [bookmark_tag]

notes = Search()
matches = notes.url_search(search_terms)

alf = Items()
if matches:
    for m in matches:
        note_title = m['title']
        note_path = m['path']
        links = m['links']
        for l in links:
            url_title = l['url_title']
            url = l['url']
            # subtitle = '%s > %s' % (url_title, url) if url_title != url else url
            subtitle = 'NOTE: {0} URL: {1}...'.format(note_title, url[:30])
            alf.setItem(
                title=url_title,
                subtitle=subtitle,
                arg=url,
                quicklookurl=url
            )
            alf.addMod(
                'cmd',
                note_path,
                'Open MD Note',
                icon_path='icons/markdown.png',
                icon_type='image'
            )
            alf.addMod(
                'alt',
                url,
                "Copy URL to Clipboard",
                icon_path='icons/clipboard.png',
                icon_type='image'
            )
            alf.addModsToItem()
            alf.addItem()
else:
    alf.setItem(
        title='No Bookmarks found...',
        subtitle='try again',
        valid=False
    )
    alf.addItem()
alf.write()
