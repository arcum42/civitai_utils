import hashlib
import json
import civitai

filename = "models/ponyDiffusionV6XL_v6.safetensors"

model_info = civitai.get_model_info_from_file(filename)

print("Model name: ", model_info["model"]["name"])