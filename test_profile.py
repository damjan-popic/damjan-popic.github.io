"""Regression checks for the profile photograph and bilingual placement."""
import tempfile
import unittest
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit
import yaml
from build import ROOT, build


class Images(HTMLParser):
    def __init__(self):
        super().__init__()
        self.images = []
        self.metadata = {}

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'img':
            self.images.append(attrs)
        if tag == 'meta' and attrs.get('property', '').startswith('og:image'):
            self.metadata[attrs['property']] = attrs.get('content', '')


class ProfileTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.work = tempfile.TemporaryDirectory()
        cls.output = Path(cls.work.name) / 'site'
        build(cls.output)
        cls.site = yaml.safe_load((ROOT / 'site.yml').read_text(encoding='utf-8'))

    @classmethod
    def tearDownClass(cls):
        cls.work.cleanup()

    def test_photo_on_home_and_bio_in_both_languages(self):
        config = self.site.get('profile_photo')
        if not config:
            self.skipTest('Profile photograph deliberately disabled in site.yml')
        for route, lang in [('index.html', 'sl'), ('sl/index.html', 'sl'),
                            ('en/index.html', 'en'), ('sl/o-meni/index.html', 'sl'),
                            ('en/about/index.html', 'en')]:
            with self.subTest(route=route):
                path = self.output / route
                parsed = Images()
                parsed.feed(path.read_text(encoding='utf-8'))
                self.assertEqual(len(parsed.images), 1)
                image = parsed.images[0]
                self.assertEqual(image['alt'], config['alt'][lang])
                self.assertEqual(image['width'], str(config['width']))
                self.assertEqual(image['height'], str(config['height']))
                target = (path.parent / urlsplit(image['src']).path).resolve()
                source = ROOT / 'assets' / config['file']
                self.assertEqual(target.read_bytes(), source.read_bytes())
                expected_url = self.site['url'].rstrip('/') + '/assets/' + config['file']
                self.assertEqual(parsed.metadata['og:image'], expected_url)
                self.assertEqual(parsed.metadata['og:image:alt'], config['alt'][lang])

    def test_course_pages_do_not_acquire_the_profile_photo(self):
        for route in ['en/teaching/agrft/index.html', 'sl/poucevanje/agrft/index.html']:
            parsed = Images()
            parsed.feed((self.output / route).read_text(encoding='utf-8'))
            self.assertNotIn('og:image', parsed.metadata)
            self.assertNotIn('class="profile-photo"', (self.output / route).read_text(encoding='utf-8'))

    def test_photo_styles_preserve_natural_aspect_ratio(self):
        css = (ROOT / 'assets/style.css').read_text(encoding='utf-8')
        self.assertIn('.profile-photo img{display:block;width:100%;height:auto;', css)
        self.assertNotIn('object-fit:cover', css)


if __name__ == '__main__':
    unittest.main()
