# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from fastapi_gh.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from fastapi_gh.model.http_validation_error import HTTPValidationError
from fastapi_gh.model.validation_error import ValidationError
