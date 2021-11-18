*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  testi  testi123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  testi  testi123
    Input New Command
    Input Credentials  testi  testi123
    Output Should Contain  Username is already taken

Register With Too Short Username And Valid Password
    Input Credentials  te  testi123
    Output Should Contain  Invalid username or password

Register With Valid Username And Too Short Password
    Input Credentials  testi  testi
    Output Should Contain  Invalid username or password

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  testi  wasdwasd
    Output Should Contain  Invalid username or password

*** Keywords ***
Input New Command And Create User
    Input New Command
    