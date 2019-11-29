from ssb_pseudonymization.func import lookuptable

def test_lookuptable():
    config = {
        'table': ['foo', 'bar', 'baz']
    }

    p = lookuptable.apply(config, 'Something')
    assert p == 'bar' 

