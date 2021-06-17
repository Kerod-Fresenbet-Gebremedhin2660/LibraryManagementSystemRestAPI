def regenerate_address(email: str):
    email = email.replace("%40", "@")
    return email
