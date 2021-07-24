import hashlib
import itertools
import string
import time

stri = hashlib.sha256(b'6bGxL')  # An example string.
pas = stri.hexdigest()


def main() -> str:
    start = time.time()
    for digits in range(1, 6):
        print("Trying with... %s digits." % digits)
        for pwd in itertools.product((
            string.ascii_lowercase+string.ascii_uppercase+string.digits)[::-1],
                repeat=digits):
            join_it = ''.join(pwd)  # Join the array.
            byte_it = str.encode(join_it)  # Encode the string into byte form.
            sha_it = hashlib.sha256(byte_it)  # Hash it.
            hex_it = sha_it.hexdigest()
            if hex_it == pas:
                end = time.time()
                print(end - start)
                return join_it
print(main())
