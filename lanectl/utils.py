import re

def extract_blocks(script: str) -> list[str]:
    return re.findall(r"\{([^{}]+:[^{}]*)\}", script)
