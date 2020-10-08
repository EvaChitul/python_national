import time

def timeme(fnc):
    print('Decorating {} ...'.format(fnc))

    def get_timing(*args):

        fnc_args = ', '.join(repr(arg) for arg in args)
        fnc_name = fnc.__name__

        start_timing = time.perf_counter()
        result = fnc(*args)
        fnc_run_time = time.perf_counter() - start_timing

        print("Running {} with args: {}, took {}".format(
            fnc_name, fnc_args, fnc_run_time))

        return result

    return get_timing


from timeme import timeme

@timeme
def sleep(seconds):
    print('sleep has been called with {}s: '.format(
        seconds))

    time.sleep(seconds)


@timeme
def factorial(n):
    print('factorial has been called with n: {}'.format(n))

    if n < 2:
        return 1
    else:
        return n * factorial(n-1)


sleep(3)
factorial(6)
