from django.forms import ModelForm
from mainapp.models import Request, Review


class RequestForm(ModelForm):

    class Meta:
        model = Request
        fields = ["name", "phone", "case", "region", "app_type", "message"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"
            if field.label == "Сообщение":
                field.widget.attrs["rows"] = 6


class ReviewForm(ModelForm):

    class Meta:
        model = Review
        fields = ["name", "case", "text"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"
            if field.label == "Отзыв":
                field.widget.attrs["rows"] = 6
