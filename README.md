Marmot
======

Getting Started
---------------

- Change directory into your newly created project.

    cd marmot

- Create a Python virtual environment.

    python3 -m venv env

- Upgrade packaging tools.

    env/bin/pip install --upgrade pip setuptools

- Install the project in editable mode with its testing requirements.

    env/bin/pip install -e ".[testing]"

- Configure the database.

    env/bin/initialize_marmot_db development.ini

- Run your project's tests.

    env/bin/pytest

- Run your project.

    env/bin/pserve development.ini


## Design

Primary concepts: resources, representations, types

- A resource is object representing a "named thing"
- A representation is an instance
- A type defines a resource, including its parameters


### Requirements, ideas, scratch notes

* REST resources
* CRUD on resources
* resource linking
* optional linked resource expansion
* bulk requests (SCIM style)
* query string translation to backend query
* schema validation
* revisioning of resources
* logging
* unit tests
* functional tests
* CLI
