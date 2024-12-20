import sqlite3


class Database:
    def __init__(self, conn_path: str) -> None:
        self.conn = sqlite3.connect(conn_path)
    

    def create_tables(self) -> None:
        cur = self.conn.cursor()

        cur.execute("""
        CREATE TABLE IF NOT EXISTS questions (
            id INTEGER PRIMARY KEY,
            question TEXT,
            answer TEXT
        )
        """)
        cur.execute("""
        CREATE TABLE IF NOT EXISTS times (
            id INTEGER PRIMARY KEY,
            time TEXT,
            is_enable BOOLEAN
        )
        """)

        self.conn.commit()
        cur.close()
    
    def init_values(self) -> None:
        cur = self.conn.cursor()

        cur.execute("""
        INSERT INTO questions (question, answer) VALUES
        ('What is the primary language used for web development?', 'JavaScript'),
        ('Which language is known for its use in data science?', 'Python'),
        ('What is the language used for styling web pages?', 'CSS'),
        ('What is the name of the markup language used to create web pages?', 'HTML'),
        ('Which language is primarily used for iOS app development?', 'Swift'),
        ('What language is commonly used for Android app development?', 'Java'),
        ('What is the language used for server-side scripting in web development?', 'PHP'),
        ('Which language is known for its use in machine learning?', 'Python'),
        ('What language is primarily used for game development?', 'C++'),
        ('Which language is used for creating Windows applications?', 'C#'),
        ('What is the language used for database queries?', 'SQL'),
        ('Which language is known for its simplicity and readability?', 'Python'),
        ('What is the language used for system programming?', 'C'),
        ('Which language is used for writing scripts in web browsers?', 'JavaScript'),
        ('What language is often used for scientific computing?', 'R'),
        ('Which language is used for creating Android apps?', 'Kotlin'),
        ('What is the language used for developing cross-platform mobile apps?', 'Flutter'),
        ('Which language is known for its use in embedded systems?', 'C'),
        ('What is the language used for automating tasks in Excel?', 'VBA'),
        ('Which language is used for writing smart contracts on Ethereum?', 'Solidity'),
        ('What language is commonly used for data analysis?', 'Python'),
        ('Which language is used for creating RESTful APIs?', 'JavaScript'),
        ('What language is used for writing web applications on the server side?', 'Ruby'),
        ('Which language is known for its functional programming features?', 'Haskell'),
        ('What is the language used for writing browser extensions?', 'JavaScript'),
        ('Which language is used for statistical computing?', 'R'),
        ('What language is commonly used for cloud computing?', 'Go'),
        ('Which language is used for writing scripts in Linux?', 'Bash'),
        ('What is the language used for creating graphics and games in browsers?', 'WebGL'),
        ('Which language is used for writing test scripts?', 'Python'),
        ('What is the language used for writing automation scripts for web applications?', 'Selenium'),
        ('Which language is used for writing mobile applications on iOS?', 'Objective-C'),
        ('What is the language used for creating interactive web pages?', 'JavaScript'),
        ('Which language is used for writing configuration files?', 'YAML'),
        ('What is the language used for building microservices?', 'Go'),
        ('Which language is used for writing web APIs?', 'Node.js'),
        ('What is the primary language used for data visualization?', 'JavaScript'),
        ('Which language is used for writing serverless functions?', 'JavaScript'),
        ('What is the language used for writing desktop applications?', 'Electron'),
        ('Which language is known for its use in artificial intelligence?', 'Python'),
        ('What is the language used for writing command-line tools?', 'Rust'),
        ('Which language is used for writing mobile applications on Android?', 'Java'),
        ('What is the language used for creating interactive data visualizations?', 'D3.js'),
        ('Which language is used for writing backend applications?', 'Node.js'),
        ('What is the language used for writing performance-critical applications?', 'C++'),
        ('Which language is commonly used for web scraping?', 'Python'),
        ('What is the language used for writing concurrent applications?', 'Go'),
        ('Which language is used for writing event-driven applications?', 'JavaScript'),
        ('What is the language used for writing data pipelines?', 'Python'),
        ('Which language is used for writing embedded applications?', 'C'),
        ('What is the language used for writing machine learning models?', 'Python'),
        ('Which language is used for writing web servers?', 'Node.js'),
        ('What is the language used for writing mobile applications on iOS?', 'Swift');
        """)

        cur.execute("""
        INSERT INTO times (time, is_enable) VALUES
        ('00:00:00', 0),
        ('00:00:00', 0),
        ('00:00:00', 0);
        """)

        self.conn.commit()
        cur.close()
    
    def get_enables_clocks(self) -> list:
        cur = self.conn.cursor()

        cur.execute("SELECT time FROM times WHERE is_enable = 1")
        data = cur.fetchall()

        cur.close()
        return data
    
    def get_random_question(self) -> tuple[str, str]:
        cur = self.conn.cursor()

        cur.execute("SELECT question, answer FROM questions ORDER BY RANDOM()")
        data = cur.fetchone()

        cur.close()
        return data
    
    def drop_tables(self) -> None:
        cur = self.conn.cursor()

        cur.execute("""
        DROP TABLE IF EXISTS questions;
        """
        )
        cur.execute("""
        DROP TABLE IF EXISTS times;
        """
        )

        self.conn.commit()
        cur.close()
    
    def update_times(self, data) -> None:
        for i in range(3):
            self.update_time(i+1, data[i])
    
    def update_time(self, id: int, data) -> None:
        cur = self.conn.cursor()

        cur.execute("""
        UPDATE times
        SET time = ?, is_enable = ?
        WHERE id = ?;
        """, (data[0], data[1], id)
        )

        self.conn.commit()
        cur.close()

    def close(self) -> None:
        self.conn.close()
