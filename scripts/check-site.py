import shutil
from html.parser import HTMLParser
from pathlib import Path


class NoticeParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.headings = 0

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        if tag in {"script", "video", "audio", "source", "img", "iframe", "object", "embed", "link"}:
            raise ValueError(f"Unexpected external or media element: {tag}")
        if any(key in values for key in {"src", "srcset", "poster"}):
            raise ValueError("The notice must not load external or embedded assets")
        if tag == "h1":
            self.headings += 1


allowed = {"index.html", "404.html"}
root = Path(__file__).resolve().parents[1]
for path in root.rglob("*"):
    if any(part in {".git", "site"} for part in path.relative_to(root).parts):
        continue
    if path.is_file() and path.suffix.lower() in {".mp4", ".webm", ".mov", ".png", ".jpg", ".webp", ".woff", ".woff2"}:
        raise ValueError(f"Unverified media remains: {path.relative_to(root)}")
if (root / "claude-directory-deck.html").exists():
    raise ValueError("The withdrawn presentation must not be published")
for name in sorted(allowed):
    source = (root / name).read_text()
    parser = NoticeParser()
    parser.feed(source)
    if parser.headings != 1:
        raise ValueError(f"Expected one heading in {name}")
    if "base64," in source or "url(" in source or "@import" in source:
        raise ValueError(f"Embedded assets are not allowed in {name}")
    if "licensing review" not in source:
        raise ValueError(f"Missing review notice in {name}")
output = root / "site"
if output.exists():
    shutil.rmtree(output)
output.mkdir()
for name in allowed:
    shutil.copyfile(root / name, output / name)
assert {path.name for path in output.iterdir()} == allowed
print("Verified text-only notice and explicit publishing allowlist")
