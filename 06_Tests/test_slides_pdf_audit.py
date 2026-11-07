"""Test PDF Proposal compliance for UGREEN AI NAS Hackathon Round 1.
"""

from pathlib import Path
import re
import pypdf

BASE_DIR = Path(r"G:\我的雲端硬碟\260803_opencode\01_賽事專區\202611_UGREEN_AI_NAS_Hackathon")
PDF_PATH = BASE_DIR / "04_Slides_PDF" / "UGREEN_AI_NAS_Round1_Project_Proposal.pdf"


def test_proposal_pdf_compliance():
    assert PDF_PATH.exists(), f"Proposal PDF missing at {PDF_PATH}"

    reader = pypdf.PdfReader(str(PDF_PATH))
    assert len(reader.pages) == 2, f"Expected balanced 2-page PDF, got {len(reader.pages)}"

    full_text = "\n".join(page.extract_text() for page in reader.pages)

    # Check that all 10 questions are present
    for i in range(1, 11):
        assert f"[{i}]" in full_text or f"{i}." in full_text, f"Question {i} missing in PDF text!"

    # Word count check
    words = re.findall(r"\b[A-Za-z0-9_-]+\b", full_text)
    print(f"[PDF AUDIT] Total words extracted from PDF: {len(words)}")
    assert "phantom-sovereign-guard" in full_text
    assert "Jack Hu" in full_text
    assert "static-pass" in full_text
    print("[PASS] Proposal PDF passed 10-question coverage and 2-page balanced layout audit!")


if __name__ == "__main__":
    test_proposal_pdf_compliance()
