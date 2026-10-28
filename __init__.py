"""CAA providers that can read identifiers hidden by Keep Only Tags."""

from picard.plugin3.api import Metadata
from picard.coverart.providers.caa import CoverArtProviderCaa
from picard.coverart.providers.caa_release_group import CoverArtProviderCaaReleaseGroup


class _HiddenIdsMixin:
    """Restore identifiers only inside the provider's private metadata copy."""

    OPTIONS = None
    ID_TAG = None

    def __init__(self, coverart):
        super().__init__(coverart)
        private_metadata = Metadata()
        private_metadata.copy(self.metadata)
        for tag in ("musicbrainz_albumid", "musicbrainz_releasegroupid"):
            if not private_metadata.get(tag):
                # Script variables beginning with '_' use '~' internally.
                hidden = private_metadata.get("~ko_" + tag)
                if hidden:
                    private_metadata[tag] = hidden
        self.metadata = private_metadata

    def enabled(self):
        # Never send an empty identifier to the Cover Art Archive.
        return bool(self.metadata.get(self.ID_TAG)) and super().enabled()


class HiddenIdsRelease(_HiddenIdsMixin, CoverArtProviderCaa):
    NAME = "CAA Hidden IDs: Release"
    TITLE = "Cover Art From Hidden Tags: Release"
    ID_TAG = "musicbrainz_albumid"


class HiddenIdsReleaseGroup(_HiddenIdsMixin, CoverArtProviderCaaReleaseGroup):
    NAME = "CAA Hidden IDs: Release Group"
    TITLE = "Cover Art From Hidden Tags: Release Group"
    ID_TAG = "musicbrainz_releasegroupid"


def enable(api):
    """Register providers through Picard's supported plugin interface."""
    api.register_cover_art_provider(HiddenIdsRelease)
    api.register_cover_art_provider(HiddenIdsReleaseGroup)
