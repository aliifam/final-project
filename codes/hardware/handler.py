def get_pod_key():
    try:
        device_code = request.args.get("device_code")
        if not device_code:
            return jsonify({"error": "device_code is required"}), 400
        pod = Pod.query.filter_by(device_code=device_code).first()
        if not pod:
            return jsonify({"error": "Pod not found"}), 404
        pod.last_online = int(datetime.now().timestamp())
        db.session.commit()
        qrcode = QRCode.query.filter_by(pod_id=pod.id).order_by(QRCode.current_expired.desc()).first()
        response = {
            "qr": []
        }
        if qrcode:
            if qrcode.current_code:
                response["qr"].append({
                    "value": qrcode.current_code,
                    "until": str(qrcode.current_expired),
                })
            if qrcode.next_code:
                response["qr"].append({
                    "value": qrcode.next_code,
                    "until": "",
                })
        master_key = os.getenv("POD_MASTER_KEY")
        if master_key:
            response["qr"].append({
                "value": master_key,
                "until": "",
            })
        return jsonify(response), 200
    except Exception as e:
        logging.error(f"Error in get_pod_key: {e}", exc_info=True)
        return jsonify({"error": "Internal server error"}), 500
