from django.http import HttpResponse
from django.shortcuts import render

from ldap_test import settings
from ldap import SCOPE_SUBTREE

import ldap

group01 = 0
group02 = 0
group03 = 0

# Create your views here.
# def index(request):
#     global group01
#     global group02
#     global group03
#
#     context = {}
#     context['test'] = 'test'
#     checkgroup = ""
#     if request.method == "POST":
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         usernamenew = username+"@etcg.com"
#         print(username+'  '+password)
#         try:
#             l = ldap.initialize(settings.AUTH_LDAP_SERVER_URI)
#
#             print(l.simple_bind_s(usernamenew, password))
#             ldap_base = "dc=etcg,dc=com"
#             query = "(cn="+username+")"
#             result = l.search_s(ldap_base, ldap.SCOPE_SUBTREE, query)
#             check = result[0][0].find("OU=")
#             for i in range(result[0][0].find("OU=")+3, len(result[0][0])):
#                 checkgroup += (result[0][0][i])
#                 if result[0][0][i+1] == ",":
#                     break
#             print(checkgroup)
#             context['test'] = username
#             context['group'] = checkgroup
#             context['ip'] = get_client_ip(request)
#
#             runLogin(context['ip'], checkgroup)
#
#             if checkgroup == "01_Neighbor":
#                 group01 += 1
#             elif checkgroup == "02_Server":
#                 group02 += 1
#             elif checkgroup == "03_Internet":
#                 group03 += 1
#
#             print(group01)
#             print(group02)
#             print(group03)
#
#
#             return render(request, template_name='siteldap/home.html', context=context)
#         except ldap.LDAPError:
#             context['error'] = 'username or password incorrect'
#             return render(request, template_name='siteldap/index.html', context=context)
#
#     else:
#         usernamenew = username + "@etcg.com"
#         print(username + '  ' + password)
#         return render(request, template_name='siteldap/index.html', context=context)

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def index(req):
    context = {}
    username = "khing"
    print("eiei")
    password = "cash$C0w"
    usernamenew = username+"@etcg.com"
    l = ldap.initialize('ldap://10.148.0.3')
    try:

        print(str(l))
        print(l.simple_bind_s(usernamenew, password))
        ldap_base = "dc=etcg,dc=com"
        criteria = "(&(objectClass=user)(sAMAccountName=username))"
        attributes = ['displayName']
        result = l.search_s(ldap_base, ldap.SCOPE_SUBTREE, criteria, attributes)
        results = [entry for dn, entry in result if isinstance(entry, dict)]
        print(results)
        print("\nzaza\n\n")
        return render(req, 'sso/index.html', context)



    finally:

        l.unbind()

