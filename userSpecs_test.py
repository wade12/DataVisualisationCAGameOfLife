import unittest

from userSpecs import UserSpecs

class TestUserSpecs(unittest.TestCase):

    def setUp(self):
        self.userSpecs = UserSpecs()

    def test_default_constructor(self):
        self.assertEquals(0, self.userSpecs.dice)
        self.assertEquals('null', self.userSpecs.name)
        self.assertEquals('null', self.userSpecs.country)
        self.assertEquals('null', self.userSpecs.gender)
        self.assertEquals(0, self.userSpecs.age)
        self.assertEquals('null', self.userSpecs.status)

    def test_userSpecs_get_methods(self):
        self.assertEquals(0, self.userSpecs.getDice())
        self.assertEquals('null', self.userSpecs.getName())
        self.assertEquals('null', self.userSpecs.getCountry())
        self.assertEquals('null', self.userSpecs.getGender())
        self.assertEquals(0, self.userSpecs.getAge())
        self.assertEquals('null', self.userSpecs.getStatus())
        self.assertEquals(0, self.userSpecs.getElectricity())
        self.assertEquals(0, self.userSpecs.getWater())
        self.assertEquals(0, self.userSpecs.getLess2Dollars())

    def test_userSpecs_set_methods(self):
        self.userSpecs.setDice(47)
        self.assertEquals(47, self.userSpecs.getDice())
        self.userSpecs.setName('Paddy')
        self.assertEquals('Paddy', self.userSpecs.getName())
        self.userSpecs.setCountry('Ireland')
        self.assertEquals('Ireland', self.userSpecs.getCountry())
        self.userSpecs.setGender('male')
        self.assertEquals('male', self.userSpecs.getGender())
        self.userSpecs.setAge(21)
        self.assertEquals(21, self.userSpecs.getAge())
        self.userSpecs.setStatus('single')
        self.assertEquals('single', self.userSpecs.getStatus())
        self.userSpecs.setElectricity(1)
        self.assertEquals(1, self.userSpecs.getElectricity())
        self.userSpecs.setWater(1)
        self.assertEquals(1, self.userSpecs.getWater())
        self.userSpecs.setLess2Dollars(1)
        self.assertEquals(1, self.userSpecs.getLess2Dollars())
        

if __name__ == '__main__':
    unittest.main()

