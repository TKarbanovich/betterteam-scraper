# betterteam-scraper

## Multilevel web scrapper of the Betterteam web site.

# Prerequisites
Docker should be installed on the machine beforehand.

# Set up:
Build image. 
1) Pull repo.
2) Enter repo directory.
3) From the project directory run:
```bash
$ docker build . -t "scrapy"
```

# Usage:
Run this docker container with the following bash command:
```bash
$ docker  run  -v $(pwd):'/usr/src/app/shared_volume/' scrapy
```
Instead of $(pwd) specify needed folder.



<div id="header" align="center">
  <img src="https://media.giphy.com/media/kH6CqYiquZawmU1HI6/giphy.gif" width="100"/>
</div>
