# Caesar Cipher — Basic Encryption & Decryption

**DecodeLabs Cybersecurity Fellowship | Batch 2026 | Project 2**  
**Analyst:** Phyllis Kemuma

---

## Overview

This project implements a **Caesar Cipher** — one of the oldest and most foundational encryption techniques in cryptography. It demonstrates the core concept of **data confidentiality**: transforming readable plaintext into unreadable ciphertext using a mathematical key, and reversing that transformation through decryption.

> *"This track isn't about cracking codes — it's about Data Confidentiality."*  
> — DecodeLabs Project 2 Brief

The project is delivered in two forms:
- `caesar_cipher.py` — a Python script that runs in the terminal
- `caesar_cipher.html` — a fully interactive web interface that runs in any browser

---

## What is a Caesar Cipher?

A Caesar Cipher is a **substitution cipher** that shifts every letter in a message by a fixed number of positions in the alphabet. It is named after Julius Caesar, who reportedly used a shift of 3 to protect military communications.

**Example with shift = 3:**

```
Plaintext:  H  E  L  L  O
            ↓  ↓  ↓  ↓  ↓
Ciphertext: K  H  O  O  R
```

To decrypt, the process is reversed — each letter is shifted back by the same key.

---

## The Math

The Caesar Cipher works by converting letters to numbers (via ASCII), applying modular arithmetic, and converting back.

**Encryption formula:**
```
E(x) = (ord(char) − base + shift) % 26 + base
```

**Decryption formula:**
```
D(x) = (ord(char) − base − shift) % 26 + base
```

Where:
- `ord(char)` converts a character to its ASCII integer
- `base` is 65 for uppercase (A) or 97 for lowercase (a)
- `shift` is the secret key (1–25)
- `% 26` handles wrap-around — so Z shifted by 3 becomes C, not a character beyond the alphabet

**Step-by-step trace for the letter `A` with shift = 3:**

```
'A'  →  ord('A') = 65  →  65 − 65 = 0  →  0 + 3 = 3  →  3 % 26 = 3  →  3 + 65 = 68  →  chr(68) = 'D'
```

**Key Python functions used:**
- `ord(char)` — converts a character to its ASCII integer value
- `chr(num)` — converts an integer back to its character

---

## Files

| File | Description |
|------|-------------|
| `caesar_cipher.py` | Python terminal implementation with encrypt/decrypt functions |
| `caesar_cipher.html` | Interactive web interface — no installation required |

---

## How to Run

### Python (Terminal)

**Requirements:** Python 3.x — no external libraries needed.

```bash
python3 caesar_cipher.py
```

You will be prompted to enter your message and shift key. The program outputs the encrypted ciphertext and decrypts it back to verify the round-trip.

**Sample output:**
```
=======================================================
   DECODELABS - Caesar Cipher Encryption Tool
=======================================================

Enter your message: Hello, DecodeLabs!
Enter shift key (e.g. 3): 3

[ORIGINAL]  : Hello, DecodeLabs!
[ENCRYPTED] : Khoor, GhfrghOdev!
[DECRYPTED] : Hello, DecodeLabs!

✅ Verification PASSED — Decryption matches original!

=======================================================
Concept: Symmetric Encryption — same key locks & unlocks
Weakness: Only 25 possible keys → easy to brute-force
=======================================================
```

### Web Interface (Browser)

No installation or server required. Simply open `caesar_cipher.html` in any modern browser (Chrome, Firefox, Edge, Safari).

**Features:**
- Type any message and see encryption update in real time
- Drag the shift key slider (1–25) to change the key
- View the live algorithm trace showing every mathematical step for the first character
- Copy encrypted or decrypted output with one click
- Verification indicator confirms the round-trip is successful

---

## Key Concepts Demonstrated

**Symmetric Encryption**  
The same key is used to both encrypt and decrypt the message. This is the foundational concept behind modern symmetric algorithms like AES.

**The IPO Model of Cryptographic Systems**  
- Input → Plaintext (raw message) + Key (shift value)  
- Process → Algorithm (the shift formula with modular arithmetic)  
- Output → Ciphertext (encrypted, unreadable message)

**Modular Arithmetic**  
The `% 26` operation ensures the cipher wraps around within the 26-letter alphabet. Without it, shifting the letter Z by 3 would produce a character outside the alphabet entirely.

**ASCII Encoding**  
Text must become numbers before it can become math. Every character has an ASCII value — uppercase A is 65, lowercase a is 97. The cipher works on these integer values, not the letters themselves.

**Edge Case Handling**  
- Uppercase and lowercase letters are handled separately using their respective ASCII bases (65 and 97)
- Spaces, numbers, and punctuation are passed through unchanged — only letters are shifted

---

## Known Vulnerability

The Caesar Cipher is intentionally simple and is **not secure for real-world use**. It has two critical weaknesses:

1. **Tiny key space** — Only 25 possible shift values exist. An attacker can brute-force all 25 in under a second.

2. **Pattern preservation** — The cipher preserves letter frequency patterns. Since the letter 'E' is the most common in English, statistical analysis of ciphertext (frequency analysis) reveals the shift key without needing to try all 25 options.

This is why modern encryption (AES-256, RSA) uses keys with billions of possible values and multiple rounds of transformation. The Caesar Cipher's value is educational — it teaches the core mechanics of substitution, key-based transformation, and reversible encryption that underpin all modern cryptographic systems.

---

## Project Deliverables Checklist

- [x] Encrypt user text using Caesar Cipher logic
- [x] Decrypt the encrypted text using the reverse formula
- [x] Display both encrypted and decrypted output
- [x] Handle edge cases (spaces, punctuation, uppercase, lowercase)
- [x] Validate with round-trip verification (decrypted == original)
- [x] Implement user-selectable shift key
- [x] Provide live algorithm trace showing the mathematical steps

---

## Folder Contents

```
Project_2_Encryption/
├── caesar_cipher.py      # Python terminal script
├── caesar_cipher.html    # Web interface
└── README.md             # This file
```

---

*DecodeLabs Cybersecurity Fellowship — Batch 2026*  
*Phyllis Kemuma | phyliskemuma6@gmail.com | Nairobi, Kenya*