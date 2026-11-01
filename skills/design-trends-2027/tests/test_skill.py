"""Offline regression checks. Run: python3 -m unittest discover -s tests -v."""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / 'SKILL.md'
RECIPES = ROOT / 'references' / 'application-recipes.md'


class SkillTests(unittest.TestCase):
    def test_frontmatter_and_language(self):
        text = SKILL.read_text(encoding='utf-8')
        self.assertRegex(text, r'\A---\nname: design-trends-2027\n')
        for value in ('license: MIT', 'author: AI Evolution Polska', 'description:',
                      "user's language", 'Polish or English', 'Pre-flight', 'reduced motion'):
            self.assertIn(value, text)
        self.assertTrue((ROOT / 'LICENSE').is_file())
        self.assertIn('Permission is hereby granted', (ROOT / 'LICENSE').read_text())

    def test_relative_links_resolve_and_no_private_paths(self):
        for path in ROOT.rglob('*.md'):
            text = path.read_text(encoding='utf-8')
            self.assertNotRegex(text, r'(?i)(?:/home/|/Users/|[A-Z]:\\\\|/mnt/[a-z]/)')
            for target in re.findall(r'\]\(([^)]+)\)', text):
                if target.startswith(('https://', 'http://', '#', 'mailto:')):
                    continue
                target = target.split('#', 1)[0]
                self.assertFalse(target.startswith('/'), (path, target))
                resolved = (path.parent / target).resolve()
                self.assertTrue(resolved.is_relative_to(ROOT), (path, target))
                self.assertTrue(resolved.exists(), (path, target))

    def test_sixteen_complete_recipes(self):
        text = RECIPES.read_text(encoding='utf-8')
        sections = re.split(r'(?m)^## (\d+)\. ', text)[1:]
        self.assertEqual([int(x) for x in sections[::2]], list(range(1, 17)))
        for number, body in zip(sections[::2], sections[1::2]):
            for field in ('Decision and use', 'Composition', 'Color', 'Typography',
                          'Imagery', 'Motion', 'Anti-pattern', 'QA', 'Brief example'):
                with self.subTest(direction=number, field=field):
                    self.assertIn(f'**{field}:**', body)

    def test_routing_and_evidence_guards(self):
        text = SKILL.read_text(encoding='utf-8')
        for n in range(1, 17):
            self.assertRegex(text, rf'(?m)^\| {n} ')
        for value in ('one lead', 'supporting directions', 'placeholder',
                      'actual output', 'not measured 2027', 'tested versus proposed'):
            self.assertIn(value, text)
        self.assertIn('independent editorial additions', text)

    def test_new_directions_have_distinct_assets_and_sources(self):
        project = ROOT.parents[1]
        readme = (project / 'README.md').read_text(encoding='utf-8')
        sources = (ROOT / 'references' / 'sources.md').read_text(encoding='utf-8')
        for name in ('data-poetry', 'biomorphic', 'monochrome'):
            asset = project / 'assets' / f'trends-{name}.png'
            with self.subTest(asset=name):
                self.assertTrue(asset.is_file())
                self.assertGreater(asset.stat().st_size, 1000)
                self.assertIn(f'assets/trends-{name}.png', readme)
                self.assertEqual(asset.read_bytes()[:8], b'\x89PNG\r\n\x1a\n')
        for source in ('flight-patterns', 'century-of-design-part-ii', 'the-bauhaus-1919-1933'):
            self.assertIn(source, sources)
        self.assertIn('not evidence of 2027 adoption', sources)


if __name__ == '__main__':
    unittest.main()
