import os
import json
from pelican import signals

"""
Creates a folder in your Pelican content folder called "json"
and createa  file called "latest_url.json" that looks like

    {
        'url': full url of post
        'title': Title of post
    }


"""


class GetLatestPost(object):

    def __init__(self, generators, *args, **kwargs):
        self.articles = generators.articles
        self.settings = generators.settings

        self.contentpath = self.settings.get('PATH')
        self.siteurl = self.settings.get('SITEURL')
        self.output_path = os.path.join(self.contentpath, 'json')
        self.latest_post = self.articles[0]
        self.latest_url = self._get_latest_post()
        self.to_json = {}

    def write_json_to_file(self):
        self._ensure_path()
        with open(self.output_path + '/latest_url.json', 'w') as f:
            json.dump(self.to_json, f, indent=4)

    def _ensure_path(self):
        if not os.path.exists(self.output_path):
            os.mkdir(self.output_path)

    def _get_latest_post(self):
        return self.latest_post.url

    def generate_output(self):
        self.to_json = dict(
            url="%s/%s/" % (self.siteurl, self.latest_url),
            title=self.latest_post.metadata.get('title')
        )
        self.write_json_to_file()


def get_generators(generators):
    output = GetLatestPost(generators)
    output.generate_output()


def register():
    signals.article_generator_finalized.connect(get_generators)
