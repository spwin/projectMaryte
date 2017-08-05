import multiprocessing

bind = "unix:/var/run/sockets/app.sock"
workers = multiprocessing.cpu_count() * 2 + 1
threads = multiprocessing.cpu_count() * 2 + 1
