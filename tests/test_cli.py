# tests/test_cli.py

import pytest

from fibonacci_tdd_kata.cli import build_parser, main


def test_parser_accepts_single_number():
    args = build_parser().parse_args(["15", "--modulo", "100"])
    assert args.n == 15
    assert args.modulo == 100


def test_parser_accepts_range():
    args = build_parser().parse_args(["--start", "1", "--end", "5", "--modulo", "100"])
    assert args.start == 1
    assert args.end == 5
    assert args.modulo == 100


def test_main_prints_single_value(monkeypatch, capsys):
    monkeypatch.setattr("sys.argv", ["fibonacci-tdd-kata", "15", "--modulo", "100"])
    main()
    assert capsys.readouterr().out.strip() == "10"


def test_main_prints_range(monkeypatch, capsys):
    monkeypatch.setattr("sys.argv", ["fibonacci-tdd-kata", "--start", "1", 
                                     "--end", "5", "--modulo", "100"])
    main()
    lines = capsys.readouterr().out.strip().splitlines()
    assert lines == ["1", "2", "3", "4", "5"]


def test_main_requires_an_argument(monkeypatch):
    monkeypatch.setattr("sys.argv", ["fibonacci-tdd-kata", "--modulo", "100"])
    with pytest.raises(SystemExit):
        main()