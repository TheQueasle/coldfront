# Coldfront - Resource Allocation System

Coldfront is an open source resource allocation system designed to provide a
central portal for administration, reporting, and measuring scientific impact
of HPC resources. Coldfront was created to help HPC centers manage access to a
diverse set of resources across large groups of users and provide a rich set of
extensible meta data for comprehensive reporting. Coldfront is written in
Python and released under the GPLv3 license.

## Features

- Allocation/Subscription based system for managing access to resources
- Collect Project, Grant, and Publication data from users
- Define custom attributes on resources and subscriptions
- Email notifications for expiring/renewing access to resources
- Integration with 3rd party systems for automation and access control
- Center director approval system and annual project reviews

## Contact Information

If you would like a live demo followed by QA, please contact us at
ccr-coldfront-admin-list@listserv.buffalo.edu. You can also contact us for
general inquiries and installation troubleshooting.

If you would like to join our mailing list to receive news and updates, please
send an email to listserv@listserv.buffalo.edu with no subject, and the
following command in the body of the message:

subscribe ccr-open-coldfront-list@listserv.buffalo.edu first_name last_name

## Quick Install

- Coldfront requires Python 3.6, memcached, and redis.

### CentOS (7.5)

Install EPEL then install required packages:

```
sudo yum install epel-release
sudo yum install python36 python36-devel memcached redis
```

For Django 2.2 on CentOS 7.5+, you will also need a newer version of sqlite
installed and available to the user that will run the ColdFront App.

```bash
wget https://www.sqlite.org/2019/sqlite-autoconf-3280000.tar.gz
tar -xvf sqlite-autoconf-3280000.tar.gz
cd sqlite-autoconf-3280000 || exit
./configure
make -j "$(nproc)"
sudo make install
```

Once installed, you will need to add `/usr/local/bin` to `PATH` (if not already
there for the user that will run ColdFront.  You will also need to add
`/usr/local/lib` to `LD_LIBRARY_PATH`

```bash
export PATH=/usr/local/bin:${PATH}
export LD_LIBRARY_PATH=/usr/local/lib:${LD_LIBRARY_PATH}
```

### Ubuntu (16.04)

```bash
sudo add-apt-repository ppa:jonathonf/python-3.6
sudo apt-get update
sudo apt-get install python3.6 python3.6-venv memcached redis-server
```

1. Clone Coldfront in a new directory and create a Python virtual environment
   for Coldfront

```bash
mkdir coldfront_app
cd coldfront_app
git clone https://github.com/ubccr/coldfront.git
python3.6 -mvenv venv
```

1. Activate the virtual environment and install the required Python packages

```bash
source venv/bin/activate
cd coldfront
pip install wheel
pip install -r requirements.txt
```

1. Copy `config/local_settings.py.sample` to `config/local_settings.py`.

```bash
cp config/local_settings.py.sample config/local_settings.py
```

Open `config/local_settings.py` and update the following:

- Update `SECRET_KEY`. Consider making the length at least 50 characters long.
- Update `TIME_ZONE` if necessary
- Uncomment line `EMAIL_ADMIN_LIST`
- Uncomment line `EMAIL_DIRECTOR_EMAIL_ADDRESS`

1. Copy `config/local_strings.py.sample` to `config/local_strings.py` and
   update if desired.

```bash
cp config/local_strings.py.sample config/local_strings.py
```

1. Run initial setup

```bash
python manage.py initial_setup
```

1. Optional: Add some test data

```bash
python manage.py load_test_data
```

1. Start development server

```bash
python manage.py runserver 0.0.0.0:8000
```

1. Point your browser to [http://localhost:8000](http://localhost:8000)

- You can log in as `admin` with password `test1234`.
- You can log in as a PI using username `cgray` with password `test1234`.
- You can log in as another PI using username `sfoster` with password `test1234`.

Password for all users is also `teset1234`.

## Directory structure

- coldfront
  - core - The core Coldfront application
    - field_of_science
    - grant
    - portal
    - project
    - publication
    - resource
    - subscription
    - user
    - utils
  - libs - Helper libraries
    - plugins - Plugins that can be configured in Coldfront
      - freeipa
      - iquota
      - ldap_user_search
      - mokey_oidc
      - slurm
      - system_monitor

## License

Coldfront is released under the GPLv3 license. See the LICENSE file.
