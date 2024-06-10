#!/usr/bin/env python

import argparse
import json
import os
import shutil
import subprocess
import sys
import tarfile
from datetime import datetime

# import wget

# def download_untar_store(url, tmp_path, dest_path):
#     """
#     Download a tar.gz file containing one folder,
#     extract that folder and move the content inside dest_path
#     """

#     extract_path = os.path.join(tmp_path, "extract")

#     os.makedirs(tmp_path, exist_ok=True)

#     # download data
#     filename = wget.download(url, out=tmp_path)
#     tarfile_path = os.path.join(tmp_path, filename)
#     tar = tarfile.open(tarfile_path)
#     tar.extractall(extract_path)

#     if len(list(os.listdir(extract_path))) > 1:
#         print("More then one folder in zipped file, aborting !")
#     else:
#         for folder in os.listdir(extract_path):
#             folder_path = os.path.join(extract_path, folder)

#             print(f"Copy data to {dest_path}")
#             shutil.copytree(folder_path, dest_path)
#             print("Done !")

#     shutil.rmtree(tmp_path)


def main():
    # Parse Command Line
    parser = argparse.ArgumentParser(description="Create data manager JSON.")
    parser.add_argument("--out", dest="output", action="store", help="JSON filename")
    parser.add_argument(
        "--version", dest="version", action="store", help="Version of the DB"
    )
    parser.add_argument("--db-type", dest="db_type", action="store", help="Type of DB")

    args = parser.parse_args()

    # the output file of a DM is a json containing args that can be used by the DM
    # most tools mainly use these args to find the extra_files_path for the DM, which can be used
    # to store the DB data
    with open(args.output) as fh:
        params = json.load(fh)

    workdir = params["output_data"][0]["extra_files_path"]
    os.mkdir(workdir)

    time = datetime.utcnow().strftime("%Y-%m-%dT%H%M%SZ")
    db_value = f"db_v{args.version}_type_{args.db_type}_downloaded_{time}"
    db_path = os.path.join(workdir, db_value)

    # create DB
    if args.db_type == "test-db":  # only copy the test DB

        # TODO check if tool is installed
        # check if install_databases.py is there
        # command_args = ["install_databases.py", "-h"]
        # proc = subprocess.Popen(args=command_args, shell=False)
        # return_code = proc.wait()
        # if return_code:
        #     print("Error downloading Pharokka database.", file=sys.stderr)
        #     sys.exit(return_code)

        # copy the test DB
        test_db_path = os.path.join(
            os.path.dirname(os.path.realpath(__file__)), "test_db"
        )  # relative to the DM script
        command_args = ["cp", "-r", test_db_path, db_path]

    else:

        # Downlaod EUKulele DB
        command_args = [
            "EUKulele",
            "download",
            "--database",
            args.db_type,
            "--out_dir",
            db_path,
        ]

    proc = subprocess.Popen(args=command_args, shell=False)
    return_code = proc.wait()
    if return_code:
        print("Error downloading EUKulele database.", file=sys.stderr)
        sys.exit(return_code)

    # Update Data Manager JSON and write to file
    data_manager_entry = {
        "data_tables": {
            "eukulele_db_versioned": {
                "value": db_value,
                "dbkey": args.db_type,
                "version": args.version,
                "name": f"EUKulele DB ({args.db_type}) version {args.version} downloaded at {datetime.now()}",
                "path": db_path,
            }
        }
    }

    with open(os.path.join(args.output), "w+") as fh:
        json.dump(data_manager_entry, fh, sort_keys=True)


if __name__ == "__main__":
    main()
