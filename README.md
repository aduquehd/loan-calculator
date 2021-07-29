# Loan Payment Calculator

## Description

It's built on Python 3.7 and implemented on Docker, so it's very easy to use.

When you run the application (see docker command bellow) you just need to write the input values that the application
will ask. Those parameters will be validated, and you can see any errors possible.

Every method involved in the behavior of the Loan Payment Calculator application has a unit test with a high coverage
percentage.

The methods are very simple, following the single responsibility principle.

## Application structure

The distribution of the application is this:

The src directory contains all the application files, split by handlers; the handlers are split by common
functionalities.

The test directory contains all the tests split by functionality (handlers).

- src/
    - handlers/
    - loan_calculator.py
- test/
    - loan_calculator/
        - handlers/
        - utils/

## Running the application & Unit Tests

### Build the docker image

`docker build -t loan_calculator .`

### Run Unit Tests

`docker run -it loan_calculator /bin/bash -c "python -m pytest"`

# Execute the loan calculator

`docker run -i loan_calculator`
