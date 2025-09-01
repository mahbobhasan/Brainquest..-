from sslcommerz_lib import SSLCOMMERZ 
from flask import Flask, request, jsonify, redirect
from sslcommerz_lib import SSLCOMMERZ
from payment_controller import add_new_transaction
from user_controller import get_user_details
from course_controller import get_course_details
from flask import make_response
# SSLCommerz credentials (sandbox for testing)
STORE_ID = "sazib65887285e7dea"
STORE_PASS = "sazib65887285e7dea@ssl"
IS_SANDBOX = True  # Set False for live


def initiate_payment(request:request,connector):

    data = request.form
    final_dict={}
    for key in data.keys():
        final_dict[key]=data[key]
    final_dict['status']='pending'
    res=add_new_transaction(data=final_dict,connector=connector)

    student=get_user_details(cursor=connector.cursor,id=final_dict['user'])

    if res:
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
            'tran_id': data['id'],   # Unique transaction ID
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
    else:
        return res