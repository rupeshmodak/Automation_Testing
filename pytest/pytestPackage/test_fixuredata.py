import logging

import pytest

from pytestPackage.BaseClass import BaseClass


@pytest.mark.usefixtures("datafixture")
class Testdata(BaseClass):
    def test_data(self, datafixture):
        log = self.getLogger()
        log.info(datafixture[0])
        log.info(datafixture[1])
        log.info(datafixture[2])
        print(datafixture[0])
        print(datafixture[1])
        print(datafixture[2])



