import codecs
import time

def encode(s):
    start_time = time.time()
    if not isinstance(s,str):
        raise TypeError
    origlen = len(s)
    crypted = ""
    digitmapping = dict(zip('1234567890!"#€%&/()=','!"#€%&/()=1234567890'))
    if len(s) > 1000:
        raise ValueError
    for c in s:
        if c.isalpha():
            if c in "äåö":
                raise ValueError
            if c.islower():
                c=c.upper()
            elif c.isupper():
                c=c.lower()
            # Rot13 the character for maximum security
            crypted+=codecs.encode(c,'rot13')
        elif c in digitmapping:
          crypted+=digitmapping[c]
        else:
            raise ValueError
    i = origlen
    while (True):
        current_time = time.time()
        if ((current_time - start_time) > 0.05):
            break
    return crypted

def decode(s):
    return encode(s)



