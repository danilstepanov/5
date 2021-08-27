*** Settings ***
Library           ../../keywords/Web.py
Library           ../../keywords/Keywords.py

*** Test Cases ***

delete_permission
    [Documentation]    c57158
    [Setup]    init_test    delete_permission
    ${rowbeforedelete}      get_number_rows_from_table      signserver_permission
	${username}     get_any_username_with_permission
	${webans}       delete_permission   ${username}
	should be true  ${webans}
	${rowafterdelete}      get_number_rows_from_table      signserver_permission
	should not be equal as integers     ${rowbeforedelete}      ${rowafterdelete}

delete_productgroup
    [Documentation]    c56573
    [Setup]    init_test    delete_productgroup
    ${rowbeforedelete}      get_number_rows_from_table      signserver_productgroup
	${name}         get_any_productgroup
	${webans}       delete_one_productgroup   ${name}
	should be true  ${webans}
	${rowafterdelete}      get_number_rows_from_table      signserver_productgroup
	should not be equal as integers     ${rowbeforedelete}      ${rowafterdelete}

delete_signscript
    [Documentation]    c57162
    [Setup]    init_test    delete_signscript
    ${rowbeforedelete}      get_number_rows_from_table      signserver_signscript
	${name}         get_any_signscript
	${webans}       delete_one_signscript   ${name}
	should be true  ${webans}
	${rowafterdelete}      get_number_rows_from_table      signserver_signscript
	should not be equal as integers     ${rowbeforedelete}      ${rowafterdelete}

delete_user
    [Documentation]    c180417
    [Setup]    init_test    delete_user
    ${rowbeforedelete}      get_number_rows_from_table      auth_user
	${name}         get_any_user
	${webans}       delete_one_user   ${name}
	should be true  ${webans}
	${rowafterdelete}      get_number_rows_from_table      auth_user
	should not be equal as integers     ${rowbeforedelete}      ${rowafterdelete}

*** Keywords ***
init_test
    [Arguments]    ${test_name}
    ${time}    Get Time    epoch
    Set Test Variable    ${uniq_name}    ${test_name}_${time}
