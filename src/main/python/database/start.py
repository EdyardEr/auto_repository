from sqlalchemy import create_engine

'dialect+driver://username:password@host:port/database'
# engine = Engine()
engine = create_engine('sqlite:///sqlite3.db')  # используя относительный путь
print(engine)
print(engine.connect())
print(engine)

# import psycopg2
# from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT # Устанавливаем соединение с postgres
# connection = psycopg2.connect(user="postgres", password="1111")
# connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)#
# Создаем курсор для выполнения операций с базой данныхcursor = connection.cursor()
# sql_create_database = # Создаем базу данных
# cursor.execute('create database sqlalchemy_tuts')# Закрываем соединение
# cursor.close()
# connection.close()

# engine = create_engine('sqlite:////path/to/sqlite3.db')  # абсолютный путь

def main():
    """Main entry point of program"""
    # Подключение к базе данных через SQLAlchemy
    with resources.path(
        "project.data", "author_book_publisher.db"
    ) as sqlite_filepath:
        engine = create_engine(f"sqlite:///{sqlite_filepath}")
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    # Определяем число книг, изданных каждым издательством
    books_by_publisher = get_books_by_publishers(session, ascending=False)
    for row in books_by_publisher:
        print(f"Publisher: {row.name}, total books: {row.total_books}")
    print()

    # Определяем число авторов у каждого издательства
    authors_by_publisher = get_authors_by_publishers(session)
    for row in authors_by_publisher:
        print(f"Publisher: {row.name}, total authors: {row.total_authors}")
    print()

    # Иерархический вывод данных
    authors = get_authors(session)
    output_author_hierarchy(authors)

    # Добавляем новую книгу
    add_new_book(
        session,
        author_name="Stephen King",
        book_title="The Stand",
        publisher_name="Random House",
    )

    # Вывод обновленных сведений
    authors = get_authors(session)
    output_author_hierarchy(authors)