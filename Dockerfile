FROM selenium/standalone-chrome:4.7.2-20221219


USER root
RUN sudo mkdir -p etc/opt/chrome/policies/managed/

COPY --chmod=777 auto_select_certificate.json etc/opt/chrome/policies/managed/
COPY --chmod=777 client.core.coregcp.kaymera.com.pfx /home/seluser/client.core.coregcp.kaymera.com.pfx
COPY --chmod=777 init-ca.sh /home/seluser/init-ca.sh
COPY --chmod=777 empty_pass.txt /home/seluser/empty_pass.txt
COPY --chmod=777 ca_pass.txt /home/seluser/ca_pass.txt

RUN sudo update-ca-certificates

RUN apt -qqy update \
    && apt -qqy --no-install-recommends install \
    libnss3-tools \
    libnss3


USER seluser

WORKDIR /home/seluser

RUN ./init-ca.sh

#TODO  -enter password  lient.core.coregcp.kaymera.com
