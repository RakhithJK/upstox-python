# coding: utf-8

"""
    Upstox Developer API

    Build your App on the Upstox platform  ![Banner](https://api-v2.upstox.com/api-docs/images/banner.jpg \"banner\")  # Introduction  Upstox API is a set of rest APIs that provide data required to build a complete investment and trading platform. Execute orders in real time, manage user portfolio, stream live market data (using Websocket), and more, with the easy to understand API collection.  All requests are over HTTPS and the requests are sent with the content-type ‘application/json’. Developers have the option of choosing the response type as JSON or CSV for a few API calls.  To be able to use these APIs you need to create an App in the Developer Console and generate your **apiKey** and **apiSecret**. You can use a redirect URL which will be called after the login flow.  If you are a **trader**, you can directly create apps from Upstox mobile app or the desktop platform itself from **Apps** sections inside the **Account** Tab. Head over to <a href=\"http://account.upstox.com/developer/apps\" target=\"_blank\">account.upstox.com/developer/apps</a>.</br> If you are a **business** looking to integrate Upstox APIs, reach out to us and we will get a custom app created for you in no time.  It is highly recommended that you do not embed the **apiSecret** in your frontend app. Create a remote backend which does the handshake on behalf of the frontend app. Marking the apiSecret in the frontend app will make your app vulnerable to threats and potential issues.   # noqa: E501

    OpenAPI spec version: v2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ProfitAndLossChargesData(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'total': 'float',
        'brokerage': 'float',
        'taxes': 'ProfitAndLossChargesTaxes',
        'charges': 'ProfitAndLossOtherChargesTaxes'
    }

    attribute_map = {
        'total': 'total',
        'brokerage': 'brokerage',
        'taxes': 'taxes',
        'charges': 'charges'
    }

    def __init__(self, total=None, brokerage=None, taxes=None, charges=None):  # noqa: E501
        """ProfitAndLossChargesData - a model defined in Swagger"""  # noqa: E501
        self._total = None
        self._brokerage = None
        self._taxes = None
        self._charges = None
        self.discriminator = None
        if total is not None:
            self.total = total
        if brokerage is not None:
            self.brokerage = brokerage
        if taxes is not None:
            self.taxes = taxes
        if charges is not None:
            self.charges = charges

    @property
    def total(self):
        """Gets the total of this ProfitAndLossChargesData.  # noqa: E501

          Total charges for the user  # noqa: E501

        :return: The total of this ProfitAndLossChargesData.  # noqa: E501
        :rtype: float
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ProfitAndLossChargesData.

          Total charges for the user  # noqa: E501

        :param total: The total of this ProfitAndLossChargesData.  # noqa: E501
        :type: float
        """

        self._total = total

    @property
    def brokerage(self):
        """Gets the brokerage of this ProfitAndLossChargesData.  # noqa: E501

        Brokerage charges for the order  # noqa: E501

        :return: The brokerage of this ProfitAndLossChargesData.  # noqa: E501
        :rtype: float
        """
        return self._brokerage

    @brokerage.setter
    def brokerage(self, brokerage):
        """Sets the brokerage of this ProfitAndLossChargesData.

        Brokerage charges for the order  # noqa: E501

        :param brokerage: The brokerage of this ProfitAndLossChargesData.  # noqa: E501
        :type: float
        """

        self._brokerage = brokerage

    @property
    def taxes(self):
        """Gets the taxes of this ProfitAndLossChargesData.  # noqa: E501


        :return: The taxes of this ProfitAndLossChargesData.  # noqa: E501
        :rtype: ProfitAndLossChargesTaxes
        """
        return self._taxes

    @taxes.setter
    def taxes(self, taxes):
        """Sets the taxes of this ProfitAndLossChargesData.


        :param taxes: The taxes of this ProfitAndLossChargesData.  # noqa: E501
        :type: ProfitAndLossChargesTaxes
        """

        self._taxes = taxes

    @property
    def charges(self):
        """Gets the charges of this ProfitAndLossChargesData.  # noqa: E501


        :return: The charges of this ProfitAndLossChargesData.  # noqa: E501
        :rtype: ProfitAndLossOtherChargesTaxes
        """
        return self._charges

    @charges.setter
    def charges(self, charges):
        """Sets the charges of this ProfitAndLossChargesData.


        :param charges: The charges of this ProfitAndLossChargesData.  # noqa: E501
        :type: ProfitAndLossOtherChargesTaxes
        """

        self._charges = charges

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(ProfitAndLossChargesData, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ProfitAndLossChargesData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other