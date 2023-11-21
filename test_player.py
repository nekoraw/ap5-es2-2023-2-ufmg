from player import Player


def test_take_damage():
    test_player = Player(health=200, defense=50)
    remaining_health = test_player.take_damage(100)
    assert remaining_health == 150


def test_deal_damage():
    test_player = Player(crit_rate=0, attack=300)
    damage_dealt = test_player.attack_user()
    assert damage_dealt == 300


def test_deal_crit_damage():
    test_player = Player(crit_rate=1, attack=300, crit_damage=2)
    damage_dealt = test_player.attack_user()
    assert damage_dealt == 900





