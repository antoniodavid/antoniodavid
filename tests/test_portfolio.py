from html.parser import HTMLParser
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]



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


    def test_static_page_has_no_remote_assets_or_unneeded_script(self):
        tags = [tag for tag, _ in self.parser.elements]
        self.assertNotIn("script", tags)
        self.assertNotIn("<script", self.page.lower())
        self.assertNotRegex(self.styles.lower(), r"@import\s+url\s*\(")
        self.assertNotRegex(self.styles.lower(), r"url\s*\(\s*[\"']?https?://")

if __name__ == "__main__":
    unittest.main()
