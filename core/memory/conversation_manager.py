from config.database import get_db_connection


class ConversationManager:

    def save_conversation(self, query, response):

        print("Saving conversation...")

        conn = get_db_connection()

        cursor = conn.cursor()

        sql = """
        INSERT INTO conversations
        (query, response)
        VALUES (%s, %s)
        """

        cursor.execute(sql, (query, response))

        conn.commit()

        print("Conversation saved!")

        cursor.close()
        conn.close()