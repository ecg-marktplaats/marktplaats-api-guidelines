from docutils import nodes
from docutils.parsers.rst import Directive
from docutils.parsers.rst.directives.tables import Table
from sphinx.util.compat import make_admonition
from docutils.parsers.rst.directives import unchanged
from docutils import statemachine, nodes, frontend


def get_column_widths(header):
    widths = [0] * len(header)

    for i in range(len(header)):
        if header[i] is not None and len(header[i]) > widths[i]:
            widths[i] = len(header[i])

    return widths

def build_table(columns, rows, colwidth = None, sort_column = -1, target_prefix = 'error'):
    # see parsers/rst/states.py, build_table()
    # it's a mess and so is this
    table = nodes.table()

    # make the header block, I swear it's not my fault it's so convoluted
    tgroup = nodes.tgroup(cols=len(columns))
    table += tgroup

    colwidths = colwidth
    if colwidth == None:
        colwidths = get_column_widths(columns)

    for i in xrange(len(columns)):
        tgroup += nodes.colspec(colwidth=colwidths[i])

    thead = nodes.thead()
    row = nodes.row()
    for i, label in enumerate(columns):
        attributes = {
            'morerows': 0,
            'morecols': 0,
            'stub': False,
            }
        par = nodes.paragraph()
        par.append(nodes.Text(label, label))
        entry = nodes.entry(**attributes)
        entry += par
        row += entry
    thead.append(row)
    tgroup += thead

    tbody = nodes.tbody()
    tgroup += tbody
    # end of header block; whew

    for rowlist in rows:
        row = nodes.row()

        def columns():
            for i, c in enumerate(rowlist):
                par = nodes.paragraph()
                if i == sort_column:
                    targetid = "%s-%s" %(target_prefix, c)
                    targetnode = nodes.target('', '', ids=[targetid])
                    par.append(targetnode)

                if isinstance(c, statemachine.StringList):
                    for line in c:
                        par += nodes.line(line, line)
                elif isinstance(c, nodes.Element):
                    par += c
                else:
                    par += nodes.Text(c, c)
                e = nodes.entry()
                e.append(par)
                yield e

        row.extend(columns())

        tbody.append(row)

    return table
