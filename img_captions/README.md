# Image Captions for Pelican

If an image has a title tag, the `<img>` tag will be wrapped in a `<figure>` tag and include a `<figcaption>`

    [Alt Text][My Image]
    
    [My Image]: {filename}/images/my_image.jpg "My Caption Here"
    

Results in 
```
<figure class="image">
    <img alt="My Image" src="www.mysite.com/images/my_image.jpg" title="My Caption Here">
    <figcaption>My Caption Here</figcaption>
</figure>
```
  
  
