import unittest
from device.models import HardwareManufacturer, Software, Hardware, SoftwareChoices, HardwareChoices
from api.tests.test_api import api_test


# Device Models
@api_test()
class TestApiHardwareManufacturer():
    str_model = 'device.HardwareManufacturer'
    model = HardwareManufacturer
    url_base = '/api/hardwaremanufacturer/'
    example = {
        'name': 'Manufacturer'
    }

@api_test()
class TestApiHardwareChoices():
    str_model = 'device.HardwareChoices'
    model = SoftwareChoices
    url_base = '/api/hardwarechoices/'
    example = {
        'description': 'Desktop'
    }

@api_test()
class TestApiSoftwareChoices():
    str_model = 'device.SoftwareChoices'
    model = SoftwareChoices
    url_base = '/api/softwarechoices/'
    example = {
        'description': 'Operative System'
    }

@api_test()
class TestApiSoftware():
    fk_models = ['device.SoftwareChoices']
    str_model = 'device.Software'
    model = Software
    url_base = '/api/software/'
    example = {
        'name': 'eventoL',
        'version': 'v2.0'
    }

@api_test()
class TestApiHardware():
    fk_models = ['device.HardwareManufacturer', 'device.HardwareChoices']
    str_model = 'device.Hardware'
    model = Hardware
    url_base = '/api/hardware/'
    example = {
        'model': 'model',
        'serial': '19827398172ASDF'
    }

if __name__ == '__main__':
    unittest.main()
