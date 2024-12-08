class Article:
    def __init__(self, author, magazine, title):
        self._author = author
        self._magazine = magazine
        self._title = title
    @property 
    def title (self):
        return self._title
    @title.setter
    def title (self, title):
        if hasattr(self,"_title"):
            raise Exception("Title cannot be changed")
        else:
            if isinstance(title, str) and (len(title) >= 5 and len(title) <= 50):
                self._title = title
    @property
    def author (self):
        return self._author
    @author.setter
    def author (self,author):
        if isinstance(author, Author):
            self._author = author
    @property 
    def magazine (self):
        return self._magazine
    @magazine.setter
    def magazine (self, magazine):
        if isinstance(magazine, Magazine):
            self._magazine = magazine
class Author:
    def __init__(self, name):
        self._name = name
        self._articles = []
        self._magazines = tuple()
    @property 
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if hasattr(self, "_name"):
            raise Exception("Name cannot be changed")
        else: 
            if isinstance(name, str) and len(name) > 0:
                self._name = name
    def articles(self):
        return self._articles

    def magazines(self):
        return self._magazines
    def add_magazine(self, magazine):
        magazine = Magazine(magazine.name, magazine.category)
        self._magazines.append(magazine)

    def add_article(self, magazine, title):
        article = Article(self, self._name,magazine, title)
        self._articles.append(article)

    def topic_areas(self):
        if len(self._magazines) > 0:
            return [magazine.category for magazine in self._magazines]
        else:
            return None

class Magazine:
    def __init__(self, name, category):
        self._name = name
        self._category = category
        self._articles = []
        self._contributors = []
    @property 
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if (len(name) >=2 and len(name) <= 16) and isinstance(name, str):
            self._name = name
    @property
    def category(self):
        return self._category
    @category.setter
    def category (self, category):
        if isinstance(category, str) and len(category) > 0:
            self._category = category
    def articles(self):
        return self._articles
    def add_article(self, author, title):
        article = Article(self,author, title)
        self._articles.append(article)

    def contributors(self):
        return self._contributors
    def add_contributor(self, author):
        author = Author(author.name)
        self._contributors.append(author)

    def article_titles(self):
        if len(self._articles) > 0:
            return [article.title for article in self._articles]
        else:
            return None

    def contributing_authors(self):
        if len(self._contributors) > 2:
            return [x for x in self._contributors]     
        else:
            return None