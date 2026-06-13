# ============================================================
# PROJECT 2: Basic Encryption & Decryption
# Caesar Cipher Implementation
# DecodeLabs Cybersecurity Fellowship - Batch 2026
# ============================================================

# ----------------------------------
# THE CORE ENCRYPTION FUNCTION
# ----------------------------------
def encrypt(plaintext, shift):
    """
    Takes readable text (plaintext) and scrambles it using a shift key.
    Only letters are shifted — spaces and punctuation stay as-is.
    """
    ciphertext = ""  # We'll build the encrypted result here

    for char in plaintext:  # Loop through every character in the message

        # Handle UPPERCASE letters (A=65, Z=90 in ASCII)
        if char.isupper():
            # Step 1: ord(char) converts letter to ASCII number  e.g. 'A' → 65
            # Step 2: - 65 shifts range from 65-90 down to 0-25  e.g. 65-65 = 0
            # Step 3: + shift adds our key                        e.g. 0+3 = 3
            # Step 4: % 26 wraps around if we go past Z           e.g. 25+3=28 → 28%26=2 (C)
            # Step 5: + 65 brings it back to ASCII range          e.g. 3+65 = 68
            # Step 6: chr() converts number back to letter        e.g. 68 → 'D'
            encrypted_char = chr((ord(char) - 65 + shift) % 26 + 65)
            ciphertext += encrypted_char

        # Handle LOWERCASE letters (a=97, z=122 in ASCII)
        elif char.islower():
            # Same logic, but base is 97 instead of 65
            encrypted_char = chr((ord(char) - 97 + shift) % 26 + 97)
            ciphertext += encrypted_char

        # If it's a space, number, or punctuation — leave it alone
        else:
            ciphertext += char

    return ciphertext


# ----------------------------------
# THE CORE DECRYPTION FUNCTION
# ----------------------------------
def decrypt(ciphertext, shift):
    """
    Reverses the encryption. Uses the same shift, but in the OPPOSITE direction.
    D(x) = (x - n) % 26  ← notice the MINUS instead of PLUS
    """
    plaintext = ""

    for char in ciphertext:

        if char.isupper():
            # Same formula, but SUBTRACT the shift to reverse it
            decrypted_char = chr((ord(char) - 65 - shift) % 26 + 65)
            plaintext += decrypted_char

        elif char.islower():
            decrypted_char = chr((ord(char) - 97 - shift) % 26 + 97)
            plaintext += decrypted_char

        else:
            plaintext += char  # Non-letters pass through unchanged

    return plaintext


# ----------------------------------
# THE MAIN PROGRAM (User Interface)
# ----------------------------------
def main():
    print("=" * 55)
    print("   DECODELABS - Caesar Cipher Encryption Tool")
    print("=" * 55)

    # Get input from the user
    message = input("\nEnter your message: ")
    shift   = int(input("Enter shift key (e.g. 3): "))

    # Perform encryption
    encrypted = encrypt(message, shift)
    print(f"\n[ORIGINAL]  : {message}")
    print(f"[ENCRYPTED] : {encrypted}")

    # Perform decryption (proving we can reverse it)
    decrypted = decrypt(encrypted, shift)
    print(f"[DECRYPTED] : {decrypted}")

    # Verify the round-trip worked
    if decrypted == message:
        print("\n✅ Verification PASSED — Decryption matches original!")
    else:
        print("\n❌ Verification FAILED — Something went wrong.")

    print("\n" + "=" * 55)
    print("Concept: Symmetric Encryption — same key locks & unlocks")
    print("Weakness: Only 25 possible keys → easy to brute-force")
    print("=" * 55)


# Run the program
if __name__ == "__main__":
    main()
