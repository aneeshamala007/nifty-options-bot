# filename: nifty_options_bot.py
import streamlit as st
from fyers_api import accessToken, fyersModel
from datetime import datetime
import webbrowser

# ---------- SETTINGS ----------
client_id = "DGRC24PYVS-100"
secret_key = "ZZ552QOS5G"
redirect_uri = "http://127.0.0.1:8080"
response_type = "code"
grant_type = "authorization_code"

# ---------- UI ----------
st.title("📈 NIFTY Options Signal Bot")
capital = st.number_input("Enter capital (₹)", value=10000)
st.markdown("##### Strategy: Trend + Volume + OI")
st.markdown("")

# ---------- AUTH ----------
auth_code = st.text_input("Paste Fyers Auth Code", "")
if st.button("Authenticate"):
    session = accessToken.SessionModel(
        client_id=client_id,
        secret_key=secret_key,
        redirect_uri=redirect_uri,
        response_type=response_type,
        grant_type=grant_type
    )
    session.set_token(auth_code)
    response = session.generate_token()
    access_token = response["access_token"]

    # Create Fyers object
    fyers = fyersModel.FyersModel(client_id=client_id, token=access_token, log_path="")

    st.success("✅ Fyers Authenticated")

    # ---------- BASIC LOGIC ----------
    # Here you fetch NIFTY trend and get ATM CE/PE
    # Let's assume trend is bullish
    trend = "bullish"
    strike = "NSE:NIFTY24516500CE"
    ltp = 120  # mocked, can fetch real
    sl = ltp - 15
    target = ltp + 25
    qty = capital // (ltp * 50)

    st.markdown(f"### ✅ Trade Signal:")
    st.markdown(f"**Type:** Buy {strike}")
    st.markdown(f"**Entry:** ₹{ltp}")
    st.markdown(f"**Target:** ₹{target}")
    st.markdown(f"**Stop Loss:** ₹{sl}")
    st.markdown(f"**Qty:** {qty} (lot size 50)")

    # Chart Embed (TradingView)
    st.components.v1.html('''
        <iframe src="https://in.tradingview.com/widgetembed/?frameElementId=tradingview_0f2e1&symbol=NSE%3ANIFTY&interval=1&hidesidetoolbar=1&symboledit=1&hideideas=1&theme=light&style=1" width="100%" height="400" frameborder="0"></iframe>
    ''', height=400)

