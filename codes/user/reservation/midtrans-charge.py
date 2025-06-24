payload = {
    "payment_type": payment_type,
    "transaction_details": {
        "order_id": transaction.id,
        "gross_amount": transaction.gross_amount - referral_discount - voucher_discount
    },
    "item_details": item_details,
    "customer_details" : {
        "first_name": user.name,
        "email": user.email,
        "phone": user.phone
    },  
    "qris": { "acquirer": "gopay" },
    "custom_expiry": {
        "order_time": datetime.fromtimestamp(transaction.created_at, tz=timezone(timedelta(hours=7))).strftime('%Y-%m-%d %H:%M:%S %z'),
        "expiry_duration": transaction_expired_time,
        "unit": "minute"
    }
}
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Authorization": f"Basic {auth_key}",
    "X-Override-Notification": webhook_url
}
response = requests.post(f"{midtrans_url}/charge", json=payload, headers=headers)
response_data = response.json()