PY2NB
=====

Overview
________

PY2NB is a small utility for turning python scripts into Jupyter notebooks and
convert module-level multi-line (triple quoted) string literals into Markdown
cells. It also converts the specialized comment strings (i.e., ``#%%``) that
`Don Jayamanne's Jupyter Extension <https://github.com/DonJayamanne/vscodeJupyter>`_
for `Visual Studio Code <https://code.visualstudio.com/>`_ interprets
as cell breaks/divisions into cell breaks in the returned notebook.

What's New
__________

Release notes in reverse chronological order:

0.0.3 (2017-10-22)
  Improved support for input files with Windows-style CRLF terminators. The
  line terminators of the output now match those of the input.

0.0.2 (2017-10-10)
  Bugfix release.

0.0.1 (2017-10-08)
  Added support for raw notebook cells and a unit test.

0.0.0 (2017-08-24)
  Forked from `sklam/py2nb <https://github.com/sklam/py2nb>`_ and modified to
  support the VS Code Jupyter extension.
