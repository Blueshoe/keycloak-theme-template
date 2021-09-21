# keycloak-theme-template
This is a cookiecutter template for Keycloak custom themes.

---


## Purpose

This template is used to scaffold a custom theme for [Keycloak](https://www.keycloak.org/).

## Installation

Firstly, you will need to install [cookiecutter](https://cookiecutter.readthedocs.io/en/latest/):

```bash
pip install cookiecutter
```

---

## Usage

Create a new project with
```bash
cookiecutter gh:Blueshoe/keycloak-theme-template
```
and answer the questions accordingly.

## What's in

This template creates the entire project layout required for a theme repository. We're usually
building our themes directly into a custom Keycloak container image.
The development setup comprises the following components
- a docker-compose setup for local development:
  - Keycloak image from the requested tag
  - PostgreSQL database
  - a Mock SMTP server to send mails to and get instant feedback about the styles and layout   
- start development with the official _keycloak_ theme as a basis
- a comprehensible documentation how to do things
- a Dockerfile to build and provide the customized image

## Credits
This cookiecutter template is heavily inspired by [keycloak-theme-govuk](https://github.com/UKHomeOffice/keycloak-theme-govuk). Please check out their awesome work.

