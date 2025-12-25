"""This module contains all test data that is used in test cases related to user operations."""

from faker import Faker

from models.requests.register_user_requests import RegisterUserRequestsModel


class UserData:
    _faker = Faker()

    @property
    def valid_registration_models(self) -> list[RegisterUserRequestsModel]:
        """Returns list with two `RegisterUserRequestsModel` instances.

        One model contains only required fields, another includes optional fields.
        Each property access generates fresh test data.

        Returns:
            list[RegisterUserRequestsModel]: List of two registration models.
        """
        model_with_mandatory_fields = RegisterUserRequestsModel(
            username=self._faker.user_name(),
            email=self._faker.email(),
            password=self._faker.password(),
        )

        model_with_optionals_fields = RegisterUserRequestsModel(
            username=self._faker.user_name(),
            email=self._faker.email(),
            password=self._faker.password(),
            firstName=self._faker.first_name(),
            lastName=self._faker.last_name(),
        )

        return [model_with_mandatory_fields, model_with_optionals_fields]


user_data = UserData()
