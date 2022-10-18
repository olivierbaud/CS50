from project import add_category, clean_data, learn, get_stats, Categories, Operation
import pytest

categories = Categories("test_add_category.json")
good_data ={
        'Date': '2022/08/18',
        'Memo': 'card 7152 countdown fe rrymead christchurch',
        'Amount': -36.45,
        'Type': 'DEBIT',
    }
dict_test = {
    "savings": ["savethechang"],
    "transport": ["parking"],
    "groceries": ["countdown","new world"]
}
no_header_data = [
    {
        '2022/08/18': '2022/08/19',
        '2022081802': '2022081901',
        'DEBIT': '',
        '': '',
        'CARD 7152 COUNTDOWN FE RRYMEAD CHRISTCHURCH': 'SAVETHECHANG E 18 Aug 22',
        '-36.45': '-3.55'
    }
]
good_data2 = [
    {
        'Date': '2022/08/18',
        'Unique Id': '2022081802',
        'Tran Type': 'DEBIT',
        'Cheque Number': '',
        'Payee': 'DEBIT',
        'Memo': 'CARD 7152 COUNTDOWN FE RRYMEAD CHRISTCHURCH',
        'Amount': '-36.45'
    }
]
good_result ={
        'Date': '2022/08/18',
        'Memo': 'card 7152 countdown fe rrymead christchurch',
        'Amount': -36.45,
        'Type': 'DEBIT',
    }
data_w_category = {
        'Date': '2022/08/18',
        'Memo': 'card 7152 countdown fe rrymead christchurch',
        'Amount': -36.45,
        'Type': 'DEBIT',
        'Category': 'groceries'
    }

def test_add_category_from_dict():
    result = add_category([Operation(**good_data)], dict_test)[0]
    assert  result.category == "groceries"

def test_add_category_from_file():
    result = add_category([Operation(**good_data)], categories.dict)[0]
    assert result.category == "groceries"

def test_add_category_file_not_found():
    with pytest.raises(SystemExit):
        Categories("")

def test_clean_data_no_header():
    with pytest.raises(SystemExit):
        clean_data(no_header_data)

def test_clean_data_good_data():
    result = clean_data(good_data2)[0]
    expected = [Operation(**good_result)][0]
    assert result.date == expected.date
    assert result.type == expected.type
    assert result.memo == expected.memo
    assert result.amount == expected.amount

def test_learn_existing_category():
    result = learn([Operation(**data_w_category)], categories)[0]
    assert result.category == 'groceries'

def test_learn_no_cat_add_existing_cat(monkeypatch):
    result = learn([Operation(**good_data)], categories)[0]
    monkeypatch.setattr('builtins.input', lambda _: 'groceries')
    assert result.category == 'groceries'

line1 = {
        'Date': '2022/08/18',
        'Memo': 'card 7152 countdown ferrymead christchurch',
        'Amount': -49.50,
        'Type': 'DEBIT',
        'Category': 'groceries'
    }
line2 = {
        'Date': '2022/08/21',
        'Memo': 'card 7152 new world christchurch',
        'Amount': -50.50,
        'Type': 'DEBIT',
        'Category': 'groceries'
    }
line3 = {
        'Date': '2022/08/23',
        'Memo': 'card 7152 parking woolston christchurch',
        'Amount': -10,
        'Type': 'DEBIT',
        'Category': 'transport'
    }
line4 = {
        'Date': '2022/08/28',
        'Memo': 'card 7152 parking cbd christchurch',
        'Amount': -5,
        'Type': 'DEBIT',
        'Category': 'transport'
    }

def test_get_stats_lines_1and2():
    assert get_stats([Operation(**line) for line in [line1,line2]], categories) == {'groceries': '-100.00', 'transport': '0.00'}

def test_get_stats_lines_3and4():
    assert get_stats([Operation(**line) for line in [line3,line4]], categories) == {'groceries': '0.00', 'transport': '-15.00'}

def test_get_stats_all_lines():
    assert get_stats([Operation(**line) for line in [line1,line2,line3,line4]], categories) == {'groceries': '-100.00', 'transport': '-15.00'}
