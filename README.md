# Netflix VFX Naming

A Python module supporting VFX naming, following the Netflix Partner recommendations for Shot and Version naming.

<https://partnerhelp.netflixstudios.com/hc/en-us/articles/360057627473-VFX-Shot-and-Version-Naming-Recommendations>

<https://partnerhelp.netflixstudios.com/hc/en-us/articles/360055781274-VFX-Plate-Naming-Best-Practices>

<https://partnerhelp.netflixstudios.com/hc/en-us/articles/360000611467-VFX-Best-Practices>

## Initial Setup

Clone this repository to your development directory.

Then, in the cloned repository:

```bash
# Create and activate virtual environment
uv venv  # if using Astral's uv utility
# or
python3.9 -m venv .venv  # standard python

source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install development and notebook dependencies
uv pip install -e ".[dev, notebook]"  # if using Astral's uv utility
# or
python -m pip install -e ".[dev, notebook]"  # standard python

# Install pre-commit hooks
pre-commit install
```

### Examples

You can run the examples:

```bash
# Run tests
pytest

# Code Coverage
pytest --cov=netflix_vfx_naming tests

# Coverage Report
pytest --cov=netflix_vfx_naming tests --cov-report=html

# Try the example scripts
python scripts/example_shot_usage.py
python scripts/example_show_usage.py

# Try the Jupyter notebook
jupyter notebook

# In the Jupyter interface that opens, open the "shot_examples" notebook and step through it.
```

### Source Layout

```bash
netflix-vfx-naming/
├── src/                     # Main package directory
│   └── netflix_vfx_naming/  # Your source code goes here
├── tests/                   # Test directory
├── bin/                     # Command-line utilities (if provided)
├── docs/                    # Documentation
├── scripts/                 # Utility scripts
└── notebooks/               # Jupyter notebooks
```

## Development Workflow

1. Create feature branch
2. Make changes
3. Run tests: `pytest`
4. Run pre-commit: `pre-commit run --all-files`
5. Commit and push
6. Create pull request

See the [DEVELOPMENT](./DEVELOPMENT.md) file for more specifics.

## Contributing

Contributions to improve this module are welcome! Please submit issues and pull requests on GitHub.

## License

This module is MIT licensed. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

This module used [Marc Goodner's](https://github.com/robotdad) [python-template](https://github.com/robotdad/python-template) as the starting template.
