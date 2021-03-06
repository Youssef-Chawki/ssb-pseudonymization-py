# SSB Pseudonymization Functions
> Data pseudonymization functions used by Statistics Norway (SSB)

[![PyPI version](https://img.shields.io/pypi/v/ssb-pseudonymization.svg)](https://pypi.python.org/pypi/ssb-pseudonymization/)
[![Status](https://img.shields.io/pypi/status/ssb-pseudonymization.svg)](https://pypi.python.org/pypi/ssb-pseudonymization/)
[![License](https://img.shields.io/pypi/l/ssb-pseudonymization.svg)](https://pypi.python.org/pypi/ssb-pseudonymization/)


Pseudonymization is a data management and de-identification procedure by which personally identifiable information fields within a data record are replaced by one or more artificial identifiers, or pseudonyms. A single pseudonym for each replaced field or collection of replaced fields makes the data record less identifiable while remaining suitable for data analysis and data processing.

This lib contains functions that can be used to implement data pseudonymization. In SSB we're invoking these
functions within our Spark data management platform, by wrapping the lib as [UDFs](https://jaceklaskowski.gitbooks.io/mastering-spark-sql/spark-sql-udfs.html).

It is important to note that pseudonymization is not the same as _anonymization_. While pseudonymization targets directly identifying elements, the real information might still be identifiable e.g. by using inherent information such as correlation between data elements. Thus, sensitive data that has been pseudonomized using the functions in this library should still be regarded as sensitive.

The library is currently in a "pre-alpha" stage. We're currently experimenting with the architecture
related to how and when psedonymization is being applied in our data management platform. Also, currently there are only a few and simplistic functions in this library. Breaking changes should be expected.


## Installation

```python
pip install ssb-pseudonymization
```


## Usage example

### Invoking a function

A pseudo function accepts a config dictionary and a value argument to be pseudonymized.

```python
from ssb_pseudonymization.func import fpe

func_config = {
    'key': 'some-secret-key', 
    'alphabet': string.ascii_letters + ' '
}

p = fpe.apply(func_config, 'Ken sent me')
# p = 'fMLzJCeVJfP'
```

### Invoking a function in a generic way

To invoke a pseudo function in a more generic way, you can use the `pseudo_func` facade:

```python
from ssb_pseudonymization import pseudo_func

func_config_json = json.dumps({
    'func': 'fpe',
    'key': 'some-secret-key', 
    'alphabet': string.ascii_letters + ' '
})
p = pseudo_func.invoke(func_config_json, "Ken sent me")
# p = 'fMLzJCeVJfP'
```
Notice that the config must be a json string and you must specify
the function in config (`func='...'`).

For more examples and usage, have a look at the [tests](https://github.com/statisticsnorway/ssb-pseudonymization-py/tree/master/tests).


## Development setup

Run `make help` to see common development commands.

```
install-build-tools            Install required tools for build/dev
build                          Build dist
test                           Run tests
clean                          Clean all build artifacts
release-validate               Validate that a distribution will render properly on PyPI
release-test                   Release a new version, uploading it to PyPI Test
release                        Release a new version, uploading it to PyPI
bump-version-patch             Bump patch version, e.g. 0.0.1 -> 0.0.2
bump-version-minor             Bump minor version, e.g. 0.0.1 -> 0.1.0
```

Refer to the `Makefile` to see details about the different tasks.


### Testing

Run tests for all python distributions using
```sh
make test
```

This will require that your dev machine has the required python distributions installed locally.
(You can install python distributions using [pyenv](https://realpython.com/intro-to-pyenv/).)


## Releasing

*Prerequisites:*
You will need to register accounts on [PyPI](https://pypi.org/account/register/) and [TestPyPI](https://test.pypi.org/account/register/).

Before releasing, make sure you're working on a "new" version number. You can bump the version using the [bumpversion tool](https://medium.com/@williamhayes/versioning-using-bumpversion-4d13c914e9b8).

Also, make sure to update release notes.

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
* 0.0.2
    * Improve docs


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
