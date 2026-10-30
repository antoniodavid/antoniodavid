from html.parser import HTMLParser
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]


def css_color(styles, token):
    match = re.search(rf"--{token}:\s*(#[0-9a-fA-F]{{6}})\s*;", styles)
    if match is None:
        raise AssertionError(f"Missing color token --{token}")
    value = match.group(1).lstrip("#")
    return tuple(int(value[index : index + 2], 16) for index in (0, 2, 4))


def relative_luminance(color):
    channels = []
    for channel in color:
        value = channel / 255
        channels.append(
            value / 12.92 if value <= 0.04045 else ((value + 0.055) / 1.055) ** 2.4
        )
    return sum(
        weight * channel
        for weight, channel in zip((0.2126, 0.7152, 0.0722), channels)
    )


def contrast_ratio(first, second):
    lighter, darker = sorted((relative_luminance(first), relative_luminance(second)), reverse=True)
    return (lighter + 0.05) / (darker + 0.05)


class PortfolioMarkup(HTMLParser):
    def __init__(self):
        super().__init__()
        self.elements = []
        self.text = []
        self.list_items = []
        self._open_list_items = []

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        self.elements.append((tag, attributes))
        if tag == "li":
            self._open_list_items.append({"hrefs": [], "text": []})
        elif tag == "a" and self._open_list_items:
            self._open_list_items[-1]["hrefs"].append(attributes.get("href", ""))

    def handle_startendtag(self, tag, attrs):
        self.elements.append((tag, dict(attrs)))

    def handle_data(self, data):
        self.text.append(data)
        for item in self._open_list_items:
            item["text"].append(data)

    def handle_endtag(self, tag):
        if tag == "li" and self._open_list_items:
            item = self._open_list_items.pop()
            self.list_items.append(
                {"hrefs": item["hrefs"], "text": " ".join(item["text"]).casefold()}
            )


class PortfolioTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        page_path = ROOT / "site" / "index.html"
        cls.page = page_path.read_text(encoding="utf-8") if page_path.exists() else ""
        cls.styles_path = ROOT / "site" / "styles.css"
        cls.styles = (
            cls.styles_path.read_text(encoding="utf-8")
            if cls.styles_path.exists()
            else ""
        )
        cls.readme = (ROOT / "README.md").read_text(encoding="utf-8")
        cls.parser = PortfolioMarkup()
        cls.parser.feed(cls.page)

    def test_page_has_an_accessible_semantic_document_shell(self):
        self.assertIn("<!doctype html>", self.page.lower())
        self.assertRegex(self.page, r'<html\b[^>]*\blang=["\']en["\']')
        self.assertIn('name="viewport"', self.page)
        self.assertIn("<title>", self.page)
        self.assertIn('href="./styles.css"', self.page)

        tags = [tag for tag, _ in self.parser.elements]
        self.assertIn("nav", tags)
        self.assertIn("main", tags)
        self.assertIn("footer", tags)
        self.assertEqual(tags.count("h1"), 1)
        self.assertIn('id="main-content"', self.page)
        self.assertIn('href="#main-content"', self.page)

    def test_featured_projects_match_the_verified_public_stack(self):
        page_text = " ".join(self.parser.text).lower()
        for name in ("odf agent team", "odoo language server", "osem"):
            with self.subTest(project=name):
                self.assertIn(name, page_text)
        for language in ("typescript", "rust", "go"):
            with self.subTest(language=language):
                self.assertIn(language, page_text)

    def test_oca_work_links_to_selected_pull_requests_with_honest_status(self):
        expected = {
            "https://github.com/OCA/delivery-carrier/pull/1079",
            "https://github.com/OCA/delivery-carrier/pull/1082",
            "https://github.com/OCA/stock-logistics-reporting/pull/404",
            "https://github.com/OCA/bank-statement-import/pull/864",
        }
        for href in expected:
            with self.subTest(merged_pull_request=href):
                item = next(
                    (item for item in self.parser.list_items if href in item["hrefs"]),
                    None,
                )
                self.assertIsNotNone(item, f"missing contribution row for {href}")
                self.assertIn("merged", item["text"])

        billcom_url = "https://github.com/OCA/l10n-usa/pull/166"
        billcom_item = next(
            (item for item in self.parser.list_items if billcom_url in item["hrefs"]),
            None,
        )
        self.assertIsNotNone(billcom_item, "Bill.com #166 must be explicitly listed")
        self.assertIn("open for review", billcom_item["text"])
        self.assertNotIn("merged", billcom_item["text"])
        self.assertNotIn("lead architect", billcom_item["text"])

    def test_deep_accent_text_meets_normal_text_contrast_on_both_papers(self):
        accent = css_color(self.styles, "color-accent-deep")
        for paper_token in ("color-paper", "color-paper-2"):
            with self.subTest(background=paper_token):
                paper = css_color(self.styles, paper_token)
                self.assertGreaterEqual(contrast_ratio(accent, paper), 4.5)

    def test_styles_support_responsive_keyboard_and_reduced_motion_use(self):
        self.assertTrue(self.styles.strip(), "The site stylesheet should exist.")
        self.assertIn(":focus-visible", self.styles)
        self.assertIn("prefers-reduced-motion", self.styles)
        self.assertIn("@media", self.styles)
        self.assertNotIn("transition: all", self.styles.lower())

    def test_static_page_has_no_remote_assets_or_unneeded_script(self):
        tags = [tag for tag, _ in self.parser.elements]
        self.assertNotIn("script", tags)
        self.assertNotIn("<script", self.page.lower())
        self.assertNotRegex(self.styles.lower(), r"@import\s+url\s*\(")
        self.assertNotRegex(self.styles.lower(), r"url\s*\(\s*[\"']?https?://")

if __name__ == "__main__":
    unittest.main()
