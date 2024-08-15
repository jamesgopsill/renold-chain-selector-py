# A python client for the Renold Chain Selector

A python wrapper that provides a wrapper around the awesome [Renold Chain Selector](https://www.renoldchainselector.com/ChainSelector). We hope this will help individuals in integrating the selctor into their design workflows. We use it within our courses to teach our students about design automation.

## Contents

- [Getting Started](#getting-started)
- [Contributing](#contributing)
- [Documentation](#documentation)
- [Formatting](#formatting)
- [Testing](#testing)

## Getting started

I haven't put the package on pypi just yet so installing the package requires installing it from the [repo](https://stackoverflow.com/questions/15268953/how-to-install-python-package-from-github).

```
> pip install git+https://github.com/jamesgopsill/renold-chain-selector-py.git#egg=gtr
```

You can then use it in your python code like so:

```python
from renold import (
    get_chain_options,
    ChainCriteria,
    ProductRange,
    Standard,
    ChainOptionsResponse,
)

criteria: ChainCriteria = {
    "power_value_type": "InputPower",
    "power_value": 10,
    "speed_value_type": "InputSpeed",
    "speed_value": 1_000,
    "start_speed": 1,
    "finish_speed": 1000,
    "speed_increment": 10,
    "target_working_life": 15_000,
    "working_life_tolerance": 100,
    "driving_sprocket_teeth": 19,
    "driven_sprocket_teeth": 19,
    "centre_distance_rounding_mode": "EvenNumberOfLinks",
    "centre_distance": 900,
    "number_of_links": 0,
    "user_supplied_number_of_links": False,
    "driving_machine_characteristics": "SlightShocks",
    "driven_machine_characteristics": "ModerateShocks",
    "lubrication_regime": "Insufficient",
    "environment_condition": "Normal",
    "environment_domain": "Indoor",
    "product_range_id": ProductRange.SYNERGY,
    "chain_standard_id": Standard.BRITISH,
    "unit": "Metric",
}

r = get_chain_options(criteria)
if r.ok:
    data: ChainOptionsResponse = r.json()
    pprint(data)
```

The are more examples in the `examples` folder if you want to learn more about what the tool can do. The docs also provide an overview of all the functions one can call.

## Contributing

I would recommend creating a virtual environment for development work.

```
python -m venv .venv
```

Then activate it using.

```
[Mac/Linux]
> source .venv/bin/activate
[Windows]
> .venv/Scripts/activate
```

Then install the development requirements.

```
> pip install -r requirements_dev.txt
```

And then install the package within your local virtual dev environment.

```
> pip install -e .
```

## Documentation

Documentation is generated using [pdoc](https://pdoc.dev/):

```
> pdoc ./src/renold
```

```
> pdoc ./src/renold -o ./docs
```

## Formatting

And we format the code using [black](https://github.com/psf/black).

```
black src/
```

## Testing

Testing uses [unittest](https://docs.python.org/3/library/unittest.html).

```
python -m unittest -v
```