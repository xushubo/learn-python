# coding:utf-8
import itchat
import re

itchat.auto_login()

friends = itchat.get_friends(update=True)[0:]
for i in friends:
	print(signature)
