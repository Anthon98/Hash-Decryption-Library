import multiprocessing as mp
import itertools
import hashlib
import logging
import string
import time

from random import randint

logging.getLogger().setLevel(logging.INFO)

stri = hashlib.sha256(b'6bGa')  # An example string.
pas = stri.hexdigest()


# Shuffle our text due to how itertools nest loops it through.
def string_shuffle(s) -> str:
    len_s = len(s)
    s_list = list(s)
    for i in range(0, len_s - 1):
        rpos = randint(i + 1, len_s - 1)
        s_list[rpos], s_list[i] = s_list[i], s_list[rpos]
    shuffled = ""
    for i in range(len_s):
        shuffled = shuffled + s_list[i]
    return shuffled


def main(rng) -> str:
    start = time.time()
    for digits in range(1, 6):
        for pwd in itertools.product(string_shuffle(
            string.ascii_lowercase+string.ascii_uppercase+string.digits)[::-1],
                repeat=digits):
            join_it = ''.join(pwd)  # Join the array.
            byte_it = str.encode(join_it)  # Encode the string into byte form.
            sha_it = hashlib.sha256(byte_it)  # Hash it.
            hex_it = sha_it.hexdigest()
            # End task after N seconds. No pool stopper yet.
            if time.perf_counter() >= 10:
                return
            if hex_it == pas:
                end = time.time()
                logging.info("%s took %s sec." % (join_it, end - start))
                return join_it


if __name__ == '__main__':
    p = mp.Pool()
    a = p.map(main, range(12))  # Assuming your CPU is strong enough.
    finish = time.perf_counter()
    print("Finished running after %s seconds" % finish)
