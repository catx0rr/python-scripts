# PDF Sniper #

### Extract | Crack | Encrypt | Read ###

---

## NOTES ##

### !! DEPENDECIES !! ###
    `pdfsniper pdftotext module:
        Linux: libpoppler
               - sudo apt-get install libpoppler-cpp-dev
        Windows: Microsoft Visual C++ 14.0
               - Get it with "Microsoft Visual C++ Build Tools": https://visualstudio.microsoft.com/downloads/`

---

### !! ISSUES !! ###
    `Decrypt option: Some of encryption algorithm is not supported as per PyPDF2
        NotImplementedError: only algorithm code 1 and 2 are supported.

    Note: Tried on some encrypted pdf and used a well known passwordlist, worked as it should be.

    SEE: Issues on these pages.
        github: https://github.com/mstamy2/PyPDF2/issues/53
                https://github.com/mstamy2/PyPDF2/issues/378

        stackoverflow:
                https://stackoverflow.com/questions/50751267/only-algorithm-code-1-and-2-are-supported`

---

### !! DOCUMENTATIONS !! ###
        `PyPDF2: https://pythonhosted.org/PyPDF2/PdfFileReader.html
        pdftotext: https://pypi.org/project/pdftotext/`


---

### EXAMPLES ###

* Sample of decrypting a pdf using dictionary
![decrypt img sample](images/decrypt.png)

* Password has been decrypted using a well known dictionary
![decrypted img sample](images/decrypted.png)

* Sample of extracted texts inside the pdf file
![extracted img sample](images/extracted.png)

---

### FUTURE UPDATES ###

` Will add a password remover so the text on the file can be extracted.`