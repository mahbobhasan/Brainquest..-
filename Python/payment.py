from sslcommerz_lib import SSLCOMMERZ 
from flask import Flask, request, jsonify, redirect
from sslcommerz_lib import SSLCOMMERZ

# SSLCommerz credentials (sandbox for testing)
STORE_ID = "sazib65887285e7dea"
STORE_PASS = "sazib65887285e7dea@ssl"
IS_SANDBOX = True  # Set False for live


def initiate_payment(request:request):
    data = request.form

    # SSLCommerz settings
    settings = {
        'store_id': STORE_ID,
        'store_pass': STORE_PASS,
        'issandbox': IS_SANDBOX
    }

    sslcz = SSLCOMMERZ(settings)

    # Payment details
    post_body = {
        'total_amount': data['amount'],
        'currency': "BDT",
        'tran_id': data['tran_id'],   # Unique transaction ID
        'success_url': "http://localhost:5000/api/payment-success",
        'fail_url': "http://localhost:5000/api/payment-fail",
        'cancel_url': "http://localhost:5000/api/payment-cancel",
        'emi_option': 0,
        'cus_name': data['name'],
        'cus_email': data['email'],
        'cus_phone': data['phone'],
        'cus_add1': data['address'],
        'cus_city': "Dhaka",
        'cus_country': "Bangladesh",
        'shipping_method': "NO",
        'product_name': data['course_name'],
        'product_category': "Online Course",
        'product_profile': "general"
    }

    response = sslcz.createSession(post_body)
    return jsonify(response)