from vitalstyles import commentparser



class TestComment:
    def test_remove_common_stars(self):
        assert commentparser.Comment('*A\n*B\n*C\n').comment == 'A\nB\nC'
        assert commentparser.Comment('* A\n* B\n* C\n').comment == 'A\nB\nC'
        assert commentparser.Comment('  * A\n  *B\n  *  C\n').comment == ' A\nB\n  C'    

    def test_remove_common_whitespace(self):
        assert commentparser.Comment('   A\n  B\n    C\n').comment == ' A\nB\n  C'

    def test_to_html(self):
        assert commentparser.Comment('# Hello world').to_html() == '<h1>Hello world</h1>'
        assert commentparser.Comment('# Hello world\n\nTest').to_html() == '<h1>Hello world</h1>\n<p>Test</p>'



class TestParse:
    def test_simple(self):
        assert commentparser.Parse('/**\nT\n*/')[0].comment == 'T'
        assert commentparser.Parse('/**\nTest\n*/')[0].comment == 'Test'
        assert commentparser.Parse('/**\nTest multiple words\n*/')[0].comment == 'Test multiple words'

    def test_single_line(self):
        assert len(commentparser.Parse('/**Test*/')) == 0
        assert len(commentparser.Parse('/** Test */')) == 0

    def test_multimatch(self):
        assert commentparser.Parse('/**\nt1\n*/ Garbage here.. /**\nt2\n*/').unicodelist() == [u't1', u't2']

    def test_multiline(self):
        assert commentparser.Parse('/**\nA\nB\nC\n*/')[0].comment == 'A\nB\nC'

    def test_multiline_whitespace_on_first_line(self):
        assert commentparser.Parse('/**     \nA\n*/')[0].comment == 'A'

    def test_multiline_whitespace_on_last_line(self):
        assert commentparser.Parse('/**\nA\n        */')[0].comment == 'A'

    def test_remove_common_whitespace(self):
        assert commentparser.Parse('/**\n   A\n  B\n    C\n*/')[0].comment == ' A\nB\n  C'

    def test_remove_common_stars(self):
        assert commentparser.Parse('/**\n*A\n*B\n*C\n*/')[0].comment == 'A\nB\nC'
        assert commentparser.Parse('/**\n* A\n* B\n* C\n*/')[0].comment == 'A\nB\nC'
        assert commentparser.Parse('/**\n  * A\n  *B\n  *  C\n*/')[0].comment == ' A\nB\n  C'