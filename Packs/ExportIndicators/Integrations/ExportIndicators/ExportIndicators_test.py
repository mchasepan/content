"""Imports"""
import json
import pytest
import demistomock as demisto

IOC_RES_LEN = 38

'''Tests'''


@pytest.mark.helper_commands
class TestHelperFunctions:
    @pytest.mark.get_outbound_ioc_values
    def test_get_outbound_ioc_values_1(self, mocker):
        """Test on_demand"""
        from ExportIndicators import get_outbound_ioc_values, RequestArguments
        with open('ExportIndicators_test/TestHelperFunctions/iocs_cache_values_text.json', 'r') as iocs_text_values_f:
            iocs_text_dict = json.loads(iocs_text_values_f.read())
            mocker.patch.object(demisto, 'getIntegrationContext', return_value={"last_output": iocs_text_dict})
            request_args = RequestArguments(query='', out_format='text', limit=50, offset=0)
            ioc_list = get_outbound_ioc_values(
                on_demand=True,
                request_args=request_args
            )
            for ioc_row in ioc_list:
                assert ioc_row in iocs_text_dict

    @pytest.mark.get_outbound_ioc_values
    def test_get_outbound_ioc_values_2(self, mocker):
        """Test update by not on_demand with no refresh"""
        import CommonServerPython as CSP
        mocker.patch.object(CSP, 'parse_date_range', return_value=(1578383899, 1578383899))
        import ExportIndicators as ei
        with open('ExportIndicators_test/TestHelperFunctions/iocs_cache_values_text.json', 'r') as iocs_text_values_f:
            iocs_text_dict = json.loads(iocs_text_values_f.read())
            mocker.patch.object(demisto, 'getIntegrationContext', return_value={"last_output": iocs_text_dict})
            mocker.patch.object(ei, 'refresh_outbound_context', return_value=iocs_text_dict)
            mocker.patch.object(demisto, 'getLastRun', return_value={'last_run': 1578383898000})
            request_args = ei.RequestArguments(query='', out_format='text', limit=50, offset=0)
            ioc_list = ei.get_outbound_ioc_values(
                on_demand=False,
                request_args=request_args,
                cache_refresh_rate='1 minute'
            )
            for ioc_row in ioc_list:
                assert ioc_row in iocs_text_dict

    @pytest.mark.get_outbound_ioc_values
    def test_get_outbound_ioc_values_3(self, mocker):
        """Test update by not on_demand with refresh"""
        import CommonServerPython as CSP
        mocker.patch.object(CSP, 'parse_date_range', return_value=(1578383898, 1578383898))
        import ExportIndicators as ei
        with open('ExportIndicators_test/TestHelperFunctions/iocs_cache_values_text.json', 'r') as iocs_text_values_f:
            iocs_text_dict = json.loads(iocs_text_values_f.read())
            mocker.patch.object(demisto, 'getIntegrationContext', return_value={"last_output": iocs_text_dict})
            mocker.patch.object(ei, 'refresh_outbound_context', return_value=iocs_text_dict)
            mocker.patch.object(demisto, 'getLastRun', return_value={'last_run': 1578383898000})
            request_args = ei.RequestArguments(query='', out_format='text', limit=50, offset=0)
            ioc_list = ei.get_outbound_ioc_values(
                on_demand=False,
                request_args=request_args,
                cache_refresh_rate='1 minute'
            )
            for ioc_row in ioc_list:
                assert ioc_row in iocs_text_dict

    @pytest.mark.get_outbound_ioc_values
    def test_get_outbound_ioc_values_4(self, mocker):
        """Test update by request params change - limit"""
        import CommonServerPython as CSP
        mocker.patch.object(CSP, 'parse_date_range', return_value=(1578383898, 1578383898))
        import ExportIndicators as ei
        with open('ExportIndicators_test/TestHelperFunctions/iocs_cache_values_text.json', 'r') as iocs_text_values_f:
            iocs_text_dict = json.loads(iocs_text_values_f.read())
            mocker.patch.object(demisto, 'getIntegrationContext', return_value={"last_output": iocs_text_dict,
                                                                                "last_limit": 1, "last_offset": 0,
                                                                                "last_query": "type:ip",
                                                                                "last_format": "text"})
            mocker.patch.object(ei, 'refresh_outbound_context', return_value=iocs_text_dict)
            mocker.patch.object(demisto, 'getLastRun', return_value={'last_run': 1578383898000})
            request_args = ei.RequestArguments(query='type:ip', out_format='text', limit=50, offset=0)
            ioc_list = ei.get_outbound_ioc_values(
                on_demand=False,
                request_args=request_args,
                cache_refresh_rate='1 minute'
            )
            for ioc_row in ioc_list:
                assert ioc_row in iocs_text_dict

    @pytest.mark.get_outbound_ioc_values
    def test_get_outbound_ioc_values_5(self, mocker):
        """Test update by request params change - offset"""
        import CommonServerPython as CSP
        mocker.patch.object(CSP, 'parse_date_range', return_value=(1578383898, 1578383898))
        import ExportIndicators as ei
        with open('ExportIndicators_test/TestHelperFunctions/iocs_cache_values_text.json', 'r') as iocs_text_values_f:
            iocs_text_dict = json.loads(iocs_text_values_f.read())
            mocker.patch.object(demisto, 'getIntegrationContext', return_value={"last_output": iocs_text_dict,
                                                                                "last_limit": 50, "last_offset": 1,
                                                                                "last_query": "type:ip",
                                                                                "last_format": "text"})
            mocker.patch.object(ei, 'refresh_outbound_context', return_value=iocs_text_dict)
            mocker.patch.object(demisto, 'getLastRun', return_value={'last_run': 1578383898000})
            request_args = ei.RequestArguments(query='type:ip', out_format='text', limit=50, offset=0)
            ioc_list = ei.get_outbound_ioc_values(
                on_demand=False,
                request_args=request_args,
                cache_refresh_rate='1 minute'
            )
            for ioc_row in ioc_list:
                assert ioc_row in iocs_text_dict

    @pytest.mark.get_outbound_ioc_values
    def test_get_outbound_ioc_values_6(self, mocker):
        """Test update by request params change - query"""
        import CommonServerPython as CSP
        mocker.patch.object(CSP, 'parse_date_range', return_value=(1578383898, 1578383898))
        import ExportIndicators as ei
        with open('ExportIndicators_test/TestHelperFunctions/iocs_cache_values_text.json', 'r') as iocs_text_values_f:
            iocs_text_dict = json.loads(iocs_text_values_f.read())
            mocker.patch.object(demisto, 'getIntegrationContext', return_value={"last_output": iocs_text_dict,
                                                                                "last_limit": 50, "last_offset": 0,
                                                                                "last_query": "type:URL",
                                                                                "last_format": "text"})
            mocker.patch.object(ei, 'refresh_outbound_context', return_value=iocs_text_dict)
            mocker.patch.object(demisto, 'getLastRun', return_value={'last_run': 1578383898000})
            request_args = ei.RequestArguments(query='type:ip', out_format='text', limit=50, offset=0)
            ioc_list = ei.get_outbound_ioc_values(
                on_demand=False,
                request_args=request_args,
                cache_refresh_rate='1 minute'
            )
            for ioc_row in ioc_list:
                assert ioc_row in iocs_text_dict

    @pytest.mark.list_to_str
    def test_list_to_str_1(self):
        """Test invalid"""
        from ExportIndicators import list_to_str
        with pytest.raises(AttributeError):
            invalid_list_value = 2
            list_to_str(invalid_list_value)

        with pytest.raises(AttributeError):
            invalid_list_value = {'invalid': 'invalid'}
            list_to_str(invalid_list_value)

    @pytest.mark.list_to_str
    def test_list_to_str_2(self):
        """Test empty"""
        from ExportIndicators import list_to_str
        assert list_to_str(None) == ''
        assert list_to_str([]) == ''
        assert list_to_str({}) == ''

    @pytest.mark.list_to_str
    def test_list_to_str_3(self):
        """Test non empty fields"""
        from ExportIndicators import list_to_str
        valid_list_value = [1, 2, 3, 4]
        assert list_to_str(valid_list_value) == '1,2,3,4'
        assert list_to_str(valid_list_value, '.') == '1.2.3.4'
        assert list_to_str(valid_list_value, map_func=lambda x: f'{x}a') == '1a,2a,3a,4a'

    @pytest.mark.get_params_port
    def test_get_params_port_1(self):
        """Test invalid"""
        from CommonServerPython import DemistoException
        from ExportIndicators import get_params_port
        params = {'longRunningPort': 'invalid'}
        with pytest.raises(DemistoException):
            get_params_port(params)

    @pytest.mark.get_params_port
    def test_get_params_port_2(self):
        """Test empty"""
        from ExportIndicators import get_params_port
        params = {'longRunningPort': ''}
        with pytest.raises(ValueError):
            get_params_port(params)

    @pytest.mark.get_params_port
    def test_get_params_port_3(self):
        """Test valid"""
        from ExportIndicators import get_params_port
        params = {'longRunningPort': '80'}
        assert get_params_port(params) == 80

    @pytest.mark.refresh_outbound_context
    def test_refresh_outbound_context_1(self, mocker):
        """Test out_format=text"""
        import ExportIndicators as ei
        with open('ExportIndicators_test/TestHelperFunctions/demisto_iocs.json', 'r') as iocs_json_f:
            iocs_json = json.loads(iocs_json_f.read())
            mocker.patch.object(ei, 'find_indicators_with_limit', return_value=iocs_json)
            request_args = ei.RequestArguments(query='', out_format='text')
            ei_vals = ei.refresh_outbound_context(request_args)
            for ioc in iocs_json:
                ip = ioc.get('value')
                assert ip in ei_vals

    @pytest.mark.refresh_outbound_context
    def test_refresh_outbound_context_2(self, mocker):
        """Test out_format= XSOAR json"""
        import ExportIndicators as ei
        with open('ExportIndicators_test/TestHelperFunctions/demisto_iocs.json', 'r') as iocs_json_f:
            iocs_json = json.loads(iocs_json_f.read())
            mocker.patch.object(ei, 'find_indicators_with_limit', return_value=iocs_json)
            request_args = ei.RequestArguments(query='', out_format='XSOAR json')
            ei_vals = ei.refresh_outbound_context(request_args)
            assert isinstance(ei_vals, str)
            ei_vals = json.loads(ei_vals)
            assert iocs_json == ei_vals

    @pytest.mark.refresh_outbound_context
    def test_refresh_outbound_context_3(self, mocker):
        """Test out_format=xsoar-csv"""
        import ExportIndicators as ei
        with open('ExportIndicators_test/TestHelperFunctions/demisto_iocs.json', 'r') as iocs_json_f:
            iocs_json = json.loads(iocs_json_f.read())
            mocker.patch.object(ei, 'find_indicators_with_limit', return_value=iocs_json)
            request_args = ei.RequestArguments(query='', out_format='XSOAR csv')
            ei_vals = ei.refresh_outbound_context(request_args)
            with open('ExportIndicators_test/TestHelperFunctions/iocs_out_csv.txt', 'r') as iocs_out_f:
                iocs_out = iocs_out_f.read()
                assert iocs_out == ei_vals

    @pytest.mark.refresh_outbound_context
    def test_refresh_outbound_context_4(self, mocker):
        """Test out_format=XSOAR json-seq"""
        import ExportIndicators as ei
        with open('ExportIndicators_test/TestHelperFunctions/demisto_iocs.json', 'r') as iocs_json_f:
            iocs_json = json.loads(iocs_json_f.read())
            mocker.patch.object(ei, 'find_indicators_with_limit', return_value=iocs_json)
            request_args = ei.RequestArguments(query='', out_format='XSOAR json-seq')
            ei_vals = ei.refresh_outbound_context(request_args)
            with open('ExportIndicators_test/TestHelperFunctions/iocs_out_json_seq.txt', 'r') as iocs_out_f:
                iocs_out = iocs_out_f.read()
                assert iocs_out == ei_vals

    @pytest.mark.refresh_outbound_context
    def test_refresh_outbound_context_5(self, mocker):
        """Test out_format=json"""
        import ExportIndicators as ei
        with open('ExportIndicators_test/TestHelperFunctions/demisto_url_iocs.json', 'r') as iocs_json_f:
            iocs_json = json.loads(iocs_json_f.read())
            mocker.patch.object(ei, 'find_indicators_with_limit', return_value=iocs_json)
            request_args = ei.RequestArguments(query='', out_format='json')
            ei_vals = ei.refresh_outbound_context(request_args)
            assert isinstance(ei_vals, str)
            ei_vals = json.loads(ei_vals)
            with open('ExportIndicators_test/TestHelperFunctions/iocs_out_json.json', 'r') as iocs_json_out_f:
                iocs_json_out = json.loads(iocs_json_out_f.read())
                assert iocs_json_out == ei_vals

    @pytest.mark.refresh_outbound_context
    def test_refresh_outbound_context_6(self, mocker):
        """Test out_format=json-seq"""
        import ExportIndicators as ei
        with open('ExportIndicators_test/TestHelperFunctions/demisto_iocs.json', 'r') as iocs_json_f:
            iocs_json = json.loads(iocs_json_f.read())
            mocker.patch.object(ei, 'find_indicators_with_limit', return_value=iocs_json)
            request_args = ei.RequestArguments(query='', out_format='json-seq')
            ei_vals = ei.refresh_outbound_context(request_args)
            with open('ExportIndicators_test/TestHelperFunctions/iocs_out_json_seq_old.txt', 'r') as iocs_out_f:
                iocs_out = iocs_out_f.read()
                for iocs_out_line in iocs_out.split('\n'):
                    assert iocs_out_line in ei_vals

    @pytest.mark.refresh_outbound_context
    def test_refresh_outbound_context_7(self, mocker):
        """Test out_format=csv"""
        import ExportIndicators as ei
        with open('ExportIndicators_test/TestHelperFunctions/demisto_iocs.json', 'r') as iocs_json_f:
            iocs_json = json.loads(iocs_json_f.read())
            mocker.patch.object(ei, 'find_indicators_with_limit', return_value=iocs_json)
            request_args = ei.RequestArguments(query='', out_format='csv')
            ei_vals = ei.refresh_outbound_context(request_args)
            with open('ExportIndicators_test/TestHelperFunctions/iocs_out_csv_old.txt', 'r') as iocs_out_f:
                iocs_out = iocs_out_f.read()
                for ioc in iocs_out.split('\n'):
                    assert ioc in ei_vals

    @pytest.mark.find_indicators_with_limit
    def test_find_indicators_with_limit_1(self, mocker):
        """Test find indicators limit"""
        import ExportIndicators as ei
        with open('ExportIndicators_test/TestHelperFunctions/demisto_iocs.json', 'r') as iocs_json_f:
            iocs_json = json.loads(iocs_json_f.read())
            limit = 30
            mocker.patch.object(ei, 'find_indicators_with_limit_loop', return_value=(iocs_json, 1))
            ei_vals = ei.find_indicators_with_limit(indicator_query='', limit=limit, offset=0)
            assert len(ei_vals) == limit

    @pytest.mark.find_indicators_with_limit
    def test_find_indicators_with_limit_and_offset_1(self, mocker):
        """Test find indicators limit and offset"""
        import ExportIndicators as ei
        with open('ExportIndicators_test/TestHelperFunctions/demisto_iocs.json', 'r') as iocs_json_f:
            iocs_json = json.loads(iocs_json_f.read())
            limit = 30
            offset = 1
            mocker.patch.object(ei, 'find_indicators_with_limit_loop', return_value=(iocs_json, 1))
            ei_vals = ei.find_indicators_with_limit(indicator_query='', limit=limit, offset=offset)
            assert len(ei_vals) == limit
            # check that the first value is the second on the list
            assert ei_vals[0].get('value') == '212.115.110.19'

    @pytest.mark.find_indicators_with_limit_loop
    def test_find_indicators_with_limit_loop_1(self, mocker):
        """Test find indicators stops when reached last page"""
        import ExportIndicators as ei
        with open('ExportIndicators_test/TestHelperFunctions/demisto_iocs.json', 'r') as iocs_json_f:
            iocs_dict = {'iocs': json.loads(iocs_json_f.read())}
            limit = 50
            mocker.patch.object(demisto, 'searchIndicators', return_value=iocs_dict)
            ei_vals, nxt_pg = ei.find_indicators_with_limit_loop(indicator_query='', limit=limit)
            assert nxt_pg == 1  # assert entered into loop

    @pytest.mark.find_indicators_with_limit_loop
    def test_find_indicators_with_limit_loop_2(self, mocker):
        """Test find indicators stops when reached limit"""
        import ExportIndicators as ei
        with open('ExportIndicators_test/TestHelperFunctions/demisto_iocs.json', 'r') as iocs_json_f:
            iocs_dict = {'iocs': json.loads(iocs_json_f.read())}
            limit = 30
            mocker.patch.object(demisto, 'searchIndicators', return_value=iocs_dict)
            ei.PAGE_SIZE = IOC_RES_LEN
            ei_vals, nxt_pg = ei.find_indicators_with_limit_loop(indicator_query='', limit=limit,
                                                                 last_found_len=IOC_RES_LEN)
            assert nxt_pg == 1  # assert entered into loop

    @pytest.mark.create_values_out_dict
    def test_create_values_out_dict_1(self):
        """Test XSOAR CSV out"""
        from ExportIndicators import create_values_out_dict, FORMAT_XSOAR_CSV, RequestArguments
        with open('ExportIndicators_test/TestHelperFunctions/demisto_iocs.json', 'r') as iocs_json_f:
            iocs_json = json.loads(iocs_json_f.read())
            request_args = RequestArguments(query='', out_format=FORMAT_XSOAR_CSV)
            csv_out = create_values_out_dict(iocs_json, request_args)
            # assert len(csv_out) == IOC_RES_LEN + 1
            with open('ExportIndicators_test/TestHelperFunctions/iocs_out_csv.txt', 'r') as iocs_out_f:
                expected_csv_out = iocs_out_f.read()
                for csv_line in csv_out.values():
                    assert csv_line in expected_csv_out

    @pytest.mark.create_values_out_dict
    def test_create_values_out_dict_2(self):
        """Test XSOAR JSON out"""
        from ExportIndicators import create_values_out_dict, FORMAT_XSOAR_JSON, CTX_VALUES_KEY, RequestArguments
        with open('ExportIndicators_test/TestHelperFunctions/demisto_iocs.json', 'r') as iocs_json_f:
            iocs_json = json.load(iocs_json_f)
            request_args = RequestArguments(query='', out_format=FORMAT_XSOAR_JSON)
            json_out = json.loads(create_values_out_dict(iocs_json, request_args).get(CTX_VALUES_KEY))
            assert json_out == iocs_json

    @pytest.mark.create_values_out_dict
    def test_create_values_out_dict_3(self):
        """Test XSOAR JSON_SEQ out"""
        from ExportIndicators import create_values_out_dict, FORMAT_XSOAR_JSON_SEQ, CTX_VALUES_KEY, RequestArguments
        with open('ExportIndicators_test/TestHelperFunctions/demisto_iocs.json', 'r') as iocs_json_f:
            iocs_json = json.loads(iocs_json_f.read())
            request_args = RequestArguments(query='', out_format=FORMAT_XSOAR_JSON_SEQ)
            json_seq_out = create_values_out_dict(iocs_json, request_args).get(CTX_VALUES_KEY)
            for seq_line in json_seq_out.split('\n'):
                assert json.loads(seq_line) in iocs_json

    @pytest.mark.create_values_out_dict
    def test_create_values_out_dict_4(self):
        """Test TEXT out"""
        from ExportIndicators import create_values_out_dict, FORMAT_TEXT, CTX_VALUES_KEY, RequestArguments
        with open('ExportIndicators_test/TestHelperFunctions/demisto_iocs.json', 'r') as iocs_json_f:
            iocs_json = json.loads(iocs_json_f.read())
            request_args = RequestArguments(query='', out_format=FORMAT_TEXT)
            text_out = create_values_out_dict(iocs_json, request_args).get(CTX_VALUES_KEY)
            with open('ExportIndicators_test/TestHelperFunctions/iocs_cache_values_text.json', 'r') as iocs_txt_f:
                iocs_txt_json = json.load(iocs_txt_f)
                for line in text_out.split('\n'):
                    assert line in iocs_txt_json

    @pytest.mark.create_values_out_dict
    def test_create_values_out_dict_5(self):
        """Test JSON out"""
        from ExportIndicators import create_values_out_dict, FORMAT_JSON, CTX_VALUES_KEY, RequestArguments
        with open('ExportIndicators_test/TestHelperFunctions/demisto_url_iocs.json', 'r') as iocs_json_f:
            iocs_json = json.load(iocs_json_f)
            request_args = RequestArguments(query='', out_format=FORMAT_JSON)
            json_out = json.loads(create_values_out_dict(iocs_json, request_args).get(CTX_VALUES_KEY))
            with open('ExportIndicators_test/TestHelperFunctions/iocs_out_json.json', 'r') as iocs_json_out_f:
                iocs_json_out = json.loads(iocs_json_out_f.read())
                assert iocs_json_out == json_out

    @pytest.mark.create_values_out_dict
    def test_create_values_out_dict_6(self):
        """Test JSON_SEQ out"""
        from ExportIndicators import create_values_out_dict, FORMAT_JSON_SEQ, CTX_VALUES_KEY, RequestArguments
        with open('ExportIndicators_test/TestHelperFunctions/demisto_url_iocs.json', 'r') as iocs_json_f:
            iocs_json = json.loads(iocs_json_f.read())
            request_args = RequestArguments(query='', out_format=FORMAT_JSON_SEQ)
            json_seq_out = create_values_out_dict(iocs_json, request_args).get(CTX_VALUES_KEY)
            with open('ExportIndicators_test/TestHelperFunctions/iocs_out_json.json', 'r') as iocs_json_out_f:
                iocs_json_out = json.load(iocs_json_out_f)
                for seq_line in json_seq_out.split('\n'):
                    assert json.loads(seq_line) in iocs_json_out

    @pytest.mark.create_values_out_dict
    def test_create_values_out_dict_7(self):
        """Test CSV out"""
        from ExportIndicators import create_values_out_dict, FORMAT_CSV, RequestArguments
        with open('ExportIndicators_test/TestHelperFunctions/demisto_iocs.json', 'r') as iocs_json_f:
            iocs_json = json.loads(iocs_json_f.read())
            request_args = RequestArguments(query='', out_format=FORMAT_CSV)
            csv_out = create_values_out_dict(iocs_json, request_args)
            # assert len(csv_out) == IOC_RES_LEN + 1
            with open('ExportIndicators_test/TestHelperFunctions/iocs_out_csv_old.txt', 'r') as iocs_out_f:
                expected_csv_out = iocs_out_f.read()
                for csv_line in csv_out.values():
                    assert csv_line in expected_csv_out

    @pytest.mark.validate_basic_authentication
    def test_validate_basic_authentication(self):
        """Test Authentication"""
        from ExportIndicators import validate_basic_authentication
        username, password = 'user', 'pwd'
        data = {
            "empty_auth": {},
            "basic_missing_auth": {
                "Authorization": "missing basic"
            },
            "colon_missing_auth": {
                "Authorization": "Basic bWlzc2luZ19jb2xvbg=="
            },
            "wrong_length_auth": {
                "Authorization": "Basic YTpiOmM="
            },
            "wrong_credentials_auth": {
                "Authorization": "Basic YTpi"
            },
            "right_credentials_auth": {
                "Authorization": "Basic dXNlcjpwd2Q="
            }
        }
        assert not validate_basic_authentication(data.get('empty_auth'), username, password)
        assert not validate_basic_authentication(data.get('basic_missing_auth'), username, password)
        assert not validate_basic_authentication(data.get('colon_missing_auth'), username, password)
        assert not validate_basic_authentication(data.get('wrong_length_auth'), username, password)
        assert not validate_basic_authentication(data.get('wrong_credentials_auth'), username, password)
        assert validate_basic_authentication(data.get('right_credentials_auth'), username, password)

    @pytest.mark.validate_basic_authentication
    def test_panos_url_formatting(self):
        from ExportIndicators import panos_url_formatting, CTX_VALUES_KEY
        with open('ExportIndicators_test/TestHelperFunctions/demisto_url_iocs.json', 'r') as iocs_json_f:
            iocs_json = json.loads(iocs_json_f.read())

            # strips port numbers
            returned_dict = panos_url_formatting(iocs=iocs_json, drop_invalids=True, strip_port=True)
            returned_output = returned_dict.get(CTX_VALUES_KEY)
            assert returned_output == "1.2.3.4/wget\nwww.demisto.com/cool"

            # should ignore indicators with port numbers
            returned_dict = panos_url_formatting(iocs=iocs_json, drop_invalids=True, strip_port=False)
            returned_output = returned_dict.get(CTX_VALUES_KEY)
            assert returned_output == 'www.demisto.com/cool'

    @pytest.mark.validate_basic_authentication
    def test_create_proxysg_out_format(self):
        from ExportIndicators import create_proxysg_out_format, CTX_VALUES_KEY
        with open('ExportIndicators_test/TestHelperFunctions/demisto_url_iocs.json', 'r') as iocs_json_f:
            iocs_json = json.loads(iocs_json_f.read())

            # classify all categories
            returned_dict = create_proxysg_out_format(iocs=iocs_json, category_default="default", category_attribute='')
            returned_output = returned_dict.get(CTX_VALUES_KEY)
            assert returned_output == "define category category2\n1.2.3.4:89/wget\nend\n" \
                                      "define category category1\nhttps://www.demisto.com/cool\nend\n"

            # listed category does not exist - all results should be in default category
            returned_dict = create_proxysg_out_format(iocs=iocs_json, category_default="default",
                                                      category_attribute="category3")
            returned_output = returned_dict.get(CTX_VALUES_KEY)
            assert returned_output == "define category default\n1.2.3.4:89/wget\n" \
                                      "https://www.demisto.com/cool\nend\n"

            # list category2 only, the rest go to default
            returned_dict = create_proxysg_out_format(iocs=iocs_json, category_default="default",
                                                      category_attribute="category2")
            returned_output = returned_dict.get(CTX_VALUES_KEY)
            assert returned_output == "define category category2\n1.2.3.4:89/wget\nend\n" \
                                      "define category default\nhttps://www.demisto.com/cool\nend\n"

    @pytest.mark.validate_basic_authentication
    def test_create_mwg_out_format(self):
        from ExportIndicators import create_mwg_out_format, CTX_VALUES_KEY
        with open('ExportIndicators_test/TestHelperFunctions/demisto_url_iocs.json', 'r') as iocs_json_f:
            iocs_json = json.loads(iocs_json_f.read())

            # listed category does not exist - all results should be in default category
            returned_dict = create_mwg_out_format(iocs=iocs_json, mwg_type="ip")
            returned_output = returned_dict.get(CTX_VALUES_KEY)

            assert returned_output == "type=ip\n\"1.2.3.4:89/wget\" \"AutoFocus Feed\"\n\"" \
                                      "https://www.demisto.com/cool\" \"AutoFocus V2,VirusTotal," \
                                      "Alien Vault OTX TAXII Feed\""

    @pytest.mark.validate_basic_authentication
    def test_create_json_out_format(self):
        from ExportIndicators import create_json_out_format, CTX_VALUES_KEY
        with open('ExportIndicators_test/TestHelperFunctions/demisto_url_iocs.json', 'r') as iocs_json_f:
            iocs_json = json.loads(iocs_json_f.read())

            # listed category does not exist - all results should be in default category
            returned_dict = create_json_out_format(iocs=iocs_json)
            returned_output = json.loads(returned_dict.get(CTX_VALUES_KEY))

            assert returned_output[0].get('indicator') == '1.2.3.4:89/wget'
            assert isinstance(returned_output[0].get('value'), dict)

            assert returned_output[1].get('indicator') == 'https://www.demisto.com/cool'
            assert isinstance(returned_output[1].get('value'), dict)
