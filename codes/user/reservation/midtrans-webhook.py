if not all([order_id, transaction_status, fraud_status, signature_key_from_midtrans]):
    return jsonify({"error": "Invalid notification data"}), 400
recalculated_signature = hashlib.sha512(f"{order_id}{status_code}{gross_amount}{server_key}".encode()).hexdigest()
if recalculated_signature != signature_key_from_midtrans:
    logging.error(f"Signature mismatch from Midtrans: {recalculated_signature} != {signature_key_from_midtrans}")
    return jsonify({"error": "Invalid signature"}), 400
logging.info(f"Recalculated signature: {recalculated_signature} match with {signature_key_from_midtrans}")
transaction = Transaction.query.filter_by(id=order_id).first()
bookings = Booking.query.filter_by(transaction_id=order_id).all()
if not transaction:
    return jsonify({"message": "Transaction not found"}), 404