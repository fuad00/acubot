FROM secfa/docker-awvs
COPY awvs_starter.sh /awvs_starter.sh
COPY change_credentials.sh /home/acunetix/.acunetix/change_credentials.sh
RUN chmod +x /awvs_starter.sh
RUN chmod +x /home/acunetix/.acunetix/change_credentials.sh
ENTRYPOINT ["/awvs_starter.sh"]
