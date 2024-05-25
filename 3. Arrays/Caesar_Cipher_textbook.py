class CaesarCipher:
    """Class for doing encryption and decryption using a Caesar cipher."""

    def __init__(self, shift):
        """Construct Caesar cipher using given integer shift for rotation."""
        encoder = [None] * 26  # Temporary array for encryption
        decoder = [None] * 26  # Temporary array for decryption

        # Loop through all letters in the alphabet
        for k in range(26):
            # Calculate encrypted letter based on the shift, and store it in encoder array
            encoder[k] = chr((k + shift) % 26 + ord("A"))
            # Calculate decrypted letter based on the shift, and store it in decoder array
            decoder[k] = chr((k - shift) % 26 + ord("A"))

        # Join the encrypted letters into a string and store it in self.forward
        self.forward = "".join(encoder)
        # Join the decrypted letters into a string and store it in self.backward
        self.backward = "".join(decoder)

    def encrypt(self, message):
        """Return string representing encrypted message."""
        return self.transform(message, self.forward)

    def decrypt(self, secret):
        """Return decrypted message given encrypted secret."""
        return self.transform(secret, self.backward)

    def transform(self, original, code):
        """Utility to perform transformation based on given code string."""
        msg = list(original)  # Convert original message to a list of characters
        # Loop through each character in the original message
        for k in range(len(msg)):
            if msg[k].isupper():  # Check if the character is uppercase
                j = ord(msg[k]) - ord(
                    "A"
                )  # Calculate the index of the character in the alphabet
                msg[k] = code[j]  # Replace the character based on the given code string
        return "".join(msg)  # Join the replaced characters into a string


# Main program
if __name__ == "__main__":
    cipher = CaesarCipher(3)  # Create a CaesarCipher object with a shift of 3
    message = "THE EAGLE IS IN PLAY; MEET AT JOE S."  # Original message
    coded = cipher.encrypt(message)  # Encrypt the message
    print("Secret:", coded)  # Print the encrypted ciphertext
    answer = cipher.decrypt(coded)  # Decrypt the ciphertext
    print("Message:", answer)  # Print the decrypted original message
