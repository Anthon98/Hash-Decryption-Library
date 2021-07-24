import hashlib
import itertools
import string
import time
import logging

logging.getLogger().setLevel(logging.INFO)

stri = hashlib.sha256(b'6bG')  # An example string.
pas = stri.hexdigest()

def main() -> str:
    start = time.time()
    for digits in range(1, 6):
        logging.info("Trying with... %s digits." % digits)
        for pwd in itertools.product((
            string.ascii_lowercase+string.ascii_uppercase+string.digits)[::-1],
                repeat=digits):
            join_it = ''.join(pwd)  # Join the array.
            byte_it = str.encode(join_it)  # Encode the string into byte form.
            sha_it = hashlib.sha256(byte_it)  # Hash it.
            hex_it = sha_it.hexdigest()
            if hex_it == pas:
                end = time.time()
                logging.info(end - start)
                return join_it

if __name__ == '__main__':
    logging.info(main())