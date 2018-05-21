# PY2NB: Python To Notebook Converter

This is a small utility for turning python scripts into Jupyter notebooks and
convert module-level multi-line (triple quoted) string literals into Markdown
cells. It also converts the specialized comment strings (i.e., `#%%`) that
[Don Jayamanne's Jupyter Extension](https://github.com/DonJayamanne/vscodeJupyter)
for [Visual Studio Code](https://code.visualstudio.com/) interprets
as cell breaks/divisions into cell breaks in the returned notebook.

- Single modification from blueogive/py2nb fork is to allow my __fake docstring__ obtained from the ast to source converter

## Why?

I wanted a tool to create user examples that can be executed as normal python
scripts so that they can be copy-and-pasted easily and can be rendered as
notebook for better readability (e.g., nice styling, results embedded).

Also,

* Notebooks are nice to look at but slow to write; and
* They do not play well with version control.


## Install

Install using `pip`:

```bash
pip install git+https://github.com/caiofcm/py2nb.git
```

Alternatively, you can create a local clone of this repository and install
from it:

```bash
git clone https://github.com/caiofcm/py2nb.git
pip install py2nb/
```

## Usage


To convert a python script into a notebook:

```bash

python -m py2nb input.py output.ipynb
```

## Samples

See `tests` directory.

## How It Works

Uses python ``tokenize`` (builtin tokenizer library) for tokenization. String
literals with triple quote at column zero are converted into a comment token
with special ``<markdowncell>``, ``<rawcell>`` and ``<codecell>`` to feed into
the Python importer in IPython version 3. The processed tokens are untokenized
using the ``tokenize`` module so that untouched line looks exactly the same as
the input.

The beginning of a Python code cells may be denoted with a comment string
like this:

```python
#%%
```

Triple-quoted comments are converted to Markdown cells:

```python
"""
This comment will be converted to a Markdown cell.
"""
```

However, if the triple-quoted comment begins with the word `Raw`, the
comment will be converted to a raw notebook cell:

```python
"""Raw
// This Javascript will be placed into a Raw cell in the output notebook.
<script>
jQuery(document).ready(function($) {

$(window).load(function(){
$('#preloader').fadeOut('slow',function(){$(this).remove();});
});

});
</script>
"""
```
