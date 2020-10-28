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
        self.data = all_data
    
    def sortBySeason(seasonsToInclude):
        if "S1" in seasonsToInclude:
            

pdata = PlayerData("67", False)
print(pdata.data)
for i in pdata.data:
    print(i["swing"])
