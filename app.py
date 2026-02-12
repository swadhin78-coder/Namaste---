from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create-payment', methods=['POST'])
def create_payment():
    data = request.json
    amount = data.get('amount')
    item = data.get('item')
    
    # এখানে SSLCommerz বা Bkash API লিঙ্ক জেনারেট করবেন
    # আপাতত আমরা টেস্ট করার জন্য একটি ডামি সাকসেস ইউআরএল দিচ্ছি
    payment_url = "https://your-payment-gateway-link.com" 
    
    return jsonify({"payment_url": payment_url})

if __name__ == '__main__':
    app.run(debug=True)