# here I only want to return config.yaml and params.yaml, to read it
# to read those files we need path, so instread of hardcoding, we can keep that in a constant

from pathlib import Path

CONFIG_FILE_PATH= Path("config/config.yaml")
PARAMS_FILE_PATH= Path("params.yaml")