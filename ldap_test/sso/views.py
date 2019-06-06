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
#             ldap_base = "dc=pcnmanage,dc=net"
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


def index(req):
    context = {}
    username = "khing"
    print("eiei")
    password = "FGErok75"
    usernamenew = username+"@etcg.com"

    try:
        l = ldap.initialize('ldap://35.240.208.53')
        print(str(l))
        context['test'] = l.simple_bind(usernamenew, password)
        return render(req, 'sso/index.html', context)


    except ldap.LDAPError:
        context['error'] = 'username and password incorrect'
        print("eiei========================="+context['error'])
        return render(req, 'sso/index.html', context)

