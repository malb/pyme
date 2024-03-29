#!/usr/bin/env python
# $Id$
# Copyright (C) 2004,2008 Igor Belyi <belyi@users.sourceforge.net>
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program; if not, write to the Free Software
#    Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

# Sample of key deletion
# It deletes keys for joe@foo.bar generated by genkey.pl script

from pyme import core

core.check_version(None)

# Note that we need to collect all keys out of the iterator return by c.op_keylist_all()
# method before starting to delete them. If you delete a key in the middle of iteration
# c.op_keylist_next() will raise INV_VALUE exception

c = core.Context()
# 0 in keylist means to list not only public but secret keys as well.
for thekey in [x for x in c.op_keylist_all("joe@foo.bar", 0)]:
    # 1 in delete means to delete not only public but secret keys as well.
    c.op_delete(thekey, 1)
