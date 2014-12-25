# My Pelican Plugins #

These are the [Pelican][pelican] plugins that I've written for my blogs.

## Latest URL ##

Creates a JSON file  `<content_path>/json/latest_url.json`

*Note:* You will need to add the 'json' folder to your static paths. See [here][staticpath] under `STATIC_PATHS` for more info.

```JSON
{
	"url": "full url to post",
	"title": "Title of the post"
}
```

## Tags List ##

Creates a JSON file  `<content path>/json/tags.json` 

*Note:* You will need to add the 'json' folder to your static paths. See [here][staticpath] under `STATIC_PATHS` for more info.

```JSON
{
	"tags": [
		"list",
		"of",
		"tags"
	]
}
```

[pelican]: http://blog.getpelican.com
[staticpath]: http://docs.getpelican.com/en/3.5.0/settings.html
