import json
import os
from pelican import signals


"""
Creates a folder in your Pelican content folder called "json"
and createa  file called "tags.json"

"""


class Tags(object):

    def __init__(self, generators, *args, **kwargs):
        self.articles = generators.articles
        self.settings = generators.settings

        self.filename = '/tags.json'
        self.contentpath = self.settings.get('PATH')
        self.siteurl = self.settings.get('SITEURL')
        self.output_path = os.path.join(self.contentpath, 'json')
        self.tags_list = []

    def write_json_to_file(self):
        self._ensure_path()
        with open(self.output_path + self.filename, 'w') as f:
            json.dump({"tags": self.tags_list}, f, indent=4)

    def _ensure_path(self):
        if not os.path.exists(self.output_path):
            os.mkdir(self.output_path)

    def generate_output(self):
        for article in self.articles:
            for tag in article.metadata.get('tags'):
                if tag not in self.tags_list:
                    self.tags_list.append(tag.name)
        self.write_json_to_file()


def get_generators(generators):
    output = Tags(generators)
    output.generate_output()


def register():
    signals.article_generator_finalized.connect(get_generators)
