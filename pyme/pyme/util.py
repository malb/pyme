# $Id$
# Copyright (C) 2002 John Goerzen
# <jgoerzen@complete.org>
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

import gpgme
from errors import errorcheck

def process_constants(starttext, dict):
    """Called by the constant libraries to load up the appropriate constants
    from the C library."""
    index = len(starttext)
    for identifier in dir(gpgme):
        if not identifier.startswith(starttext):
            continue
        name = identifier[index:]
        dict[name] = getattr(gpgme, identifier)
        
class GpgmeWrapper:
    """Base class all Pyme wrappers for GPGME functionality.  Not to be
    instantiated directly."""
    def __repr__(self):
        return '<instance of %s.%s with GPG object at %s>' % \
               (__name__, self.__class__.__name__,
                self.wrapped)

    def __str__(self):
        return repr(self)

    def _getctype(self):
        raise NotImplementedException
    
    def __getattr__(self, name):
        """On-the-fly function generation."""
        if name[0] == '_' or self._getnameprepend() == None:
            return None
        name = self._getnameprepend() + name
        if self._errorcheck(name):
            def _funcwrap(*args, **kwargs):
                args = [self.wrapped] + list(args)
                return errorcheck(apply(getattr(gpgme, name), args, kwargs),
                                  "Invocation of " + name)
        else:
            def _funcwrap(*args, **kwargs):
                args = [self.wrapped] + list(args)
                return apply(getattr(gpgme, name), args, kwargs)
            
        return _funcwrap

