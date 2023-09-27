import pytest

import sender_stand_request
import data
import configuration
from sender_stand_request import token

@pytest.mark.parametrize("name_kit", [pytest.param("a"),
                                      pytest.param("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"),
                                      pytest.param("QWErty"),
                                      pytest.param("Мария"),
                                      pytest.param(" Человек и КО "),
                                      pytest.param("123"),
                                      pytest.param("№%@,")
                                      ])
def test_positive_assert(name_kit):
    sender_stand_request.post_new_user()
    body = sender_stand_request.get_kit_body(name_kit)
    act = sender_stand_request.post_new_client_kit(body).status_code
    exp = 201
    assert act == exp
    act = sender_stand_request.post_new_client_kit(body).json()["name"]
    ext = body["name"]
    assert act == ext


@pytest.mark.parametrize("kit_name", [(""),
                                      ("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD"),
                                      (),
                                      (123)])
def test_negative_assert_code_400(kit_name):
    sender_stand_request.post_new_user()
    body = sender_stand_request.get_kit_body(kit_name)
    act = sender_stand_request.post_new_client_kit(body).status_code
    exp = 400
    assert act == exp


