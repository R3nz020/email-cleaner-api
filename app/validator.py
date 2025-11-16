from email_validator import validate_email, EmailNotValidError

def clean_and_validate_emails(email_list):
    cleaned = []
    invalid = []
    for email in email_list:
        original = email
        email = email.strip().lower()
        email = email.replace('\u200b', '')
        email = ''.join(email.split())
        try:
            valid = validate_email(email)
            cleaned.append(valid.email)
        except EmailNotValidError:
            invalid.append(original)
    return cleaned, invalid
    
def extract_domain(email):
    try:
        valid = validate_email(email)
        return valid.normalized.split('@')[1]
    except EmailNotValidError:
        return None    