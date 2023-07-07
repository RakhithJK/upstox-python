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

class UserFundMarginData(object):
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
        'used_margin': 'float',
        'payin_amount': 'float',
        'span_margin': 'float',
        'adhoc_margin': 'float',
        'notional_cash': 'float',
        'available_margin': 'float',
        'exposure_margin': 'float'
    }

    attribute_map = {
        'used_margin': 'used_margin',
        'payin_amount': 'payin_amount',
        'span_margin': 'span_margin',
        'adhoc_margin': 'adhoc_margin',
        'notional_cash': 'notional_cash',
        'available_margin': 'available_margin',
        'exposure_margin': 'exposure_margin'
    }

    def __init__(self, used_margin=None, payin_amount=None, span_margin=None, adhoc_margin=None, notional_cash=None, available_margin=None, exposure_margin=None):  # noqa: E501
        """UserFundMarginData - a model defined in Swagger"""  # noqa: E501
        self._used_margin = None
        self._payin_amount = None
        self._span_margin = None
        self._adhoc_margin = None
        self._notional_cash = None
        self._available_margin = None
        self._exposure_margin = None
        self.discriminator = None
        if used_margin is not None:
            self.used_margin = used_margin
        if payin_amount is not None:
            self.payin_amount = payin_amount
        if span_margin is not None:
            self.span_margin = span_margin
        if adhoc_margin is not None:
            self.adhoc_margin = adhoc_margin
        if notional_cash is not None:
            self.notional_cash = notional_cash
        if available_margin is not None:
            self.available_margin = available_margin
        if exposure_margin is not None:
            self.exposure_margin = exposure_margin

    @property
    def used_margin(self):
        """Gets the used_margin of this UserFundMarginData.  # noqa: E501

        Positive values denote the amount blocked into an Open order or position.  Negative value denotes the amount being released.  # noqa: E501

        :return: The used_margin of this UserFundMarginData.  # noqa: E501
        :rtype: float
        """
        return self._used_margin

    @used_margin.setter
    def used_margin(self, used_margin):
        """Sets the used_margin of this UserFundMarginData.

        Positive values denote the amount blocked into an Open order or position.  Negative value denotes the amount being released.  # noqa: E501

        :param used_margin: The used_margin of this UserFundMarginData.  # noqa: E501
        :type: float
        """

        self._used_margin = used_margin

    @property
    def payin_amount(self):
        """Gets the payin_amount of this UserFundMarginData.  # noqa: E501

        Instant payin will reflect here  # noqa: E501

        :return: The payin_amount of this UserFundMarginData.  # noqa: E501
        :rtype: float
        """
        return self._payin_amount

    @payin_amount.setter
    def payin_amount(self, payin_amount):
        """Sets the payin_amount of this UserFundMarginData.

        Instant payin will reflect here  # noqa: E501

        :param payin_amount: The payin_amount of this UserFundMarginData.  # noqa: E501
        :type: float
        """

        self._payin_amount = payin_amount

    @property
    def span_margin(self):
        """Gets the span_margin of this UserFundMarginData.  # noqa: E501

        Amount blocked on futures and options towards SPAN  # noqa: E501

        :return: The span_margin of this UserFundMarginData.  # noqa: E501
        :rtype: float
        """
        return self._span_margin

    @span_margin.setter
    def span_margin(self, span_margin):
        """Sets the span_margin of this UserFundMarginData.

        Amount blocked on futures and options towards SPAN  # noqa: E501

        :param span_margin: The span_margin of this UserFundMarginData.  # noqa: E501
        :type: float
        """

        self._span_margin = span_margin

    @property
    def adhoc_margin(self):
        """Gets the adhoc_margin of this UserFundMarginData.  # noqa: E501

        Payin amount credited through a manual process  # noqa: E501

        :return: The adhoc_margin of this UserFundMarginData.  # noqa: E501
        :rtype: float
        """
        return self._adhoc_margin

    @adhoc_margin.setter
    def adhoc_margin(self, adhoc_margin):
        """Sets the adhoc_margin of this UserFundMarginData.

        Payin amount credited through a manual process  # noqa: E501

        :param adhoc_margin: The adhoc_margin of this UserFundMarginData.  # noqa: E501
        :type: float
        """

        self._adhoc_margin = adhoc_margin

    @property
    def notional_cash(self):
        """Gets the notional_cash of this UserFundMarginData.  # noqa: E501

        The amount maintained for withdrawal  # noqa: E501

        :return: The notional_cash of this UserFundMarginData.  # noqa: E501
        :rtype: float
        """
        return self._notional_cash

    @notional_cash.setter
    def notional_cash(self, notional_cash):
        """Sets the notional_cash of this UserFundMarginData.

        The amount maintained for withdrawal  # noqa: E501

        :param notional_cash: The notional_cash of this UserFundMarginData.  # noqa: E501
        :type: float
        """

        self._notional_cash = notional_cash

    @property
    def available_margin(self):
        """Gets the available_margin of this UserFundMarginData.  # noqa: E501

        Total margin available for trading  # noqa: E501

        :return: The available_margin of this UserFundMarginData.  # noqa: E501
        :rtype: float
        """
        return self._available_margin

    @available_margin.setter
    def available_margin(self, available_margin):
        """Sets the available_margin of this UserFundMarginData.

        Total margin available for trading  # noqa: E501

        :param available_margin: The available_margin of this UserFundMarginData.  # noqa: E501
        :type: float
        """

        self._available_margin = available_margin

    @property
    def exposure_margin(self):
        """Gets the exposure_margin of this UserFundMarginData.  # noqa: E501

        Amount blocked on futures and options towards Exposure  # noqa: E501

        :return: The exposure_margin of this UserFundMarginData.  # noqa: E501
        :rtype: float
        """
        return self._exposure_margin

    @exposure_margin.setter
    def exposure_margin(self, exposure_margin):
        """Sets the exposure_margin of this UserFundMarginData.

        Amount blocked on futures and options towards Exposure  # noqa: E501

        :param exposure_margin: The exposure_margin of this UserFundMarginData.  # noqa: E501
        :type: float
        """

        self._exposure_margin = exposure_margin

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
        if issubclass(UserFundMarginData, dict):
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
        if not isinstance(other, UserFundMarginData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other