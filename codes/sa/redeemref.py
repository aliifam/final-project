def redeem_referral(referral_code: str, transaction_id:str):
    try:
        transaction = Transaction.query.filter_by(id=transaction_id).first()
        referrer = User.query.filter_by(username=referral_code).first()
        referred = User.query.filter_by(id=transaction.user_id).first()
        discount_amount = transaction.amount * 0.07
        new_referral = Referral(
            transaction_id=transaction.id,
            referrer_user_id=referrer.id,
            referred_user_id=referred.id,
            referral_code=referral_code,
            discount_amount=discount_amount,
            referrer_income=discount_amount,
        )
        db.session.add(new_referral)
        transaction.amount -= discount_amount
        db.session.commit()
        return discount_amount, referral_code
    except Exception as e:
        logging.error(f"Error rolling back referral: {e}")
        return False