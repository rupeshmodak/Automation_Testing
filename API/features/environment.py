import requests

from utilities.configuration import get_config
from utilities.resourses import APIResources


def after_scenario(context, scenario):
    if "library" in scenario.tags:
        url_delete = get_config()['API']['endpoint'] + APIResources.deleteBook

        response_del = requests.post(url_delete, json={"ID": context.bookID}, headers=context.headers, )
        deletebook = response_del.json()
        print(deletebook)
        assert deletebook['msg'] == 'book is successfully deleted'


