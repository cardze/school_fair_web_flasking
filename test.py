select_table = {
    'club': '''SELECT * FROM for_web.club_info;''',
    'product': '''SELECT * FROM for_web.product_list;''',
    'user': '''SELECT * FROM for_web.user_db;'''
}
print(str(select_table['club']))
