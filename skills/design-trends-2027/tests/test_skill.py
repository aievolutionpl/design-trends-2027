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

    def test_twenty_complete_recipes(self):
        text = RECIPES.read_text(encoding='utf-8')
        sections = re.split(r'(?m)^## (\d+)\. ', text)[1:]
        self.assertEqual([int(x) for x in sections[::2]], list(range(1, 21)))
        for number, body in zip(sections[::2], sections[1::2]):
            for field in ('Decision and use', 'Composition', 'Color', 'Typography',
                          'Imagery', 'Motion', 'Anti-pattern', 'QA', 'Brief example'):
                with self.subTest(direction=number, field=field):
                    self.assertIn(f'**{field}:**', body)

    def test_routing_and_evidence_guards(self):
        text = SKILL.read_text(encoding='utf-8')
        for n in range(1, 21):
            self.assertRegex(text, rf'(?m)^\| {n} ')
        for value in ('one lead', 'supporting directions', 'placeholder',
                      'actual output', 'not measured 2027', 'tested versus proposed'):
            self.assertIn(value, text)
        self.assertIn('independent editorial additions', text)

    def test_twenty_polish_prompts(self):
        text = RECIPES.read_text(encoding='utf-8')
        sections = re.split(r'(?m)^<a id="styl-(\d{2})"></a>\n', text)[1:]
        self.assertEqual([int(n) for n in sections[::2]], list(range(1, 21)))
        prompts = []
        for number, body in zip(sections[::2], sections[1::2]):
            for field in ('Podstawy stylu', 'Kiedy używać', 'Kompozycja', 'Kolor',
                          'Typografia', 'Materiały', 'Unikać', 'Prompt dla agenta'):
                with self.subTest(direction=number, field=field):
                    self.assertIn(f'**{field}:**', body)
            prompt = re.search(r'\*\*Prompt dla agenta:\*\*\s*```text\n(.+?)\n```', body, re.S)
            self.assertIsNotNone(prompt, number)
            if prompt is None:
                continue
            prompts.append(prompt.group(1))
            for token in ('[FORMAT]', '[MARKA]', '[CEL]', '[ODBIORCY]', '[TREŚĆ]', '[CTA]'):
                self.assertIn(token, prompt.group(1))
        self.assertEqual(len(set(prompts)), 20)

    def test_twenty_images_and_sources(self):
        project = ROOT.parents[1]
        readme = (project / 'README.md').read_text(encoding='utf-8')
        sources = (ROOT / 'references' / 'sources.md').read_text(encoding='utf-8')
        headings = [int(x) for x in re.findall(r'^### (\d{2})\. ', readme, re.M)]
        self.assertEqual(headings, list(range(1, 21)))
        images = re.findall(r'!\[[^]]*\]\((assets/style-\d{2}\.png)\)', readme)
        self.assertEqual(images, [f'assets/style-{n:02d}.png' for n in range(1, 21)])
        content = []
        for n, image in enumerate(images, 1):
            asset = project / image
            with self.subTest(asset=image):
                self.assertTrue(asset.is_file())
                self.assertGreater(asset.stat().st_size, 1000)
                self.assertEqual(asset.read_bytes()[:8], b'\x89PNG\r\n\x1a\n')
                self.assertIn(f'application-recipes.md#styl-{n:02d}', readme)
                content.append(asset.read_bytes())
        self.assertEqual(len(set(content)), 20)
        for source in ('flight-patterns', 'century-of-design-part-ii', 'the-bauhaus-1919-1933'):
            self.assertIn(source, sources)
        self.assertIn('not evidence of 2027 adoption', sources)
        for source in ('nngroup.com/articles/neobrutalism', 'reprographix.ink/risograph-printing/guide',
                       '10.37186/swrks/7.2/3', 'omoro.io/photography/clay-style'):
            self.assertIn(source, sources)


if __name__ == '__main__':
    unittest.main()
