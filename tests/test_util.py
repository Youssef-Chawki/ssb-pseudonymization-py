from ssb_pseudonymization.util import validate_func_params
from ssb_pseudonymization.exceptions import PseudoFuncInvalidConfigError
import pytest

def test_validate_func_params():
    config = {
        'param1': 'someval',
        'param2': 42,
        'param3': None
    }
    ## ok
    mandatory = ['param1', 'param2']
    validate_func_params(config, mandatory)

    # not ok
    with pytest.raises(PseudoFuncInvalidConfigError):
        mandatory = ['param1', 'param4']
        validate_func_params(config, mandatory)

    # not ok (since param3 == None)
    with pytest.raises(PseudoFuncInvalidConfigError):
        mandatory = ['param1', 'param2', 'param3']
        validate_func_params(config, mandatory)

