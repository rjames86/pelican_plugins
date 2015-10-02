from pelican import signals

from bs4 import BeautifulSoup

import logging
logger = logging.getLogger(__name__)

def wrap(to_wrap, wrap_in):
    contents = to_wrap.replace_with(wrap_in)
    wrap_in.append(contents)

def content_object_init(instance):

    if instance._content is not None:
        content = instance._content
        soup = BeautifulSoup(content)

        if 'img' in content:
            for img in soup('img'):
                if img.get('title'):
                    new_tag = soup.new_tag('figure')
                    new_tag['class'] = 'image'
                    caption = soup.new_tag('figcaption')
                    caption.string = img['title']
                    img.append(caption)
                    wrap(img, new_tag)
        instance._content = soup.decode()

def register():
    signals.content_object_init.connect(content_object_init)