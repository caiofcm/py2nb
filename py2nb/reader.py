from __future__ import absolute_import, division, print_function

import re
import sys
from collections import namedtuple
import tokenize

if sys.version_info[0] == 2:
    TokenInfo = namedtuple('TokenInfo', 'type string start end line')

    def _generate_tokens(readline):
        return map(lambda x: TokenInfo(*x), tokenize.generate_tokens(readline))

else:
    TokenInfo = tokenize.TokenInfo
    _generate_tokens = tokenize.tokenize


def read(filename):
    """
    Read a regular Python file with special formatting and performance
    preprocessing on it.  The result is a string that conforms to the IPython
    notebook version 3 python script format.
    """
    with open(filename, 'rb') as fin:
        token_gen = _generate_tokens(fin.readline)
        cvt_docstr_gen = convert_toplevel_docstring(token_gen)
        nl_gen = fix_newlines(cvt_docstr_gen)
        out = list(nl_gen)

    formatted = tokenize.untokenize(out).decode('utf-8')
    return fix_empty_lines(formatted)


# =============================================================================
#                                   Helpers
# =============================================================================
linetermdct = {
    '\r\n': re.compile(r'\r\n')
    , '\r': re.compile(r'\r(?!\n)')
    , '\n': re.compile(r'(?<!\r)\n')
}

def lineterm(text, dct=linetermdct):
    """Return a string representation of the line term style of the input text.
    """
    for style, regex in dct.items():
        if re.search(regex, text):
            return style
    return '\n'


def convert_toplevel_docstring(tokens):
    for token in tokens:
        # For each string
        if token.type == tokenize.STRING:
            text = token.string
            # Must be a docstring
            if text.startswith('"""') or text.startswith("'''") or text.startswith('\'"""'):
                text = text.replace('\\n', '\n') #For the fake docstring
                rawre = re.compile(r'([\"\']{3})Raw\r?\n')
                text, rawsub = re.subn(rawre, r'\1', text, count=1)
                term = lineterm(text)
                startline, startcol = token.start
                # Starting column MUST be 0
                if startcol == 0:
                    endline, endcol = token.end
                    lines = ['# ' + line
                             for line in text.strip('"\' ' + term).splitlines()]
                    text = term.join(lines)
                    if rawsub:
                        fmtstr = '# <rawcell>' + term + '{0}' + term + \
                                 '# <codecell>'
                        fmt = fmtstr.format(text)
                    else:
                        fmtstr = '# <markdowncell>' + term + '{0}' + term + \
                                 '# <codecell>'
                        fmt = fmtstr.format(text)
                    yield TokenInfo(type=tokenize.COMMENT,
                                    start=(startline, startcol),
                                    end=(endline, endcol),
                                    string=fmt,
                                    line='#')
                    # To next token
                    continue
        # For special comments
        elif token.type == tokenize.COMMENT:
            # Convert special comment marks to cell boundaries.
            if token.string.startswith('#%%'):
                startline, startcol = token.start
                # Starting column MUST be 0
                if startcol == 0:
                    endline, endcol = token.end
                    fmt = '# <codecell>\n'
                    yield TokenInfo(type=tokenize.COMMENT,
                                    start=(startline, startcol),
                                    end=(endline, endcol),
                                    string=fmt,
                                    line='#')
                    # To next token
                    continue
        # Return untouched
        yield token



def fix_newlines(tokens):
    first = True
    curline = 1
    for token in tokens:
        if first:
            first = False
            curline = token.end[0] + 1
        else:
            # Fill NEWLINE token in between
            while curline < token.start[0]:
                yield TokenInfo(type=tokenize.NEWLINE,
                                string='\n',
                                start=(curline, 0),
                                end=(curline, 0),
                                line='\n', )
                curline += 1

            curline = token.end[0] + 1
        yield token


def fix_empty_lines(text):
    def gen():
        for line in text.splitlines():
            if not line.strip():
                # Empty line
                yield ''
            else:
                yield line

    return '\n'.join(gen())
