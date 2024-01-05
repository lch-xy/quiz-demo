import requests
from bs4 import BeautifulSoup
import pymysql

# 函数：从数据库获取未填写中文意思的单词数据
def get_words_to_update():
    connection = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='mysqlTest@1234',
        database='ielts'
    )

    cursor = connection.cursor()
    query = "SELECT id, en_example FROM vocabulary_words where ch_example is null"
    cursor.execute(query)
    words_to_update = cursor.fetchall()
    cursor.close()
    connection.close()

    return words_to_update

# 函数：获取单词的中文意思
def get_chinese_meaning(word):
    url = f'https://dict.youdao.com/result?word={word}&lang=en'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    trans_containers = soup.find_all('div', class_='trans-container')

    if trans_containers and len(trans_containers) >= 2:
        # 选择第二个trans-container下的所有li元素，然后获取其文本内容
        chinese_meaning = trans_containers[1].find('ul').find_all('li')
        chinese_meaning = '；'.join(li.text.strip() for li in chinese_meaning)
        return chinese_meaning
    else:
        print(f"Could not find translation for the word: {word}")
        return None



# 函数：将单词及其中文意思写入数据库
def write_to_database(word_id, chinese_meaning):
    connection = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='mysqlTest@1234',
        database='ielts'
    )

    cursor = connection.cursor()
    query = "UPDATE vocabulary_words SET ch_example = %s WHERE id = %s"
    cursor.execute(query, (chinese_meaning, word_id))
    connection.commit()

    cursor.close()
    connection.close()

# 主程序
if __name__ == "__main__":
    words_to_update = get_words_to_update()

    for word_info in words_to_update:
        word_id, en_example = word_info
        chinese_meaning = get_chinese_meaning(en_example)
        write_to_database(word_id, chinese_meaning)

