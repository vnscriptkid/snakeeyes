from flask import url_for

from lib.tests import ViewTestMixin, assert_status_with_message


class TestPage(object):
    def test_home_page(self, client):
        """ Home page should respond with a success 200. """
        response = client.get(url_for('page.home'))
        assert response.status_code == 200

    def test_terms_page(self, client):
        """ Terms page should respond with a success 200. """
        response = client.get(url_for('page.terms'))
        assert response.status_code == 200

    def test_privacy_page(self, client):
        """ Privacy page should respond with a success 200. """
        response = client.get(url_for('page.privacy'))
        assert response.status_code == 200

    def test_404_page(self, client):
        """ 404 errors should show the custom 404 page. """
        response = client.get('/nochancethispagewilleverexistintheapp')

        assert_status_with_message(404, response, 'Error 404')
