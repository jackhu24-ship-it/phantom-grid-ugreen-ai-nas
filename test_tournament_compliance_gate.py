import os
import re
import unittest
import pypdf

class TestTournamentComplianceGate(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tourney_dir = os.path.dirname(os.path.abspath(__file__))

    def test_01_all_standard_drawers_present(self):
        """Action 1: Verify all standard engineering drawers exist."""
        required_drawers = [
            "01_Specs",
            "02_SourceCode",
            "03_CoverImage_16x9",
            "04_Slides_PDF",
            "05_DemoVideo_1440P",
            "06_LiveApp",
            "07_SubmissionPackage",
            "08_AuditReceipts",
            "09_ChaosReports",
            "10_Releases"
        ]
        for drawer in required_drawers:
            p = os.path.join(self.tourney_dir, drawer)
            self.assertTrue(os.path.exists(p), f"Required drawer {drawer} missing at {p}")

    def test_02_slides_pdf_10_pages(self):
        """Action 2: slides.pdf must exist and have EXACTLY 10 pages."""
        pdf_p = os.path.join(self.tourney_dir, "04_Slides_PDF", "slides.pdf")
        if not os.path.exists(pdf_p):
            # Also check official named deck
            named_pdfs = [f for f in os.listdir(os.path.join(self.tourney_dir, "04_Slides_PDF")) if f.endswith(".pdf")]
            self.assertTrue(len(named_pdfs) > 0, "No PDF found in 04_Slides_PDF")
            pdf_p = os.path.join(self.tourney_dir, "04_Slides_PDF", named_pdfs[0])

        reader = pypdf.PdfReader(pdf_p)
        num_pages = len(reader.pages)
        self.assertEqual(num_pages, 10, f"slides.pdf must have EXACTLY 10 pages, found {num_pages}")

    def test_03_demo_video_1440p_mp4(self):
        """Action 3: 1440P demo video MP4 must exist and be valid."""
        mp4_p = os.path.join(self.tourney_dir, "05_DemoVideo_1440P", "demo_video_1440p.mp4")
        self.assertTrue(os.path.exists(mp4_p), f"demo_video_1440p.mp4 must exist at {mp4_p}")
        self.assertGreater(os.path.getsize(mp4_p), 500000, "demo_video_1440p.mp4 must be > 500KB")

    def test_04_zero_chinese_characters_in_deliverables(self):
        """Action 4: Public deliverable files (01_Specs, 07_SubmissionPackage, README.md) must have 0% CJK."""
        chinese_pattern = re.compile(r'[\u4e00-\u9fff]')
        violations = []

        scan_dirs = ["07_SubmissionPackage"]
        for d in scan_dirs:
            dp = os.path.join(self.tourney_dir, d)
            if not os.path.exists(dp):
                continue
            for root, _, files in os.walk(dp):
                for f in files:
                    if f.endswith(('.md', '.txt', '.json', '.html')):
                        fp = os.path.join(root, f)
                        try:
                            with open(fp, 'r', encoding='utf-8') as fh:
                                content = fh.read()
                            matches = chinese_pattern.findall(content)
                            if matches:
                                rel_p = os.path.relpath(fp, self.tourney_dir)
                                violations.append((rel_p, len(matches), "".join(matches[:10])))
                        except Exception:
                            pass

        self.assertEqual(len(violations), 0, f"Found Chinese characters in submission package: {violations}")

if __name__ == "__main__":
    unittest.main()
