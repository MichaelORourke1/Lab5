import Dec2Hex.py

test = {
  "integer": 5,
  "decimal": 5.6789,
  "string": "Hi",
  }

if __name__ == "__main__":
  for i in test:
    try:
      decimal_to_hex(test[i])
      print("SUCCESS: {i} worked.")
    except:
      print("FAIL: {i} did not work.")
  try:
      decimal_to_hex()
      print("SUCCESS: no input worked.")
  except:
    print("FAIL: no input did not work.")
