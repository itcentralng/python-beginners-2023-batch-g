# For each of the following string methods,
# explain how it works with an example
# 1. find
text = "this is a boy"
print(text.find('i'))
# 2. format
email_body = "Hello {}, how are you?"
print(email_body.format('Aliyu'))
print(email_body.format('Hauwa'))
# 3. index
text = "this is a boy"
print(text.index('i'))
# 4. isalnum
text = "thisis1boy"
print(text.isalnum())
# 5. isalpha
text = "this is a boy"
print(text.isalpha())
# 6. isdecimal
text = "2"
print(text.isdecimal())
# 6.1 isdigit
text = "2"
print(text.isdigit())
# 7. islower
# 8. isupper
# 9. upper
# 10. lower
# 11. replace
text = "this is a boy"
print(text.replace("this is", "that was"))

text = "Khadija"
print(text.replace("ja", "jat"))
# 12. split
text = "Aliyu Mohammad Nur"
email_body = "Hello {}, how are you?"
print(email_body.format(text.split(" ")[1]))
# 13. strip
text = "Hi "
print(text.strip())
# 14. join
emails = ["user@email.com", "user2@gmail.com", "test@gmail.com"]
t = ";".join(emails)
print(t)
# 15. istitle