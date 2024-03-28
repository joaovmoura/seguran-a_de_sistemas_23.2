key = [2, 0, 3, 1]


def feistel_cipher(text, rounds):
    for _ in range(rounds):
        text = cipher_round(text, key)
    return text

def feistel_decipher(text, rounds):
    for _ in range(rounds):
        text = decipher_round(text, key)
    return text

def cipher_round(text, key):
    left = text[:4]
    right = text[4:]

    new_left = xor(left, feistel_function(right, key))
    return right + new_left

def decipher_round(text, key):
    left = text[:4]
    right = text[4:]

    new_left = xor(right, feistel_function(left, key))
    return new_left + left

def feistel_function(right, key):
    permuted_data = []
    for i in range(len(key)):
        permuted_data.append(right[key[i]])
    return permuted_data

def xor(a, b):
    return bytes(x ^ y for x, y in zip(a, b))


def main():
    text = feistel_cipher(b'valorant', 4)
    print(text)
    decrypted_text = feistel_decipher(text, 4)
    print(decrypted_text)

if __name__ == "__main__":
    main()