#! /usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'Raúl Jornet Calomarde'
__contact__ = 'rjornetc@openmailbox.org'
__copyright__ = 'Copyright © 2015, Raúl Jornet Calomarde'
__license__ = '''License GPLv3+: GNU GPL version 3 or any later
This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or any later version. This program
is distributed  in the hope that it will be useful, but WITHOUT ANY WARRANTY;
without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR
PURPOSE. See the GNU General Public License for more details.
<http://www.gnu.org/licenses/>'''
__date__ = '2015-08-09'
__version__ = '1.0'

import decimal

def compress(string, char_table):
    i = 0
    int_string = 0
    base = len(char_table) + 1
    for character in string:
        int_string += (char_table.index(character) + 1) * (base ** i)
        i += 1
    return int_string


def decompress(int_string, char_table):
    int_string = decimal.Decimal(int_string)
    string = ''
    base = decimal.Decimal(len(char_table) + 1)
    while int_string >= 1:
        finished = False
        while not finished:
            try:
                string += char_table[int(int_string % base - 1)]
                finished = True
            except:
                decimal.getcontext().prec += 1
        int_string = int_string / base
    return string
