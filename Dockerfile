FROM base_image
COPY ./install/install_libs.sh /project_name/install/
COPY ./requirements.txt /project_name
WORKDIR /project_name
RUN ./install/install_libs.sh
COPY ./src /project_name/src
COPY ./config/config.yml /project_name/config/
EXPOSE 6000
CMD ["/bin/sh", "-c", "cd /project_name && python ./src/project_name/service/project_name.py"]