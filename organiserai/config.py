import json
from os.path import expanduser, exists

DEFAULT_CONFIG = {
    "watch_directories": ["~/watch"],
    "file_destinations": {
         # Movies
        ".mp4": "~/Movies",
        ".mkv": "~/Movies",
        ".mov": "~/Movies",
        ".avi": "~/Movies",
        ".flv": "~/Movies",
        ".wmv": "~/Movies",
        ".webm": "~/Movies",
        ".mpeg": "~/Movies",
        ".mpg": "~/Movies",
        ".m4v": "~/Movies",

        # Music
        ".mp3": "~/Music",
        ".wav": "~/Music",
        ".flac": "~/Music",
        ".aac": "~/Music",
        ".ogg": "~/Music",
        ".m4a": "~/Music",
        ".wma": "~/Music",
        ".aiff": "~/Music",
        ".alac": "~/Music",
        ".mid": "~/Music",
        ".midi": "~/Music",

        # Documents
        ".pdf": "~/Documents",
        ".doc": "~/Documents",
        ".docx": "~/Documents",
        ".txt": "~/Documents",
        ".rtf": "~/Documents",
        ".odt": "~/Documents",
        ".xls": "~/Documents",
        ".xlsx": "~/Documents",
        ".csv": "~/Documents",
        ".ppt": "~/Documents",
        ".pptx": "~/Documents",
        ".md": "~/Documents",
        ".tex": "~/Documents",
        ".json": "~/Documents",
        ".xml": "~/Documents",
        ".yaml": "~/Documents",
        ".yml": "~/Documents",
        ".epub": "~/Documents",

        # Pictures
        ".jpg": "~/Pictures",
        ".jpeg": "~/Pictures",
        ".png": "~/Pictures",
        ".gif": "~/Pictures",
        ".bmp": "~/Pictures",
        ".tiff": "~/Pictures",
        ".tif": "~/Pictures",
        ".svg": "~/Pictures",
        ".heic": "~/Pictures",
        ".webp": "~/Pictures",
        ".ico": "~/Pictures",
        ".raw": "~/Pictures",
    },
    "ollama": {
        "url": "http://localhost:11434",
        "model": "llama3",
        "use_api_key": False,
        "api_key": ""
    }
}

def load_config(path="config.json"):
    if not exists(path):
        with open(path, "w") as f:
            json.dump(DEFAULT_CONFIG, f, indent=2)
        print(f"[organise-ai] Created default config at {path}")

    with open(path, "r") as f:
        cfg = json.load(f)

    cfg["watch_directories"] = [expanduser(p) for p in cfg["watch_directories"]]
    return cfg