email = input("Enter your email : ").strip()

username = email[:email.index('@')]
domain = email[email.index('@')+1:]

print('Your username is : '+username)
print('Your domain name is : '+domain)
