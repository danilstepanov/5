*** Settings ***
Library		Selenium2Library
Library           ../../keywords/Keywords.py

*** Test Cases ***
delete_signed_file
    [Documentation]    c222766
    [Setup]    init_test    delete_signed_file
    ${ans}      delete sign file
    should be true  ${ans}

sign_and_delete_file
    [Documentation]    c222639
    [Setup]    init_test    delete_signed_file
    ${project_name}    post signing    /home/stp/test/st.tar    stp    1
    ${ans}      delete sign file
    should be true  ${ans}


*** Keywords ***
init_test
    [Arguments]    ${test_name}
    ${time}    Get Time    epoch
    Set Test Variable    ${uniq_name}    ${test_name}_${time}