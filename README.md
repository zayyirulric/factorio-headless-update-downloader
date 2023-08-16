# Factorio Server Updater
Downloader for the updates for Factorio running on an x64 Linux headless server
# How to use
Run `main.py` and supply your current server's version number.
```bash
shell> python3 main.py
Found latest 'core-linux_headless64' stable version: 1.1.87
Please give your current version number in the format listed in https://updater.factorio.com/get-available-versions
        > 1.1.74
Now downloading update for 'core-linux_headless64' version from 1.1.74 to 1.1.75
...
Finished downloading all updates.
```
# How to update Factorio
In your Factorio server's root directory, run
`./bin/x64/factorio --apply-update update-<FROM_VERSION>-<TO_VERSION>.zip`

Example: 
```bash
./bin/x64/factorio --apply-update update-1.1.86-1.1.87.zip
```
