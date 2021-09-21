FROM {{ cookiecutter.keycloak_image }}:{{ cookiecutter.keycloak_tag }} AS keycloak

RUN mkdir /opt/jboss/keycloak/themes/{{ cookiecutter.theme_title }}
COPY ./{{ cookiecutter.theme_title }} /opt/jboss/keycloak/themes/{{ cookiecutter.theme_title }}
