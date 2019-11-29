from ssb_pseudonymization.exceptions import PseudoFuncInvalidConfigError
from ssb_pseudonymization.exceptions import PseudoFuncError
from ssb_pseudonymization import pseudo_func
import json
import string
import pytest

def config_json(config_dict):
    return json.dumps(config_dict)


def test_generic_invocation():
    config = config_json({
        'func': 'fpe',
        'key': 'some-secret-key', 
        'alphabet': string.ascii_letters + ' '
    })
    p = pseudo_func.invoke(config, "Ken sent me")
    assert p == 'fMLzJCeVJfP' 


def test_generic_invocation_without_func_param():
    config = config_json({
        'key': 'some-secret-key', 
        'alphabet': string.ascii_letters + ' '
    })
    with pytest.raises(PseudoFuncInvalidConfigError):
        pseudo_func.invoke(config, "whatever")


def test_generic_invocation_using_unknown_func_param():
    config = config_json({
        'func': 'non_existent_func',
        'key': 'some-secret-key', 
        'alphabet': string.ascii_letters + ' '
    })
    with pytest.raises(PseudoFuncError):
        pseudo_func.invoke(config, "whatever")
