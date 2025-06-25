def validate_referral_code(referral_code: str, transaction_id: str) -> bool:
    try:
        transaction = Transaction.query.filter_by(id=transaction_id).first()
        user_referring = User.query.filter_by(username=referral_code).first()
        referral = Referral.query.filter_by(transaction_id=transaction.id).first()
        if referral:
            return False
        if user_referring.id == transaction.user_id:
            return False
        if not user_referring:
            logging.info(f"Referral code {referral_code} not found.")
            return False
        user_referring_status = Kyc.query.filter_by(user_id=user_referring.id).first()
        if not user_referring_status:
            logging.info(f"User {user_referring.username} has no KYC status.")
            return False
        if user_referring_status.status != KYCStatusEnum.APPROVED:
            logging.info(f"User {user_referring.username} has not been approved for KYC.")
            return False
        return True
    except Exception as e:
        logging.error(f"Error validating referral code: {e}")
        return False