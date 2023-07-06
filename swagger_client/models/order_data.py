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

class OrderData(object):
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
        'exchange': 'str',
        'price': 'float',
        'product': 'str',
        'quantity': 'int',
        'status': 'str',
        'tag': 'str',
        'validity': 'str',
        'average_price': 'float',
        'disclosed_quantity': 'int',
        'exchange_order_id': 'str',
        'exchange_timestamp': 'str',
        'instrument_token': 'str',
        'is_amo': 'bool',
        'status_message': 'str',
        'order_id': 'str',
        'order_request_id': 'str',
        'order_type': 'str',
        'parent_order_id': 'str',
        'tradingsymbol': 'str',
        'order_timestamp': 'str',
        'filled_quantity': 'int',
        'transaction_type': 'str',
        'trigger_price': 'float',
        'placed_by': 'str',
        'variety': 'str'
    }

    attribute_map = {
        'exchange': 'exchange',
        'price': 'price',
        'product': 'product',
        'quantity': 'quantity',
        'status': 'status',
        'tag': 'tag',
        'validity': 'validity',
        'average_price': 'average_price',
        'disclosed_quantity': 'disclosed_quantity',
        'exchange_order_id': 'exchange_order_id',
        'exchange_timestamp': 'exchange_timestamp',
        'instrument_token': 'instrument_token',
        'is_amo': 'is_amo',
        'status_message': 'status_message',
        'order_id': 'order_id',
        'order_request_id': 'order_request_id',
        'order_type': 'order_type',
        'parent_order_id': 'parent_order_id',
        'tradingsymbol': 'tradingsymbol',
        'order_timestamp': 'order_timestamp',
        'filled_quantity': 'filled_quantity',
        'transaction_type': 'transaction_type',
        'trigger_price': 'trigger_price',
        'placed_by': 'placed_by',
        'variety': 'variety'
    }

    def __init__(self, exchange=None, price=None, product=None, quantity=None, status=None, tag=None, validity=None, average_price=None, disclosed_quantity=None, exchange_order_id=None, exchange_timestamp=None, instrument_token=None, is_amo=None, status_message=None, order_id=None, order_request_id=None, order_type=None, parent_order_id=None, tradingsymbol=None, order_timestamp=None, filled_quantity=None, transaction_type=None, trigger_price=None, placed_by=None, variety=None):  # noqa: E501
        """OrderData - a model defined in Swagger"""  # noqa: E501
        self._exchange = None
        self._price = None
        self._product = None
        self._quantity = None
        self._status = None
        self._tag = None
        self._validity = None
        self._average_price = None
        self._disclosed_quantity = None
        self._exchange_order_id = None
        self._exchange_timestamp = None
        self._instrument_token = None
        self._is_amo = None
        self._status_message = None
        self._order_id = None
        self._order_request_id = None
        self._order_type = None
        self._parent_order_id = None
        self._tradingsymbol = None
        self._order_timestamp = None
        self._filled_quantity = None
        self._transaction_type = None
        self._trigger_price = None
        self._placed_by = None
        self._variety = None
        self.discriminator = None
        if exchange is not None:
            self.exchange = exchange
        if price is not None:
            self.price = price
        if product is not None:
            self.product = product
        if quantity is not None:
            self.quantity = quantity
        if status is not None:
            self.status = status
        if tag is not None:
            self.tag = tag
        if validity is not None:
            self.validity = validity
        if average_price is not None:
            self.average_price = average_price
        if disclosed_quantity is not None:
            self.disclosed_quantity = disclosed_quantity
        if exchange_order_id is not None:
            self.exchange_order_id = exchange_order_id
        if exchange_timestamp is not None:
            self.exchange_timestamp = exchange_timestamp
        if instrument_token is not None:
            self.instrument_token = instrument_token
        if is_amo is not None:
            self.is_amo = is_amo
        if status_message is not None:
            self.status_message = status_message
        if order_id is not None:
            self.order_id = order_id
        if order_request_id is not None:
            self.order_request_id = order_request_id
        if order_type is not None:
            self.order_type = order_type
        if parent_order_id is not None:
            self.parent_order_id = parent_order_id
        if tradingsymbol is not None:
            self.tradingsymbol = tradingsymbol
        if order_timestamp is not None:
            self.order_timestamp = order_timestamp
        if filled_quantity is not None:
            self.filled_quantity = filled_quantity
        if transaction_type is not None:
            self.transaction_type = transaction_type
        if trigger_price is not None:
            self.trigger_price = trigger_price
        if placed_by is not None:
            self.placed_by = placed_by
        if variety is not None:
            self.variety = variety

    @property
    def exchange(self):
        """Gets the exchange of this OrderData.  # noqa: E501

        Exchange to which the order is associated  # noqa: E501

        :return: The exchange of this OrderData.  # noqa: E501
        :rtype: str
        """
        return self._exchange

    @exchange.setter
    def exchange(self, exchange):
        """Sets the exchange of this OrderData.

        Exchange to which the order is associated  # noqa: E501

        :param exchange: The exchange of this OrderData.  # noqa: E501
        :type: str
        """
        allowed_values = ["NSE", "NFO", "CDS", "BSE", "BCD", "MCX"]  # noqa: E501
        if exchange not in allowed_values:
            raise ValueError(
                "Invalid value for `exchange` ({0}), must be one of {1}"  # noqa: E501
                .format(exchange, allowed_values)
            )

        self._exchange = exchange

    @property
    def price(self):
        """Gets the price of this OrderData.  # noqa: E501

        Price at which the order was placed  # noqa: E501

        :return: The price of this OrderData.  # noqa: E501
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this OrderData.

        Price at which the order was placed  # noqa: E501

        :param price: The price of this OrderData.  # noqa: E501
        :type: float
        """

        self._price = price

    @property
    def product(self):
        """Gets the product of this OrderData.  # noqa: E501

        Shows if the order was either Intraday, Delivery, CoverOrder or OneCancelsOther  # noqa: E501

        :return: The product of this OrderData.  # noqa: E501
        :rtype: str
        """
        return self._product

    @product.setter
    def product(self, product):
        """Sets the product of this OrderData.

        Shows if the order was either Intraday, Delivery, CoverOrder or OneCancelsOther  # noqa: E501

        :param product: The product of this OrderData.  # noqa: E501
        :type: str
        """
        allowed_values = ["I", "D", "CO", "OCO", "MTF"]  # noqa: E501
        if product not in allowed_values:
            raise ValueError(
                "Invalid value for `product` ({0}), must be one of {1}"  # noqa: E501
                .format(product, allowed_values)
            )

        self._product = product

    @property
    def quantity(self):
        """Gets the quantity of this OrderData.  # noqa: E501

        Quantity with which the order was placed  # noqa: E501

        :return: The quantity of this OrderData.  # noqa: E501
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this OrderData.

        Quantity with which the order was placed  # noqa: E501

        :param quantity: The quantity of this OrderData.  # noqa: E501
        :type: int
        """

        self._quantity = quantity

    @property
    def status(self):
        """Gets the status of this OrderData.  # noqa: E501

        Indicates the current status of the order. Valid order status’ are outlined in the table below  # noqa: E501

        :return: The status of this OrderData.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this OrderData.

        Indicates the current status of the order. Valid order status’ are outlined in the table below  # noqa: E501

        :param status: The status of this OrderData.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def tag(self):
        """Gets the tag of this OrderData.  # noqa: E501

        Tag to uniquely identify an order  # noqa: E501

        :return: The tag of this OrderData.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this OrderData.

        Tag to uniquely identify an order  # noqa: E501

        :param tag: The tag of this OrderData.  # noqa: E501
        :type: str
        """

        self._tag = tag

    @property
    def validity(self):
        """Gets the validity of this OrderData.  # noqa: E501

        Order validity (DAY- Day and IOC- Immediate or Cancel (IOC) order)  # noqa: E501

        :return: The validity of this OrderData.  # noqa: E501
        :rtype: str
        """
        return self._validity

    @validity.setter
    def validity(self, validity):
        """Sets the validity of this OrderData.

        Order validity (DAY- Day and IOC- Immediate or Cancel (IOC) order)  # noqa: E501

        :param validity: The validity of this OrderData.  # noqa: E501
        :type: str
        """
        allowed_values = ["DAY", "IOC"]  # noqa: E501
        if validity not in allowed_values:
            raise ValueError(
                "Invalid value for `validity` ({0}), must be one of {1}"  # noqa: E501
                .format(validity, allowed_values)
            )

        self._validity = validity

    @property
    def average_price(self):
        """Gets the average_price of this OrderData.  # noqa: E501

        Average price at which the qty got traded  # noqa: E501

        :return: The average_price of this OrderData.  # noqa: E501
        :rtype: float
        """
        return self._average_price

    @average_price.setter
    def average_price(self, average_price):
        """Sets the average_price of this OrderData.

        Average price at which the qty got traded  # noqa: E501

        :param average_price: The average_price of this OrderData.  # noqa: E501
        :type: float
        """

        self._average_price = average_price

    @property
    def disclosed_quantity(self):
        """Gets the disclosed_quantity of this OrderData.  # noqa: E501

        The quantity that should be disclosed in the market depth  # noqa: E501

        :return: The disclosed_quantity of this OrderData.  # noqa: E501
        :rtype: int
        """
        return self._disclosed_quantity

    @disclosed_quantity.setter
    def disclosed_quantity(self, disclosed_quantity):
        """Sets the disclosed_quantity of this OrderData.

        The quantity that should be disclosed in the market depth  # noqa: E501

        :param disclosed_quantity: The disclosed_quantity of this OrderData.  # noqa: E501
        :type: int
        """

        self._disclosed_quantity = disclosed_quantity

    @property
    def exchange_order_id(self):
        """Gets the exchange_order_id of this OrderData.  # noqa: E501

        Unique order ID assigned by the exchange for the order placed  # noqa: E501

        :return: The exchange_order_id of this OrderData.  # noqa: E501
        :rtype: str
        """
        return self._exchange_order_id

    @exchange_order_id.setter
    def exchange_order_id(self, exchange_order_id):
        """Sets the exchange_order_id of this OrderData.

        Unique order ID assigned by the exchange for the order placed  # noqa: E501

        :param exchange_order_id: The exchange_order_id of this OrderData.  # noqa: E501
        :type: str
        """

        self._exchange_order_id = exchange_order_id

    @property
    def exchange_timestamp(self):
        """Gets the exchange_timestamp of this OrderData.  # noqa: E501

        User readable time at which the order was placed or updated  # noqa: E501

        :return: The exchange_timestamp of this OrderData.  # noqa: E501
        :rtype: str
        """
        return self._exchange_timestamp

    @exchange_timestamp.setter
    def exchange_timestamp(self, exchange_timestamp):
        """Sets the exchange_timestamp of this OrderData.

        User readable time at which the order was placed or updated  # noqa: E501

        :param exchange_timestamp: The exchange_timestamp of this OrderData.  # noqa: E501
        :type: str
        """

        self._exchange_timestamp = exchange_timestamp

    @property
    def instrument_token(self):
        """Gets the instrument_token of this OrderData.  # noqa: E501

        Identifier issued by Upstox used for subscribing to live market quotes  # noqa: E501

        :return: The instrument_token of this OrderData.  # noqa: E501
        :rtype: str
        """
        return self._instrument_token

    @instrument_token.setter
    def instrument_token(self, instrument_token):
        """Sets the instrument_token of this OrderData.

        Identifier issued by Upstox used for subscribing to live market quotes  # noqa: E501

        :param instrument_token: The instrument_token of this OrderData.  # noqa: E501
        :type: str
        """

        self._instrument_token = instrument_token

    @property
    def is_amo(self):
        """Gets the is_amo of this OrderData.  # noqa: E501

        Signifies if the order is an After Market Order  # noqa: E501

        :return: The is_amo of this OrderData.  # noqa: E501
        :rtype: bool
        """
        return self._is_amo

    @is_amo.setter
    def is_amo(self, is_amo):
        """Sets the is_amo of this OrderData.

        Signifies if the order is an After Market Order  # noqa: E501

        :param is_amo: The is_amo of this OrderData.  # noqa: E501
        :type: bool
        """

        self._is_amo = is_amo

    @property
    def status_message(self):
        """Gets the status_message of this OrderData.  # noqa: E501

        Indicates the reason when any order is rejected, not modified or cancelled  # noqa: E501

        :return: The status_message of this OrderData.  # noqa: E501
        :rtype: str
        """
        return self._status_message

    @status_message.setter
    def status_message(self, status_message):
        """Sets the status_message of this OrderData.

        Indicates the reason when any order is rejected, not modified or cancelled  # noqa: E501

        :param status_message: The status_message of this OrderData.  # noqa: E501
        :type: str
        """

        self._status_message = status_message

    @property
    def order_id(self):
        """Gets the order_id of this OrderData.  # noqa: E501

        Unique order ID assigned internally for the order placed  # noqa: E501

        :return: The order_id of this OrderData.  # noqa: E501
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this OrderData.

        Unique order ID assigned internally for the order placed  # noqa: E501

        :param order_id: The order_id of this OrderData.  # noqa: E501
        :type: str
        """

        self._order_id = order_id

    @property
    def order_request_id(self):
        """Gets the order_request_id of this OrderData.  # noqa: E501

        Apart from 1st order it shows the count of how many requests were sent  # noqa: E501

        :return: The order_request_id of this OrderData.  # noqa: E501
        :rtype: str
        """
        return self._order_request_id

    @order_request_id.setter
    def order_request_id(self, order_request_id):
        """Sets the order_request_id of this OrderData.

        Apart from 1st order it shows the count of how many requests were sent  # noqa: E501

        :param order_request_id: The order_request_id of this OrderData.  # noqa: E501
        :type: str
        """

        self._order_request_id = order_request_id

    @property
    def order_type(self):
        """Gets the order_type of this OrderData.  # noqa: E501

        Type of order. It can be one of the following MARKET refers to market order<br>LIMIT refers to Limit Order<br>SL refers to Stop Loss Limit<br>SL-M refers to Stop loss market  # noqa: E501

        :return: The order_type of this OrderData.  # noqa: E501
        :rtype: str
        """
        return self._order_type

    @order_type.setter
    def order_type(self, order_type):
        """Sets the order_type of this OrderData.

        Type of order. It can be one of the following MARKET refers to market order<br>LIMIT refers to Limit Order<br>SL refers to Stop Loss Limit<br>SL-M refers to Stop loss market  # noqa: E501

        :param order_type: The order_type of this OrderData.  # noqa: E501
        :type: str
        """
        allowed_values = ["MARKET", "LIMIT", "SL", "SL-M"]  # noqa: E501
        if order_type not in allowed_values:
            raise ValueError(
                "Invalid value for `order_type` ({0}), must be one of {1}"  # noqa: E501
                .format(order_type, allowed_values)
            )

        self._order_type = order_type

    @property
    def parent_order_id(self):
        """Gets the parent_order_id of this OrderData.  # noqa: E501

        In case the order is part of the second or third leg of a CO or OCO, the parent order ID is indicated here  # noqa: E501

        :return: The parent_order_id of this OrderData.  # noqa: E501
        :rtype: str
        """
        return self._parent_order_id

    @parent_order_id.setter
    def parent_order_id(self, parent_order_id):
        """Sets the parent_order_id of this OrderData.

        In case the order is part of the second or third leg of a CO or OCO, the parent order ID is indicated here  # noqa: E501

        :param parent_order_id: The parent_order_id of this OrderData.  # noqa: E501
        :type: str
        """

        self._parent_order_id = parent_order_id

    @property
    def tradingsymbol(self):
        """Gets the tradingsymbol of this OrderData.  # noqa: E501

        Shows the trading symbol of the instrument  # noqa: E501

        :return: The tradingsymbol of this OrderData.  # noqa: E501
        :rtype: str
        """
        return self._tradingsymbol

    @tradingsymbol.setter
    def tradingsymbol(self, tradingsymbol):
        """Sets the tradingsymbol of this OrderData.

        Shows the trading symbol of the instrument  # noqa: E501

        :param tradingsymbol: The tradingsymbol of this OrderData.  # noqa: E501
        :type: str
        """

        self._tradingsymbol = tradingsymbol

    @property
    def order_timestamp(self):
        """Gets the order_timestamp of this OrderData.  # noqa: E501

        User readable timestamp at which the order was placed  # noqa: E501

        :return: The order_timestamp of this OrderData.  # noqa: E501
        :rtype: str
        """
        return self._order_timestamp

    @order_timestamp.setter
    def order_timestamp(self, order_timestamp):
        """Sets the order_timestamp of this OrderData.

        User readable timestamp at which the order was placed  # noqa: E501

        :param order_timestamp: The order_timestamp of this OrderData.  # noqa: E501
        :type: str
        """

        self._order_timestamp = order_timestamp

    @property
    def filled_quantity(self):
        """Gets the filled_quantity of this OrderData.  # noqa: E501

        The total quantity traded from this particular order  # noqa: E501

        :return: The filled_quantity of this OrderData.  # noqa: E501
        :rtype: int
        """
        return self._filled_quantity

    @filled_quantity.setter
    def filled_quantity(self, filled_quantity):
        """Sets the filled_quantity of this OrderData.

        The total quantity traded from this particular order  # noqa: E501

        :param filled_quantity: The filled_quantity of this OrderData.  # noqa: E501
        :type: int
        """

        self._filled_quantity = filled_quantity

    @property
    def transaction_type(self):
        """Gets the transaction_type of this OrderData.  # noqa: E501

        Indicates whether the order was a buy or sell order  # noqa: E501

        :return: The transaction_type of this OrderData.  # noqa: E501
        :rtype: str
        """
        return self._transaction_type

    @transaction_type.setter
    def transaction_type(self, transaction_type):
        """Sets the transaction_type of this OrderData.

        Indicates whether the order was a buy or sell order  # noqa: E501

        :param transaction_type: The transaction_type of this OrderData.  # noqa: E501
        :type: str
        """
        allowed_values = ["BUY", "SELL"]  # noqa: E501
        if transaction_type not in allowed_values:
            raise ValueError(
                "Invalid value for `transaction_type` ({0}), must be one of {1}"  # noqa: E501
                .format(transaction_type, allowed_values)
            )

        self._transaction_type = transaction_type

    @property
    def trigger_price(self):
        """Gets the trigger_price of this OrderData.  # noqa: E501

        If the order was a stop loss order then the trigger price set is mentioned here  # noqa: E501

        :return: The trigger_price of this OrderData.  # noqa: E501
        :rtype: float
        """
        return self._trigger_price

    @trigger_price.setter
    def trigger_price(self, trigger_price):
        """Sets the trigger_price of this OrderData.

        If the order was a stop loss order then the trigger price set is mentioned here  # noqa: E501

        :param trigger_price: The trigger_price of this OrderData.  # noqa: E501
        :type: float
        """

        self._trigger_price = trigger_price

    @property
    def placed_by(self):
        """Gets the placed_by of this OrderData.  # noqa: E501

        Uniquely identifies the user  # noqa: E501

        :return: The placed_by of this OrderData.  # noqa: E501
        :rtype: str
        """
        return self._placed_by

    @placed_by.setter
    def placed_by(self, placed_by):
        """Sets the placed_by of this OrderData.

        Uniquely identifies the user  # noqa: E501

        :param placed_by: The placed_by of this OrderData.  # noqa: E501
        :type: str
        """

        self._placed_by = placed_by

    @property
    def variety(self):
        """Gets the variety of this OrderData.  # noqa: E501

        Order complexity  # noqa: E501

        :return: The variety of this OrderData.  # noqa: E501
        :rtype: str
        """
        return self._variety

    @variety.setter
    def variety(self, variety):
        """Sets the variety of this OrderData.

        Order complexity  # noqa: E501

        :param variety: The variety of this OrderData.  # noqa: E501
        :type: str
        """

        self._variety = variety

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
        if issubclass(OrderData, dict):
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
        if not isinstance(other, OrderData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
