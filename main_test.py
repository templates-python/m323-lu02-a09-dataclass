# test_main.py
from team import Team
from main import add_member

def test_add_member():
    team = Team(name='Team A')
    add_member(team, 'Alice')
    assert team.members == ['Alice']

    add_member(team, 'Bob')
    assert team.members == ['Alice', 'Bob']

def test_main_behavior(monkeypatch, capsys):
    # Simulate the main block
    team1 = Team(name='Team A')
    team2 = Team(name='Team B')

    add_member(team1, 'Alice')
    add_member(team2, 'Bob')

    expected_output = (
        "Team A Mitglieder: ['Alice']\n"
        "Team B Mitglieder: ['Bob']\n"
    )

    # Capture the print output
    with capsys.disabled():
        print(f'{team1.name} Mitglieder: {team1.members}')
        print(f'{team2.name} Mitglieder: {team2.members}')

    captured = capsys.readouterr()
    assert captured.out == expected_output