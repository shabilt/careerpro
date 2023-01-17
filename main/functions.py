import string
import random
from urllib import request
# from django.http import HttpResponse
# from decimal import Decimal
# import urllib.request
import urllib.parse
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from threading import Thread
import requests

# from django.utils.timezone import datetime


# from order.models import Order, OrderItem
from datetime import timedelta

# import requests

class ThreadWithReturnValue(Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs={}, Verbose=None):
        Thread.__init__(self, group, target, name, args, kwargs)
        self._return = None
    def run(self):
        # print(type(self._target))
        if self._target is not None:
            self._return = self._target(*self._args,
                                                **self._kwargs)
    def join(self, *args):
        Thread.join(self, *args)
        return self._return


# def get_client_ip(request):
#     x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
#     if x_forwarded_for:
#         ip = x_forwarded_for.split(',')[0]
#     else:
#         ip = request.META.get('REMOTE_ADDR')
#     return ip


# def generate_unique_id(size=8, chars=string.ascii_lowercase + string.digits):
#     return ''.join(random.choice(chars) for _ in range(size))


# def generate_form_errors(args,formset=False):
#     message = ''
#     if not formset:
#         for field in args:
#             if field.errors:
#                 message += field.errors  + "|"
#         for err in args.non_field_errors():
#             message += str(err) + "|"

#     elif formset:
#         for form in args:
#             for field in form:
#                 if field.errors:
#                     message +=field.errors + "|"
#             for err in form.non_field_errors():
#                 message += str(err) + "|"
#     return message[:-1]


def get_auto_id(model):
    auto_id = 1
    latest_auto_id =  model.objects.all().order_by("-auto_id")[:1]
    if latest_auto_id:
        for auto in latest_auto_id:
            auto_id = auto.auto_id + 1
    return auto_id

# def get_auto_id(model):
#     year = str(datetime.now().date().year)
#     auto_id = "1-" + year
#     if(model.objects.all().exists()):
#         latest_auto_id = model.objects.all().order_by("-date_added").first()
#         arr = str(latest_auto_id.auto_id).split("-")
#         if(arr[1]==year):
#             latest_date = latest_auto_id.date_added
#             instances = model.objects.filter(date_added = latest_date)
#             count = 0
#             for item in instances:
#                 arr = str(latest_auto_id.auto_id).split("-")
#                 if(int(arr[0])>count):
#                     count = arr[0]
#             x = int(count) + 1
#             auto_id =  str(x) + "-" + year  
#     return auto_id


# def get_ref_id(model):
#     ref_id = 1
#     latest_ref_id = model.objects.all().order_by("-ref_id")[:1]
    
#     if latest_ref_id:
#         for ref in latest_ref_id:
#             ref_id = ref.ref_id + 1       
#     return ref_id


# def get_pk_id(model):
#     pk_id = 1
#     latest_pk_id =  model.objects.all().order_by("-date_joined")[:1]
#     if latest_pk_id:
#         for auto in latest_pk_id:
#             pk_id = auto.pk + 1
#     return pk_id



# def get_timezone(request):
#     if "set_user_timezone" in request.session:
#         user_time_zone = request.session['set_user_timezone']
#     else:
#         user_time_zone = "Asia/Kolkata"
#     return user_time_zone
 
# def sendSMS(phone, message,):
    # data =  urllib.parse.urlencode({'apikey': apikey, 'numbers': numbers,
    #     'message' : message, 'sender': sender,})
    # data = data.encode('utf-8')
    # request = urllib.request.Request("https://api.textlocal.in/send/?")
    # f = urllib.request.urlopen(request, data)
    # fr = f.read()

    # print(message)
    # return(True)


# def send_common_mail(html_context,to_email,subject,template):
#     def func(html_context,to_email,subject,template):
#         html_content = render_to_string(template, html_context)
#         r = requests.post('https://mail-sender.vingb.com/custom-mail/c405249d-eb67-43d4-ba0c-c1c24840eeba', data={
#             "to_email": to_email,
#             "subject": subject,
#             "html_data": html_content
#         })
    
#     t1 = ThreadWithReturnValue(target=func,args=(html_context,to_email,subject,template))
#     t1.start()





# def sendSMS(apikey, numbers, sender, message,):
#     data =  urllib.parse.urlencode({'apikey': apikey, 'numbers': numbers,
#         'message' : message, 'sender': sender,})
#     data = data.encode('utf-8')
#     request = urllib.request.Request("https://api.textlocal.in/send/?")
#     f = urllib.request.urlopen(request, data)
#     fr = f.read()
#     return(fr)











def send_common_mail(html_context,to_email,subject):
    def func(html_context,to_email,subject):
        html_content = render_to_string('email_templates/common_template1.html', html_context)
        r = requests.post('https://mail-sender.vingb.com/custom-mail/edf554f6-c207-4ec7-a657-9285913a9a35', data={
            "to_email": to_email,
            "subject": subject,
            "html_data": html_content
        }
        )
    t1 = ThreadWithReturnValue(target=func,args=(html_context,to_email,subject))
    t1.start()



def password_generater(length):
    length = 8
    chars = string.ascii_letters + string.digits + '!@#$%^&*()'
    rnd = random.SystemRandom()
    return(''.join(rnd.choice(chars) for i in range(length)))


