# Create local env to run planemo

* Install conda/mamba

```
mamba create -n planemo-env python=3.7
mamba activate planemo-env
pip install -U planemo
```

# lint

```
planemo lint data_manager/eukulele_db_fetcher.xml --biocontainers
```

# Serve locally

```
cd EUKulele
planemo serve data_manager/eukulele_db_fetcher.xml --biocontainers --galaxy_root ~/git/galaxy
```

# Server tool and DM

Note: Do not run planemo inside the tool repository, it will automatically use the tool-data folder instead of the galaxy/tool-data folder

```
cd ~
planemo serve /home/paul/git/people/mina/EUKulele/eukulele-DM/DM/data_manager/eukulele_db_fetcher.xml /home/paul/git/people/mina/EUKulele/Eukulele2.xml --biocontainers --galaxy_root ~/git/galaxy
```