# qa-baseline

A simple question answering baseline.
It ssings a score to each candidate answer depending on how many times and at which rank the candidate ansers appear in the title and snippet of Bing results.

## Installation

The only requirement is [py-web-search](https://github.com/rohithpr/py-web-search):

```
pip install py-web-search
```

## Usage
```
usage: qa-baseline.py [-h] -q QUESTION -a ANSWERS [ANSWERS ...] [-r RESULTS]
                      [-l LANG]

optional arguments:
  -h, --help            show this help message and exit
  -q QUESTION, --question QUESTION
                        the question you want to ask
  -a ANSWERS [ANSWERS ...], --answers ANSWERS [ANSWERS ...]
                        the candidate answers
  -r RESULTS, --results RESULTS
                        The number of search engine results to consider
  -l LANG, --lang LANG  The language of the question
```

Example:
```
python qa-baseline.py -q "who invented python ?" -a guido carlo -l en -r 30
```

returns:

```
guido - probablity: 0.6645  raw score: 0.6835
carlo - probablity: 0.3355  raw score: 0.0000
```
