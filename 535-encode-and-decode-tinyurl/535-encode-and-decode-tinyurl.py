class Codec:
    alphabet = 'abcdefghijklmnopqrstuvwxyz@#$%^&*()!ASDFGHJKKLQWERTY0123456789'
    def __init__(self):
        self.codeTourl=dict()
        self.urlTocode=dict()
        
    def encode(self, longUrl: str) -> str:
        while longUrl not in self.urlTocode:
            code=''.join(random.choice(Codec.alphabet) for _ in range(6))
            if code not in self.codeTourl:
                self.codeTourl[code]=longUrl
                self.urlTocode[longUrl]=code
        return 'http://tinyurl.com/' + code      
        

    def decode(self, shortUrl: str) -> str:
        return self.codeTourl[shortUrl.split("/")[-1]]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))