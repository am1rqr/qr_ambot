from tortoise import Model, fields


class TimedModel(Model):
    updated_at = fields.DatetimeField(auto_now=True)
    created_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Users(TimedModel):
    user_id = fields.BigIntField(primary_key=True)
    username = fields.CharField(max_length=32, null=True)
    box_size = fields.IntField(default=10)
    border = fields.IntField(default=4)
    fill_color = fields.CharField(max_length=32, default='black')
    back_color = fields.CharField(max_length=32, default='white')
    file_format = fields.CharField(max_length=7, default='png')
    status = fields.CharField(max_length=6, default='active')  # active, banned