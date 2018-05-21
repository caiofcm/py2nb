
'"""\n## Test Default Initial Amount\n\n    A\n    '

#%%
"""Raw
<script>
jQuery(document).ready(function($) {

$(window).load(function(){
$('#preloader').fadeOut('slow',function(){$(this).remove();});
});

});
</script>

<style type="text/css">
div#preloader { position: fixed;
left: 0;
top: 0;
z-index: 999;
width: 100%;
height: 100%;
overflow: visible;
background: #fff url('http://preloaders.net/preloaders/720/Moving%20line.gif') no-repeat center center;
}

</style>

<div id="preloader"></div>
"""

#%%
"""Raw
<script>
function code_toggle() {
if (code_shown){
$('div.input').hide('500');
$('#toggleButton').val('Show Code')
} else {
$('div.input').show('500');
$('#toggleButton').val('Hide Code')
}
code_shown = !code_shown
}

$( document ).ready(function(){
code_shown=false;
$('div.input').hide()
});
</script>
<form action="javascript:code_toggle()"><input type="submit" id="toggleButton" value="Show Code">
</form>
"""

#%%
"""Raw
<style type="text/css">
p.tightontop {
  margin-top: 0px;
  padding-top: 0px;
  width: 100%;
}

img.rescale {
  width: 100%;
  height: auto;
}
</style>

<div class="page-header tightontop">
<div class="row tightontop">
  <div class="col-sm-12 col-md-12 col-lg-12">
  <img class="img-responsive rescale" src="img/masthead.jpg" alt="masthead"></img>
  </div> <!-- /col-sm-12 -->
</div> <!-- /row -->
<div class="row">
  <div class="col-sm-4 col-md-4 col-lg-4">
  <p class="text-left tightontop">
  John Smith, Analyst
  </p>
  </div> <!-- /col-sm-4 -->
  <div class="col-sm-4 col-md-4 col-lg-4">
  <p class="text-center tightontop">
  Example, Inc.
  </p>
  </div> <!-- /col-sm-? -->
  <div class="col-sm-4 col-md-4 col-lg-4">
  <p class="text-right tightontop">
  MMMMMM DD, YYYY
  </p>
  </div> <!-- /col-sm-4 -->
</div> <!-- /row -->
</div> <!-- /page-header -->
"""

#%%
"""
# Sample Script/Notebook
"""

#%%
# from __future__ imports must come at the beginning of the file
from __future__ import absolute_import, print_function, division

#%%
"""
Triple-quoted comments like this one are converted to
[Markdown](https://daringfireball.net/projects/markdown/) cells,
which support basic typography when the _Jupyter notebook_ is rendered. You
can create lists:
1. like
1. this
1. one.
"""

#%%
import os

"""
## A `Hello, World` Function
"""

"""
This is a *hello, world* function.
"""

#%%
def hello(who='World'):
    """ This is a docstring.
    """
    return "Hello, " + who


#%%
"""
I have added some helper functions to round out the conventional structure of
a Python script. This example is trivial, making the helper functions seem
pedantic.
"""

#%%
def main():
    return hello()


#%%
if __name__ == '__main__':
    print(main())

""" With the [Python
Markdown](http://jupyter-contrib-nbextensions.readthedocs.io/en/latest/nbextensions/python-markdown/readme.html)
extension enabled, the combination of VSCode, the Jupyter extension for Code,
and the Jupyter Notebook stack amount to a literate programming
environment for Python. For example, you can write expressions like
`hello('Jim')` in Markdown cells and the notebook will resolve them within the
Python REPL: {{hello('Jim')}}.

Using the Python Markdown extension in this manner comes with two gotchas:
1. If you want the Python expressions within your Markdown cells to be resolved
in, say, the HTML version of your notebook, you must execute and save the
notebook file (`*.ipynb`) before using `nbconvert` to transform the notebook.
1. You must *trust* the notebook (i.e., by clicking `File` -> `Trust Notebook`
within the notebook interface) before the Python Markdown extension will be
able to resolve Python expressions within your Markdown cells.
"""
