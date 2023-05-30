empty_bytes = bytes(4)
data_bytes = bytes(b'\xFF\xFF')
mutable_bytes = bytearray()

print(mutable_bytes) # bytearray(b'')
print(type(mutable_bytes)) # bytearray
print(empty_bytes) # 00000000
print(data_bytes) # ffff
print(type(empty_bytes)) # bytes
