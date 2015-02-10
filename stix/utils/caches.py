# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import weakref
import collections

class Cachable(object):
    __instance_cache = collections.defaultdict(weakref.WeakValueDictionary)

    @classmethod
    def lookup(cls, id):
        return Cachable.__instance_cache[cls][id]

    def _cache_put(self, object=None, id=None):
        object = object or self
        id  = id or object.id_

        if not id:
            raise ValueError("Cachable item must have an id")

        Cachable.__instance_cache[object.__class__][id] = object


