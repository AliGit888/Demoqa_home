from pages.swag_labs import SwagLabs

def test_check_icon(browser):
    demo_qa_home = SwagLabs(browser)
    demo_qa_home.visit()
    demo_qa_home.exist_icon()
    demo_qa_home.exist_logo()
    demo_qa_home.exist_password()
    assert demo_qa_home.exist_icon()
    assert demo_qa_home.exist_logo()
    assert demo_qa_home.exist_password()