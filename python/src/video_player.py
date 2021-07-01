"""A video player class."""

from .video_library import VideoLibrary
from .video_playlist import Playlist
from random import randrange


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self._playlists = []

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        list_video_names = self._video_library.get_all_videos()
        print("Here's a list of all available videos:")
        for vid in sorted(list_video_names, key=lambda x: x.title):
            print(vid.title + " (" + vid.video_id + ") [" + ' '.join(vid.tags) + "]")

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        list_video_names = self._video_library.get_all_videos()
        if video_id not in [vid.video_id for vid in list_video_names]:
            print("Cannot play video: Video does not exist")
        else:
            for vid in list_video_names:
                if vid.status == 'playing' or vid.status == 'paused':
                    print("Stopping video: " + vid.title)
                    vid._status = 'stopped'
            for vid in list_video_names:
                if vid.video_id == video_id:
                    print("Playing video: " + vid.title)
                    vid._status = 'playing'

    def stop_video(self):
        """Stops the current video."""
        list_video_names = self._video_library.get_all_videos()
        if 'playing' not in [vid.status for vid in list_video_names] and 'paused' not in [vid.status for vid in list_video_names]:
            print("Cannot stop video: No video is currently playing")
        else:
            for vid in list_video_names:
                if vid.status == 'playing' or vid.status == 'paused':
                    print("Stopping video: " + vid.title)
                    vid._status = 'stopped'

    def play_random_video(self):
        """Plays a random video from the video library."""
        list_video_names = self._video_library.get_all_videos()
        for vid in list_video_names:
            if vid.status == 'playing' or vid.status == 'paused':
                print("Stopping video: " + vid.title)
                vid._status = 'stopped'
        vid = list_video_names[randrange(len(list_video_names))]
        vid._status = 'playing'
        print("Playing video: " + vid.title)


    def pause_video(self):
        """Pauses the current video."""
        list_video_names = self._video_library.get_all_videos()
        if 'playing' not in [vid.status for vid in list_video_names] and 'paused' not in [vid.status for vid in list_video_names]:
            print("Cannot pause video: No video is currently playing")
        else:
            for vid in list_video_names:
                if vid.status == 'paused':
                    print("Video already paused: " + vid.title)
                if vid.status == 'playing':
                    print("Pausing video: " + vid.title)
                    vid._status = 'paused'


    def continue_video(self):
        """Resumes playing the current video."""
        list_video_names = self._video_library.get_all_videos()
        if 'paused' not in [vid.status for vid in list_video_names]:
            if 'playing' in [vid.status for vid in list_video_names]:
                print("Cannot continue video: Video is not paused")
            else:
                print("Cannot continue video: No video is currently playing")
        for vid in list_video_names:
            if vid.status == 'paused':
                print("Continuing video: " + vid.title)

    def show_playing(self):
        """Displays video currently playing."""
        list_video_names = self._video_library.get_all_videos()
        if 'playing' not in [vid.status for vid in list_video_names] and 'paused' not in [vid.status for vid in list_video_names]:
            print("No video is currently playing")
        for vid in list_video_names:
            if vid.status == 'playing':
                print("Currently playing: " + vid.title + " (" + vid.video_id + ") [" + ' '.join(vid.tags) + "]")
            elif vid.status == 'paused':
                print("Currently playing: " + vid.title + " (" + vid.video_id + ") [" + ' '.join(vid.tags) + "] - PAUSED")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        name_playlists = []
        for playlist in self._playlists:
            name_playlists.append(playlist.title)
        if playlist_name.lower() in [i.lower() for i in name_playlists]:
            print("Cannot create playlist: A playlist with the same name already exists")
        else:
            self._playlists.append(Playlist(playlist_name))
            print("Successfully created new playlist: " + playlist_name)

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        name_playlists = []
        for playlist in self._playlists:
            name_playlists.append(playlist.title)
        list_video_names = self._video_library.get_all_videos()
        if playlist_name.lower() not in [i.lower() for i in name_playlists]:
            print("Cannot add video to " + playlist_name + ": Playlist does not exist")
        elif video_id not in [vid.video_id for vid in list_video_names]:
            print("Cannot add video to " + playlist_name + ": Video does not exist")
        for p1, p2 in zip([i.lower() for i in name_playlists], name_playlists):
            if playlist_name.lower() == p1 and video_id in Playlist(playlist_name).video_ids:
                print("Cannot add video to " + playlist_name + ": Video already added")


        if video_id in Playlist(playlist_name).video_ids:
            print("Cannot add video to " + playlist_name + ": Video already added")
        else:
            for vid in list_video_names:
                if vid.video_id == video_id:
                    Playlist(playlist_name).video_ids.append(vid.video_id)
                    print("Added video to " + playlist_name + ": " + vid.title)


    def show_all_playlists(self):
        """Display all playlists."""
        return list(self._playlists.values())
        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
