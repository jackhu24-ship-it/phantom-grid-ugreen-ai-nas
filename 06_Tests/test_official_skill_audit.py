"""Official UGREEN Skill Package Static Compliance Audit.
Tests the skill against UGREEN's official static checker check-skill.mjs.
"""

import json
import subprocess
from pathlib import Path

BASE_DIR = Path(r"G:\我的雲端硬碟\260803_opencode\01_賽事專區\202611_UGREEN_AI_NAS_Hackathon")
CHECKER_SCRIPT = BASE_DIR / "official_starter_kit" / "uliya-skill-kit" / "scripts" / "check-skill.mjs"
TARGET_SKILL_DIR = BASE_DIR / "03_SourceCode" / "phantom-sovereign-guard"


def test_official_static_checker_full_pass():
    assert CHECKER_SCRIPT.exists(), f"Official checker script not found at {CHECKER_SCRIPT}"
    assert TARGET_SKILL_DIR.exists(), f"Target skill directory not found at {TARGET_SKILL_DIR}"

    cmd = ["node", str(CHECKER_SCRIPT), str(TARGET_SKILL_DIR)]
    res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")

    assert res.returncode == 0, f"check-skill.mjs exited with non-zero code {res.returncode}: {res.stderr}"

    data = json.loads(res.stdout)
    assert data["status"] == "static-pass", f"Expected static-pass but got {data['status']}"
    assert data["summary"]["errors"] == 0, f"Errors found: {data['summary']['errors']}"
    assert data["summary"]["warnings"] == 0, f"Warnings found: {data['summary']['warnings']}"
    assert len(data["diagnostics"]) == 0, f"Diagnostics not empty: {data['diagnostics']}"
    print(f"[PASS] {data['target']['skillName']} passed official UGREEN check-skill.mjs with 0 errors and 0 warnings!")


if __name__ == "__main__":
    test_official_static_checker_full_pass()
