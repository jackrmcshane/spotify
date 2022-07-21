
import spotipy
from spotipy.oauth2 import SpotifyOAuth

from bots.bot import SpotifyBot

from wrappers.auth import AUTH
from wrappers.playlist import Playlist
from wrappers.track import Track



class SorterBot(SpotifyBot):

    def __init__(self, auth):
        super(SorterBot, self).__init__(auth)
        self.pairs = self.get_playlist_tracks_pairs()


    # working!
    def get_liked_library(self):
        results = self.auth.spotify.current_user_saved_tracks()
        tracks = [item['track'] for item in results['items']]

        while results['next']:
            results = self.auth.spotify.next(results)
            tracks.extend([item['track'] for item in results['items']])

        return list(map(Track, tracks))


    def sort_liked_library(self):
        # get liked tracks
        liked_tracks = self.get_liked_library()
        # for track in liked_tracks:
        #   self.add_track_to_genre_playlist(track, track.get_genres())

        track = liked_tracks[0]
        self.add_track_to_genre_playlist(track, track.get_genres(self.auth))



        # # for each track in liked library,
        # for track in liked_tracks:
        #     # for each genre of track
        #     for genre in track.get_genres(self.auth):
        #         self.add_track_to_genre_playlist(genre, track)

            # remove track from liked library
            #self.auth.spotify.current_user_saved_tracks_delete(track.get_uri())



    def add_track_to_genre_playlist(self, liked_track, genres):
        get_playlist = lambda tup: tup[0]
        get_tracks = lambda tup: tup[1]

        genres.append('Newwork')
        playlist_names = [get_playlist(tup).get_name() for tup in self.pairs]
        for genre in genres:
            if genre in playlist_names:
                ind = playlist_names.index(genre)
                track_names = [t.get_name() for t in get_tracks(self.pairs[ind])]
                if liked_track.get_name() in track_names:
                    continue
                else:
                    # add track to playlist
                    playlist_id = get_playlist(self.pairs[ind]).get_id()
                    self.auth.spotify.playlist_add_items(playlist_id, liked_track.get_uri())
            else:
                # create playlist
                new_playlist = Playlist(self.auth.spotify.user_playlist_create(
                    self.auth.spotify.current_user()['id'],
                    genre,
                    public=False
                ))

                print(new_playlist.get_name())
                pairs.append(tuple(new_playlist, self.get_playlist_tracks(new_playlist.get_id())))
                print(get_playlist(pairs[-1]).get_name(), len(get_tracks(pairs[-1])))

                # add track to playlist
                # playlist_id = get_playlist(self.pairs[ind]).get_id()
                # self.auth.spotify.playlist_add_items(playlist_id, liked_track.get_id())

                # append playlist and tracks to pairs
                    





        # # if genre is already a playlist
        # if genre in playlist_names:
        #     # check that track is not already in playlist
        #     ind = playlist_names.index(genre)
        #     print(genre + ': ' + str(ind))
        #     # if track is in playlist
        #         # continue
        #     # else
        #         # add track to playlist
        # # else
        #     # create playlist
        #     # add track to playlist
