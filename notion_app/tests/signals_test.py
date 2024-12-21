import pytest
from notion_app.models import ExampleModel

@pytest.mark.django_db
def test_example_model_save():
    obj = ExampleModel.objects.create(name="Test Signal 2")

    assert ExampleModel.objects.filter(name="Test Signal 2").count() == 1

    assert obj.id is not None
