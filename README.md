# Geocaching
## Tools and resources
Here are some useful websites for solving puzzles, plotting coordinates, and mapping waypoints, among other things.
- https://www.boxentriq.com/
- https://www.geocachingtoolbox.com/
- https://www.guballa.de/vigenere-solver
- https://www.dcode.fr/
- https://www.cryptool.org/en/cto/
- https://rumkin.com/tools/cipher/
- https://www.simonsingh.net/The_Black_Chamber/chamberguide.html
- https://www.cryptogram.org/resource-area/solve-a-cipher/
- https://www.cryptoprograms.com/
- https://parmstro.weebly.com/solving-puzzles.html
- http://luthorien.altervista.org/Tools/
- https://www.geocacherscompass.com/puzzle-resources/

## Cache Info
`cache_info.py` is a script that takes a GCXXXXX code and fetches details from the assosiated Geocache page. It will work with any cache page, but it's purpose is to assist in solving puzzles by looking for hidden information, such as background image URL, HTML comments, etc.

## Ciphers
The `ciphers.py` file contains simple ciphers such as the [Vigenère cipher](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher), and [Caesar Cipher](https://en.wikipedia.org/wiki/Caesar_cipher). There are also 'helper' methods for solving or cracking these ciphers.

### Vigenère
There is a method to assist in guessing the keys and plain text message given two encrypted samples of the same text. There are a couple of exceptions: the keys used are the same number of characters as the message, and the key for the second sample is the same as the key for the first sample minus the first character of the key. For exmaple, imagine you have two encrypted messages: `ADLNHEJLQKOD` and `KLGFWTSGNSMM`, you don't know the keys used, or even the plain text (Attack at dawn), you just know the message is the same when decrypted with the right keys. The method will iterate over the the possibilities and print them for you to review.

## ToDo
There are many things I want to implement into this project, this is a non-exhaustive list.
### Ciphers
- [x] Caesar
- [x] Vigenere
- [ ] Playfair
- [ ] Cipher detection
### Cache Page Analysis
- [X] ID/Title
- [X] Hidden by/Hidden Date
- [X] Difficulty/Terrain/Size
- [X] Hint
- [X] Background image URL
- [X] Related webpage URL
- [X] Attributes list
- [X] Short description (raw html content/comments are visible)
- [X] Long description (raw html content/comments are visible)
- [ ] Text pattern detection
### Pattern Recognition
- [ ] Palindromes
- [ ] First letter of each word/sentence