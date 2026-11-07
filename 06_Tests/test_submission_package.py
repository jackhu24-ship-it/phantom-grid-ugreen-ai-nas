"""Audit Devpost Submission Package for UGREEN AI NAS Hackathon.
"""

from pathlib import Path
import re

BASE_DIR = Path(r"G:\我的雲端硬碟\260803_opencode\01_賽事專區\202611_UGREEN_AI_NAS_Hackathon")
COPY_FILE = BASE_DIR / "07_SubmissionPackage" / "Devpost_Official_Submission_Copy.md"
ZIP_PATH = BASE_DIR / "10_Releases" / "phantom-sovereign-guard.zip"
PDF_PATH = BASE_DIR / "04_Slides_PDF" / "UGREEN_AI_NAS_Round1_Project_Proposal.pdf"


def test_submission_package():
    assert COPY_FILE.exists(), f"Submission copy missing at {COPY_FILE}"
    assert ZIP_PATH.exists(), f"Release zip missing at {ZIP_PATH}"
    assert PDF_PATH.exists(), f"Proposal PDF missing at {PDF_PATH}"

    text = COPY_FILE.read_text(encoding="utf-8")

    # Short Pitch check
    match = re.search(r"## 1\. Short Pitch[^\n]*\n+([^\n]+)", text)
    assert match, "Short pitch section missing!"
    pitch = match.group(1).strip()
    assert len(pitch) <= 280, f"Short pitch exceeds 280 chars ({len(pitch)} chars): {pitch}"

    # Check 10 questions
    for i in range(1, 11):
        assert f"{i}. " in text, f"Question {i} missing from submission copy!"

    # Check Dual Seal
    assert "COMMANDER JACK HU" in text
    assert "XIAOMI" in text

    print(f"[PASS] Submission package fully verified! Short pitch: {len(pitch)} chars. All files ready for 1-click submission!")


if __name__ == "__main__":
    test_submission_package()
