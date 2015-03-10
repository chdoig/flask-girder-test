# Installation

- Install [conda](http://conda.pydata.org/):

```
wget http://bit.ly/miniconda
bash Miniconda-latest-Linux-x86_64.sh
bash install.sh
```

- Setup

```
# Create the environment with all the dependencies
conda env create
# Activate the environment
source activate topic_space

# Install girder web interface
girder-install web

# Intall girder plugins
girder-install plugin
```


# Usage

If you haven't done so, activate your environment:

```
source activate topic_space
```

- Run Girder

```
# Start mongodb
$mongod --dbpath <your_mongo_db_path> &

# Start girder server
$girder-server

```

The girder web interface will be available:

http://localhost:8080/

- Run Flask app

```
$python run.py
```

The flask web interface will be available:

http://localhost:5000/

# Notes

- In the Admin Console, you need to add your other application e.g. http://localhost:5000 under CORS Allowed Origins
in Settings -> Advanced Settings.

