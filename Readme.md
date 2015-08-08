# Instagram Consumer
----
Example created with [Flask](http://flask.pocoo.org/) to consume Instagram API.
[http://instaconsumer.herokuapp.com/](http://instaconsumer.herokuapp.com/)

## How it works:

`/`: Get recents photos of logged user.
```python
# Example
# http://instaconsumer.herokuapp.com/
```
`/<username>`: Get photos searching by username.
```python
# Example
# http://instaconsumer.herokuapp.com/guilhermelouro
```

`/popular`: Get popular photos of Instagram.
```python
# Example
# http://instaconsumer.herokuapp.com/popular
```

`/tag/<tag_name>`: Get photos searching by hashtag.
```python
# Example
# http://instaconsumer.herokuapp.com/tag/python
```

`?text=LoremIpsum`: Change the central text of the page.
```python
# Example
"""
http://instaconsumer.herokuapp.com/?text=LoremIpsum
http://instaconsumer.herokuapp.com/guilhermelouro?text=LoremIpsum
http://instaconsumer.herokuapp.com/popular?text=LoremIpsum
http://instaconsumer.herokuapp.com/tag/python?text=LoremIpsum
"""
```

