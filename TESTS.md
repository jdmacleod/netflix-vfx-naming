# Tests

## Running Tests

```bash
pytest

# display test files with progress
pytest -v

# display individual tests with progress
pytest -vv
```

### Test Coverage

```bash
pytest --cov=netflix_vfx_naming tests

pytest --cov=netflix_vfx_naming tests --cov-report=html
```

## References

<https://enterprisecraftsmanship.com/posts/you-naming-tests-wrong/>

<https://osherove.com/blog/2005/4/3/naming-standards-for-unit-tests.html>
