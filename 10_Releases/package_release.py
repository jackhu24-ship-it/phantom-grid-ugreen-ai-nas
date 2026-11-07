"""Package phantom-sovereign-guard into official Pre-test Skill Package ZIP.
"""

import shutil
import zipfile
from pathlib import Path

BASE_DIR = Path(r"G:\我的雲端硬碟\260803_opencode\01_賽事專區\202611_UGREEN_AI_NAS_Hackathon")
SOURCE_DIR = BASE_DIR / "03_SourceCode" / "phantom-sovereign-guard"
RELEASE_DIR = BASE_DIR / "10_Releases"
ZIP_PATH = RELEASE_DIR / "phantom-sovereign-guard.zip"


def create_package():
    assert SOURCE_DIR.exists(), f"Source directory {SOURCE_DIR} does not exist."
    RELEASE_DIR.mkdir(parents=True, exist_ok=True)

    if ZIP_PATH.exists():
        ZIP_PATH.unlink()

    with zipfile.ZipFile(ZIP_PATH, "w", zipfile.ZIP_DEFLATED) as z:
        for p in SOURCE_DIR.rglob("*"):
            if p.is_file():
                rel_path = p.relative_to(SOURCE_DIR)
                z.write(p, arcname=str(rel_path))
                # Also include with folder prefix for maximum compatibility
                z.write(p, arcname=f"phantom-sovereign-guard/{rel_path}")

    print(f"[PACKAGE] Successfully built {ZIP_PATH} ({ZIP_PATH.stat().st_size} bytes)")


if __name__ == "__main__":
    create_package()
