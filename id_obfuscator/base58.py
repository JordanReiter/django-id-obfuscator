#!/usr/bin/env python
##
## Copyright 2009 Adriana Lukas & Alec Muffett
##
## Licensed under the Apache License, Version 2.0 (the "License"); you
## may not use this file except in compliance with the License. You
## may obtain a copy of the License at
##
## http://www.apache.org/licenses/LICENSE-2.0
##
## Unless required by applicable law or agreed to in writing, software
## distributed under the License is distributed on an "AS IS" BASIS,
## WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
## implied. See the License for the specific language governing
## permissions and limitations under the License.
##

"""docstring goes here""" # :-)

# spec: http://www.flickr.com/groups/api/discuss/72157616713786392/

from __future__ import print_function

__b58chars = '123456789abcdefghijkmnopqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ'
__b58base = len(__b58chars) # let's not bother hard-coding

def b58encode(value):
    """
    encode integer 'value' as a base58 string; returns string
    """

    encoded = ''
    while value >= __b58base:
        div, mod = divmod(value, __b58base)
        encoded = __b58chars[mod] + encoded # add to left
        value = div
    encoded = __b58chars[value] + encoded # most significant remainder
    return encoded

def b58decode(encoded):
    """
    decodes base58 string 'encoded' to return integer
    """

    value = 0
    column_multiplier = 1;
    for c in encoded[::-1]:
        column = __b58chars.index(c)
        value += column * column_multiplier
        column_multiplier *= __b58base
    return value

if __name__ == '__main__':
    x = b58encode(12345678)
    print(x, '26gWw')
    print(b58decode(x), 12345678)

characters = __b58chars
base = __b58base
