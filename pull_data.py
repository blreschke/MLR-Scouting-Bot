from structs import PlateAppearance as PA
from structs import *

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
            data = stringFromSource("https://redditball.com/api/v2/plays/byPitcher?pitcher=" + player_num + "&csv=true")

            milr_data = stringFromSource("https://milr.redditball.com/api/v2/plays/byPitcher?pitcher=" + player_num + "&csv=true")


        else:
            data = stringFromSource("https://redditball.com/api/v2/plays/byBatter?batter=" + player_num + "&csv=true")

            milr_data = stringFromSource("https://milr.redditball.com/api/v2/plays/byPitcher?pitcher=" + player_num + "&csv=true")

        #splits single string by lines
        pa_data = data.splitlines()
        milr_pa_data = milr_data.splitlines()
        all_pas = []
        #Skips first line in list (headers)
        for i in milr_pa_data[1:]:
            #splits lines into array of data
            pa_list = i.split(',')
            curr_pa = PA(pa_list[0], pa_list[1], pa_list[2], pa_list[3], pa_list[4], pa_list[5], pa_list[6], pa_list[7], pa_list[8], pa_list[9], pa_list[10], pa_list[11], pa_list[12], pa_list[13])
            all_pas.append(curr_pa)

        for i in pa_data[1:]:
            #splits lines into array of data
            pa_list = i.split(',')
            curr_pa = PA(pa_list[0], pa_list[1], pa_list[2], pa_list[3], pa_list[4], pa_list[5], pa_list[6], pa_list[7], pa_list[8], pa_list[9], pa_list[10], pa_list[11], pa_list[12], pa_list[13])
            all_pas.append(curr_pa)
        self.data = all_pas

    def getPitches(self):
        pitches = []
        for i in self.data:
            pitches.append(i.pitch)
        return pitches

    def getSwings(self):
        pitches = []
        for i in self.data:
            swings.append(i.swing)
        return pitches

    def determineSeason(league, gameID):
        if (league == "MLR"):
            if int(gameID) > 0:
                return "what"
        return "in progress"

    def stringFromSource(source):
        url = "https://redditball.com/api/v2/plays/byPitcher?pitcher=" + player_num + "&csv=true"

        with urllib.request.urlopen(url) as url:
            data = url.read().decode()
        return data
pdata = PlayerData("67", False)
for i in pdata.data:
    print(i.game)