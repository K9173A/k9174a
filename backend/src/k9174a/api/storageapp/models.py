import time
import uuid

from django.db import models


def get_current_timestamp() -> int:
    return int(time.time() * 1e6)


def get_uuid4() -> str:
    return str(uuid.uuid4())


class Tag(models.Model):
    title = models.CharField(max_length=64)


class File(models.Model):
    id = models.UUIDField(primary_key=True, default=get_uuid4, editable=False)
    file = models.FileField(null=False)
    description = models.CharField(max_length=512, null=True)
    created_ts = models.BigIntegerField(default=get_current_timestamp)
    modified_ts = models.BigIntegerField(default=get_current_timestamp)
    deleted_ts = models.BigIntegerField(null=True)
    # tags = models.ManyToManyField(to=Tag)

    def __str__(self) -> str:
        return f'{self.file.name} (uuid="{self.id}")'
