def teams_list(india_team, pakisthan_team):
        """
        Return predefined lists of cricket players for India and Pakistan teams.
        
        This function ignores input parameters and returns hardcoded team rosters
        for the India and Pakistan cricket teams.
        
        Args:
            india_team: Not used. This parameter is overwritten by the function.
            pakisthan_team: Not used. This parameter is overwritten by the function.
        
        Returns:
            tuple: A tuple containing two lists:
                - india_team (list): List of Indian cricket players including Virat Kohli, 
                                     Rohit Sharma, and Jasprit Bumrah.
                - pakisthan_team (list): List of Pakistani cricket players including Babar Azam, 
                                         Shaheen Afridi, and Fakhar Zaman.
        
        Example:
            >>> india, pakistan = teams_list(None, None)
            >>> india
            ['Virat Kohli', 'Rohit Sharma', 'Jasprit Bumrah']
            >>> pakistan
            ['Babar Azam', 'Shaheen Afridi', 'Fakhar Zaman']
        """
        india_team = ["Virat Kohli", "Rohit Sharma", "Jasprit Bumrah"]
        pakisthan_team = ["Babar Azam", "Shaheen Afridi", "Fakhar Zaman"]
        return india_team, pakisthan_team