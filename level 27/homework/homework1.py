def check_age(age):
    if age >=18:
        return "Access Granted"
    else:
        return "Access Denied"

print(check_age(10))
print(check_age(19))