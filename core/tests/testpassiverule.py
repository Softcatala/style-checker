# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 Jordi Mas i Hernandez <jmas@softcatala.org>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place - Suite 330,
# Boston, MA 02111-1307, USA.

import unittest
from passiverule import PassiveRule
from document import Document

class TestPassiveRule(unittest.TestCase):


    def test_non_passive_sentence(self):
        doc = Document('No serà prou ràpid')
        rule = PassiveRule()
        matches = rule.check(doc.get_paragraphs()[0])
        self.assertEquals(0, len(matches))

    def test_passive_sentence(self):
        doc = Document('No va ser robat per en Joan')
        rule = PassiveRule()
        matches = rule.check(doc.get_paragraphs()[0])
        self.assertEquals(1, len(matches))


if __name__ == '__main__':
    unittest.main()
