import random
from datetime import datetime, timedelta

def generate_card_info():
    # Generate unique card info
    card_number = ''.join([str(random.randint(0, 9)) for _ in range(16)])
    cvv_number = ''.join([str(random.randint(0, 9)) for _ in range(3)])
    exp_date = datetime.now() + timedelta(days=random.randint(30, 365))  # Expiration date within next year
    return {'card_number': card_number, 'cvv_number': cvv_number, 'exp_date': exp_date}