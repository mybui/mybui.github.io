```python
from pyspark.sql.session import SparkSession

spark = SparkSession.builder.appName("bookRev").getOrCreate()
```

Read inputs


```python
rating_df = spark.read.load("data/ratings.csv", format="csv", sep=";", inferSchema="true", header="true")
book_df = spark.read.load("data/books.csv", format="csv", sep=";", inferSchema="true", header="true")
user_df = spark.read.load("data/users.csv", format="csv", sep=";", inferSchema="true", header="true")
```

Check schemas


```python
rating_df
```




    DataFrame[User-ID: int, ISBN: string, Book-Rating: int]




```python
book_df
```




    DataFrame[ISBN: string, Book-Title: string, Book-Author: string, Year-Of-Publication: int, Publisher: string, Image-URL-S: string, Image-URL-M: string, Image-URL-L: string]




```python
user_df
```




    DataFrame[User-ID: string, Location: string, Age: string]




```python
spark.sql("SHOW DATABASES").show()
```

    +---------+
    |namespace|
    +---------+
    |  default|
    +---------+
    


Create tables

### 1. Top 5 books receive highest average ratings (must receive at least 100 ratings) 


```python
from pyspark.sql.functions import col

valid_book_df = rating_df.groupBy('ISBN').count().where(col('count') >= 100).select('ISBN')
```

Number of books received at least 100 ratings


```python
valid_book_df.count()
```




    731




```python
from pyspark.sql.functions import desc

top_5 = valid_book_df.join(rating_df, 'ISBN').groupBy('ISBN').avg()\
                     .join(book_df, 'ISBN').sort(desc('avg(Book-Rating)'))\
                     .select('ISBN', 'Book-Title', 'avg(Book-Rating)').show(5)
```

    +----------+--------------------+------------------+
    |      ISBN|          Book-Title|  avg(Book-Rating)|
    +----------+--------------------+------------------+
    |0439064864|Harry Potter and ...|6.6117647058823525|
    |0439139597|Harry Potter and ...| 6.541237113402062|
    |0439136350|Harry Potter and ...| 6.467005076142132|
    |0590353403|Harry Potter and ...| 6.363095238095238|
    |043935806X|Harry Potter and ...|  5.57185628742515|
    +----------+--------------------+------------------+
    only showing top 5 rows
    


### 2. Top 5 U.S. states that review the most books


```python
from pyspark.sql.functions import split, lower

state_df = user_df.withColumn("City", split(col("Location"), ",").getItem(0))\
       .withColumn("State", split(col("Location"), ",").getItem(1))\
       .withColumn("Country", split(col("Location"), ",").getItem(2))\
       .select('User-ID', 'State', 'Country', 'Age')
```


```python
state_df.show(5)
```

    +-------+----------------+---------------+----+
    |User-ID|           State|        Country| Age|
    +-------+----------------+---------------+----+
    |      1|        new york|            usa|NULL|
    |      2|      california|            usa|  18|
    |      3| yukon territory|         russia|NULL|
    |      4|        v.n.gaia|       portugal|  17|
    |      5|           hants| united kingdom|NULL|
    +-------+----------------+---------------+----+
    only showing top 5 rows
    



```python
state_df.filter("Country LIKE '%usa%'").groupBy('State').count().sort(desc('count')).show(5)
```

    +-------------+-----+
    |        State|count|
    +-------------+-----+
    |   california|19663|
    |        texas| 8291|
    |     new york| 7756|
    |      florida| 6928|
    | pennsylvania| 5975|
    +-------------+-----+
    only showing top 5 rows
    


### 3. Top 5 books that receive the most international ratings (count only the number of countries from which they receive their ratings)


```python
rating_df = rating_df.withColumnRenamed('User-ID', 'UserID')
state_df = state_df.withColumnRenamed('User-ID', 'UserID')
book_df = book_df.withColumnRenamed('Book-Title', 'BookTitle')
```


```python
rating_df.createOrReplaceTempView("rating")
state_df.createOrReplaceTempView("state")
book_df.createOrReplaceTempView("book")
```


```python
spark.sql('SHOW TABLES').show()
```

    +--------+---------+-----------+
    |database|tableName|isTemporary|
    +--------+---------+-----------+
    |        |     book|       true|
    |        |   rating|       true|
    |        |    state|       true|
    +--------+---------+-----------+
    



```python
spark.sql("SELECT rating.ISBN, first(BookTitle), COUNT(Country)\
          FROM rating\
          JOIN state\
          ON rating.UserID = state.UserID\
          JOIN book\
          ON rating.ISBN = book.ISBN\
          GROUP BY rating.ISBN\
          ORDER BY COUNT(Country) DESC\
          LIMIT 5").show()
```

    +----------+-----------------------+--------------+
    |      ISBN|first(BookTitle, false)|count(Country)|
    +----------+-----------------------+--------------+
    |0971880107|            Wild Animus|          2502|
    |0316666343|   The Lovely Bones:...|          1295|
    |0385504209|      The Da Vinci Code|           883|
    |0060928336|   Divine Secrets of...|           732|
    |0312195516|   The Red Tent (Bes...|           723|
    +----------+-----------------------+--------------+
    


### 4. What is America's top 5 favourite books?


```python
spark.sql("SELECT rating.ISBN, first(BookTitle) AS Title, COUNT(rating.UserID)\
          FROM rating\
          JOIN state\
          ON rating.UserID = state.UserID\
          JOIN book\
          ON rating.ISBN = book.ISBN\
          WHERE Country LIKE '%usa%'\
          GROUP BY rating.ISBN\
          ORDER BY COUNT(rating.UserID) DESC\
          LIMIT 5").show()
```

    +----------+--------------------+-------------+
    |      ISBN|               Title|count(UserID)|
    +----------+--------------------+-------------+
    |0971880107|         Wild Animus|         1196|
    |0316666343|The Lovely Bones:...|          932|
    |0385504209|   The Da Vinci Code|          704|
    |0060928336|Divine Secrets of...|          594|
    |0312195516|The Red Tent (Bes...|          564|
    +----------+--------------------+-------------+
    

