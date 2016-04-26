# vim:ft=sh
# Use the official Jenkins docker image as our base image
FROM jenkins:1.609.1
MAINTAINER aussio

# Set the user to root for the following commands since the user is Jenkins by default.
# (because the jenkins base image sets it so)
# Set the user back to jenkins once we're done
USER root
RUN mkdir /var/log/jenkins
RUN chown -R jenkins:jenkins /var/log/jenkins
USER jenkins

ENV JAVA_OPTS="-Xmx8192m"
ENV JENKINS_OPTS="--handlerCountStartup=100 --handlerCountMax=300 --logfile=/var/log/jenkins/jenkins.log"
