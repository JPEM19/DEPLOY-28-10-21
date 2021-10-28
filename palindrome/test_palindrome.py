import palindrome


class TestPalindrome:
    def test_palindrome(self):
        assert "palindrome" == palindrome.check("ana") 
    
    def test_palindrome(self):
        assert "not palindrome" == palindrome.check("abc")  
    
    def test_palindrome(self):
        assert "palindrome" == palindrome.check("nadan")
    
    def test_palindrome(self):
        assert "palindrome" == palindrome.check("reconocer")     
    
    def test_palindrome(self):
        assert "not palindrome" == palindrome.check("elefante") 
