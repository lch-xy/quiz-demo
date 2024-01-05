import mysql.connector
from mysql.connector import Error
import random
from datetime import datetime

def create_connection():
    """创建MySQL数据库连接"""
    try:
        connection = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='mysqlTest@1234',
            database='ielts'
        )
        if connection.is_connected():
            print("成功连接到MySQL数据库")
            return connection
    except Error as e:
        print(f"连接错误: {e}")
        return None
        
def close_connection(connection):
    """关闭数据库连接"""
    if connection.is_connected():
        connection.close()
        print("关闭数据库连接")


def get_random_phrase(cursor, table_name):
    """从数据库中随机选择一个短语"""
    try:
        cursor.execute(f'SELECT id, ch_example, en_example FROM {table_name} ORDER BY RAND() LIMIT 1')
        result = cursor.fetchone()
        if result is not None:
            return result[0], result[1], result[2]
        else:
            print("数据库中没有短语数据")
            return None, None, None
    except Error as e:
        print(f"查询错误: {e}")
        return None, None, None

def update_review_info_failure(connection, cursor, phrase_id, table_name):
    """更新短语的复习信息"""
    try:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute(f'UPDATE {table_name} SET review_cnt = review_cnt + 1, failure = failure + 1, last_review_date = %s WHERE id = %s', (current_time, phrase_id))
        connection.commit()
    except Error as e:
        print(f"更新错误: {e}")
        

def update_review_info_success(connection, cursor, phrase_id, table_name):
    """更新短语的复习信息"""
    try:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute(f'UPDATE {table_name} SET review_cnt = review_cnt + 1, success = success + 1, last_review_date = %s WHERE id = %s', (current_time, phrase_id))
        connection.commit()
    except Error as e:
        print(f"更新错误: {e}")
       
def choose_review_type():
    """选择复习类型"""
    print("请选择复习类型:")
    print("1. 复习写作")
    print("2. 复习口语")
    print("3. 复习单词")
    
    
    while True:
        choice = input("输入对应数字 (1/2/3): ")
        if choice in ('1', '2', '3'):
            return choice
        else:
            print("无效的输入，请重新输入 (1/2/3)")

def quiz():
    # 选择复习类型
    review_type = choose_review_type()

    # 根据选择的复习类型设置表名
    if review_type == '1':
        table_name = 'writing_phrases'
    elif review_type == '2':
        table_name = 'speaking_phrases'
    elif review_type == '3':
        table_name = 'vocabulary_words'
    else:
        print("无效的选择")
        return

    # 连接到数据库
    connection = create_connection()

    if connection:
        try:
            # 创建一个游标对象
            cursor = connection.cursor()

            while True:
                # 输出一个空行
                print("\n")
                # 随机选择一个短语
                phrase_id, chinese_phrase, correct_english_translation = get_random_phrase(cursor, table_name)

                # 显示中文短语，并获取用户输入的英文翻译
                user_translation = input(f"中文: {chinese_phrase}\n请输入英文翻译 (输入 'exit' 退出): ")

                # 判断用户输入是否为 exit，如果是则退出循环和程序
                if user_translation.lower() == 'exit':
                    break

                # 判断用户输入是否正确
                if user_translation.lower() == correct_english_translation.lower():
                    print("回答正确！")
                    # 更新复习信息
                    update_review_info_success(connection, cursor, phrase_id, table_name)
                else:
                    update_review_info_failure(connection, cursor, phrase_id, table_name)
                    print(f"回答错误，正确答案是: {correct_english_translation}")
                    

                    
        finally:
            # 关闭游标和数据库连接
            cursor.close()
            close_connection(connection)

# 运行程序
if __name__ == "__main__":
    quiz()
