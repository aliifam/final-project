def google_login():
    try:
        GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
        GOOGLE_REDIRECT_URI = os.getenv("GOOGLE_USER_REDIRECT_URI")
        google_auth_url = (
            "https://accounts.google.com/o/oauth2/auth"
            "?response_type=code"
            f"&client_id={GOOGLE_CLIENT_ID}"
            f"&redirect_uri={GOOGLE_REDIRECT_URI}"
            "&scope=openid%20email%20profile"
        )
        return redirect(google_auth_url)
    except Exception as e:
        logging.error(f"Error in google_login: {e}")
        return jsonify({"message": "Internal server error"}), 500

def google_callback():
    try:
        code = request.args.get("code")
        if not code:
            return jsonify({"message": "Code not provided"}), 400
        # change code with access token
        token_url = "https://oauth2.googleapis.com/token"
        GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
        GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")
        GOOGLE_REDIRECT_URI = os.getenv("GOOGLE_USER_REDIRECT_URI")
        token_data ={
            "code": code,
            "client_id": GOOGLE_CLIENT_ID,
            "client_secret": GOOGLE_CLIENT_SECRET,
            "redirect_uri": GOOGLE_REDIRECT_URI,
            "grant_type": "authorization_code"
        }
        token_response = requests.post(token_url, data=token_data)
        token_data = token_response.json()
        access_token = token_data.get("access_token")
        if not access_token:
            return jsonify({"message": "Invalid code"}), 400
        
        # get user info
        user_info_res = requests.get(
            "https://www.googleapis.com/oauth2/v1/userinfo",
            headers={"Authorization": f"Bearer {access_token}"},
        )
        user_info = user_info_res.json()
        email = user_info.get("email")
        
        user = User.query.filter_by(email=email).first()
        token = str(uuid.uuid4())
        new_token = Token(token=token, email=email)
        db.session.add(new_token)
        db.session.commit()
        return redirect(f"{os.getenv('FRONTEND')}/sso?token={token}")
    except Exception as e:
        logging.error(f"Error in google_callback: {e}")
        return jsonify({"message": "Internal server error"}), 500