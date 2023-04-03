# py-pdf.github.io
Website py-pdf

## Install requirements
```
$ pip install -r requirements.txt
$ pre-commit install
```

## Launch local server with livereload
```
$ invoke livereload
```

## Adding a Python dependency
1. Edit `requirements.in`
2. Run `pip-compile requirements.in` to generate `requirements.txt`

## Publish
```
$ make github
```
