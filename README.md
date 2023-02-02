# pydra-tasks-ants

[![PyPI - Version][pypi-version]][pypi-project]
[![PyPI - Python Version][pypi-pyversions]][pypi-project]

-----

Pydra tasks for ANTs.

[Pydra][pydra] is a dataflow engine which provides
a set of lightweight abstractions for DAG
construction, manipulation, and distributed execution.

[ANTs][ants] is the Advanced Normalization Tools package.
It computes high-dimensional mappings
to capture the statistics of brain structure and function.

## Installation

```console
pip install pydra-tasks-ants
```

## Development

This project is managed with [Hatch][hatch]:

```console
pipx install hatch
```

To run the test suite:

```console
hatch run test:no-cov
```

To fix linting issues:

```console
hatch run lint:fix
```

## License

`pydra-tasks-fsl` is distributed under the terms of the [Apache License 2.0][license] license.

[pypi-project]: https://pypi.org/project/pydra-tasks-ants
[pypi-version]: https://img.shields.io/pypi/v/pydra-tasks-ants.svg
[pypi-pyversions]: https://img.shields.io/pypi/pyversions/pydra-tasks-ants.svg
[pydra]: https://pydra.readthedocs.io/
[ants]: https://stnava.github.io/ANTs/
[hatch]: https://hatch.pypa.io/
[license]: https://spdx.org/licenses/Apache-2.0.html
