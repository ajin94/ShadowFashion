#!/usr/bin/env python

bind = "0.0.0.0:9876"

worker_class = 'gevent'
timeout = 300
keepalive = 1
debug = False
tmp_upload_dir ='/tmp'

accesslog = "-"
loglevel = 'warning'
access_log_format = '%(t)s %(h)s %(U)s "%(r)s"  %(s)s %(b)s "%(f)s" "%(a)s" [%(D)s microseconds]'