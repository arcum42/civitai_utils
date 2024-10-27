import json
import os
import hashlib
import requests
import progressbar as pb

def get_hash(file):
    sha256_hash = hashlib.sha256()
    widgets = ['Calculating hash: ',
           pb.Bar('*'),' (',
           pb.Timer(format= 'elapsed time: %(elapsed)s'),
           ') ',
          ]
    bar = pb.ProgressBar(max_value=1, widgets=widgets).start()

    i = 0
    filesize = os.path.getsize(file)
    with open(file, "rb") as f:
        for byte_block in iter(lambda: f.read(4096),b""):
            progress = i/filesize
            sha256_hash.update(byte_block)
            bar.update(progress)
            i += 4096

        print("\n")
        hash = sha256_hash.hexdigest()
        print(f"Hash = {hash}")
        return hash
    
def get_model_info_from_hash(hash):
    r = requests.get("https://civitai.com/api/v1/model-versions/by-hash/" + hash)
    return r.json()

def get_model_info_from_file(file):
    print(f"Input file: {file}")
    return get_model_info_from_hash(get_hash(file))