# PDF Sniper

## Extract | Crack | Encrypt | Read 

---

#### NOTES

### DEPENDECIES

#### pdfsniper pdftotext module:

Linux: libpoppler

- ```$ sudo apt-get install libpoppler-cpp-dev```
        
Windows: Microsoft Visual C++ 14.0
- [Get it with Microsoft Visual C++ Build Tools](https://visualstudio.microsoft.com/downloads/)

---

### ISSUES
Decrypt option: 

- Some of encryption algorithm is not supported as per PyPDF2       
- NotImplementedError: only algorithm code 1 and 2 are supported.

Note: 
- Tried on some encrypted pdf and used a well known passwordlist, worked as it should be.

SEE: Issues on these pages.
- github: [PyPDF2 Issue on Github 53](https://github.com/mstamy2/PyPDF2/issues/53)
          [PyPDF2 Issue on Github 378](https://github.com/mstamy2/PyPDF2/issues/378)

stackoverflow:
- [Stackoverflow Algorithm code 1 and 2](https://stackoverflow.com/questions/50751267/only-algorithm-code-1-and-2-are-supported)

---

### DOCUMENTATIONS

- [PyPDF2](https://pythonhosted.org/PyPDF2/PdfFileReader.html)
- [pdftotext](https://pypi.org/project/pdftotext/)


---

### EXAMPLES

* Sample of decrypting a pdf using dictionary
![decrypt sample](https://github.com/catx0rr/python-scripts/blob/master/pdfsniper/images/decrypt.PNG)

* Password has been decrypted using a well known dictionary
![decrypted sample](https://github.com/catx0rr/python-scripts/blob/master/pdfsniper/images/decrypted.PNG)

* Sample of extracted texts inside the pdf file
![extracted sample](https://github.com/catx0rr/python-scripts/blob/master/pdfsniper/images/extracted.PNG)

---

### FUTURE UPDATES 

* Will add a password remover so the text on the file can be extracted. (Maybe)