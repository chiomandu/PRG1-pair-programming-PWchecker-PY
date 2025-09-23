
## **Line-Specific Questions:**

**L1 (import datetime):**
- What do you think this line does?
- What happens if we remove this line?

**L3 (OUTPUT_FILE = "./checking_password_log.txt"):**
- What type of data is stored in OUTPUT_FILE?
- What does the "./" at the start mean?
- Why do you think this is defined as a constant at the top rather than inside a function?

**L19 has_upper = any(char.isupper() for char in password):**
- What type of data will be stored in `has_upper`?
- What is the purpose of the line?

## **PREDICT Questions (PRIMM Methodology):**

**Before running the code, predict:**

1. **What will happen when we run the first test?**
   - `print(check_password("ada"))`
   - Will this print True or False? Why?
   - What will be written to the log file?

2. **What will happen when we run the second test?**
   - `print(check_password("AdaLovelace123"))`
   - Will this print True or False? Why?
   - What will be written to the log file?

3. **File behaviour predictions:**
   - What happens if we run the program multiple times?

4. **Function behavior predictions:**
   - What would happen if we called `check_password("")` (empty string)?
   - What would happen with `check_password("PASSWORD")`?
   - What would happen with `check_password("password")`?

5. **Edge case predictions:**
   - What about exactly 8 characters: `check_password("Password")`?
   - What about 9 characters but no uppercase: `check_password("password1")`?
