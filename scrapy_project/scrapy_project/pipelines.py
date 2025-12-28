import sqlite3


class SQLitePipeline:

    def open_spider(self, spider):
        self.connection = sqlite3.connect("../database/data.db")
        self.cursor = self.connection.cursor()

    def close_spider(self, spider):
        self.connection.commit()
        self.connection.close()

    def process_item(self, item, spider):

        if spider.name == "books_spider":
            self.cursor.execute("""
                INSERT INTO books (title, price, availability, rating)
                VALUES (?, ?, ?, ?)
            """, (
                item.get("title"),
                item.get("price"),
                item.get("availability"),
                item.get("rating")
            ))

        elif spider.name == "quotes_spider":
            self.cursor.execute("""
                INSERT INTO quotes (quote, author, tags)
                VALUES (?, ?, ?)
            """, (
                item.get("quote"),
                item.get("author"),
                ",".join(item.get("tags"))
            ))

        return item
