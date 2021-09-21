import re
import sys

PROJECT_SLUG_REGEX = "^[a-z0-9]([-a-z0-9]*[a-z0-9])?(\.[a-z0-9]([-a-z0-9]*[a-z0-9])?)*$"
project_slug = '{{ cookiecutter.project_slug }}'

if not re.match(PROJECT_SLUG_REGEX, project_slug):
    print(f"ERROR: {project_slug} is not a valid project slug. It must resemble a valid domain name.")
    # exits with status 1 to indicate failure
    sys.exit(1)

