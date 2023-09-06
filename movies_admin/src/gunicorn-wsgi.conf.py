bind = "0.0.0.0:8000"
workers = 2
wsgi_app = "project.wsgi:application"
worker_class = "gthread"
threads = 4  # valid for gthread

max_requests = 1000
max_requests_jitter = 2
timeout = 30

worker_tmp_dir = "/dev/shm"  # /dev/shm uses the shm filesystem—shared memory, and in-memory filesystem

accesslog = errorlog = "-"  # log to stdout
