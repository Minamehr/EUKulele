# Create local env to run planemo

* Install conda/mamba

```
mamba create -n planemo-env python=3.7
mamba activate planemo-env
pip install -U planemo
```

# lint

```
planemo lint DM/data_manager/eukulele_db_fetcher.xml --biocontainers
```

# Serve locally

```
cd EUKulele/eukulele-DM
planemo serve DM/data_manager/eukulele_db_fetcher.xml --biocontainers --galaxy_root ~/git/galaxy
```

# Serve tool and DM

Note: Do not run planemo inside the tool repository, it will automatically use the tool-data folder instead of the galaxy/tool-data folder

```
cd EUKulele/eukulele-DM
planemo serve DM/data_manager/eukulele_db_fetcher.xml ../Eukulele2.xml --biocontainers --galaxy_root ~/git/galaxy
```

## Check if tool and DM work together

In Galaxy go to:

* Admin
* Local Data
* Check if DM is in **Installed Data Managers**
* Click it
* Run the tool with Database type: test-db (or real DB, but takes long)
* Admin
* Data Tables
* eukulele_db_versioned
* Chekc if new table was made

* Go to the tool
* Check if new table can be found by: `Select a eukulele database `


# Test download locally

```
EUKulele download --database mmetsp --out_dir mmetsp
```

