from flask import Flask, redirect, request
import urllib.parse

app = Flask(__name__)

# This function ONLY forwards the code+state to your local frontend
@app.route("/api/x_callback")
def x_callback():
    code = request.args.get("code")
    state = request.args.get("state")

    print("Received code:", code)
    print("Received state:", state)

    if not code or not state:
        return "Invalid OAuth callback", 400

    # Forward to your frontend (http)
    frontend_url = "http://localhost:8000/x/callback"

    full_callback_url = request.url
    print("Full Twitter callback URL:", full_callback_url)

    # Reattach code + state
    # redirect_url = f"{frontend_url}?code={urllib.parse.quote(code)}&state={urllib.parse.quote(state)}"

    # Forward original vercel URL to fastapi
    encoded = urllib.parse.quote(full_callback_url)
    redirect_url = f"{frontend_url}?url={encoded}"

    return redirect(redirect_url)
