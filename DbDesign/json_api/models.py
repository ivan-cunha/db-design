from django.db import models


class Link(models.Model):
    """Model for storing links related to resources"""

    id = models.AutoField(primary_key=True)
    self = models.URLField(max_length=2048)  # Link to the resource itself
    related = models.URLField(
        max_length=2048, blank=True, null=True
    )  # Link to related resources

    def __str__(self):
        return f"Link(self={self.self}, related={self.related})"


class Person(models.Model):
    """Model for people data"""

    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    twitter = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Comment(models.Model):
    """Model for comments on articles"""

    id = models.AutoField(primary_key=True)
    body = models.TextField()
    author = models.ForeignKey(Person, on_delete=models.CASCADE)
    links = models.OneToOneField(Link, on_delete=models.CASCADE)

    def __str__(self):
        return f"Comment(body={self.body[:20]}...)"


class Article(models.Model):
    """Model for articles"""

    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=255)

    title = models.CharField(max_length=255)
    links = models.OneToOneField(Link, on_delete=models.CASCADE)
    author = models.ForeignKey(Person, on_delete=models.CASCADE)
    comments = models.ManyToManyField(Comment, through="ArticleComment")

    def __str__(self):
        return self.title


class ArticleComment(models.Model):
    """Junction table for Many-to-Many relationship between Article and Comment"""

    id = models.AutoField(primary_key=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)

    class Meta:
        unique_together = (("article", "comment"),)
