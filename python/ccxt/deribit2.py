# -*- coding: utf-8 -*-

# PLEASE DO NOT EDIT THIS FILE, IT IS GENERATED AND WILL BE OVERWRITTEN:
# https://github.com/ccxt/ccxt/blob/master/CONTRIBUTING.md#how-to-contribute-code
import json
from ast import literal_eval

from ccxt.base.decimal_to_precision import TICK_SIZE
from ccxt.base.errors import ArgumentsRequired
from ccxt.base.errors import AuthenticationError
from ccxt.base.errors import DDoSProtection
from ccxt.base.errors import ExchangeError
from ccxt.base.errors import ExchangeNotAvailable
from ccxt.base.errors import InsufficientFunds
from ccxt.base.errors import InvalidOrder
from ccxt.base.errors import NotSupported
from ccxt.base.errors import OrderNotFound
from ccxt.base.errors import PermissionDenied
from ccxt.base.exchange import Exchange


class deribit2(Exchange):
    def describe(self):
        return self.deep_extend(super(deribit2, self).describe(), {
            'id': 'deribit2',
            'name': 'Deribit',
            'countries': ['NL'],  # Netherlands
            'version': 'v2',
            'userAgent': None,
            'rateLimit': 2000,
            'has': {
                'CORS': True,
                'editOrder': True,
                'fetchOrder': True,
                'fetchOrders': False,
                'fetchOpenOrders': True,
                'fetchClosedOrders': True,
                'fetchMyTrades': True,
                'fetchTickers': False,
            },
            'urls': {
                'test': 'https://test.deribit.com',
                'logo': 'https://user-images.githubusercontent.com/1294454/'
                        '41933112-9e2dd65a-798b-11e8-8440-5bab2959fcb8.jpg',
                'api': 'https://www.deribit.com',
                'www': 'https://www.deribit.com',
                'doc': [
                    'https://docs.deribit.com',
                    'https://github.com/deribit',
                ],
                'fees': 'https://www.deribit.com/pages/information/fees',
                'referral': 'https://www.deribit.com/reg-1189.4038',
            },
            'api': {
                'public': {
                    'get': [
                        'test',
                        'ticker',
                        'get_time',
                        'get_index',
                        'get_summary',
                        'get_currencies',
                        'get_funding_rate_value',
                        'get_order_book',
                        'get_instruments',
                        'get_trade_volumes',
                        'get_announcements',
                        'get_last_trades_by_instrument',
                    ],
                },
                'private': {
                    'get': [
                        'get_positions',
                        'get_order_state',
                        'get_account_summary',
                        'get_new_announcements',
                        'get_open_orders_by_instrument',
                        'get_user_trades_by_currency',
                        'get_user_trades_by_currency_and_time',
                        'get_user_trades_by_instrument',
                        'get_user_trades_by_instrument_and_time',
                        'get_order_history_by_instrument',
                        'get_stop_order_history',
                        'get_deposits',
                        'get_transfers',
                        'get_withdrawals'
                    ],
                    'post': [
                        'buy',
                        'sell',
                        'edit',
                        'cancel',
                        'cancel_all',
                    ],
                },
            },
            'exceptions': {
                # 0 or absent Success, No error
                '9999': PermissionDenied,  # "api_not_enabled" User didn't enable API for the Account
                '10000': AuthenticationError,
                # "authorization_required" Authorization issue, invalid or absent signature etc
                '10001': ExchangeError,  # "error" Some general failure, no public information available
                '10002': InvalidOrder,  # "qty_too_low" Order quantity is too low
                '10003': InvalidOrder,
                # "order_overlap" Rejection, order overlap is found and self-trading is not enabled
                '10004': OrderNotFound,
                # "order_not_found" Attempt to operate with order that can't be found by specified id
                '10005': InvalidOrder,
                # "price_too_low <Limit>" Price is too low, <Limit> defines current limit for the operation
                '10006': InvalidOrder,
                # "price_too_low4idx <Limit>" Price is too low for current index, <Limit> defines current
                # bottom limit for the operation
                '10007': InvalidOrder,
                # "price_too_high <Limit>" Price is too high, <Limit> defines current up limit for the operation
                '10008': InvalidOrder,
                # "price_too_high4idx <Limit>" Price is too high for current index, <Limit> defines current up
                # limit for the operation
                '10009': InsufficientFunds,  # "not_enough_funds" Account has not enough funds for the operation
                '10010': OrderNotFound,  # "already_closed" Attempt of doing something with closed order
                '10011': InvalidOrder,  # "price_not_allowed" This price is not allowed for some reason
                '10012': InvalidOrder,  # "book_closed" Operation for instrument which order book had been closed
                '10013': PermissionDenied,
                # "pme_max_total_open_orders <Limit>" Total limit of open orders has been exceeded, it is
                # applicable for PME users
                '10014': PermissionDenied,
                # "pme_max_future_open_orders <Limit>" Limit of count of futures' open orders has been exceeded,
                # it is applicable for PME users
                '10015': PermissionDenied,
                # "pme_max_option_open_orders <Limit>" Limit of count of options' open orders has been exceeded,
                # it is applicable for PME users
                '10016': PermissionDenied,
                # "pme_max_future_open_orders_size <Limit>" Limit of size for futures has been exceeded,
                # it is applicable for PME users
                '10017': PermissionDenied,
                # "pme_max_option_open_orders_size <Limit>" Limit of size for options has been exceeded,
                # it is applicable for PME users
                '10019': PermissionDenied,  # "locked_by_admin" Trading is temporary locked by admin
                '10020': ExchangeError,  # "invalid_or_unsupported_instrument" Instrument name is not valid
                '10022': InvalidOrder,  # "invalid_quantity" quantity was not recognized as a valid number
                '10023': InvalidOrder,  # "invalid_price" price was not recognized as a valid number
                '10024': InvalidOrder,  # "invalid_max_show" max_show parameter was not recognized as a valid number
                '10025': InvalidOrder,
                # "invalid_order_id" Order id is missing or its format was not recognized as valid
                '10026': InvalidOrder,  # "price_precision_exceeded" Extra precision of the price is not supported
                '10027': InvalidOrder,
                # "non_integer_contract_amount" Futures contract amount was not recognized as integer
                '10028': DDoSProtection,  # "too_many_requests" Allowed request rate has been exceeded
                '10029': OrderNotFound,  # "not_owner_of_order" Attempt to operate with not own order
                '10030': ExchangeError,  # "must_be_websocket_request" REST request where Websocket is expected
                '10031': ExchangeError,  # "invalid_args_for_instrument" Some of arguments are not recognized as valid
                '10032': InvalidOrder,  # "whole_cost_too_low" Total cost is too low
                '10033': NotSupported,  # "not_implemented" Method is not implemented yet
                '10034': InvalidOrder,  # "stop_price_too_high" Stop price is too high
                '10035': InvalidOrder,  # "stop_price_too_low" Stop price is too low
                '11035': InvalidOrder,  # "no_more_stops <Limit>" Allowed amount of stop orders has been exceeded
                '11036': InvalidOrder,
                # "invalid_stoppx_for_index_or_last" Invalid StopPx (too high or too low) as to current index or market
                '11037': InvalidOrder,
                # "outdated_instrument_for_IV_order" Instrument already not available for trading
                '11038': InvalidOrder,  # "no_adv_for_futures" Advanced orders are not available for futures
                '11039': InvalidOrder,  # "no_adv_postonly" Advanced post-only orders are not supported yet
                '11040': InvalidOrder,  # "impv_not_in_range 0..499%" Implied volatility is out of allowed range
                '11041': InvalidOrder,
                # "not_adv_order" Advanced order properties can't be set if the order is not advanced
                '11042': PermissionDenied,  # "permission_denied" Permission for the operation has been denied
                '11044': OrderNotFound,  # "not_open_order" Attempt to do open order operations with the not open order
                '11045': ExchangeError,  # "invalid_event" Event name has not been recognized
                '11046': ExchangeError,
                # "outdated_instrument" At several minutes to instrument expiration, corresponding advanced implied
                # volatility orders are not allowed
                '11047': ExchangeError,
                # "unsupported_arg_combination" The specified combination of arguments is not supported
                '11048': ExchangeError,  # "not_on_this_server" The requested operation is not available on this server.
                '11050': ExchangeError,  # "invalid_request" Request has not been parsed properly
                '11051': ExchangeNotAvailable,  # "system_maintenance" System is under maintenance
                '11030': ExchangeError,
                # "other_reject <Reason>" Some rejects which are not considered as very often,
                # more info may be specified in <Reason>
                '11031': ExchangeError,
                # "other_error <Error>" Some errors which are not considered as very often,
                # more info may be specified in <Error>
            },
            'precisionMode': TICK_SIZE,
            'options': {
                'fetchTickerQuotes': True,
            },
        })

    @staticmethod
    def get_symbol_to_unified_symbol_dict(markets):
        symbol_to_unified_symbol_dict = dict()
        for market in markets:
            _id, base, quote = market["instrument_name"], market['base_currency'], market['quote_currency']
            tokens = _id.split("-")
            if len(tokens) > 2:
                continue
            identifier = tokens[-1]
            if identifier == "PERPETUAL":
                symbol = base + "/" + quote
            else:
                symbol = base + "/" + identifier
            symbol_to_unified_symbol_dict[symbol] = _id
        return {_id: symbol for symbol, _id in symbol_to_unified_symbol_dict.items()}

    def fetch_markets(self, *args, **kwargs):
        response = self.public_get_get_currencies()
        currencies = self.safe_value(response, 'result')
        all_instruments = list()
        for currency_data in currencies:
            instrument_response = self.public_get_get_instruments({'currency': currency_data['currency']})
            instruments = self.safe_value(instrument_response, 'result')
            all_instruments.extend(instruments)
        result = []
        symbol_to_unified_symbol_dict = self.get_symbol_to_unified_symbol_dict(all_instruments)
        for instrument in all_instruments:
            market = instrument
            _id = self.safe_string(market, 'instrument_name')
            base_id = self.safe_string(market, 'base_currency')
            quote_id = self.safe_string(market, 'quote_currency')
            base = self.common_currency_code(base_id)
            quote = self.common_currency_code(quote_id)
            symbol = symbol_to_unified_symbol_dict.get(_id, _id)
            result.append({
                'id': _id,
                'symbol': symbol,
                'base': base,
                'quote': quote,
                'active': market['is_active'],
                'precision': {
                    'amount': market.get('contract_size', market['min_trade_amount']),
                    'price': market['tick_size'],
                },
                'limits': {
                    'amount': {
                        'min': market['min_trade_amount'],
                    },
                    'price': {
                        'min': market['tick_size'],
                    },
                },
                'type': market['kind'],
                'spot': False,
                'future': market['kind'] == 'future',
                'option': market['kind'] == 'option',
                'info': market,
            })
        return result

    def get_positions(self):
        self.load_markets()
        response = self.public_get_get_currencies()
        currencies = self.safe_value(response, 'result')
        positions_to_return = list()
        for currency_data in currencies:
            positions = self.private_get_get_positions({"currency": currency_data["currency"]})
            for position in positions["result"]:
                liq_price = position["estimated_liquidation_price"]
                size = position["size"]
                if size:
                    result = {'info': position, "symbol": self.find_market(position["instrument_name"])["symbol"],
                              "quantity": abs(position["size"]), "leverage": 0,
                              "maintenance_margin": position["maintenance_margin"],
                              "liquidation_price": max(liq_price, 0)}
                    positions_to_return.append(result)
        return positions_to_return

    def fetch_balance(self, params=None):
        if params is None:
            params = {}
        response = self.public_get_get_currencies()
        currencies = self.safe_value(response, 'result')
        all_instruments_balance = dict()
        for currency_data in currencies:
            instrument_response = self.private_get_get_account_summary({"currency": currency_data["currency"]})
            instrument_balance = self.safe_value(instrument_response, 'result')
            all_instruments_balance[instrument_balance['currency']] = {
                'free': self.safe_float(instrument_balance, 'available_funds'),
                'used': self.safe_float(instrument_balance, 'maintenance_margin'),
                'total': self.safe_float(instrument_balance, 'equity'),
            }
        return self.parse_balance(all_instruments_balance)

    def fetch_deposit_address(self, currency, params=None):
        if params is None:
            params = {}
        response = self.private_get_get_account_summary({'currency': currency})
        address = self.safe_string(response, 'deposit_address')
        return {
            'currency': self.common_currency_code(currency),
            'address': address,
            'tag': None,
            'info': response,
        }

    def parse_ticker(self, ticker, market=None):
        timestamp = self.safe_integer(ticker, 'timestamp')
        symbol = self.find_symbol(self.safe_string(ticker, 'instrument_name'), market)
        last = self.safe_float(ticker, 'last_price')
        stats = self.safe_value(ticker, 'stats')
        return {
            'symbol': symbol,
            'timestamp': timestamp,
            'datetime': self.iso8601(timestamp),
            'high': self.safe_float(ticker, 'high'),
            'low': self.safe_float(ticker, 'low'),
            'bid': self.safe_float(ticker, 'best_bid_price'),
            'bidVolume': None,
            'ask': self.safe_float(ticker, 'best_ask_price'),
            'askVolume': None,
            'vwap': None,
            'open': None,
            'close': last,
            'last': last,
            'previousClose': None,
            'change': None,
            'percentage': None,
            'average': None,
            'baseVolume': None,
            'quoteVolume': self.safe_float(stats, 'volume'),
            'info': ticker,
        }

    def fetch_ticker(self, symbol, params=None):
        if params is None:
            params = {}
        self.load_markets()
        market = self.market(symbol)
        request = {
            'instrument_name': market['id'],
        }
        response = self.public_get_ticker(self.extend(request, params))
        return self.parse_ticker(response['result'], market)

    def parse_trade(self, trade, market=None):
        _id = self.safe_string(trade, 'trade_id')
        order_id = self.safe_string(trade, 'order_id')
        symbol = None
        if market is not None:
            symbol = market['symbol']
        timestamp = self.safe_integer(trade, 'timestamp')
        side = self.safe_string_2(trade, 'side', 'direction')
        price = self.safe_float(trade, 'price')
        amount = self.safe_float(trade, 'amount')
        cost = None
        if amount and price:
            cost = round(amount / price, 8)
        fee = None
        fee_cost = self.safe_float(trade, 'fee')
        if fee_cost is not None:
            fee_currency_id = self.safe_string(trade, 'fee_currency')
            fee_currency_code = self.common_currency_code(fee_currency_id)
            fee = {
                'cost': fee_cost,
                'currency': fee_currency_code,
            }
        return {
            'id': _id,
            'info': trade,
            'timestamp': timestamp,
            'datetime': self.iso8601(timestamp),
            'symbol': symbol,
            'order': order_id,
            'type': None,
            'side': side,
            'takerOrMaker': None,
            'price': price,
            'amount': amount,
            'cost': cost,
            'fee': fee,
        }

    def fetch_trades(self, symbol, since=None, limit=None, params=None):
        if params is None:
            params = {}
        self.load_markets()
        market = self.market(symbol)
        request = {
            'instrument_name': market['id'],
        }
        if limit is not None:
            request['count'] = limit
        else:
            request['count'] = 1000
        response = self.public_get_get_last_trades_by_instrument(self.extend(request, params))
        result = self.safe_value(response, 'result', [])
        trades = self.safe_value(result, 'trades', [])
        return self.parse_trades(trades, market, since, limit)

    def fetch_order_book(self, symbol, limit=None, params=None):
        if params is None:
            params = {}
        self.load_markets()
        market = self.market(symbol)
        request = {
            'instrument_name': market['id'],
        }
        response = self.public_get_get_order_book(self.extend(request, params))
        timestamp = self.nonce()
        order_book = self.parse_order_book(response['result'], timestamp, 'bids', 'asks')
        return self.extend(order_book, {
            'nonce': self.safe_integer(response['result'], 'timestamp'),
        })

    def parse_order_status(self, status):
        statuses = {
            'open': 'open',
            'cancelled': 'canceled',
            'filled': 'closed',
        }
        return self.safe_string(statuses, status, status)

    def parse_order(self, order, market=None):
        timestamp = self.safe_integer(order, 'creation_timestamp')
        last_update = self.safe_integer(order, 'last_update_timestamp')
        last_trade_timestamp = self.safe_integer(order, 'last_update_timestamp')
        _id = self.safe_string(order, 'order_id')
        price = self.safe_float(order, 'stop_price') or self.safe_float(order, 'price')
        average = self.safe_float(order, 'average_price')
        amount = self.safe_float(order, 'amount')
        filled = self.safe_float(order, 'filled_amount') or 0.
        if last_trade_timestamp is None:
            if filled is not None:
                if filled > 0:
                    last_trade_timestamp = last_update
        remaining = None
        cost = None
        if filled is not None:
            if amount is not None:
                remaining = amount - filled
            if price is not None:
                cost = round(amount / (average or price), 8)
        status = self.parse_order_status(self.safe_string(order, 'order_state'))
        side = self.safe_string(order, 'direction')
        if side is not None:
            side = side.lower()
        market_id = self.safe_string(order, 'instrument_name')
        symbol = None
        if market_id in self.markets_by_id:
            market = self.markets_by_id[market_id]
            symbol = market['symbol']
        fee_cost = self.safe_float(order, 'commission')
        if fee_cost is not None:
            fee_cost = abs(fee_cost)
        fee = {
            'cost': fee_cost,
            'currency': symbol.split("/")[0],
        }
        _type = self.safe_string(order, 'order_type')

        return {
            'info': order,
            'id': _id,
            'timestamp': timestamp,
            'datetime': self.iso8601(timestamp),
            'last_trade_timestamp': last_trade_timestamp,
            'symbol': symbol,
            'type': _type,
            'side': side,
            'price': price,
            'amount': amount,
            'cost': cost,
            'average': average,
            'filled': filled,
            'remaining': remaining,
            'status': status,
            'fee': fee,
            'trades': None,  # todo: parse trades
        }

    def fetch_order(self, _id, symbol=None, params=None):
        if params is None:
            params = {}
        self.load_markets()
        request = {
            'order_id': _id,
        }
        response = self.private_get_get_order_state(self.extend(request, params))
        result = self.safe_value(response, 'result')
        if result is None:
            raise OrderNotFound(self.id + ' fetchOrder() ' + self.json(response))
        return self.parse_order(result)

    def create_order(self, symbol, _type, side, amount, price=None, params=None):
        if params is None:
            params = {}
        self.load_markets()
        request = {
            'instrument_name': self.market_id(symbol),
            'amount': amount,
            'type': _type,
            # 'post_only': 'false' or 'true', https://github.com/ccxt/ccxt/issues/5159
        }
        if price is not None:
            request['price'] = price
        method = 'privatePost' + self.capitalize(side)
        response = getattr(self, method)(self.extend(request, params))
        order = self.safe_value(response['result'], 'order')
        if order is None:
            return response
        return self.parse_order(order)

    def edit_order(self, _id, symbol, _type, side, amount=None, price=None, params={}):
        self.load_markets()
        request = {
            'order_id': _id,
        }
        if amount is not None:
            request['amount'] = amount
        if price is not None:
            request['price'] = price
        response = self.private_post_edit(self.extend(request, params))
        result = self.safe_value(response, 'result', [])
        order = self.safe_value(result, 'order', {})
        return self.parse_order(order)

    def cancel_order(self, _id, symbol=None, params=None):
        if params is None:
            params = {}
        self.load_markets()
        request = {
            'order_id': _id,
        }
        response = self.private_post_cancel(self.extend(request, params))
        result = self.safe_value(response, 'result', {})
        return self.parse_order(result)

    def fetch_open_orders(self, symbol=None, since=None, limit=None, params=None):
        if params is None:
            params = {}
        if symbol is None:
            raise ArgumentsRequired(self.id + ' fetchClosedOrders() requires a `symbol` argument')
        self.load_markets()
        market = self.market(symbol)
        request = {
            'instrument_name': market['id'],
        }
        response = self.private_get_get_open_orders_by_instrument(self.extend(request, params))
        result = self.safe_value(response, 'result', [])
        return self.parse_orders(result, market, since, limit)

    def fetch_closed_orders(self, symbol=None, since=None, limit=None, params=None):
        if params is None:
            params = {}
        if symbol is None:
            raise ArgumentsRequired(self.id + ' fetchClosedOrders() requires a `symbol` argument')
        self.load_markets()
        market = self.market(symbol)
        request = {
            'instrument_name': market['id'],
        }
        response = self.private_get_get_order_history_by_instrument(self.extend(request, params))
        result = self.safe_value(response, 'result', [])
        return self.parse_orders(result, market, since, limit)

    def fetch_my_trades(self, symbol=None, since=None, limit=None, params=None):
        if params is None:
            params = {}
        self.load_markets()
        market = self.market(symbol)
        request = {
            'instrument_name': market['id'],
        }
        if limit is not None:
            request['count'] = limit  # default = 20
        response = self.private_get_get_user_trades_by_instrument(self.extend(request, params))
        result = self.safe_value(response, 'result', [])
        trades = self.safe_value(result, 'trades', [])
        return self.parse_trades(trades, market, since, limit)

    def get_stop_order_history(self, symbol):
        self.load_markets()
        currency = "BTC" if symbol.startswith("BTC") else "ETH"
        response = \
            self.private_get_get_stop_order_history({"currency": currency, "instrument_name": self.market_id(symbol)})
        result = self.safe_value(response, 'result', {})
        stops = self.safe_value(result, 'entries', [])
        to_return = list()
        for stop in stops:
            to_return.append(self.parse_stop_order(stop))
        return to_return

    def parse_stop_order(self, order):
        timestamp = self.safe_integer(order, 'timestamp')
        last_trade_timestamp = self.safe_integer(order, 'last_update_timestamp')
        _id = self.safe_string(order, 'order_id')
        stop_id = self.safe_string(order, 'stop_id')
        price = self.safe_float(order, 'price')
        stop_price = self.safe_float(order, 'stop_price')
        amount = self.safe_float(order, 'amount')
        status = self.parse_order_status(self.safe_string(order, 'order_state'))
        side = self.safe_string(order, 'direction')
        market_id = self.safe_string(order, 'instrument_name')
        symbol = None
        if market_id in self.markets_by_id:
            market = self.markets_by_id[market_id]
            symbol = market['symbol']
        return {
            'info': order,
            'id': _id,
            'timestamp': timestamp,
            'datetime': self.iso8601(timestamp),
            'last_trade_timestamp': last_trade_timestamp,
            'symbol': symbol,
            'type': "limit",
            'side': side,
            'price': price,
            'amount': amount,
            'status': status,
            'stop_id': stop_id,
            'stop_price': stop_price
        }

    def nonce(self):
        return self.milliseconds()

    def random_nonce(self, length):
        result = self.hash((self.apiKey + str(self.nonce())).encode(), 'sha512', 'base64')
        return result[:length]

    def sign(self, path, api='public', method='GET', params=None, headers=None, body=''):
        if params is None:
            params = {}
        body = body or ''
        query = '/' + 'api/' + self.version + '/' + api + '/' + path
        url = self.urls['api'] + query
        if api == 'public':
            if params:
                url += '?' + self.urlencode(params)
        else:
            self.check_required_credentials()
            uri = query
            if params:
                uri += '?' + self.urlencode(params)
                params = self.keysort(params)
            if method == "POST" and params:
                uri = query
                data = {"params": dict(params), "method": api + '/' + path}
                body = json.dumps(data)
            timestamp = str(self.nonce())
            random_nonce = self.random_nonce(16).decode()
            request_data = method + '\n' + uri + '\n' + body + '\n'
            string_to_sign = timestamp + '\n' + random_nonce + '\n' + request_data
            signature = self.hmac(self.encode(string_to_sign), self.encode(self.secret), 'sha256')
            header_val = 'deri-hmac-sha256 ' + 'id=' + self.apiKey + ',ts=' + timestamp + ',nonce=' + random_nonce + \
                         ',sig=' + self.encode(signature).decode()
            headers = {
                'Authorization': header_val
            }
            url += '?'
            if method == 'GET' and params:
                url += self.urlencode(params)
        return {'url': url, 'method': method, 'body': body, 'headers': headers}

    def handle_errors(self, http_code, reason, url, method, headers, body, response, request_headers=None, request_body=None):
        if not response:
            return  # fallback to default error handler
        #
        #     {"usOut":1535877098645376,"usIn":1535877098643364,"usDiff":2012,"testnet":false,
        #     "success":false,"message":"order_not_found","error":10004}
        #
        error = self.safe_string(response, 'error')
        if error is not None and error != '0':
            error_dict = literal_eval(error)
            error_code = self.safe_string(error_dict, 'code')
            message = self.safe_string(error_dict, 'message')
            feedback = self.id + ' ' + body
            if 'order_not_found' == message:
                raise OrderNotFound(feedback)
            exceptions = self.exceptions
            if error_code in exceptions:
                raise exceptions[error_code](feedback)
            raise ExchangeError(feedback)  # unknown message

