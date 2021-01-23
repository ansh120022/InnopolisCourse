def valid_email(email):
    import re
    return bool(re.search(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", email))


def log(file_name, text):
    with open(file_name, 'a') as f_obj:
        f_obj.write(text)
