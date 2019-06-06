import ldap

def main():
    con = ldap.initialize('ldap://35.240.208.53:389')

    user_dn = r"test3@etcg.com"
    password = "q?fUuvodoc<O]{p"

    query = "(&(objectClass=user)(sAMAccountName=khing))"
    attributes = ['displayName', 'company']

    try:
        con.simple_bind_s(user_dn, password)

        res = con.search_s("OU=AD_USER,DC=etcg,DC=com", ldap.SCOPE_SUBTREE, query)
        # username, password = input(), input()
        for i, j in res:
            print(i)
        # 'sAMAccountName':
        # for dn, entry in res:
        #     print(entry)
    except Exception as error:
        print(error)

main()
