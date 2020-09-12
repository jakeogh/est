#!/usr/bin/env python3

# pylint: disable=C0111     # docstrings are always outdated and wrong
# pylint: disable=W0511     # todo is encouraged
# pylint: disable=C0301     # line too long
# pylint: disable=R0902     # too many instance attributes
# pylint: disable=C0302     # too many lines in module
# pylint: disable=C0103     # single letter var names, func name too descriptive
# pylint: disable=R0911     # too many return statements
# pylint: disable=R0912     # too many branches
# pylint: disable=R0915     # too many statements
# pylint: disable=R0913     # too many arguments
# pylint: disable=R1702     # too many nested blocks
# pylint: disable=R0914     # too many local variables
# pylint: disable=R0903     # too few public methods
# pylint: disable=E1101     # no member for base
# pylint: disable=W0201     # attribute defined outside __init__
## pylint: disable=W0703     # catching too general exception

import os
import sys
from math import inf
import click
from icecream import ic
from kcl.inputops import enumerate_input


ic.configureOutput(includeContext=True)
# import IPython; IPython.embed()
# import pdb; pdb.set_trace()
# from pudb import set_trace; set_trace(paused=False)

global APP_NAME
APP_NAME = 'est'


# DONT CHANGE FUNC NAME
@click.command()
@click.argument("xest", type=str, nargs=1)
@click.argument("items", type=str, nargs=-1)
@click.option('--verbose', is_flag=True)
@click.option('--debug', is_flag=True)
@click.option('--ipython', is_flag=True)
@click.option('--count', type=str)
@click.option("--null", is_flag=True)
#@click.group()
def cli(xest,
        items,
        verbose,
        debug,
        ipython,
        count,
        null):

    if verbose:
        ic(sys.stdout.isatty())

    assert xest in ['long', 'short']
    long = False
    if xest == 'long':
        long = True

    if not items:
        ic('waiting for input')

    shortest = inf
    longest = 0
    for index, item in enumerate_input(iterator=items,
                                       null=null,
                                       debug=debug,
                                       verbose=verbose):
        if verbose:
            ic(index, item)
        if count:
            if count > (index + 1):
                ic(count)
                sys.exit(0)

        ilen = len(item)
        if ilen < len(shortest):
            shortest = item
            if verbose:
                ic(longest)

        if ilen > len(longest):
            longest = item
            if verbose:
                ic(longest)

        if ipython:
            import IPython; IPython.embed()

    if long:
        print(longest)
    else:
        print(shortest)
