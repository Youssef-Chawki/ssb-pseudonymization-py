from ssb_pseudonymization.func import fpe
import string

def test_fpe():
    config = {
        'key': 'some-secret-key', 
        'alphabet': string.ascii_letters + ' '
    }

    p = fpe.apply(config, 'Ken sent me')
    assert p == 'fMLzJCeVJfP' 

