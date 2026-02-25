#!/usr/bin/python3
from hi6toolkit import HTTP_Request as hp, Constant

Constant.MODULE = False

host = "lms.ikiu.ac.ir"
port = 443

req = hp(host, port, None, None, "/login/index.php", True, False, True)
req.request()
print(req.response_header)
