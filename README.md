# SSB Pseudonymization Functions
> Data pseudonymization functions used by Statistics Norway (SSB)

[![PyPi version](https://pypip.in/v/ssb-pseudonymization/badge.png)](https://crate.io/packages/sb-pseudonymization/)
[![PyPi downloads](https://pypip.in/d/ssb-pseudonymization/badge.png)](https://crate.io/packages/sb-pseudonymization/)

Pseudonymization is a data management and de-identification procedure by which personally identifiable information fields within a data record are replaced by one or more artificial identifiers, or pseudonyms. A single pseudonym for each replaced field or collection of replaced fields makes the data record less identifiable while remaining suitable for data analysis and data processing.

It is important to note that pseudonymization is not the same as _anonymization_. While pseudonymization targets directly identifying elements, the real information might still be identifiable e.g. by using inherent information such as correlation between data elements. Thus, senisitive data that has been pseudonomized using the functions in this library should still be regarded as sensitive.


## Installation

```python
pip install ssb-pseudonymization
```

This is a code libary that you import into your existing code, like so:

```python
from ssb_pseudonymization import pseudo_func
```


## Usage example

### Invoking a function

A pseudo function accepts a config dictionary and a value argument to be pseudonymized.

```python
from ssb_pseudonymization.func import fpe

config = {
    'key': 'some-secret-key', 
    'alphabet': string.ascii_letters + ' '
}

p = fpe.apply(config, 'Ken sent me')
# p = 'fMLzJCeVJfP'
```

### Invoking a function in a generic way

To invoke a pseudo function through a pseudo facade in a more generic way, you can do:

```python
from ssb_pseudonymization import pseudo_func
import json

config_json = json.dumps({
    'func': 'fpe',
    'key': 'some-secret-key', 
    'alphabet': string.ascii_letters + ' '
})
p = pseudo_func.invoke(config, "Ken sent me")
# p = 'fMLzJCeVJfP'
```
Notice that the config must be a json string and you must specify
the function in config (`func='...'`).

For more examples and usage, have a look at the tests.


## Development setup

Run `make help` to see common development commands.

```
install-build-tools            Install required tools for build/dev
build                          Build dist
test                           Run tests
release-validate               Validate that a distribution will render properly on PyPI
release-test                   Release a new version, uploading it to PyPI Test
release                        Release a new version, uploading it to PyPI
bump-version-patch             Bump patch version, e.g. 0.0.1 -> 0.0.2
bump-version-minor             Bump minor version, e.g. 0.0.1 -> 0.1.0
```

Refer to the `Makefile` to see details about the different tasks.


## Releasing

*Prerequisites:*
You will need to register accounts on [PyPI](https://pypi.org/account/register/) and [TestPyPI](https://test.pypi.org/account/register/).

Before releasing, make sure you're working on a "new" version number. You can bump the version using the [bumpversion tool](https://medium.com/@williamhayes/versioning-using-bumpversion-4d13c914e9b8).

To release and publish a new version to PyPI:
```sh
make release-validate
```

This will run tests, build distribution packages and perform some rudimentary PyPI compliancy checking.

For a dress rehearsal, you can do a test release to the [TestPyPI index](https://test.pypi.org/). TestPyPI is very useful, as you can try all the steps of publishing a package without any consequences if you mess up. Read more about TestPyPI [here](https://packaging.python.org/guides/using-testpypi/).

```sh
make release-test
```

To perform the actual release, run:
```sh
make release
```

You should see the new release appearing [here](https://pypi.org/project/ssb-pseudonymization) (it might take a couple of minutes for the index to update).


## Release History

* 0.0.1
    * Initial version with "Mickey Mouse" pseudo functions


## Meta

Statistics Norway – https://github.com/statisticsnorway

Distributed under the MIT license. See ``LICENSE`` for more information.

[https://github.com/statisticsnorway/ssb-pseudonymization-py]


## Contributing

1. Fork it (<https://github.com/statisticsnorway/ssb-pseudonymization-py/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request
