import ldap

def main():
    con = ldap.initialize('ldap://35.240.208.53:389')

    user_dn = "test3@etcg.com"
    password = "q?fUuvodoc<O]{p"

    criteria = "(&(objectClass=user)(sAMAccountName=username))"
    attributes = ['displayName', 'company']

    try:
        con.simple_bind_s(user_dn, password)
        res = con.search_s("OU=AD_USER,DC=etcg,DC=com", ldap.SCOPE_SUBTREE, '(objectClass=User)')
        for dn, entry in res:
            print(dn)
    except Exception as error:
        print(error)

main()
