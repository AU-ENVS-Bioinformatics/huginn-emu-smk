from pathlib import Path


def extract_file_name(filename: str) -> str:
    x = Path(filename)
    return x.with_suffix("").name
