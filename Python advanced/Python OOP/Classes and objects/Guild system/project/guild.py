class Guild:
    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, player):
        if player in self.players:
            return f"Player {player.name} is already in the guild."
        if player.guild != 'Unaffiliated':
            return f"Player {player.name} is in another guild."
        self.players.append(player)
        player.guild = self.name
        return f'Welcome player {player.name} to the guild {self.name}'

    def kick_player(self, player_name):
        for i in self.players:
            if i.name == player_name:
                self.players.remove(i)
                i.guild = 'Unaffiliated'
                return f"Player {player_name} has been removed from the guild."
        return f"Player {player_name} is not in the guild."

    def guild_info(self):
        res = f'Guild: {self.name}\n'
        for i in self.players:
            res += f'{i.player_info()}\n'
        return res[0:len(res) - 1]
