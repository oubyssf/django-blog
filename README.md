# Blog Project with Django and django-taggit

This project is a simple blog built with Django, incorporating functionality for tagging blog posts using the `django-taggit` library. It also includes features like full-text search, post filtering by tags, sitemaps for SEO, and a well-structured layout.

## Features

- **Blog Post Management**: Create, edit, and display blog posts.
- **Tagging System**: Use `django-taggit` to categorize posts with tags.
- **Tag Filtering**: Users can view posts filtered by specific tags.
- **Full-Text Search**: Powered by PostgreSQL's full-text search capabilities via `django.contrib.postgres.search`, allowing users to search for posts by title or content.
- **Sitemap Support**: Automatically generates a sitemap of the blog posts and tag-filtered pages for SEO purposes.