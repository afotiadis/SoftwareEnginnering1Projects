# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.parking_spot import ParkingSpot  # noqa: F401,E501
from swagger_server import util


class SpotOwner(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: int=None, name: str=None, email: str=None, id_number: str=None, phone: float=None, spots: List[ParkingSpot]=None):  # noqa: E501
        """SpotOwner - a model defined in Swagger

        :param id: The id of this SpotOwner.  # noqa: E501
        :type id: int
        :param name: The name of this SpotOwner.  # noqa: E501
        :type name: str
        :param email: The email of this SpotOwner.  # noqa: E501
        :type email: str
        :param id_number: The id_number of this SpotOwner.  # noqa: E501
        :type id_number: str
        :param phone: The phone of this SpotOwner.  # noqa: E501
        :type phone: float
        :param spots: The spots of this SpotOwner.  # noqa: E501
        :type spots: List[ParkingSpot]
        """
        self.swagger_types = {
            'id': int,
            'name': str,
            'email': str,
            'id_number': str,
            'phone': float,
            'spots': List[ParkingSpot]
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'email': 'email',
            'id_number': 'idNumber',
            'phone': 'phone',
            'spots': 'spots'
        }
        self._id = id
        self._name = name
        self._email = email
        self._id_number = id_number
        self._phone = phone
        self._spots = spots

    @classmethod
    def from_dict(cls, dikt) -> 'SpotOwner':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SpotOwner of this SpotOwner.  # noqa: E501
        :rtype: SpotOwner
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this SpotOwner.


        :return: The id of this SpotOwner.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this SpotOwner.


        :param id: The id of this SpotOwner.
        :type id: int
        """

        self._id = id

    @property
    def name(self) -> str:
        """Gets the name of this SpotOwner.


        :return: The name of this SpotOwner.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this SpotOwner.


        :param name: The name of this SpotOwner.
        :type name: str
        """

        self._name = name

    @property
    def email(self) -> str:
        """Gets the email of this SpotOwner.


        :return: The email of this SpotOwner.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email: str):
        """Sets the email of this SpotOwner.


        :param email: The email of this SpotOwner.
        :type email: str
        """

        self._email = email

    @property
    def id_number(self) -> str:
        """Gets the id_number of this SpotOwner.


        :return: The id_number of this SpotOwner.
        :rtype: str
        """
        return self._id_number

    @id_number.setter
    def id_number(self, id_number: str):
        """Sets the id_number of this SpotOwner.


        :param id_number: The id_number of this SpotOwner.
        :type id_number: str
        """

        self._id_number = id_number

    @property
    def phone(self) -> float:
        """Gets the phone of this SpotOwner.


        :return: The phone of this SpotOwner.
        :rtype: float
        """
        return self._phone

    @phone.setter
    def phone(self, phone: float):
        """Sets the phone of this SpotOwner.


        :param phone: The phone of this SpotOwner.
        :type phone: float
        """

        self._phone = phone

    @property
    def spots(self) -> List[ParkingSpot]:
        """Gets the spots of this SpotOwner.


        :return: The spots of this SpotOwner.
        :rtype: List[ParkingSpot]
        """
        return self._spots

    @spots.setter
    def spots(self, spots: List[ParkingSpot]):
        """Sets the spots of this SpotOwner.


        :param spots: The spots of this SpotOwner.
        :type spots: List[ParkingSpot]
        """

        self._spots = spots
