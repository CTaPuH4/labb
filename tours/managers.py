from django.db import models


class PublishedManager(models.Manager):
    def published(self):
        return self.select_related(
            'location',
        ).filter(
            location__is_published=True,
            is_published=True,
        )
