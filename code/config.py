# -*- coding: utf-8 -*-
import hashlib

jwt_secret = "avengers"


def hash_password(_pass):
    _pass = _pass.encode("utf-8")
    return hashlib.sha256(_pass).hexdigest()
