import palindrome


class TestPalindrome:
    def test_palindrome(self):
        assert "palindrome" == palindrome.check("ana")

    def test_palindrome2(self):
        assert "not palindrome" == palindrome.check("abc")

    def test_palindrome3(self):
        assert "palindrome" == palindrome.check("nadan")

    def test_palindrome4(self):
        assert "palindrome" == palindrome.check("reconocer")

    def test_palindrome5(self):
        assert "not palindrome" == palindrome.check("elefante")
