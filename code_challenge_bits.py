# ==========================================
# Caesar cipher.
# ==========================================
text = input("Enter your message: ")
cipher = ''
for char in text:
   if not char.isalpha():
       continue
   char = char.upper()
   code = ord(char) + 1
   if code > ord('Z'):
       code = ord('A')
   cipher += chr(code)
print(cipher)

# ==========================================
# Numbers Processor.
# ==========================================
while True:  # Loop until we break out
   line = input("Enter a line of numbers - separate them with spaces: ")
   strings = line.split()
   total = 0
   
   if strings:
       try:
           for substr in strings:
               total += float(substr)
           print("The total is:", total)
           break  # Exit the loop when successful
       except:
           print(substr, "is not a number.")
           # Loop continues, asks for input again
   else: 
       print("Please enter a number.")
       # Loop continues, asks for input again

# ==========================================
# IBAN Validator - ISO 13616 Implementation
# ==========================================
"""
The IBAN validation algorithm verifies the mathematical integrity of International Bank Account Numbers to prevent banking errors and fraud.
"""
iban = input("Enter IBAN, please: ")
iban = iban.replace(' ','')  # Remove formatting spaces

# Input validation
if not iban.isalnum():  # Check alphanumeric only
   print("You have entered invalid characters.")
elif len(iban) < 15:  # Minimum IBAN length check
   print("IBAN entered is too short.")
elif len(iban) > 31:  # Maximum IBAN length check
   print("IBAN entered is too long.")
else:
   # Step 1: Move first 4 characters to end per ISO 13616 spec
   iban = (iban[4:] + iban[0:4]).upper()
   
   # Step 2: Convert letters to numeric representation (A=10, B=11, etc.)
   iban2 = ''
   for ch in iban:
       if ch.isdigit():
           iban2 += ch  # Keep digits as-is
       else:
           # ASCII arithmetic: ord(ch) - ord('A') + 10
           # Maps A->10, B->11, C->12, ..., Z->35
           iban2 += str(10 + ord(ch) - ord('A'))
   
   # Step 3: Apply mod-97 checksum algorithm
   iban = int(iban2)
   if iban % 97 == 1:  # Valid IBAN remainder must equal 1
       print("IBAN entered is valid.")
   else:
       print("IBAN entered is invalid.")