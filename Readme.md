# Instagram Consumer
----
Exemplo feito em Flask para consumir a API do Instagram
[http://instaconsumer.herokuapp.com/](http://instaconsumer.herokuapp.com/)

## Como funciona:

`/`: Fotos recentes do usuário logado.
```python
# Exemplo
# http://instaconsumer.herokuapp.com/
```
`/<username>`: Fotos de determinado usuario
```python
# Exemplo
# http://instaconsumer.herokuapp.com/guilhermelouro
```

`/popular`: Fotos populares do instagram
```python
# Exemplo
# http://instaconsumer.herokuapp.com/popular
```

`/tag/<tag_name>`: Fotos de determinada hastag
```python
# Exemplo
# http://instaconsumer.herokuapp.com/tag/python
```

`?text=LoremIpsum`: Modifica o texto central da página
```python
# Exemplo
"""
http://instaconsumer.herokuapp.com/?text=LoremIpsum
http://instaconsumer.herokuapp.com/guilhermelouro?text=LoremIpsum
http://instaconsumer.herokuapp.com/popular?text=LoremIpsum
http://instaconsumer.herokuapp.com/tag/python?text=LoremIpsum
"""
```

