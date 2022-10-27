import sys

from uuid import uuid4
from datetime import datetime

sys.path.append("..")
from models import db, DF_User


def start_application():
    db_query_select_all()
    print("[NOTICE] Running Function=> [db_query_select_all] Complete !")
    db_query_select_by_name()
    print("[NOTICE] Running Function=> [db_query_select_by_name] Complete !")
    db_query_select_by_limit(10)
    print("[NOTICE] Running Function=> [db_query_select_by_limit] Complete !")


def db_query_select_all():
    result_data_array = db.session.query(DF_User).all()
    print("[RESULT_CONSOLE] Result_Data => [%s]" % str(result_data_array))
    print("####################################################################################")
    print("[CONSOLE] DB Query Select Successfuly ! Please Check at DBeaver ^_^")
    print("####################################################################################")


def db_query_select_by_name():
    result_data_array = db.session.query(DF_User).filter_by(df_user_name='ryan').all()
    print("[RESULT_CONSOLE] Result_Data => [%s]" % str(result_data_array))
    print("####################################################################################")
    print("[CONSOLE] DB Query Select Successfuly ! Please Check at DBeaver ^_^")
    print("####################################################################################")


def db_query_select_by_limit(result_number):
    result_data_array = db.session.query(DF_User).order_by(DF_User.df_user_name).limit(result_number).all()
    print("[RESULT_CONSOLE] Result_Data => [%s]" % str(result_data_array))
    print("####################################################################################")
    print("[CONSOLE] DB Query Select Successfuly ! Please Check at DBeaver ^_^")
    print("####################################################################################")


def main():
    print("====================================================================================")
    print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
    print("####################################################################################")
    start_application()
    print("####################################################################################")
    print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
    print("====================================================================================")


if __name__ == '__main__':
    main()
