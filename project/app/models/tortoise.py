# project/app/models/tortoise.py


from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator  # new


class TextSummary(models.Model):
    # Defining `id` field is optional, it will be defined automatically
    # if you haven't done it yourself
    url = fields.TextField()
    summary = fields.TextField()
    created_at = fields.DatetimeField(auto_now_add=True)

    def __str__(self):
        return self.url


SummarySchema = pydantic_model_creator(TextSummary)  # new
