from player import Player


def main():
    player = Player(crit_rate=1)
    print(player.take_damage(12))


if __name__ == '__main__':
    main()

