# %%
import hashlib

# %%
message = "Hello, 안녕하세요, ¡Árvíztűrő tükörfúrógép! @ 🏫📚💻🎓"
print(message)
# %%
bytestring = "Hello, 안녕하세요, ¡Árvíztűrő tükörfúrógép! @ 🏫📚💻🎓".encode("utf-8")
print(bytestring)

# %%
print("Say hi again! " + bytestring.decode("utf-8"))

# %%

def naivehash(val):
    return str(sum(ord(c) for c in val) % 100)


print("Hash of 'Hello Hashed Message!':   " + naivehash("Hello Hashed Message!"))
print("Hash of 'Hello Hashed Message 2!': " + naivehash("Hello Hashed Message 2!"))

# %%
# Hashing using SHA-256
bytestring = "My message to the world: Say Hällo to a better hash!".encode("utf-8")
print("Original message: ")
print(bytestring)

hashed_message = hashlib.sha256(bytestring).hexdigest()
print()
print("Hash: " + hashed_message)

# %%

print(f"The SHA-256 hash is {len(hashed_message)} characters long")
print(f"Number of possible hashes: {16 ** len(hashed_message)}")
