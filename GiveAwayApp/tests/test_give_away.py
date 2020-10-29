import pytest


@pytest.mark.django_db
def test_get_landing_page(client, donations, institutions):
    response = client.get('/')
    assert response.status_code == 200
    assert response.context['donations'] == 5
    assert response.context['institutions'] == 5