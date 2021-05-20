class Codec:
    lookup = []

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL."""
        n = len(self.lookup)
        self.lookup.append(longUrl)
        return f"https://tinyurl.com/{n}"

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL."""
        key = int(shortUrl.split("/")[-1])
        return self.lookup[key]


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))