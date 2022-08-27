from django.test import TestCase
from .models import Snippet
from django.http import HttpResponse
# Create your tests here.

class SnippetTestCase(TestCase):
    def setUp(self):
        Snippet.objects.create(title="new snippet",code="html5 code <b>this is bold</b>",language="HTML5")
        Snippet.objects.create(title="new_snippet_for_rust",code="fn main(){ prinln ('hello')}",language="Rust")
    def test_for_check(self):
        now = Snippet.objects.get(title="new_snippet_for_rust")
        #self.assertEqual(now.code(),'the rust code says"hello world"')
        self.assertEqual(now.title,"new_snippet_for_rust")
