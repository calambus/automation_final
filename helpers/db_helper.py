from sqlalchemy import create_engine


def clear_db_user_groups_table():
    # engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost/postgres')
    engine = create_engine('postgresql+psycopg2://postgres:postgres@172.18.0.4/postgres')
    engine.execute('TRUNCATE TABLE auth_user_groups CASCADE')


def clear_db_user_not_admin():
    # engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost/postgres')
    engine = create_engine('postgresql+psycopg2://postgres:postgres@172.18.0.4/postgres')
    engine.execute("DELETE FROM auth_user WHERE username != 'admin'")


def check_user_in_group_db(username: str, groupname: str, is_present=True):
    query = f'''
    SELECT aug.id FROM public.auth_user au
    left join public.auth_user_groups aug
        on au.id=aug.user_id 
    left join public.auth_group ag
        on ag.id=aug.group_id 
    WHERE au.username in ('{username}')
        and ag.name in ('{groupname}')
    '''
    # engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost/postgres')
    engine = create_engine('postgresql+psycopg2://postgres:postgres@172.18.0.4/postgres')
    t = engine.execute(query).fetchall()
    assert (len(t) > 0) == is_present, f'{username} not in {groupname}'
