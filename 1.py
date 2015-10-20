#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# 1.py
#
# Copyright 2015 Daria <daria@daria-535U3C>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
table = [
    [0, 2, 3, 4, 5, 6, 7, 8],
    [0, 2, 3, 0, 0, 0, 0, 0],
    [0, 0, 3, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 5, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 7, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
]


class Reader:
    list = ['12223', '1222', '45', '12224', '82', '183', '233333', '188']
    n = 8

    def get(self, i):
        return self.list[i]


class Parse:
    def matchLang(self, table, str):
        global ans
        for i in range(0, len(str) - 1):
            j = 0
            try:
                while table[int(str[i]) - 1][j] != int(str[i + 1]):
                    j += 1
                ans = "Match"
            except IndexError:
                ans = "Doesn't match"
        return ans


def main():
    r = Reader()
    p = Parse()
    for i in range(0, r.n):
        print(p.matchLang(table, r.get(i)))
    return 0


if __name__ == '__main__':
    main()
