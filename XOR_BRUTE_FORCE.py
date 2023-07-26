def xor_brute_force(content, to_match):
  for key in range (256):
    translated = ""
    for ch in content:
      translated += chr(ord(ch) ^ key)
      if to_match in translated :
        print("Key %s(0x%x): %s" % (key, key, translated))
        break;

xor_brute_force("lkwpjeia>i}ieglmja", "mymachine")
# should return Key 4 (0x04): hostname: my machine
