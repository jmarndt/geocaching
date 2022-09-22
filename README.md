# Geocaching
Tools and resources related to Geocaching
Here are some useful websites for solving puzzles, plotting coordinates, and mapping waypoints.
- https://www.boxentriq.com/
- https://www.geocachingtoolbox.com/
-

## Vigenere
The `vigenere.py` file contains methods related to the [Vigenère cipher](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher). You can encrypt or decrpyt a messgage provided you have the key.

There is also a method to assist in guessing the keys and plain text message given two encrypted samples of the same text. There are a couple of exceptions: the keys used are the same number of characters as the message, and the key for the second sample is the same as the key for the first sample minus the first character of the key. For exmaple, imagine you have two encrypted messages: `ADLNHEJLQKOD` and `KLGFWTSGNSMM`, you don't know the keys used, or even the plain text (Attack at dawn), you just know the message is the same when decrypted with the right keys. The method will iterate over the the possibilities and print them for you to review.