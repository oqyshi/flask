global_init(input())
session = create_session()
for_print = {}
for user in session.query(User).filter(User.age < 21, User.address == 'module_1').all():
    user.address = 'module_3'
session.commit()
