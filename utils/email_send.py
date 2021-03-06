# -*- coding: utf-8 -*-
from random import Random
from django.core.mail import send_mail, get_connection

from account.models import EmailVerifyRecord
from hitol.settings import DEFAULT_FROM_EMAIL

def random_str(randomlength=8):
	str = ''
	chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
	length = len(chars) - 1
	random = Random()
	for i in range(randomlength):
		str += chars[random.randint(0, length)]
	return str

def send_register_email(email, send_type='register'):
	email_record = EmailVerifyRecord()
	if send_type == 'update':
		code = random_str(4)
	else:
		code = random_str(16)
	email_record.code = code
	email_record.email = email
	email_record.send_type = send_type
	email_record.save()

	email_title = ''
	email_body = ''
	if send_type == 'register':
		email_title = '工大在线注册激活链接'
		email_body = '请点击下面的链接激活账户：http://127.0.0.1:8000/active/{0}'.format(code)

		send_status = send_mail(email_title, email_body, DEFAULT_FROM_EMAIL, [email], connection=None)
		if send_status:
			pass
	elif send_type == 'forget':
		email_title = '工大在线重置密码链接'
		email_body = '请点击下面的链接重置密码：http://127.0.0.1:8000/reset/{0}'.format(code)

		send_status = send_mail(email_title, email_body, DEFAULT_FROM_EMAIL, [email])
		if send_status:
			pass
	elif send_type == 'update':
		email_title = '工大在线邮箱修改验证码'
		email_body = '您的邮箱验证码为：{0}'.format(code)

		send_status = send_mail(email_title, email_body, DEFAULT_FROM_EMAIL, [email])
		if send_status:
			pass