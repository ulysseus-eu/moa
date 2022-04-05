FROM phusion/passenger-customizable

#   Python support.
RUN /pd_build/python.sh

# Install dependencies
RUN apt update && apt install -y \
    python-dev python3-dev build-essential git tini python3-pip nano

RUN pip3 install pipenv

USER app
WORKDIR /home/app
RUN git clone https://gitlab.com/fedstoa/moa.git
WORKDIR /home/app/moa
RUN PIPENV_VENV_IN_PROJECT=1 pipenv install --python `which python3`
RUN cp /home/app/moa/config.py.sample /home/app/moa/config.py

USER root
# Let nginx service run
RUN rm -f /etc/service/nginx/down
# Remove default configuration for nginx
RUN rm /etc/nginx/sites-enabled/default

# Create DB:
RUN mkdir -p /etc/my_init.d
ADD create_db.sh /etc/my_init.d/create_db.sh

# Have worker rune every 5 seconds
RUN mkdir /etc/service/moa_worker
ADD run_worker.sh /etc/service/moa_worker/run

# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*