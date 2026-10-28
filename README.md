# Retrieve Cover Art From Hidden Tags for MusicBrainz Picard

**Version:** 1.1.0 · **Author:** Borunzio · **Target:** MusicBrainz Picard 3.0.2

Retrieve Cover Art Archive images when Keep Only Tags hides the MusicBrainz release identifiers. The identifiers are restored only inside a private metadata copy used by the artwork providers, not in the album or file tags.

> This plugin uses Picard internal CAA classes; check compatibility after upgrading Picard. Live download/save validation remains outstanding.

## Requirements

- Picard 3 with its plugin system; implementation checked against 3.0.2.
- Keep Only Tags when using hidden IDs. Standard IDs also work when present.
- A matched album with at least one usable release or release-group ID.
- Internet access to MusicBrainz / Cover Art Archive and their image hosts.

## Install or update

In **Options > Plugins > Install Plugin**, choose **Local repository** and this repository folder, or use the repository URL once publicly hosted. Select the version tag **v1.1.0** when choosing a reference. Restart Picard after updating.

Keep the repository's `.git` directory when installing locally. This release retains the existing plugin UUID, so settings and plugin identity remain associated with the same plugin.

## Configure

1. Enable the plugin.
2. In **Cover Art**, enable **Cover Art From Hidden Tags: Release**, then **Cover Art From Hidden Tags: Release Group**.
3. Disable the corresponding built-in **Cover Art Archive: Release** and **Cover Art Archive: Release Group** providers. Otherwise they can still issue requests with empty IDs.
4. In Keep Only Tags, exclude `musicbrainz_albumid` and `musicbrainz_releasegroupid` if you do not want them written to your files.
5. Disable scripts that restore those IDs into normal writable tags.
6. Reload a matched test album after preserving any unsaved manual edits.

The providers reuse Picard's built-in CAA settings. This plugin has no separate options page. Author and release information are supplied by the manifest; the version displayed by Picard depends on the installed Git reference.

## How it works

For each provider, the plugin copies its metadata. It keeps normal identifiers if available, otherwise reads the internal `~ko_musicbrainz_albumid` and `~ko_musicbrainz_releasegroupid` variables. In tagger scripts these hidden variables are named `_ko_musicbrainz_albumid` and `_ko_musicbrainz_releasegroupid`.

Only the private copy receives the restored normal IDs. An absent ID skips the corresponding provider. Keep Only Tags remains responsible for removing unwanted writable tags.

## Scope and artwork preservation

This plugin only changes how CAA providers find IDs. It does not resize, extract, rank or compare all available artwork, and does not change fanart.tv behavior. It does not itself guarantee that the highest-resolution embedded cover is retained. Configure and verify Picard's artwork preservation settings separately before processing a library.

## Troubleshooting

| Symptom | Check |
| --- | --- |
| Empty-ID CAA request | Disable the matching built-in providers and verify Keep Only Tags supplies hidden IDs. |
| No artwork returned | Check the matched release and release group have artwork and usable IDs. |
| HTTP 403 / Forbidden | This can be an image-host access failure; hidden-ID recovery does not fix host permissions. |
| IDs still saved | Check Keep Only Tags settings and scripts that restore normal tags. |
| Duplicate provider requests | Check that only the intended providers are enabled. |
| Version shows `main` | Install from a version tag instead of the branch. |

## Remove

Disable or uninstall this plugin. To return to the built-in CAA providers, enable them again and make their required IDs available during artwork lookup.

## Validation and compatibility

The implementation was reviewed against Picard 3.0.2 source with isolated checks of private metadata behavior. A full live CAA download and audio-file save have not been certified. Test a copy of an album before broader use. Internal Picard imports may change in later releases.

## License and contributions

MIT; see [LICENSE](LICENSE). Picard's imported components remain under their own upstream licensing terms.

See [CONTRIBUTING.md](CONTRIBUTING.md) and [CHANGELOG.md](CHANGELOG.md).
