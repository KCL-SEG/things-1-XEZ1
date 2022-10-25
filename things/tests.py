from django.test import TestCase
from .models import Thing
from django.core.exceptions import ValidationError
from .models import User

class ThinigModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            '@johndoe',
            first_name='John',
            last_name='Doe',
            email='johndoe@example.org',
            password='Password123',
            bio='wag1'
        )
        self.thing = Thing.objects.create(
            name='non-materia',
            description='object of type non-material',
            quantity=1
        )

    def test_valid_thing(self):
        self._assert_thing_is_valid()

##############################

    def test_things_name_cannot_be_blank(self):
        self.thing.name = ''
        self._assert_thing_is_invalid()

    def test_name_cannot_be_more_than_30_characters_long(self):
        self.thing.name = 'x' * 31
        self._assert_thing_is_invalid()

    def test_thing_name_can_be_30_characters_long(self):
        self.thing.name = 'x' * 30
        self._assert_thing_is_valid()

    def test_thingname_must_be_uniqe(self):
        second_thing = self._create_second_thing()
        self.thing.name = second_thing.name
        self._assert_thing_is_invalid()

    def test_thingname_may_contain_numbers(self):
        self.thing.thingname =  '@j0hndoe2'
        self._assert_thing_is_valid()



    def test_things_description_can_be_blank(self):
        self.thing.description = ''
        self._assert_thing_is_valid()

    def test_description_cannot_be_more_than_120_characters_long(self):
        self.thing.description = 'x' * 121
        self._assert_thing_is_invalid()

    def test_thing_description_can_be_120_characters_long(self):
        self.thing.description = 'x' * 120
        self._assert_thing_is_valid()

    def test_thingdescription_can_be_not_uniqe(self):
        second_thing = self._create_second_thing()
        self.thing.description = second_thing.description
        self._assert_thing_is_valid()



    def test_quantity_cannot_be_more_than_120_characters_long(self):
        self.thing.quantity = 101
        self._assert_thing_is_invalid()

    def test_thing_quantity_can_be_0_characters_long(self):
        self.thing.quantity = 0
        self._assert_thing_is_valid()

    def test_thingquantity_can_be_not_uniqe(self):
        second_thing = self._create_second_thing()
        self.thing.quantity = second_thing.quantity
        self._assert_thing_is_valid()



    def test_valid_user(self):
        self._assert_user_is_valid()

    def test_user_name_cannot_be_blank(self):
        self.user.username = ''
        self._assert_user_is_invalid()

    def test_user_name_can_be_30_characters_long(self):
        self.user.username = '@' + 'x' * 29
        self._assert_user_is_valid()

    def test_user_name_cannot_be_over_30_characters_long(self):
        self.user.username = '@' + 'x' * 30
        self._assert_user_is_invalid()

    def test_username_must_be_uniqe(self):
        second_user = self._create_second_user()
        self.user.username = second_user.username
        self._assert_user_is_invalid()

    def test_username_must_start_with_at_symbol(self):
        self.user.username =  'johndoe'
        self._assert_user_is_invalid()

    def test_username_must_contain_only_alphanumericals_after_at(self):
        self.user.username =  '@john!doe'
        self._assert_user_is_invalid()

    def test_username_must_contain_at_least_3_alphanumericals_after_at(self):
        self.user.username =  '@jo'
        self._assert_user_is_invalid()

    def test_username_may_contain_numbers(self):
        self.user.username =  '@j0hndoe2'
        self._assert_user_is_valid()

    def test_username_may_contain_only_one_at(self):
        self.user.username =  '@@johndoe'
        self._assert_user_is_invalid()

    def test_username_must_start_with_at_symbol(self):
        self.user.username =  'johndoe'
        self._assert_user_is_invalid()



    def test_first_name_cannot_be_blank(self):
        self.user.first_name = ''
        self._assert_user_is_invalid()

    def test_first_name_can_be_50_characters_long(self):
        self.user.first_name = 'x' * 50
        self._assert_user_is_valid()

    def test_first_name_cannot_be_over_50_characters_long(self):
        self.user.first_name = 'x' * 51
        self._assert_user_is_invalid()

    def test_first_name_may_already_exist(self):
        second_user = self._create_second_user()
        self.user.first_name =  second_user.first_name
        self._assert_user_is_valid()



    def test_last_name_cannot_be_blank(self):
        self.user.last_name = ''
        self._assert_user_is_invalid()

    def test_last_name_can_be_50_characters_long(self):
        self.user.last_name = 'x' * 50
        self._assert_user_is_valid()

    def test_last_name_cannot_be_over_50_characters_long(self):
        self.user.last_name = 'x' * 51
        self._assert_user_is_invalid()

    def test_last_name_may_already_exist(self):
        second_user = self._create_second_user()
        self.user.last_name =  second_user.last_name
        self._assert_user_is_valid()



    def test_email_cannot_be_blank(self):
        self.user.email = ''
        self._assert_user_is_invalid()

    def test_email_must_be_unique(self):
        second_user = self._create_second_user()
        self.user.email = second_user.email
        self._assert_user_is_invalid()

    def test_email_must_contain_username(self):
        self.user.email = '@example.org'
        self._assert_user_is_invalid()

    def test_email_must_contain_at_symbol(self):
        self.user.email = 'johndoe.example.org'
        self._assert_user_is_invalid()

    def test_email_must_contain_domain_symbol(self):
        self.user.email = 'johndoe@.org'
        self._assert_user_is_invalid()

    def test_email_must_contain_domain(self):
        self.user.email = 'johndoe@example'
        self._assert_user_is_invalid()

    def test_email_must_not_contain_more_than_one_at_symbol(self):
        self.user.email = 'johndoe@@example.org'
        self._assert_user_is_invalid()



    def test_bio_can_be_blank(self):
        self.user.bio = ''
        self._assert_user_is_valid()

    def test_bio_can_be_520_characters_long(self):
        self.user.bio = 'x' * 520
        self._assert_user_is_valid()

    def test_bio_name_cannot_be_over_520_characters_long(self):
        self.user.bio = 'x' * 521
        self._assert_user_is_invalid()

    def test_bio_may_already_exist(self):
        second_user = self._create_second_user()
        self.user.bio = second_user.bio
        self._assert_user_is_valid()



##############################
    def _create_second_thing(self):
        thing = Thing.objects.create(
            name='material',
            description='materail object',
            quantity=1
        )
        return thing

    def _create_second_user(self):
        user = User.objects.create_user(
            '@janedoe',
            first_name='Jane',
            last_name='Doe',
            email='janedoe@example.org',
            password='Password123',
            bio='wag1, the second user here!'
        )
        return user

    def _assert_thing_is_valid(self):
        try:
            self.thing.full_clean()
        except (ValidationError):
            self.fail('Test thing should be valid')

    def _assert_thing_is_invalid(self):
        with self.assertRaises(ValidationError):
            self.thing.full_clean()

    def _assert_user_is_valid(self):
        try:
            self.user.full_clean()
        except (ValidationError):
            self.fail('Test user should be valid')

    def _assert_user_is_invalid(self):
        with self.assertRaises(ValidationError):
            self.user.full_clean()
