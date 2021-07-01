"""A video playlist class."""


class Playlist:
    """A class used to represent a Playlist."""

    def __init__(self, playlist_title: str, video_ids: list = []):
        """Playlist constructor"""
        self._title = playlist_title
        self._video_ids = video_ids

    @property
    def title(self) -> str:
        """Returns the title of a playlist."""
        return self._title

    @property
    def video_ids(self) -> list:
        """Returns the video ids of a playlist."""
        return self._video_ids

