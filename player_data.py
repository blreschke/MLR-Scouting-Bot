from structs import PlateAppearance as PA
import site_access
class PlayerData:


    def __init__(self, player_num, is_pitches):
        """
        Function that pulls plate appearances from the website, return a list of PA objects (see structs)
        PARAMETERS
        ----------
        pitcher_num : player ID of who we are pulling PAs for
        is_pitches: true if we are pulling for a player's pitching PAs, false if for batting PAs.
        """
        if (is_pitches):
            data = site_access.dictFromSource("https://redditball.com/api/v2/plays/byPitcher?pitcher=" + player_num + "&csv=false")

            milr_data = site_access.dictFromSource("https://milr.redditball.com/api/v2/plays/byPitcher?pitcher=" + player_num + "&csv=false")


        else:
            data = site_access.dictFromSource("https://redditball.com/api/v2/plays/byBatter?batter=" + player_num + "&csv=false")

            milr_data = site_access.dictFromSource("https://milr.redditball.com/api/v2/plays/byPitcher?pitcher=" + player_num + "&csv=false")

        all_data = milr_data + data
        sorted_data = sorted(all_data, key = lambda i: i["game"]["season"])
        self.data = sorted_data
    
    def sortBySeason(self, seasonsToInclude):
        sorted_list = []
        for i in self.data:
            curr_season = i["game"]["season"]
            if curr_season in seasonsToInclude:
                sorted_list.append(i)
        return sorted_list





pdata = PlayerData("58", True)
for i in sorted_data:
    print(i["pitch"])