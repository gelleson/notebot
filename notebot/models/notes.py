from enum import Enum

from tortoise import fields
from tortoise.models import Model


class NoteType(str, Enum):
    TEXT = "text"
    URL = "url"


class Note(Model):
    id = fields.IntField(pk=True)
    owner = fields.ForeignKeyField(
        "models.User",
        related_name="notes",
        on_delete=fields.CASCADE,
    )

    note = fields.TextField()
    note_type = fields.CharEnumField(NoteType, default=NoteType.TEXT)
    tags: fields.ReverseRelation['TagNote']

    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "notes"
        ordering = ("-created_at",)


class Tag(Model):
    name = fields.CharField(pk=True, max_length=255)

    notes: fields.ReverseRelation['TagNote']

    class Meta:
        table = "tags"
        ordering = ("name",)


class TagNote(Model):
    tag = fields.ForeignKeyField(
        "models.Tag",
        related_name="notes",
        on_delete=fields.CASCADE,
    )
    note = fields.ForeignKeyField(
        "models.Note",
        related_name="tags",
        on_delete=fields.CASCADE,
    )

    class Meta:
        table = "tag_notes"
        unique_together = ("tag", "note")
