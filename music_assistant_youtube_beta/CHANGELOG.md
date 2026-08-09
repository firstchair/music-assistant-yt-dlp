## 2.10.0b13
- Upstream Music Assistant server (beta) update to 2.10.0b13

### Upstream Release Notes
## 📦 Beta Release

_Changes since [2.10.0b12](https://github.com/music-assistant/server/releases/tag/2.10.0b12)_

### 🚀 Features and enhancements

- Allow configuring Snapcast TCP stream sample rate and bit depth (by @rwjack in #5140)
- Addendum to collection support: Enhance search ability and overwrite collection metadata on provider sync (by @fmunkes in #5226)
- More accurate release years for much reissued songs (by @marcelveldt in #5442)
- Drop the entity dropdown from the Home Assistant settings (by @marcelveldt in #5446)
- Show the real reason when AirPlay pairing fails (by @marcelveldt in #5486)

### 🐛 Bugfixes

- Fix Bose SoundTouch preset search and assignment (by @Odn0 in #5158)
- Resolve OpenSubsonic playlist tracks without per-track album and lyrics fetches (by @GraysonCAdams in #5359)
- Change ABC radio monochrome icon from black to white (by @OzGav in #5392)
- Fix Pocket Casts sync failing on episodes without a duration (by @OzGav in #5397)
- Plex: fix artist top tracks always being empty (by @MarvinSchenkel in #5405)
- Fix Bluesound players cutting off the end of a track (by @marcelveldt in #5408)
- Fix cast dashboards freezing for players with reserved characters in their id (by @MarvinSchenkel in #5415)
- Fix playback stopping after an AI Radio announcement (by @MarvinSchenkel in #5416)
- Fix Sonos S1 speakers no longer reacting instantly after a network hiccup (by @marcelveldt in #5432)
- Fix Sonos connections lingering after a provider reload (by @marcelveldt in #5433)
- Say which type failed when JSON serialization fails (by @OzGav in #5439)
- Show player settings in your own language again (by @marcelveldt in #5447)
- Keep simulated-mute speakers muted when the group volume changes (by @marcelveldt in #5449)
- Remove the last spurious error log entries for shared work (by @marcelveldt in #5453)
- Fix slow Home Assistant logins when a provider fails to finish loading (by @OzGav in #5455)
- Fix a stray error in the log when a Cast speaker fails to join a group (by @marcelveldt in #5470)
- Play announcements on muted speakers (by @marcelveldt in #5474)
- Fix the OpenAI Compatible provider failing to load (by @marcelveldt in #5487)
- Fix playlists not loading in Home Assistant (by @marcelveldt in #5489)
- Fix Apple TV now-playing screen losing progress and artwork (by @marcelveldt in #5490)
- Skip the provider search for an empty search query (by @MarvinSchenkel in #5500)
- Fix filesystem sync never converging on changed files (by @MarvinSchenkel in #5506)
- Fix file shares importing nothing and hiding playlists (#6019) (by @OzGav in #5510)
- Skip unreachable IPv6 addresses when connecting to Cast devices (by @OzGav in #5513)
- Fix broken playlists page after upgrading from stable to beta (by @marcelveldt in #5515)

### 🎨 Frontend Changes

- Add Timeline view for MusicBrainz artist events (by @dmoo500 in [#2042](https://github.com/music-assistant/frontend/pull/2042))
- Fix the Discord playback position after seeking (by @marcelveldt in [#2299](https://github.com/music-assistant/frontend/pull/2299))
- Restrict the test workflow to read-only repository access (by @marcelveldt in [#2311](https://github.com/music-assistant/frontend/pull/2311))
- Remove an unused config setting type (by @marcelveldt in [#2310](https://github.com/music-assistant/frontend/pull/2310))
- Run the test suite once per commit (by @marcelveldt in [#2309](https://github.com/music-assistant/frontend/pull/2309))
- Cover the config link buttons in the disabled-state tests (by @marcelveldt in [#2305](https://github.com/music-assistant/frontend/pull/2305))
- Import the API client normally in the companion and auth plugins (by @marcelveldt in [#2294](https://github.com/music-assistant/frontend/pull/2294))
- Clean up unused props on the player bar timeline (by @marcelveldt in [#2300](https://github.com/music-assistant/frontend/pull/2300))
- Player card no longer uses its own copy of the queue lookup (by @marcelveldt in [#2293](https://github.com/music-assistant/frontend/pull/2293))
- Only load track waveforms while something is showing them (by @marcelveldt in [#2295](https://github.com/music-assistant/frontend/pull/2295))
- Stop the player timeline animating when there is no track length (by @marcelveldt in [#2296](https://github.com/music-assistant/frontend/pull/2296))
- Document when a queue counts as active (by @marcelveldt in [#2297](https://github.com/music-assistant/frontend/pull/2297))
- Add tests for the settings field disabled state (by @marcelveldt in [#2283](https://github.com/music-assistant/frontend/pull/2283))
- Share the app mount helper across the initialization tests (by @marcelveldt in [#2288](https://github.com/music-assistant/frontend/pull/2288))
- Fix the playback position shown in Discord Rich Presence (by @marcelveldt in [#2291](https://github.com/music-assistant/frontend/pull/2291))
- Party guest page no longer changes your selected player (by @marcelveldt in [#2290](https://github.com/music-assistant/frontend/pull/2290))
- Stop test runs from reporting success when errors escape a test (by @marcelveldt in [#2292](https://github.com/music-assistant/frontend/pull/2292))
- Search for a Home Assistant entity to use as a player control (by @marcelveldt in [#2316](https://github.com/music-assistant/frontend/pull/2316))
- Add artist name sorting to library views (by @dmoo500 in [#2268](https://github.com/music-assistant/frontend/pull/2268))
- Add support for authors and narrators (by @fmunkes in [#2000](https://github.com/music-assistant/frontend/pull/2000))
- Make test fixtures match the real API models (by @marcelveldt in [#2337](https://github.com/music-assistant/frontend/pull/2337))

### 🧰 Maintenance and dependency bumps

<details>
<summary>63 changes</summary>

- Search Home Assistant entities to use as player controls (by @marcelveldt in #5271)
- Keep group players up to date regardless of who triggers the update (by @marcelveldt in #5393)
- De-duplicate the metadata controller test fixture (by @marcelveldt in #5398)
- Show what a settings action did instead of redrawing the form (by @marcelveldt in #5402)
- Make player test config mocks behave like the real config (by @marcelveldt in #5422)
- Catch vulnerabilities a dependency update pulls in indirectly (by @marcelveldt in #5424)
- Stop tests crashing at random on a shared compile cache (by @marcelveldt in #5426)
- Tidy up where the Music Quiz AI limits live (by @marcelveldt in #5428)
- Share playlist track requests again on Yandex Music and KION Music (by @marcelveldt in #5430)
- Report Sonos S1 grouping failures as proper player errors (by @marcelveldt in #5431)
- Load the AcoustID fingerprinting library only when it is needed (by @marcelveldt in #5434)
- Stop providers from reloading twice after a lost connection or settings change (by @marcelveldt in #5435)
- ⬆️ Update music-assistant-frontend to 2.17.260 (by @musicassistant-bot[bot] in #5436)
- Keep all members of a cached tuple value intact (by @marcelveldt in #5437)
- Open Subsonic: Add API token based authentication and update to py-opensonic 10.3.0 (by @khers in #5438)
- Keep the PR label in sync when the description changes (by @marcelveldt in #5441)
- Clean up unused leftovers in the Sonos S1 player (by @marcelveldt in #5443)
- Clean up unused code in the Sonos S1 error handling (by @marcelveldt in #5445)
- Share the Music Quiz AI limit checks between quiz types (by @marcelveldt in #5448)
- Fix wrong playback position and track length for HEOS players (by @marcelveldt in #5450)
- Tidy up duplicated fixtures in the controller tests (by @marcelveldt in #5451)
- Tidy up duplicated fixtures in the provider tests (by @marcelveldt in #5452)
- Fix failing cache controller test on dev (by @marcelveldt in #5456)
- Correct the cache docs on what single_flight=False does (by @marcelveldt in #5457)
- Limit the length of AI-written smart playlist descriptions (by @marcelveldt in #5458)
- Tidy up the duplicated Tidal test fixtures (by @marcelveldt in #5459)
- Tidy up the API value parser (by @marcelveldt in #5460)
- Keep a playback position of zero instead of treating it as unknown (by @marcelveldt in #5461)
- Stop the dependency check from blaming a PR for a vulnerability it did not introduce (by @marcelveldt in #5462)
- Remove duplicated code around waiting for shared work (by @marcelveldt in #5463)
- Share My Wave and My Mix track requests between listeners (by @marcelveldt in #5464)
- Keep a muted speaker working normally after it leaves a group (by @marcelveldt in #5465)
- Make the Tidal ISRC lookup test check the real API URL (by @marcelveldt in #5466)
- Show which vulnerability findings the dependency check set aside (by @marcelveldt in #5467)
- Tidy up the helper order in the API helpers module (by @marcelveldt in #5468)
- Stop confusing an unknown DLNA position or volume with zero (by @marcelveldt in #5469)
- Name the argument in dictionary parse errors (by @marcelveldt in #5471)
- Fix volume changes when unmuting a speaker (by @marcelveldt in #5473)
- Make shared-request deduplication reliable for media item arguments (by @marcelveldt in #5475)
- Fix pre-commit hooks failing when committing from a git worktree (by @marcelveldt in #5476)
- Fix DLNA players reporting a position that runs ahead of the audio (by @marcelveldt in #5477)
- Stop Sonos S1 discovery from freezing the server (by @marcelveldt in #5478)
- Prevent Sonos S1 speakers from reconnecting after a provider reload (by @marcelveldt in #5479)
- Clean up pending Sonos speaker setups when the provider is removed (by @marcelveldt in #5480)
- Stop Sonos S1 from scanning for speakers after it is turned off (by @marcelveldt in #5481)
- Keep speaker grouping correct for every user (by @marcelveldt in #5482)
- Clean up disabled players when a player provider is unloaded (by @marcelveldt in #5483)
- Keep unloading a provider when one of its players fails to shut down (by @marcelveldt in #5484)
- Add test coverage for removing a player provider (by @marcelveldt in #5485)
- Use consistent line endings in the pre-commit config file (by @marcelveldt in #5488)
- Tidy up the Sonos S1 error handling helper (by @marcelveldt in #5491)
- Stop a player registration that was cancelled halfway (by @marcelveldt in #5492)
- Adjust Snapcast and Soundcloud code owners (by @OzGav in #5494)
- ⬆️ Update music-assistant-models to 1.1.184 (by @musicassistant-bot[bot] in #5495)
- ⬆️ Update music-assistant-frontend to 2.17.261 (by @musicassistant-bot[bot] in #5496)
- Auto-merge dependency bumps without manual conflict resolution (by @MarvinSchenkel in #5499)
- Use consistent line endings in provider icon files (by @marcelveldt in #5504)
- Update airplay-cli to v0.4.12 (by @musicassistant-bot[bot] in #5505)
- Fix dependency auto-merge workflow env contract test (by @MarvinSchenkel in #5507)
- Stop AirPlay from re-sending unchanged artwork on every seek (by @marcelveldt in #5508)
- Fix local code checks failing on some numba versions (by @marcelveldt in #5512)
- ⬆️ Update music-assistant-frontend to 2.17.262 (by @musicassistant-bot[bot] in #5514)
- Name the right speaker when Sonos S1 grouping fails (by @marcelveldt in #5519)

</details>

## :bow: Thanks to our contributors

Special thanks to the following contributors who helped with this release:

@GraysonCAdams, @MarvinSchenkel, @Odn0, @OzGav, @dmoo500, @fmunkes, @khers, @marcelveldt, @rwjack

## 2.10.0b12
- Upstream Music Assistant server (beta) update to 2.10.0b12

### Upstream Release Notes
## 📦 Beta Release

_Changes since [2.10.0b11](https://github.com/music-assistant/server/releases/tag/2.10.0b11)_

### 🚀 New Providers

- Add Storytel provider integration (by @jonasbp2011 in #4054)

### 🚀 Features and enhancements

- Support getting OpenSubsonic radio stations from music source (by @frjol in #5150)
- Ask Music Quiz Trivia release year questions about compilation tracks (by @marcelveldt in #5373)
- Start audio overlays without a delay (by @marcelveldt in #5379)
- Date quiz songs without an ISRC by artist and title (by @marcelveldt in #5386)
- Apple Music: batch library sync requests to cut API usage (by @MarvinSchenkel in #5391)
- More accurate release years for Music Quiz songs (by @marcelveldt in #5413)

### 🐛 Bugfixes

- Align Spotify app volume with MA player volume on connection (by @OzGav in #5303)
- Better crossfades on tracks with long outros, ambient blends and mastered fade-outs (by @MarvinSchenkel in #5365)
- Fix missing mute control for universal group players (by @marcelveldt in #5375)
- Keep a mono sound effect at the same volume as a stereo one (by @marcelveldt in #5376)
- Fix playback stopping after the first track on grouped Sonos speakers (by @marcelveldt in #5385)
- Keep the chosen metadata language when other settings are saved (by @marcelveldt in #5396)
- Keep manually set radio name and artwork in playlists (by @OzGav in #5404)
- Fix Sonos S1 speakers hanging after a failed subscription (by @marcelveldt in #5406)
- Fix playback from Home Assistant failing with a permission error (by @MarvinSchenkel in #5410)
- Keep a synced pair of speakers muted when the group volume changes (by @marcelveldt in #5420)

### 🎨 Frontend Changes

- Fix skip forward/backward in the OS media notification (by @marcelveldt in [#2271](https://github.com/music-assistant/frontend/pull/2271))
- Tidy up the lyrics elapsed time composable (by @marcelveldt in [#2280](https://github.com/music-assistant/frontend/pull/2280))
- Guard the startup order in the app initialization tests (by @marcelveldt in [#2285](https://github.com/music-assistant/frontend/pull/2285))
- Clean up a stale queue lookup in the party guest page (by @marcelveldt in [#2286](https://github.com/music-assistant/frontend/pull/2286))
- Make the self-closing tag lint rule actually run (by @marcelveldt in [#2287](https://github.com/music-assistant/frontend/pull/2287))
- Fix Save button blocked by a setting you cannot fill in (by @marcelveldt in [#2284](https://github.com/music-assistant/frontend/pull/2284))
- Handle settings action buttons in one shared place (by @marcelveldt in [#2281](https://github.com/music-assistant/frontend/pull/2281))
- Document how a queue's active flag relates to the player's active source (by @marcelveldt in [#2282](https://github.com/music-assistant/frontend/pull/2282))
- Fix the player progress bar standing still or starting at zero (by @marcelveldt in [#2279](https://github.com/music-assistant/frontend/pull/2279))
- Make the pre-commit check fast again (by @marcelveldt in [#2277](https://github.com/music-assistant/frontend/pull/2277))

### Other Changes

- Keep ffmpeg's per-input read options with the input they belong to (by @marcelveldt in #5407)

### 🧰 Maintenance and dependency bumps

<details>
<summary>28 changes</summary>

- Notice when AI Radio loses its AI or text-to-speech engine (by @marcelveldt in #5309)
- Only fail the dependency security check on vulnerabilities a PR introduces (by @marcelveldt in #5346)
- Avoid duplicate provider requests for the same uncached data (by @marcelveldt in #5370)
- Make the group mute command work on any player (by @marcelveldt in #5374)
- Reattach a player control after it comes back (by @marcelveldt in #5377)
- Only refetch the Home Assistant entity registry when a change can affect it (by @marcelveldt in #5378)
- Keep a protocol's own setting dependencies when shown on a player (by @marcelveldt in #5382)
- Add test coverage for protocol settings shown next to a player's own (by @marcelveldt in #5383)
- Fix mismatched default when reading the preferred output protocol setting (by @marcelveldt in #5384)
- ⬆️ Update music-assistant-frontend to 2.17.259 (by @musicassistant-bot[bot] in #5387)
- ⬆️ Update music-assistant-models to 1.1.181 (by @musicassistant-bot[bot] in #5388)
- Ard sounds rebrand (by @OzGav in #5389)
- Show the real buffer depth default per device (by @marcelveldt in #5390)
- Avoid redundant Sonos S1 speaker polls after commands (by @marcelveldt in #5394)
- Accept AI quiz answers that arrive wrapped in a code fence (by @marcelveldt in #5395)
- Make the Home Assistant registry-race tests wait for the actual fetch (by @marcelveldt in #5399)
- Bound the Trivia quiz AI response the same way as the distractor parser (by @marcelveldt in #5400)
- Use one shared rule for trusting album release info in Music Quiz (by @marcelveldt in #5401)
- Don't demand a setup setting the user cannot fill in (by @marcelveldt in #5403)
- Only announce the publish IP for network discovery (by @marcelveldt in #5411)
- Remove unused extra_args parameter from ffmpeg helpers (by @marcelveldt in #5412)
- Stop stream options from piling up on repeated plays of the same item (by @marcelveldt in #5414)
- ⬆️ Update music-assistant-models to 1.1.182 (by @musicassistant-bot[bot] in #5419)
- Fix playback position being dropped from the player state (by @marcelveldt in #5421)
- Fix a misleading comment about player output settings (by @marcelveldt in #5423)
- Make the streamserver's internal address list private (by @marcelveldt in #5425)
- ⬆️ Update music-assistant-models to 1.1.183 (by @musicassistant-bot[bot] in #5427)
- Document the native libraries needed to run the tests locally (by @marcelveldt in #5429)

</details>

## :bow: Thanks to our contributors

Special thanks to the following contributors who helped with this release:

@MarvinSchenkel, @OzGav, @frjol, @jonasbp2011, @marcelveldt

## 2.10.0b11
- Upstream Music Assistant server (beta) update to 2.10.0b11

### Upstream Release Notes
## 📦 Beta Release

_Changes since [2.10.0b10](https://github.com/music-assistant/server/releases/tag/2.10.0b10)_

### 🚀 New Providers

- Add Overcast podcast provider (by @OzGav in #5151)
- Add OpenAI Compatible provider for the AI features (by @marcelveldt in #5261)
- Add OpenAI text-to-speech provider (by @marcelveldt in #5262)
- Add ABC Radio Network music provider (by @OzGav in #5321)

### 🚀 Features and enhancements

- MusicBrainz recommendations: Person/band distinction (by @dmoo500 in #4687)
- Add DSP convolution filter (by @OzGav in #4947)
- Add Safety Limiter and Compressor DSP filters (by @OzGav in #5004)
- Follow-up fixes and enhancements to author and narrator support (by @fmunkes in #5062)
- Expose external id lookup on the API (by @OzGav in #5160)
- Establish and keep the duration of podcast episodes if their feed does not supply it (by @OzGav in #5178)
- Cache podcast episode listings and batch their resume lookups (by @distante in #5179)
- Report AirPlay speakers that stay silent while shown as playing (by @marcelveldt in #5217)
- Add party duration config option (by @lordhi in #5230)
- Let each provider pick which AI and text-to-speech engine it uses (by @marcelveldt in #5253)
- Let plugins and music providers describe audio the same way (by @marcelveldt in #5264)
- Let clients correct for a clock that is out of sync (by @marcelveldt in #5266)
- Change Home Assistant player controls without reconnecting (by @marcelveldt in #5268)
- Reuse the Home Assistant device list instead of re-fetching it constantly (by @marcelveldt in #5273)
- Enter text-to-speech voices as separate values (by @marcelveldt in #5278)
- Make radio M3U export/import survive its own round trip (by @chrisuthe in #5289)
- Generate AI Radio segments at airtime instead of at run start (by @MarvinSchenkel in #5301)
- Migration for new icons for picker (by @stvncode in #5306)
- Smarter crossfade choices for quiet tails and backing vocals (by @MarvinSchenkel in #5357)

### 🐛 Bugfixes

- Fix AirPlay Receiver losing startup metadata events (by @MarvinSchenkel in #4787)
- Handle remote storage going away during a library sync (by @OzGav in #5076)
- Fix Recently played dropping explicit track plays and logging empty containers (by @chrisuthe in #5163)
- Library item counts now respect the user's provider filter (by @chrisuthe in #5165)
- Mount the NFS export as configured and scan the Subfolder inside it (by @chrisuthe in #5167)
- Wait for a running library sync to stop before unloading a provider (by @marcelveldt in #5197)
- Show the full track length after seeking (by @marcelveldt in #5198)
- Stop one component's log level from flooding the log with unrelated messages (by @marcelveldt in #5203)
- Fix playability of plain stream URLs and handle verification of URIs gracefully (by @fmunkes in #5204)
- Do not update the playback position when we are not playing in MusicCast (by @fmunkes in #5205)
- Don't let one bad Home Assistant entity break the whole HA integration (by @OzGav in #5206)
- Fix squeezelite players stuck unavailable after restart  (by @gdesmott in #5207)
- Remove the extra delay when starting a single AirPlay speaker (by @marcelveldt in #5208)
- Keep the account login dialog in step with the browser (by @marcelveldt in #5209)
- Fix speakers joining a playing group out of sync (by @marcelveldt in #5210)
- Fix Music Timeline bonus questions running out of answer options (by @marcelveldt in #5212)
- Improve Music Timeline song variety and release years (by @marcelveldt in #5213)
- Show when a Music Quiz game is restarting (by @marcelveldt in #5214)
- Load the Home Assistant settings much faster on large setups (by @marcelveldt in #5216)
- Fix AirPlay 2 speakers playing silence on multi-homed hosts (by @marcelveldt in #5219)
- Fix AirPlay speakers playing behind when grouped with a Sendspin player (by @marcelveldt in #5220)
- Fix a group start recording an instant it never used (by @marcelveldt in #5223)
- Keep speakers playing when a group switches output (by @marcelveldt in #5225)
- Fix Flow Mode progress after abandoned stream probes (by @alectogeek in #5228)
- Fix seek progress snapback before stream restart (by @alectogeek in #5229)
- Redact authorization headers from request logs (by @teancom in #5236)
- Wait for every group member's clock before anchoring playback (by @marcelveldt in #5237)
- Fix one bad join code locking out all other guests (by @marcelveldt in #5243)
- Use original release years for Music Timeline songs (by @marcelveldt in #5250)
- Announce preset changes when an impulse response is removed (by @OzGav in #5256)
- Use whitelist for MusicBrainz artist types in recommendations (by @dmoo500 in #5260)
- Keep Music Quiz lyrics in step with the audio (by @marcelveldt in #5263)
- Fix Home Assistant connection drop on large entity registries (by @marcelveldt in #5270)
- Allow multiple sessions in Audiobookshelf - fixes autoplay behavior (by @fmunkes in #5275)
- Fix muting being blocked by the volume control setting (by @marcelveldt in #5285)
- Fix media details occasionally resolving to the wrong item (by @marcelveldt in #5288)
- Remove spurious error log entries for shared requests (by @marcelveldt in #5295)
- Ensure login providers endpoint doesn't crash when HA provider has no config URL (by @OzGav in #5304)
- Recover a bridged AirPlay speaker when its stream process dies (by @marcelveldt in #5311)
- Remove phantom concurrent task sliders (by @OzGav in #5317)
- Fix Sendspin setup flow (by @arturpragacz in #5318)
- Only show library sync deletions setting for providers with library sync (by @OzGav in #5320)
- Sonos speakers now recover on their own after a network interruption (by @MarvinSchenkel in #5322)
- Bring a bridged AirPlay speaker back into its group after a failed start (by @marcelveldt in #5323)
- Recover a local audio device when its output stream dies (by @marcelveldt in #5325)
- Fix AirPlay volume changes being lost around stream start (by @marcelveldt in #5328)
- Make the Mono output channels option work on all players (by @marcelveldt in #5329)
- Apple Music: recover from throttled requests in ~1s instead of stalling playback (by @MarvinSchenkel in #5333)
- Use original release years for Trivia questions (by @marcelveldt in #5350)
- Fail unconfirmed AirPlay starts and wait for every speaker's clock (by @marcelveldt in #5352)
- Fix bridged AirPlay speakers going silent or double-started (by @marcelveldt in #5354)
- Fix mute command failing on group players (by @marcelveldt in #5364)
- Deepen the AirPlay buffer for LinkPlay devices instead of dropping PTP (by @marcelveldt in #5369)

### 🎨 Frontend Changes

- Add support for Audiobook collections (by @fmunkes in [#2155](https://github.com/music-assistant/frontend/pull/2155))
- Add "Play from beginning" for podcast episodes (by @chrisuthe in [#2184](https://github.com/music-assistant/frontend/pull/2184))
- Add DSP stereo width and crossfeed filters (by @OzGav in [#2189](https://github.com/music-assistant/frontend/pull/2189))
- Explain why joining a party or quiz failed (by @marcelveldt in [#2242](https://github.com/music-assistant/frontend/pull/2242))
- Show when a Music Quiz game is restarting (by @marcelveldt in [#2240](https://github.com/music-assistant/frontend/pull/2240))
- Start audio faster on web players (by @marcelveldt in [#2241](https://github.com/music-assistant/frontend/pull/2241))
- Fix setup wizard jumping back to a previous step (by @marcelveldt in [#2239](https://github.com/music-assistant/frontend/pull/2239))
- Remove JWT claims the server never mints (by @chrisuthe in [#2236](https://github.com/music-assistant/frontend/pull/2236))
- Fix untranslated text in the interface (by @marcelveldt in [#2244](https://github.com/music-assistant/frontend/pull/2244))
- Add convolution DSP filter with impulse response library (by @OzGav in [#2223](https://github.com/music-assistant/frontend/pull/2223))
- Keep timings correct when a device clock is out of sync (by @marcelveldt in [#2248](https://github.com/music-assistant/frontend/pull/2248))
- Keep Music Quiz lyrics in step with the audio (by @marcelveldt in [#2246](https://github.com/music-assistant/frontend/pull/2246))
- Keep settings pages up to date when other providers are added or removed (by @marcelveldt in [#2245](https://github.com/music-assistant/frontend/pull/2245))
- Tell a guest when their party or quiz session has ended (by @marcelveldt in [#2243](https://github.com/music-assistant/frontend/pull/2243))
- Maintain constant album art size on now playing view (by @OzGav in [#2237](https://github.com/music-assistant/frontend/pull/2237))
- Remove leftover panel-expansion state from the settings config editor (by @marcelveldt in [#2256](https://github.com/music-assistant/frontend/pull/2256))
- Fix a broken test assertion (by @marcelveldt in [#2255](https://github.com/music-assistant/frontend/pull/2255))
- Fix the mini equalizer position at non-standard playback speeds (by @marcelveldt in [#2250](https://github.com/music-assistant/frontend/pull/2250))
- Add missing tests for reconnect, language switching and connection warnings (by @marcelveldt in [#2249](https://github.com/music-assistant/frontend/pull/2249))
- Add missing test coverage for guest entry provider updates (by @marcelveldt in [#2253](https://github.com/music-assistant/frontend/pull/2253))
- Fix the media session progress bar throwing on every position update (by @MarvinSchenkel in [#2267](https://github.com/music-assistant/frontend/pull/2267))
- Adapt fe and icon picker with the new icon set (by @stvncode in [#2264](https://github.com/music-assistant/frontend/pull/2264))
- Show the party guest now-playing marker on the track that is playing (by @marcelveldt in [#2278](https://github.com/music-assistant/frontend/pull/2278))

### Other Changes

- Use shared port helpers in Plex Connect port allocation (by @MarvinSchenkel in #4647)
- Remove unused track info lookup from the MSX Bridge player (by @marcelveldt in #5201)
- Remove unused authentication middleware (by @marcelveldt in #5211)
- Clean up unreachable checks in player control commands (by @marcelveldt in #5286)
- Lokalise translations update (by @github-actions[bot] in #5292)
- Name FFmpeg channel layouts in one place (by @marcelveldt in #5367)

### 🧰 Maintenance and dependency bumps

<details>
<summary>90 changes</summary>

- Clean MusicBrainz identifiers from OpenSubsonic and Plex servers (by @OzGav in #5149)
- Add an Automated PR Review bot (manual pilot) (by @chrisuthe in #5185)
- Log the resolved interface and publish IP when starting cliairplay (by @marcelveldt in #5215)
- Remove an unused, empty helper function (by @marcelveldt in #5218)
- Update airplay-cli to v0.4.5 (by @musicassistant-bot[bot] in #5221)
- ⬆️ Update music-assistant-frontend to 2.17.253 (by @musicassistant-bot[bot] in #5222)
- Update airplay-cli to v0.4.6 (by @musicassistant-bot[bot] in #5224)
- Bump nnaudio from 0.3.3 to 0.3.4 (by @dependabot[bot] in #5232)
- Bump soco from 0.31.1 to 0.31.2 (by @dependabot[bot] in #5233)
- Bump async-upnp-client from 0.46.2 to 0.48.0 (by @dependabot[bot] in #5234)
- Bump syrupy from 5.2.0 to 5.5.3 (by @dependabot[bot] in #5235)
- Reduce unexpected Snapcast debug logging (by @marcelveldt in #5238)
- Enable Zeroconf discovery logging (by @marcelveldt in #5239)
- Fail faster when an AirPlay start or flush is rejected (by @marcelveldt in #5240)
- Improve AirPlay late-join buffering (by @marcelveldt in #5241)
- Keep the AirPlay track position correct after a timing correction (by @marcelveldt in #5242)
- Log which AirPlay speaker failed to start (by @marcelveldt in #5244)
- Correct outdated comments about Sendspin stream buffering (by @marcelveldt in #5245)
- Skip an AirPlay speaker that would only play silence (by @marcelveldt in #5246)
- Report AirPlay artwork rejections instead of hiding them (by @marcelveldt in #5247)
- Report the real AirPlay timing state in diagnostics (by @marcelveldt in #5248)
- Clarify a comment about how AirPlay playback is anchored (by @marcelveldt in #5249)
- Update airplay-cli to v0.4.7 (by @musicassistant-bot[bot] in #5251)
- ⬆️ Update music-assistant-frontend to 2.17.254 (by @musicassistant-bot[bot] in #5252)
- Migrate the podcast providers to the shared Overcast patterns (by @OzGav in #5254)
- Point the SiriusXM labels at the common strings (by @OzGav in #5255)
- Remove dead code from the AirPlay provider (by @marcelveldt in #5257)
- Name the plugin each AI/TTS engine comes from in the picker (by @marcelveldt in #5258)
- Test the instant an AirPlay start actually schedules (by @marcelveldt in #5259)
- Name the speaker on every cliairplay log line (by @marcelveldt in #5265)
- Fix remote access failing to reach the built-in Sendspin server (by @marcelveldt in #5267)
- Bump cryptography from 49.0.0 to 50.0.0 (by @dependabot[bot] in #5272)
- Bump aiohttp from 3.14.1 to 3.14.3 (by @dependabot[bot] in #5274)
- Also test IPv6 when listening on all network interfaces (by @marcelveldt in #5276)
- Use one shared definition for wildcard bind addresses (by @marcelveldt in #5277)
- Play AI Radio TTS clips that are rendered to a local file (by @marcelveldt in #5279)
- Let players fall back when a control is taken away (by @marcelveldt in #5280)
- Advertise all server addresses for AirPlay remote control (by @marcelveldt in #5281)
- Stop tests from failing on a port another process took (by @marcelveldt in #5282)
- Fix AriaCast receiver being unreachable on networks without internet access (by @marcelveldt in #5283)
- Correct how remote access builds its local websocket address (by @marcelveldt in #5284)
- Split voices pasted into a single value (by @marcelveldt in #5287)
- ⬆️ Update music-assistant-frontend to 2.17.255 (by @musicassistant-bot[bot] in #5290)
- ⬆️ Update music-assistant-models to 1.1.178 (by @musicassistant-bot[bot] in #5291)
- Advertise all server addresses for Snapcast and Sendspin discovery (by @marcelveldt in #5293)
- Fix duplicate requests and tasks outliving shutdown (by @marcelveldt in #5296)
- Add tests for external player control power and volume commands (by @marcelveldt in #5297)
- Turn guest access into a normal on/off setting (by @marcelveldt in #5298)
- Fix remote access failing to reach the Music Assistant API (by @marcelveldt in #5299)
- Keep bridged AirPlay speakers in sync after an audio dropout (by @marcelveldt in #5300)
- ⬆️ Update music-assistant-models to 1.1.179 (by @musicassistant-bot[bot] in #5302)
- Run the Test workflow on merge groups (by @MarvinSchenkel in #5305)
- Remove duplicated config stub from the player controller tests (by @marcelveldt in #5307)
- Stop logging spurious errors when an artwork request is cancelled (by @marcelveldt in #5308)
- Stop AI Radio and Smart Playlist from hanging on a stalled AI engine (by @marcelveldt in #5310)
- Stop AirPlay speaker starts from logging a false warning (by @marcelveldt in #5312)
- Keep grouped AirPlay speakers on the same clock (by @marcelveldt in #5313)
- Update documentation links (by @OzGav in #5314)
- Add how to contribute documentation link to PR template (by @OzGav in #5315)
- Follow-up fixes for the AirPlay status contract and solo starts (by @marcelveldt in #5316)
- ⬆️ Update music-assistant-models to 1.1.180 (by @musicassistant-bot[bot] in #5319)
- Apply a changed stream server address without a restart (by @marcelveldt in #5324)
- Wait for a full audio pipe to drain instead of erroring out (by @marcelveldt in #5326)
- Keep AirPlay speakers on the same clock when they start at different times (by @marcelveldt in #5327)
- Show the right address when the SSL certificate can't be loaded (by @marcelveldt in #5330)
- Report the address the webserver actually bound to (by @marcelveldt in #5332)
- ⬆️ Update music-assistant-frontend to 2.17.256 (by @musicassistant-bot[bot] in #5334)
- Publish the address the streamserver is actually bound to (by @marcelveldt in #5335)
- Update airplay-cli to v0.4.8 (by @musicassistant-bot[bot] in #5336)
- Keep the Character index intact when the server stops during a refresh (by @marcelveldt in #5337)
- Don't start an AirPlay session that is already outdated (by @marcelveldt in #5338)
- Run the test suite in parallel (by @MarvinSchenkel in #5341)
- Update auntie-sounds requirement to version 2.0.3 (by @OzGav in #5342)
- Remove an unused internal URL from the webserver helper (by @marcelveldt in #5343)
- Make the discovery tests independent of the host platform (by @marcelveldt in #5344)
- Only rewrite the settings file on shutdown when something changed (by @marcelveldt in #5345)
- Don't remember a mute that never happened (by @marcelveldt in #5347)
- Protect the cached Home Assistant entity list and reduce its memory use (by @marcelveldt in #5348)
- Show the real SSL status in the webserver settings (by @marcelveldt in #5349)
- Prevent short server freezes when similarity indexes are saved (by @marcelveldt in #5351)
- ⬆️ Update music-assistant-frontend to 2.17.257 (by @musicassistant-bot[bot] in #5358)
- Keep the settings file safe when a save is cancelled on shutdown (by @marcelveldt in #5360)
- Bump CodSpeedHQ/action from 5.0.1 to 5.0.2 (by @dependabot[bot] in #5361)
- Fix mono audio playing too quietly and stalling some players (by @marcelveldt in #5362)
- Fix surround sound sources being misread as stereo (by @marcelveldt in #5363)
- Update airplay-cli to v0.4.10 (by @musicassistant-bot[bot] in #5366)
- Look for a caller's own audio filter graph in every argument list (by @marcelveldt in #5368)
- Use less memory for the cached Home Assistant entity registry (by @marcelveldt in #5371)
- Update airplay-cli to v0.4.11 (by @musicassistant-bot[bot] in #5372)
- ⬆️ Update music-assistant-frontend to 2.17.258 (by @musicassistant-bot[bot] in #5381)

</details>

## :bow: Thanks to our contributors

Special thanks to the following contributors who helped with this release:

@MarvinSchenkel, @OzGav, @alectogeek, @arturpragacz, @chrisuthe, @distante, @dmoo500, @fmunkes, @gdesmott, @lordhi, @marcelveldt, @stvncode, @teancom

## 2.10.0b10
- Upstream Music Assistant server (beta) update to 2.10.0b10

### Upstream Release Notes
## 📦 Beta Release

_Changes since [2.10.0b9](https://github.com/music-assistant/server/releases/tag/2.10.0b9)_

### 🚀 Features and enhancements

- Add Stereo Width and Crossfeed DSP filters (by @OzGav in #4971)
- Announcements start faster and no longer get cut off (by @marcelveldt in #5115)
- Rename Radio Playlists plugin to Endless Mix Playlists (by @MarvinSchenkel in #5128)
- Autoplay continues your podcast or audiobook instead of switching to music (by @marcelveldt in #5141)
- Autoplay is on by default for new players (by @marcelveldt in #5144)
- A finished queue keeps its tracks so you can play it again (by @marcelveldt in #5156)
- Add Dutch to Alexa language commands (by @R3inoudR in #5166)
- Gapless seeks and reliable group sync on AirPlay players (by @marcelveldt in #5181)
- Add external_until for poll-completed external steps (by @jozefKruszynski in #5184)
- Let corrected AirPlay joins heal themselves instead of re-joining (by @marcelveldt in #5194)
- Start AirPlay late joins as soon as the speaker is ready (by @marcelveldt in #5202)

### 🐛 Bugfixes

- Handle invalid MusicBrainz identifiers in file tags gracefully (by @OzGav in #5073)
- Fix podcast playback on feeds that list a cover image before the audio (by @MarvinSchenkel in #5078)
- Fix pause failing on Cast devices streaming via Sendspin (by @MarvinSchenkel in #5083)
- Fix bit-perfect status for lossy sources (by @marcelveldt in #5087)
- Fix Audiobookshelf configuration loading (by @marcelveldt in #5088)
- Play the track you selected when shuffle is on (by @marcelveldt in #5092)
- Fix AirPlay players joining a playing group out of sync (by @marcelveldt in #5098)
- Fix lyrics and other optional values breaking on cached empty results (by @MarvinSchenkel in #5099)
- Fix volume limit enforcement for players with redirected volume control (by @OzGav in #5102)
- Show protocol-connected speakers in the Music Quiz speaker picker (by @MarvinSchenkel in #5103)
- Don't apply volume normalization to sound effects (by @MarvinSchenkel in #5105)
- Keep AI Radio segments in order and add a shuffle toggle (by @MarvinSchenkel in #5106)
- Fix Yandex My Wave stopping after initial batch (by @alectogeek in #5107)
- Automatically re-join AirPlay group members after a brief connection loss (by @marcelveldt in #5112)
- Don't render announcements twice when a player sends a HEAD request (by @marcelveldt in #5113)
- Restore player state when an announcement fails (by @marcelveldt in #5114)
- Measure true peak during loudness analysis (by @MarvinSchenkel in #5118)
- Remove stale Audiobookshelf playback sessions to avoid repeated sync failures (by @foobarth in #5120)
- Reduce deezer-python-gql log verbosity to match provider level (by @foobarth in #5121)
- Apple Music: signing in a second account no longer breaks the first (by @MarvinSchenkel in #5122)
- Don't start unrelated music when pressing play on an empty queue (by @marcelveldt in #5124)
- Fix remote access flooding the log with ICE and TURN warnings (by @MarvinSchenkel in #5125)
- Don't show the dashboard keepalive as active playback on cast players (by @MarvinSchenkel in #5127)
- Sendspin: freeze playback progress before tearing down the push stream (by @chrisuthe in #5129)
- Keep an AI Radio show and its queue in sync when either one stops (by @MarvinSchenkel in #5130)
- Snapshot Sendspin playback progress at natural end of stream (by @chrisuthe in #5131)
- Support password-protected AirPlay speakers (by @marcelveldt in #5134)
- Reconfiguring an AirPlay player can now redo or reset its pairing (by @marcelveldt in #5135)
- AirPlay playback no longer starts muted after the speaker was in standby (by @marcelveldt in #5139)
- Detect password-protected AirPlay devices more reliably (by @marcelveldt in #5147)
- Use one source of truth for AirPlay password announcements (by @marcelveldt in #5148)
- Reduce WebRTC and WiiM log noise when debug logging is enabled (by @MarvinSchenkel in #5153)
- Fix startup provider failures and show which provider needs attention (by @marcelveldt in #5162)
- Fix AirPlay noise bursts and group sync issues on Apple devices (by @marcelveldt in #5168)
- Pick a new go-librespot API port when the configured one is unavailable (by @OzGav in #5169)
- Clear stale library IDs in Audiobookshelf sync and validate cache on startup (by @foobarth in #5172)
- Stop log flooding and retry storms when artwork fails to download (by @marcelveldt in #5174)
- Stop re-sending unchanged album art around AirPlay track changes (by @marcelveldt in #5182)
- Fix late-joining AirPlay players starting out of sync (by @marcelveldt in #5186)
- Fix providers wrongly showing a setup error when they loaded fine (by @marcelveldt in #5190)
- Fix rejoining AirPlay players that start out of sync when their clock is slow to lock (by @marcelveldt in #5191)
- Fix SMB and NFS shares failing to reconnect after a reload (by @marcelveldt in #5192)
- Fix providers that depend on another provider failing to start (by @marcelveldt in #5200)

### 🎨 Frontend Changes

- Revert "Add convolution DSP filter with impulse response library" (by @stvncode in [#2222](https://github.com/music-assistant/frontend/pull/2222))
- Use vue-i18n pluralization for settings totals labels (by @geofffranks in [#2201](https://github.com/music-assistant/frontend/pull/2201))
- Add convolution DSP filter with impulse response library (by @OzGav in [#2190](https://github.com/music-assistant/frontend/pull/2190))
- Clarify the bit-perfect playback label (by @marcelveldt in [#2224](https://github.com/music-assistant/frontend/pull/2224))
- Lokalise translations update (by @[github-actions[bot]](https://github.com/apps/github-actions) in [#2226](https://github.com/music-assistant/frontend/pull/2226))
- Add a shuffle toggle to AI Radio shows (by @MarvinSchenkel in [#2227](https://github.com/music-assistant/frontend/pull/2227))
- Drop the AI Radio clear-queue-on-start option (by @MarvinSchenkel in [#2230](https://github.com/music-assistant/frontend/pull/2230))
- Rename radio actions to endless mix (by @MarvinSchenkel in [#2148](https://github.com/music-assistant/frontend/pull/2148))
- Add help text to the DSP filters and gain stages and begin migration to shadcn (by @OzGav in [#2180](https://github.com/music-assistant/frontend/pull/2180))
- Update the error banner for provider in discover apge (by @stvncode in [#2225](https://github.com/music-assistant/frontend/pull/2225))
- Fix shows vanishing from the AI Radio gallery under a non-English locale (by @MarvinSchenkel in [#2229](https://github.com/music-assistant/frontend/pull/2229))
- Show that a queue finished playing (by @marcelveldt in [#2234](https://github.com/music-assistant/frontend/pull/2234))
- Stop lint and formatting reaching into nested git worktrees (by @marcelveldt in [#2233](https://github.com/music-assistant/frontend/pull/2233))
- Stop the test suite picking up tests from nested git worktrees (by @marcelveldt in [#2232](https://github.com/music-assistant/frontend/pull/2232))

### Other Changes

- Lokalise translations update (by @github-actions[bot] in #5096)
- Move announcement handling into its own module (by @marcelveldt in #5133)

### 🧰 Maintenance and dependency bumps

<details>
<summary>32 changes</summary>

- Promote LRC formatted text in the plain lyrics tag to lrc_lyrics (by @OzGav in #5066)
- Bump actions/upload-artifact from 7.0.0 to 7.0.1 (by @dependabot[bot] in #5089)
- Bump CodSpeedHQ/action from 4.18.5 to 4.19.1 (by @dependabot[bot] in #5090)
- Bump actions/download-artifact from 8.0.0 to 8.0.1 (by @dependabot[bot] in #5091)
- ⬆️ Update music-assistant-frontend to 2.17.249 (by @musicassistant-bot[bot] in #5094)
- ⬆️ Update music-assistant-models to 1.1.174 (by @musicassistant-bot[bot] in #5095)
- Align PR review instructions with current context engineering guidance (by @MarvinSchenkel in #5097)
- Update airplay-cli to v0.3.7 (by @musicassistant-bot[bot] in #5100)
- Remove Mother Earth Radio (by @OzGav in #5104)
- Bump docker/login-action from 4.5.1 to 4.5.2 (by @dependabot[bot] in #5108)
- ⬆️ Update music-assistant-frontend to 2.17.250 (by @musicassistant-bot[bot] in #5116)
- ⬆️ Update music-assistant-models to 1.1.175 (by @musicassistant-bot[bot] in #5117)
- Update airplay-cli to v0.3.8 (by @musicassistant-bot[bot] in #5126)
- Bump docker/login-action from 4.5.2 to 4.6.0 (by @dependabot[bot] in #5137)
- Bump CodSpeedHQ/action from 4.19.1 to 5.0.1 (by @dependabot[bot] in #5138)
- Update airplay-cli to v0.3.9 (by @musicassistant-bot[bot] in #5142)
- Catch duplicate keys in translation source files (by @marcelveldt in #5145)
- Fix failing protocol play/pause tests on dev (by @marcelveldt in #5146)
- ⬆️ Update music-assistant-frontend to 2.17.251 (by @musicassistant-bot[bot] in #5152)
- ⬆️ Update music-assistant-models to 1.1.176 (by @musicassistant-bot[bot] in #5154)
- Add CI checks for pull request titles and descriptions (by @MarvinSchenkel in #5155)
- Align minimum ffmpeg version requirements in the codebase  (by @OzGav in #5159)
- Check out the base branch, and never post a bare mention (by @chrisuthe in #5164)
- ⬆️ Update music-assistant-frontend to 2.17.252 (by @musicassistant-bot[bot] in #5170)
- Update airplay-cli to v0.4.0 (by @musicassistant-bot[bot] in #5176)
- Fix noisy 'Task exception was never retrieved' errors in the log (by @marcelveldt in #5177)
- Update airplay-cli to v0.4.1 (by @musicassistant-bot[bot] in #5183)
- Update airplay-cli to v0.4.2 (by @musicassistant-bot[bot] in #5189)
- Update airplay-cli to v0.4.3 (by @musicassistant-bot[bot] in #5193)
- ⬆️ Update music-assistant-models to 1.1.177 (by @musicassistant-bot[bot] in #5195)
- Update airplay-cli to v0.4.4 (by @musicassistant-bot[bot] in #5196)
- Keep Apple TV protocol chatter out of AirPlay debug logs (by @marcelveldt in #5199)

</details>

## :bow: Thanks to our contributors

Special thanks to the following contributors who helped with this release:

@MarvinSchenkel, @OzGav, @R3inoudR, @alectogeek, @chrisuthe, @foobarth, @geofffranks, @jozefKruszynski, @marcelveldt, @stvncode

## 2.9.10
- Upstream Music Assistant server (beta) update to 2.9.10

### Upstream Release Notes
## 📦 Stable Release

_Changes since [2.9.9](https://github.com/music-assistant/server/releases/tag/2.9.9)_

### 🐛 Bugfixes

- Fix flow mode not switching sample rate between tracks on wrapped players (by @MarvinSchenkel in #4685)
- Fix AirPlay Receiver losing audio after quick reconnects (by @MarvinSchenkel in #4785)
- Fix sync group stopping playback when members are removed mid-regroup (by @MarvinSchenkel in #4815)
- Fix fake mute never reporting muted state (by @OzGav in #4839)
- Send progress metadata on Sendspin playback-state transitions (by @chrisuthe in #4876)
- Upgrade SiriusXM stream artwork URLs to https (by @OzGav in #4891)
- Fix ffmpeg stderr log flood on corrupted/malformed audio streams (by @chrisuthe in #4908)
- Raise API throttler to measured safe rate (by @jozefKruszynski in #4923)
- Release the active output protocol when a wrapped player's session ends (by @marcelveldt in #4940)
- Preserve HEOS now-playing metadata during MA-controlled playback (by @geofffranks in #5021)
- Handle invalid MusicBrainz identifiers in file tags gracefully (by @OzGav in #5073)
- Fix podcast playback on feeds that list a cover image before the audio (by @MarvinSchenkel in #5078)
- Play the track you selected when shuffle is on (by @marcelveldt in #5093)
- Fix lyrics and other optional values breaking on cached empty results (by @MarvinSchenkel in #5099)
- Restore player state when an announcement fails (by @marcelveldt in #5114)
- Apple Music: signing in a second account no longer breaks the first (by @MarvinSchenkel in #5122)
- AirPlay playback no longer starts muted after the speaker was in standby (by @marcelveldt in #5139)

### Other Changes

- [Backport to stable] Don't crash DLNA player update on malformed device metadata XML (#4682) (by @OzGav in #4840)
- Fix sync group stopping playback when members are removed mid-regroup (#4815) (by @marcelveldt in #4845)

### 🧰 Maintenance and dependency bumps

- Fix smart playlist documentation URL (by @Matthew-Kilpatrick in #5012)
- Remove Mother Earth Radio (by @OzGav in #5104)

## :bow: Thanks to our contributors

Special thanks to the following contributors who helped with this release:

@MarvinSchenkel, @Matthew-Kilpatrick, @OzGav, @chrisuthe, @geofffranks, @jozefKruszynski, @marcelveldt

## 2.10.0b9
- Upstream Music Assistant server (beta) update to 2.10.0b9

### Upstream Release Notes
## 📦 Beta Release

_Changes since [2.10.0b7](https://github.com/music-assistant/server/releases/tag/2.10.0b7)_

### 🚀 New Providers

- Add AI Radio Plugin (by @swiftbird07 in #3407)

### 🚀 Features and enhancements

- Load Discover recommendation rows on demand and improve Recently Played (by @chrisuthe in #4487)
- MSX Bridge: Party Mode QR on TVs, direct streamserver delivery, playback and CSRF hardening (by @trudenboy in #4734)
- Allow collapsing of collections in base media controller (by @fmunkes in #4806)
- Support DSP filters that need a second audio input (by @OzGav in #4872)
- AirPlay: unified cliairplay binary (native AirPlay 2, PTP, MediaRemote) (by @marcelveldt in #4879)
- Add native controls to AirPlay devices (by @marcelveldt in #4882)
- Cast dashboards to display devices (by @MarvinSchenkel in #4887)
- Fetch only needed Home Assistant entities instead of the full state dump (by @OzGav in #4890)
- Serve provider icons on demand instead of inlining them in the manifest (by @MarvinSchenkel in #4907)
- Make max_concurrent_tasks configurable (by @kiwipaulrob in #4914)
- Add announcement support for ESPHome-based Sendspin players (by @marcelveldt in #4916)
- Prevent importing Home Assistant players that are natively supported (by @marcelveldt in #4917)
- Keep player settings when a universal player is replaced by a native player (by @marcelveldt in #4921)
- ariacast_receiver: Add configurable Device Name (by @meiser79 in #4922)
- Smart fades: stop stranding the listener in silence on energy-drop transitions (by @MarvinSchenkel in #4926)
- Remote access: migrate WebRTC backend to libdatachannel (aiolibdatachannel) (by @MarvinSchenkel in #4930)
- Add start_from_beginning option for podcast playback (by @chrisuthe in #4934)
- Instant AirPlay seek, next-track and resume (by @marcelveldt in #4939)
- Start AirPlay groups after all players are ready (by @marcelveldt in #4942)
- Add High/Low-pass DSP filter (by @OzGav in #4944)
- Recommendations follow-ups: unload cleanup and Mood/Activity mix subtitles (by @marcelveldt in #4946)
- Support commanded AirPlay starts (by @marcelveldt in #4949)
- Keep all AirPlay groups connected while paused (by @marcelveldt in #4951)
- Add setup flow engine for interactive provider and player setup (by @marcelveldt in #4952)
- Improve grouped AirPlay pause fallback (by @marcelveldt in #4953)
- Reduce AirPlay debug log noise (by @marcelveldt in #4965)
- Make Open Subsonic provider use GET methods (by @khers in #4969)
- Instant AirPlay seek and next-track via flush-and-refill (by @marcelveldt in #4977)
- Add Apple TV dashboard support (by @marcelveldt in #4979)
- Expose current Music Quiz state to dashboard displays (by @marcelveldt in #4983)
- Add transpose DSP filter (by @OzGav in #5005)
- Cast Party and Music Quiz to Apple TV (by @marcelveldt in #5006)
- Guided setup flows for providers and players (by @marcelveldt in #5010)
- Start the next Music Quiz song without a delay (by @MarvinSchenkel in #5015)
- Map Bose SoundTouch preset buttons on the provider instead of per player (by @marcelveldt in #5032)
- Reject ACTION-type entries in setup flow forms (by @marcelveldt in #5033)
- Surface the player reconfigure flow (by @marcelveldt in #5034)
- Automatically enable 24-bit AirPlay playback on devices that support it (by @marcelveldt in #5044)
- Name the token in the KION and Zvuk sign-in error (by @marcelveldt in #5058)
- Expose whether a provider has a setup/reconfigure flow (by @marcelveldt in #5061)
- Add support for synchronized lyrics ID3 tags (by @medusalix in #5063)
- Reduce repeated discovery logging (by @marcelveldt in #5064)
- Show why a device output can't be selected (by @marcelveldt in #5071)
- Disable Mac AirPlay players by default (by @marcelveldt in #5080)
- Show Apple TV external playback artwork (by @marcelveldt in #5081)
- Add tests for Open Subsonic provider (by @khers in #5082)

### 🐛 Bugfixes

- Fix flow mode not switching sample rate between tracks on wrapped players (by @MarvinSchenkel in #4685)
- Fix AirPlay Receiver losing audio after quick reconnects (by @MarvinSchenkel in #4785)
- Fix squeezelite power control (by @allmazz in #4829)
- Fix: regression: cannot pause/play the Ariacast receiver stream on server side #5647 (by @AirPlr in #4871)
- Make subsonic provider check for extension it uses (by @khers in #4874)
- Send progress metadata on Sendspin playback-state transitions (by @chrisuthe in #4876)
- Fix flow-stream EOF recovery for universal-player-wrapped Cast devices (by @distante in #4878)
- Show AirPlay metadata immediately (by @marcelveldt in #4883)
- Never persist expiring Apple Music artwork URLs (by @teancom in #4884)
- Apply user provider filter to in-library album tracks (by @OzGav in #4885)
- Fix slow album art loading over remote connections (by @MarvinSchenkel in #4889)
- Upgrade SiriusXM stream artwork URLs to https (by @OzGav in #4891)
- Fix 'Player xy disconnected prematurely...' in MusicCast on pause (by @fmunkes in #4893)
- Hide flow mode sample rate when disabled (by @marcelveldt in #4894)
- Enable 24-bit audio on supported Sonos players (by @marcelveldt in #4895)
- Fix cast group unreachable after leadership handover (by @kiegsgroot in #4896)
- fix(player_queues): reset elapsed_time with the item switch in play_index (by @teancom in #4898)
- Recover Sendspin bridge clients stuck in a stale disabled state (by @OzGav in #4899)
- Fix AirPlay 2 pairing credentials not persisted to live player config (by @Randalix in #4902)
- Restore Siri Remote playback controls (by @marcelveldt in #4903)
- Fix container build: pin numkong to 7.7.0 (7.7.1 ships no wheels) (by @MarvinSchenkel in #4904)
- Fix next-track enqueue after delayed player start (by @MarvinSchenkel in #4906)
- Fix ffmpeg stderr log flood on corrupted/malformed audio streams (by @chrisuthe in #4908)
- Fix next-track enqueue after dynamic queue reindex (by @MarvinSchenkel in #4911)
- Add priority flag to playlist import background task (by @kiwipaulrob in #4913)
- Raise API throttler to measured safe rate (by @jozefKruszynski in #4923)
- Fix spontaneous pairing prompts on Apple TVs (by @marcelveldt in #4927)
- Fix player settings being ignored when audio plays via a linked protocol (by @marcelveldt in #4928)
- Keep settings and group memberships when universal players merge or get replaced (by @marcelveldt in #4929)
- Clean up leftover universal player settings after a native player takes over (by @marcelveldt in #4931)
- Fix ghost players created by the server's own AirPlay receivers (by @marcelveldt in #4935)
- Release the active output protocol when a wrapped player's session ends (by @marcelveldt in #4937)
- Fix controls for bridged AirPlay groups (by @marcelveldt in #4950)
- Stop recurring Apple TV pairing prompts from control-channel flapping (by @marcelveldt in #4954)
- Setup flow callback: keep params as plain strings (by @marcelveldt in #4955)
- Drop the AirPlay --ptp-follow clock-follow path (by @marcelveldt in #4956)
- Keep AirPlay warm playback reliable (by @marcelveldt in #4957)
- AirPlay companion control follow-ups (by @marcelveldt in #4959)
- Preserve AirPlay cleanup cancellation (by @marcelveldt in #4960)
- Keep AirPlay bridge helpers ordered (by @marcelveldt in #4961)
- Fix missing AirPlay cover art (by @marcelveldt in #4984)
- Resume synced AirPlay groups after pausing (by @marcelveldt in #4985)
- Fix draft release lookup (by @marcelveldt in #5000)
- Add release recovery source SHA (by @marcelveldt in #5003)
- Fix draft release recovery (by @marcelveldt in #5007)
- Allow immutable draft discovery (by @marcelveldt in #5009)
- Allow draft asset recovery (by @marcelveldt in #5011)
- Ignore removed library artists (by @marcelveldt in #5014)
- Friendlier setup-flow errors (AirPlay pairing, Spotify dev step) (by @marcelveldt in #5019)
- Strip trailing NUL from MusicBrainz UFID recording MBID (by @geofffranks in #5020)
- Preserve HEOS now-playing metadata during MA-controlled playback (by @geofffranks in #5021)
- Harden the setup flow engine (by @marcelveldt in #5022)
- Complete setup flow translations for late-migrated providers (by @marcelveldt in #5024)
- Fix AirPlay players being marked off while streaming (by @marcelveldt in #5029)
- Keep AirPlay protocol selection automatic (by @marcelveldt in #5031)
- Keep own config entries for control-only players (by @marcelveldt in #5036)
- Fix server hanging on startup (by @marcelveldt in #5040)
- Clarify Spotify developer key setup (by @marcelveldt in #5041)
- Fix bit-perfect AirPlay playback (by @marcelveldt in #5042)
- Update players immediately after setup (by @marcelveldt in #5043)
- Remove duplicate setup URL help (by @marcelveldt in #5046)
- Fix duplicate setup instructions (by @marcelveldt in #5049)
- Fix outdated Home Assistant token help text (by @marcelveldt in #5050)
- Fix HomePods muting themselves and ignoring volume changes (by @marcelveldt in #5051)
- Fix AirPlay speakers drifting out of sync in a group (by @marcelveldt in #5052)
- Fix providers that could no longer be added (by @marcelveldt in #5053)
- Fix playback on devices whose AirPlay output still needs pairing (by @marcelveldt in #5065)
- Don't start playing music after an announcement when nothing was playing (by @marcelveldt in #5068)
- Fix Spotify Connect multiple instances (by @marcelveldt in #5070)
- Fix provider setup flows (by @marcelveldt in #5072)
- Keep playback controls loading until the player really starts (by @marcelveldt in #5075)
- ariacast_receiver: fix tests (by @meiser79 in #5077)
- Add icon for background tasks core module (by @stvncode in #5084)

### 🎨 Frontend Changes

- Lokalise translations update (by @[github-actions[bot]](https://github.com/apps/github-actions) in [#2175](https://github.com/music-assistant/frontend/pull/2175))
- Restore audio chain icons (by @marcelveldt in [#2160](https://github.com/music-assistant/frontend/pull/2160))
- Add traditional Chinese to the Lokalise download list (by @OzGav in [#2159](https://github.com/music-assistant/frontend/pull/2159))
- Load provider icons on demand via the providers/icon command (by @MarvinSchenkel in [#2178](https://github.com/music-assistant/frontend/pull/2178))
- Refactor recommendations to be lazy loaded (by @chrisuthe in [#2141](https://github.com/music-assistant/frontend/pull/2141))
- Cast party & now-playing dashboards to display devices (by @MarvinSchenkel in [#2176](https://github.com/music-assistant/frontend/pull/2176))
- Skeleton placeholders for loading and hidden Discover rows (by @marcelveldt in [#2182](https://github.com/music-assistant/frontend/pull/2182))
- Party: return in-library tracks when a guest drills into an artist (by @MarvinSchenkel in [#2181](https://github.com/music-assistant/frontend/pull/2181))
- Remove output limiter from audio chain details (by @OzGav in [#2177](https://github.com/music-assistant/frontend/pull/2177))
- Remote access: reassemble chunked HTTP-proxy responses (by @MarvinSchenkel in [#2183](https://github.com/music-assistant/frontend/pull/2183))
- Reduce PWA startup precache (by @MarvinSchenkel in [#2185](https://github.com/music-assistant/frontend/pull/2185))
- Register transport listeners before connecting (by @MarvinSchenkel in [#2187](https://github.com/music-assistant/frontend/pull/2187))
- Support immutable GitHub releases (by @marcelveldt in [#2186](https://github.com/music-assistant/frontend/pull/2186))
- Support dashboards on older Cast runtimes (by @MarvinSchenkel in [#2191](https://github.com/music-assistant/frontend/pull/2191))
- Fix TV dashboard rendering (by @MarvinSchenkel in [#2194](https://github.com/music-assistant/frontend/pull/2194))
- Use bot for automated releases (by @marcelveldt in [#2193](https://github.com/music-assistant/frontend/pull/2193))
- Guided setup flow UI for providers and players (by @marcelveldt in [#2192](https://github.com/music-assistant/frontend/pull/2192))
- Cast the Music Quiz to a display (by @marcelveldt in [#2197](https://github.com/music-assistant/frontend/pull/2197))
- Fix Android TV dashboard rendering and tidy the now-playing layout (by @MarvinSchenkel in [#2200](https://github.com/music-assistant/frontend/pull/2200))
- Config action buttons use the dedicated invoke_action commands (by @marcelveldt in [#2204](https://github.com/music-assistant/frontend/pull/2204))
- Core config action buttons use the invoke_action command (by @marcelveldt in [#2209](https://github.com/music-assistant/frontend/pull/2209))
- Fix setup flow dialog stuck on spinner after launch (by @marcelveldt in [#2210](https://github.com/music-assistant/frontend/pull/2210))
- Keep setup-required players readable (by @marcelveldt in [#2212](https://github.com/music-assistant/frontend/pull/2212))
- Fix login behind Home Assistant ingress (by @marcelveldt in [#2216](https://github.com/music-assistant/frontend/pull/2216))
- Larger now-playing dashboard text on small cast displays (by @MarvinSchenkel in [#2218](https://github.com/music-assistant/frontend/pull/2218))
- Remove the horizontal scroll on discover page in mobile (by @stvncode in [#2221](https://github.com/music-assistant/frontend/pull/2221))

### Other Changes

- Make remote-access ma-api bridge tests deterministic (no real WebRTC handshake) (by @MarvinSchenkel in #4938)
- Simplify config options contract after setup flows (by @marcelveldt in #5017)

### 🧰 Maintenance and dependency bumps

<details>
<summary>60 changes</summary>

- Reuse cached AirPlay artwork (by @marcelveldt in #4880)
- Fetch AirPlay binaries during image builds (by @marcelveldt in #4881)
- Add descriptive error body to imageproxy 400 rejections (by @OzGav in #4897)
- ⬆️ Update music-assistant-frontend to 2.17.229 (by @music-assistant-machine in #4900)
- Remove the fixed output limiter (by @OzGav in #4901)
- Update airplay-cli to v0.1.1 (by @music-assistant-machine in #4905)
- ⬆️ Update music-assistant-frontend to 2.17.230 (by @music-assistant-machine in #4910)
- AirPlay: use one clock identity for multi-room timing (by @marcelveldt in #4915)
- Remove unused get_device_by_connection from Home Assistant provider (by @marcelveldt in #4920)
- ⬆️ Update music-assistant-models to 1.1.168 (by @music-assistant-machine in #4924)
- Update airplay-cli to v0.2.0 (by @music-assistant-machine in #4925)
- ⬆️ Update music-assistant-frontend to 2.17.231 (by @music-assistant-machine in #4932)
- Move base image to Debian trixie (by @marcelveldt in #4933)
- Bump docker/login-action from 4.4.0 to 4.5.0 (by @dependabot[bot] in #4936)
- Update airplay-cli to v0.3.0 (by @music-assistant-machine in #4941)
- ⬆️ Update music-assistant-models to 1.1.169 (by @music-assistant-machine in #4943)
- Update airplay-cli to v0.3.1 (by @music-assistant-machine in #4945)
- Restore provider method ordering (by @marcelveldt in #4948)
- ⬆️ Update music-assistant-frontend to 2.17.232 (by @music-assistant-machine in #4958)
- Install Git for temporary aiolibdatachannel source build (by @MarvinSchenkel in #4962)
- Update airplay-cli to v0.3.3 (by @music-assistant-machine in #4964)
- ⬆️ Update music-assistant-frontend to 2.17.233 (by @music-assistant-machine in #4966)
- Chromecast and Sonos: apply verbose logging changes without a restart (by @marcelveldt in #4967)
- Fix AirPlay provider sometimes failing to reload (by @marcelveldt in #4968)
- ⬆️ Update music-assistant-frontend to 2.17.234 (by @MarvinSchenkel in #4970)
- ⬆️ Update music-assistant-frontend to 2.17.235 (by @MarvinSchenkel in #4974)
- Make CI tests faster and more reliable (by @marcelveldt in #4975)
- Bump docker/login-action from 4.5.0 to 4.5.1 (by @dependabot[bot] in #4976)
- Show clearer errors for invalid media files (by @marcelveldt in #4978)
- Update airplay-cli to v0.3.4 (by @MarvinSchenkel in #4980)
- Make server releases immutable-safe (by @marcelveldt in #4988)
- ⬆️ Update music-assistant-frontend to 2.17.236 (by @MarvinSchenkel in #4989)
- ⬆️ Update music-assistant-frontend to 2.17.237 (by @MarvinSchenkel in #4990)
- Fix release startup permissions (by @marcelveldt in #4991)
- Replace legacy GitHub credentials (by @marcelveldt in #4992)
- Update airplay-cli to v0.3.5 (by @musicassistant-bot[bot] in #4996)
- Allow bot dependency updates to auto-merge (by @marcelveldt in #4997)
- ⬆️ Update music-assistant-frontend to 2.17.238 (by @musicassistant-bot[bot] in #5002)
- Fix smart playlist documentation URL (by @Matthew-Kilpatrick in #5012)
- ⬆️ Update music-assistant-frontend to 2.17.240 (by @musicassistant-bot[bot] in #5013)
- ⬆️ Update music-assistant-frontend to 2.17.241 (by @musicassistant-bot[bot] in #5018)
- Bump music-assistant-models to 1.1.171 (by @marcelveldt in #5025)
- ⬆️ Update music-assistant-models to 1.1.171 (by @musicassistant-bot[bot] in #5026)
- ⬆️ Update music-assistant-frontend to 2.17.242 (by @musicassistant-bot[bot] in #5027)
- Retire the AUTH_SESSION auth-popup mechanism (by @marcelveldt in #5030)
- Align core-module config actions with invoke_action (by @marcelveldt in #5035)
- ⬆️ Update music-assistant-frontend to 2.17.243 (by @musicassistant-bot[bot] in #5037)
- ⬆️ Update music-assistant-frontend to 2.17.244 (by @musicassistant-bot[bot] in #5038)
- ⬆️ Update music-assistant-frontend to 2.17.245 (by @musicassistant-bot[bot] in #5045)
- Update airplay-cli to v0.3.6 (by @musicassistant-bot[bot] in #5048)
- Bump alexapy from 1.29.17 to 1.30.0 (by @dependabot[bot] in #5054)
- Bump codespell from 2.4.2 to 2.4.3 (by @dependabot[bot] in #5055)
- Bump mypy from 2.1.0 to 2.3.0 (by @dependabot[bot] in #5056)
- Bump transformers from 5.6.2 to 5.14.1 (by @dependabot[bot] in #5057)
- ⬆️ Update music-assistant-models to 1.1.172 (by @musicassistant-bot[bot] in #5059)
- Clean up a duplicated setting in the built-in provider (by @marcelveldt in #5060)
- ⬆️ Update music-assistant-models to 1.1.173 (by @musicassistant-bot[bot] in #5069)
- ⬆️ Update music-assistant-frontend to 2.17.246 (by @musicassistant-bot[bot] in #5074)
- ⬆️ Update music-assistant-frontend to 2.17.247 (by @musicassistant-bot[bot] in #5085)
- ⬆️ Update music-assistant-frontend to 2.17.248 (by @musicassistant-bot[bot] in #5086)

</details>

## :bow: Thanks to our contributors

Special thanks to the following contributors who helped with this release:

@AirPlr, @MarvinSchenkel, @Matthew-Kilpatrick, @OzGav, @Randalix, @allmazz, @chrisuthe, @distante, @fmunkes, @geofffranks, @jozefKruszynski, @khers, @kiegsgroot, @kiwipaulrob, @marcelveldt, @medusalix, @meiser79, @music-assistant-machine, @stvncode, @swiftbird07, @teancom, @trudenboy


## 2.10.0b7
- Upstream Music Assistant server (beta) update to 2.10.0b7

### Upstream Release Notes
## 📦 Beta Release

_Changes since [2.10.0b6](https://github.com/music-assistant/server/releases/tag/2.10.0b6)_

### 🚀 New Providers

- Add Yandex Station player provider v1.5.1 — local Glagol control, Alice playback intercept (by @trudenboy in #3605)
- Add teddycloud provider (by @yoyixms in #4776)
- Add OneDrive filesystem provider (by @OzGav in #4791)

### 🚀 Features and enhancements

- Plex: Add extended recommendations with "Mixes For You" support (by @ajacobson in #3736)
- Yandex Smart Home: update v1.4.x → v2.2.4 — playlists as sources, skill auto-create, shared auth layer (by @trudenboy in #3834)
- Seed Last.fm personalized rows from recent plays (by @OzGav in #4457)
- Add vocal activity detection to Smart Fades (by @MarvinSchenkel in #4786)
- Return library tracks when browsing filesystem (by @teancom in #4792)
- Add complete audio processing details (by @marcelveldt in #4793)
- Preload lyrics in Music Quiz (by @marcelveldt in #4805)
- Allow any authenticated user on party and music quiz guest routes (by @teancom in #4808)
- Show AI availability in Music Quiz (by @marcelveldt in #4810)
- Smart Fades: vocal and energy aware transition planning (by @MarvinSchenkel in #4816)
- Vary songs when replaying Music Quiz (by @marcelveldt in #4817)
- Normalise synced (LRC) lyrics before storing or serving them (by @OzGav in #4823)
- Yandex Music Connect (Ynison): update to v3.4.2 — shared auth layer, lossless-safe fallback, stable stage (by @trudenboy in #4827)
- Ask Music Timeline bonuses after every placement (by @marcelveldt in #4830)
- FastMCP server: queue curation tools, agent ergonomics, opt-in simplified tool discovery (v0.17.0) (by @trudenboy in #4833)
- Include track duration and played duration in ListenBrainz submissions (by @tesmerjg in #4843)
- Add sendspin encryption support (by @arturpragacz in #4846)
- Add DSP gain and balance filters (by @OzGav in #4857)

### 🐛 Bugfixes

- Fix album version parsing and album_versions for filesystem_local provider (by @allmazz in #4746)
- Safely serialize OAuth callback values (by @MarvinSchenkel in #4796)
- Decrypt stored Google Drive client secret when re-authorizing (by @OzGav in #4797)
- Fix legacy Smart Fades centroid corruption (by @MarvinSchenkel in #4798)
- Fix radio station image passed as raw provider path in stream metadata (by @OzGav in #4800)
- Fix ORF Radiothek provider staying unloaded when startup coincides with network unavailable (by @OzGav in #4801)
- Offer fake mute control for players with protocol-provided volume (by @OzGav in #4802)
- Keep metadata scan tasks running when a library row has corrupt metadata JSON (by @OzGav in #4803)
- Bulk-resolve Sonic Similarity candidates to stop event-loop stalls (by @chrisuthe in #4804)
- Fix Music Quiz speaker selection for groups (by @marcelveldt in #4809)
- Fix Sonos S1 enqueue failing with UPnP error 701 (by @OzGav in #4813)
- Allow adding players to a dynamic sync group when all members are offline (by @OzGav in #4814)
- Fix sync group stopping playback when members are removed mid-regroup (by @MarvinSchenkel in #4815)
- Fix OOM in Smart Fades centroid repair migration (by @MarvinSchenkel in #4819)
- Fix translations in browse view of Audiobookshelf (by @fmunkes in #4820)
- Fix smart fades cutting off the outgoing track when vocal analysis data is stale (by @MarvinSchenkel in #4825)
- Fix album track order for YT Music tracks without disc info (by @MarvinSchenkel in #4826)
- Improve remote connection stability (by @marcelveldt in #4831)
- Fix fake mute never reporting muted state (by @OzGav in #4839)
- Ignore WiiM's false PLAYING report while no media is loaded (by @marcelveldt in #4844)
- Improve webrtc key file creation (by @arturpragacz in #4847)
- Don't allow ffmpeg to try range requests when using POST data (by @khers in #4850)
- Include synchronized players in audio chains (by @marcelveldt in #4856)
- Report UGP MP3 quality correctly (by @marcelveldt in #4858)
- Sort filesystem browse results in natural order (by @OzGav in #4869)

### 🎨 Frontend Changes

- Share party and quiz invitations (by @marcelveldt in [#2125](https://github.com/music-assistant/frontend/pull/2125))
- Show quiz results without scrolling (by @marcelveldt in [#2123](https://github.com/music-assistant/frontend/pull/2123))
- Avoid opening the keyboard in the player menu (by @marcelveldt in [#2124](https://github.com/music-assistant/frontend/pull/2124))
- Lokalise translations update (by @[github-actions[bot]](https://github.com/apps/github-actions) in [#2138](https://github.com/music-assistant/frontend/pull/2138))
- Clarify Music Timeline ordering (by @marcelveldt in [#2145](https://github.com/music-assistant/frontend/pull/2145))
- Use the global i18n scope for the missing-players hint (by @teancom in [#2143](https://github.com/music-assistant/frontend/pull/2143))
- Let signed-in users join guest experiences (by @marcelveldt in [#2126](https://github.com/music-assistant/frontend/pull/2126))
- Fix guest api errors (by @teancom in [#2140](https://github.com/music-assistant/frontend/pull/2140))
- Show this device in group controls (by @marcelveldt in [#2142](https://github.com/music-assistant/frontend/pull/2142))
- Also send updates when artist or title changes (by @joostlek in [#2152](https://github.com/music-assistant/frontend/pull/2152))
- Improve Music Quiz host controls (by @marcelveldt in [#2151](https://github.com/music-assistant/frontend/pull/2151))
- Improve Music Timeline answers (by @marcelveldt in [#2149](https://github.com/music-assistant/frontend/pull/2149))
- Unify list row layout and refine play affordances (by @MarvinSchenkel in [#1862](https://github.com/music-assistant/frontend/pull/1862))
- Use return values instead of deprecated next() in navigation guard (by @teancom in [#2144](https://github.com/music-assistant/frontend/pull/2144))
- Fix media controls while playing along (by @marcelveldt in [#2150](https://github.com/music-assistant/frontend/pull/2150))
- Use official Sendspin audio unlock (by @marcelveldt in [#2153](https://github.com/music-assistant/frontend/pull/2153))
- Show complete audio processing details (by @marcelveldt in [#2127](https://github.com/music-assistant/frontend/pull/2127))
- Add MiniEqualizer: waveform-driven now-playing indicator (by @dmoo500 in [#2147](https://github.com/music-assistant/frontend/pull/2147))
- Polish audio processing details (by @marcelveldt in [#2156](https://github.com/music-assistant/frontend/pull/2156))
- Show selected DSP preset in settings (by @zednotdead in [#1936](https://github.com/music-assistant/frontend/pull/1936))

### Other Changes

- Lokalise translations update (by @github-actions[bot] in #4795)
- Smart Fades: verbose logging for candidate-selection tuning (by @MarvinSchenkel in #4824)
- Lokalise translations update (by @github-actions[bot] in #4886)

### 🧰 Maintenance and dependency bumps

<details>
<summary>20 changes</summary>

- ⬆️ Update music-assistant-models to 1.1.161 (by @music-assistant-machine in #4794)
- ⬆️ Update music-assistant-frontend to 2.17.223 (by @music-assistant-machine in #4811)
- ⬆️ Update music-assistant-models to 1.1.163 (by @music-assistant-machine in #4812)
- ⬆️ Update music-assistant-frontend to 2.17.224 (by @music-assistant-machine in #4818)
- Remove outdated note that AirPlay 2 can't group (by @Kyzcreig in #4821)
- Prefer AirPlay 2 for known JBL models in automatic protocol selection (by @OzGav in #4822)
- ⬆️ Update music-assistant-frontend to 2.17.225 (by @music-assistant-machine in #4832)
- ⬆️ Update music-assistant-frontend to 2.17.226 (by @music-assistant-machine in #4837)
- Organize metadata controller methods (by @marcelveldt in #4838)
- Tidal: reliability fixes, API client cleanup and faster tests (by @jozefKruszynski in #4842)
- Remove redundant client disconnect loop from Sendspin provider unload (by @arturpragacz in #4848)
- ⬆️ Update music-assistant-frontend to 2.17.227 (by @music-assistant-machine in #4851)
- Bump mutagen from 1.47.0 to 1.48.1 (by @dependabot[bot] in #4860)
- Bump ruff from 0.15.6 to 0.15.22 (by @dependabot[bot] in #4861)
- Bump pyacoustid from 1.3.0 to 1.3.1 (by @dependabot[bot] in #4862)
- ⬆️ Update music-assistant-frontend to 2.17.228 (by @music-assistant-machine in #4865)
- Update music-assistant-models to 1.1.166 (by @MarvinSchenkel in #4868)
- Add Traditional Chinese to locales (by @OzGav in #4870)
- Deduplicate yandex_music device-code page strings into common (by @OzGav in #4873)
- Bump actions/setup-python from 6.3.0 to 7.0.0 (by @dependabot[bot] in #4877)

</details>

## :bow: Thanks to our contributors

Special thanks to the following contributors who helped with this release:

@Kyzcreig, @MarvinSchenkel, @OzGav, @ajacobson, @allmazz, @arturpragacz, @chrisuthe, @dmoo500, @fmunkes, @joostlek, @jozefKruszynski, @khers, @marcelveldt, @teancom, @tesmerjg, @trudenboy, @yoyixms, @zednotdead

## 2.9.9
- Upstream Music Assistant server (beta) update to 2.9.9

### Upstream Release Notes
## 📦 Stable Release

_Changes since [2.9.8](https://github.com/music-assistant/server/releases/tag/2.9.8)_

### 🐛 Bugfixes

- Show artwork for SiriusXM radio streams (by @MarvinSchenkel in #4684)
- Fix album artists for Apple Music compilations (by @MarvinSchenkel in #4764)
- Fix YouTube Music podcast shows being parsed as albums (by @MarvinSchenkel in #4781)
- Safely serialize OAuth callback values (by @MarvinSchenkel in #4796)
- Fix legacy Smart Fades centroid corruption (by @MarvinSchenkel in #4798)
- Fix radio station image passed as raw provider path in stream metadata (by @OzGav in #4800)
- Fix ORF Radiothek provider staying unloaded when startup coincides with network unavailable (by @OzGav in #4801)
- Offer fake mute control for players with protocol-provided volume (by @OzGav in #4802)
- Keep metadata scan tasks running when a library row has corrupt metadata JSON (by @OzGav in #4803)
- Fix Sonos S1 enqueue failing with UPnP error 701 (by @OzGav in #4813)
- Allow adding players to a dynamic sync group when all members are offline (by @OzGav in #4814)
- Fix OOM in Smart Fades centroid repair migration (by @MarvinSchenkel in #4819)
- Fix album track order for YT Music tracks without disc info (by @MarvinSchenkel in #4826)

### 🧰 Maintenance and dependency bumps

- Prefer AirPlay 2 for known JBL models in automatic protocol selection (by @OzGav in #4822)

## :bow: Thanks to our contributors

Special thanks to the following contributors who helped with this release:

@MarvinSchenkel, @OzGav

## 2.10.0b6
- Upstream Music Assistant server (beta) update to 2.10.0b6

### Upstream Release Notes
## 📦 Beta Release

_Changes since [2.10.0b5](https://github.com/music-assistant/server/releases/tag/2.10.0b5)_

### 🚀 New Providers

- Add Google Drive filesystem provider (by @OzGav in #4581)

### 🚀 Features and enhancements

- Yandex Music: update to v3.8.2 — shared auth layer, localized device-code login (by @trudenboy in #4690)
- Add timeline music quiz game (by @marcelveldt in #4722)
- Support more Music Quiz sources (by @marcelveldt in #4744)
- Add Music Quiz replay countdown (by @marcelveldt in #4751)
- Add language support to Music Trivia (by @marcelveldt in #4753)
- Add reveal flow to Music Trivia (by @marcelveldt in #4758)
- Improve Music Quiz AI distractors (by @marcelveldt in #4759)
- Add similar music to Music Quiz (by @marcelveldt in #4765)
- Choose Music Quiz playback for each game (by @marcelveldt in #4768)
- Improve smart shuffle variety (by @marcelveldt in #4773)

### 🐛 Bugfixes

- Show artwork for SiriusXM radio streams (by @MarvinSchenkel in #4684)
- Fix Music Quiz progress for late joiners (by @marcelveldt in #4728)
- Restrict Music Quiz guest queue access (by @marcelveldt in #4729)
- Hide Music Quiz answers until reveal (by @marcelveldt in #4733)
- Remove Music Quiz core privacy changes (by @marcelveldt in #4735)
- Let guests use the active experience (by @marcelveldt in #4737)
- Prevent interrupted streams from corrupting audio analysis (by @marcelveldt in #4738)
- Fix Hitster edge placement (by @marcelveldt in #4741)
- Fix Home Assistant AI and TTS defaults (by @marcelveldt in #4747)
- Fix Hitster answer and reveal flow (by @marcelveldt in #4748)
- Fix Home Assistant startup deadlock (by @marcelveldt in #4749)
- Speed up Music Timeline startup (by @marcelveldt in #4754)
- Reduce Spotify playlist loading requests (by @marcelveldt in #4755)
- Fix silent audio overlays (by @marcelveldt in #4757)
- Fix cancelled shared playback sessions (by @marcelveldt in #4762)
- Fix album artists for Apple Music compilations (by @MarvinSchenkel in #4764)
- Unify and simplify deezer flow track fetching (by @jdaberkow in #4766)
- Fix Guess the Song answer choices (by @marcelveldt in #4767)
- Improve Trivia question reliability (by @marcelveldt in #4774)
- Keep Music Quiz listen-in active between songs (by @marcelveldt in #4777)
- Improved SoundCloud artworks for playlists (by @robsonke in #4778)
- Speed up Apple Music radio startup (by @marcelveldt in #4780)
- Fix YouTube Music podcast shows being parsed as albums (by @MarvinSchenkel in #4781)
- Fix Plex Connect selecting the wrong track in long queues (by @MarvinSchenkel in #4783)
- Prepare Music Quiz before starting (by @marcelveldt in #4788)

### 🎨 Frontend Changes

- Keep Music Quiz players connected (by @marcelveldt in [#2066](https://github.com/music-assistant/frontend/pull/2066))
- Keep Music Quiz guest audio receive-only (by @marcelveldt in [#2069](https://github.com/music-assistant/frontend/pull/2069))
- Fix Music Quiz guest and host experience (by @marcelveldt in [#2065](https://github.com/music-assistant/frontend/pull/2065))
- Lokalise: Translations update (by @marcelveldt in [#2093](https://github.com/music-assistant/frontend/pull/2093))
- Move the progressive search logic into a reusable composable (by @marcelveldt in [#2073](https://github.com/music-assistant/frontend/pull/2073))
- Make release workflows aware of stable patch builds (by @marcelveldt in [#2058](https://github.com/music-assistant/frontend/pull/2058))
- Fix Music Quiz menu item icon and label (by @marcelveldt in [#2044](https://github.com/music-assistant/frontend/pull/2044))
- Add issue chooser redirecting to the support repo (by @marcelveldt in [#2040](https://github.com/music-assistant/frontend/pull/2040))
- Add diagnostics report download to settings (by @marcelveldt in [#2038](https://github.com/music-assistant/frontend/pull/2038))
- Lokalise translations update (by @[github-actions[bot]](https://github.com/apps/github-actions) in [#2032](https://github.com/music-assistant/frontend/pull/2032))
- Exclude parent directory ("..") item from selection in browse mode (by @MarvinSchenkel in [#2029](https://github.com/music-assistant/frontend/pull/2029))
- Extract the player protocol section into a dedicated component (by @marcelveldt in [#2015](https://github.com/music-assistant/frontend/pull/2015))
- Extract the config entry row into a dedicated component (by @marcelveldt in [#2013](https://github.com/music-assistant/frontend/pull/2013))
- Restore progress bar fill thickness and time-label spacing (by @MarvinSchenkel in [#1997](https://github.com/music-assistant/frontend/pull/1997))
- Restore timeline progress bar spacing in the player bar (by @MarvinSchenkel in [#1994](https://github.com/music-assistant/frontend/pull/1994))
- Lokalise translations update (by @[github-actions[bot]](https://github.com/apps/github-actions) in [#1989](https://github.com/music-assistant/frontend/pull/1989))
- Include icon aliases in IconPicker search results (by @dmoo500 in [#1972](https://github.com/music-assistant/frontend/pull/1972))
- Lokalise: Translations update (by @marcelveldt in [#1971](https://github.com/music-assistant/frontend/pull/1971))
- Lokalise translations update (by @[github-actions[bot]](https://github.com/apps/github-actions) in [#1955](https://github.com/music-assistant/frontend/pull/1955))
- Always expand players when clicking the player button from the 'now playing' screen ([#60](https://github.com/music-assistant/frontend/pull/60)) (by @joperafe in [#1944](https://github.com/music-assistant/frontend/pull/1944))
- Fix diagnostics settings breadcrumb (by @MarvinSchenkel in [#2097](https://github.com/music-assistant/frontend/pull/2097))
- Choose where Music Quiz plays (by @marcelveldt in [#2107](https://github.com/music-assistant/frontend/pull/2107))
- Improve Music Quiz playback flow (by @marcelveldt in [#2122](https://github.com/music-assistant/frontend/pull/2122))

### Other Changes

- Lokalise translations update (by @github-actions[bot] in #4756)

### 🧰 Maintenance and dependency bumps

<details>
<summary>15 changes</summary>

- Align ya-passport-auth on 1.7.0[ma] across Yandex providers (by @trudenboy in #4712)
- ⬆️ Update music-assistant-frontend to 2.17.217 (by @music-assistant-machine in #4730)
- ⬆️ Update music-assistant-models to 1.1.160 (by @music-assistant-machine in #4731)
- Add note about using server ID to validate servers (by @seadowg in #4742)
- Rename quiz game to Music Timeline (by @marcelveldt in #4750)
- ⬆️ Update music-assistant-frontend to 2.17.218 (by @music-assistant-machine in #4760)
- Bump aioaudiobookshelf and use its typed marker (by @fmunkes in #4763)
- Bump torch from 2.12.1 to 2.13.0+cpu (by @dependabot[bot] in #4769)
- Bump plexapi from 4.18.1 to 4.18.2 (by @dependabot[bot] in #4770)
- Bump fastmcp from 3.3.1 to 3.4.4 (by @dependabot[bot] in #4771)
- Bump deezer-python-gql from 0.17.0 to 0.17.1 (by @dependabot[bot] in #4772)
- ⬆️ Update music-assistant-frontend to 2.17.219 (by @music-assistant-machine in #4775)
- ⬆️ Update music-assistant-frontend to 2.17.220 (by @music-assistant-machine in #4779)
- ⬆️ Update music-assistant-frontend to 2.17.222 (by @music-assistant-machine in #4789)
- Bump pillow to 12.3.0 (by @MarvinSchenkel in #4790)

</details>

## :bow: Thanks to our contributors

Special thanks to the following contributors who helped with this release:

@MarvinSchenkel, @OzGav, @dmoo500, @fmunkes, @jdaberkow, @joperafe, @marcelveldt, @robsonke, @seadowg, @trudenboy

## 2.9.8
- Upstream Music Assistant server (beta) update to 2.9.8

### Upstream Release Notes
* Bumped the base image to fix the Spotify Connect plugin

## 2.9.7
- Upstream Music Assistant server (beta) update to 2.9.7

### Upstream Release Notes
## 📦 Stable Release

_Changes since [2.9.6](https://github.com/music-assistant/server/releases/tag/2.9.6)_

### Other Changes

- Remove HTTP diagnostics download endpoint (by @marcelveldt in #4710)

### 🧰 Maintenance and dependency bumps

- ⬆️ Update music-assistant-frontend to 2.17.186.post2 (by @music-assistant-machine in #4739)
- ⬆️ Update music-assistant-frontend to 2.17.186.post3 (by @music-assistant-machine in #4752)

## :bow: Thanks to our contributors

Special thanks to the following contributors who helped with this release:

@marcelveldt

## 2.10.0b5
- Upstream Music Assistant server (beta) update to 2.10.0b5

### Upstream Release Notes
## 📦 Beta Release

_Changes since [2.10.0b4](https://github.com/music-assistant/server/releases/tag/2.10.0b4)_

### 🚀 New Providers

- Add Rainy Mood provider (by @jlpouffier in #3844)
- Add Music Quiz plugin: multiplayer guess-the-song game (by @TimoPtr in #4572)
- Add Ambient Sounds provider with locally generated noise loops (by @marcelveldt in #4676)

### 🚀 Features and enhancements

- Add virtual player support to the Sendspin provider (by @marcelveldt in #4666)
- Add convenience API for providers to send custom events to clients (by @marcelveldt in #4670)
- Faster and more robust global search with per-provider timeouts and caching (by @marcelveldt in #4671)
- Add audio overlay support to queue playback (by @marcelveldt in #4674)
- Faster library browsing: slim summary mode for list endpoints (by @marcelveldt in #4679)
- Library list endpoints return slim summary items by default (by @marcelveldt in #4693)
- Expose party join URL and playback mode to guests (by @marcelveldt in #4694)
- Persist auth token activity at most once per hour (by @marcelveldt in #4695)
- Reduce memory usage of large play queues (by @marcelveldt in #4697)
- Add difficulty levels and optional AI wrong answers to the Music Quiz (by @marcelveldt in #4705)
- Reword the Music Quiz AI setting (by @marcelveldt in #4707)
- Expose quiz type in game state (by @marcelveldt in #4713)
- Add reusable Music Quiz answer types (by @marcelveldt in #4714)
- Prepare Music Quiz rounds for more answer types (by @marcelveldt in #4718)
- Add Music Quiz player presence (by @marcelveldt in #4723)

### 🐛 Bugfixes

- Fix stale active output protocol on sync group leader after group stop (by @MarvinSchenkel in #4650)
- Don't crash DLNA player update on malformed device metadata XML (by @MarvinSchenkel in #4682)
- Fix Spotify authentication failing after recent token changes (by @marcelveldt in #4688)
- Fix guest listen-in race conditions in the party and quiz plugins (by @marcelveldt in #4700)
- Fix Spotify authentication failing until server restart (by @marcelveldt in #4711)
- Show re-authentication prompt when a provider's login fails (by @marcelveldt in #4717)
- Prevent Music Quiz errors with no active game (by @marcelveldt in #4720)
- Recover from corrupt audio analysis cache (by @marcelveldt in #4721)
- Keep provider config values current (by @marcelveldt in #4725)
- Prevent lost Podcast Index library changes (by @marcelveldt in #4726)

### 🎨 Frontend Changes

- Show track BPM and musical key on the track details page (by @MarvinSchenkel in [#2034](https://github.com/music-assistant/frontend/pull/2034))
- Add issue chooser redirecting to the support repo (by @marcelveldt in [#2040](https://github.com/music-assistant/frontend/pull/2040))
- Add diagnostics report download to settings (by @marcelveldt in [#2038](https://github.com/music-assistant/frontend/pull/2038))
- Add Music Quiz game interface (by @TimoPtr in [#2010](https://github.com/music-assistant/frontend/pull/2010))
- Add listen-in (shared audio) for party guests (by @marcelveldt in [#2041](https://github.com/music-assistant/frontend/pull/2041))
- Make release workflows aware of stable patch builds (by @marcelveldt in [#2058](https://github.com/music-assistant/frontend/pull/2058))
- Fix Music Quiz menu item icon and label (by @marcelveldt in [#2044](https://github.com/music-assistant/frontend/pull/2044))
- Add flexible Music Quiz game routing (by @marcelveldt in [#2063](https://github.com/music-assistant/frontend/pull/2063))
- Remove the blank space between the player and the party mode dashboard view (by @GiuliaPassoni in [#1937](https://github.com/music-assistant/frontend/pull/1937))
- Improve the Discover page edit mode (by @marcelveldt in [#2062](https://github.com/music-assistant/frontend/pull/2062))
- Support Music Quiz game types (by @marcelveldt in [#2061](https://github.com/music-assistant/frontend/pull/2061))
- Customize the navigation menu with a new edit mode (by @marcelveldt in [#2060](https://github.com/music-assistant/frontend/pull/2060))
- Add audio overlay controls (by @jlpouffier in [#1753](https://github.com/music-assistant/frontend/pull/1753))
- Redesign the Music Quiz UI (by @marcelveldt in [#2054](https://github.com/music-assistant/frontend/pull/2054))
- Add difficulty selector to Music Quiz setup (by @marcelveldt in [#2048](https://github.com/music-assistant/frontend/pull/2048))
- Fix Music Quiz setup with no active game (by @marcelveldt in [#2064](https://github.com/music-assistant/frontend/pull/2064))
- Remove the blank space between the player and the party mode dashboard view (by @GiuliaPassoni in [#1937](https://github.com/music-assistant/frontend/pull/1937))
- Fix guest join links during frontend development (by @marcelveldt in [#2059](https://github.com/music-assistant/frontend/pull/2059))
- Fix Music Quiz stray error on no active game (by @marcelveldt in [#2053](https://github.com/music-assistant/frontend/pull/2053))
- Fix Music Quiz styling and menu icon (by @marcelveldt in [#2051](https://github.com/music-assistant/frontend/pull/2051))

### Other Changes

- Remove HTTP diagnostics download endpoint (by @marcelveldt in #4709)

### 🧰 Maintenance and dependency bumps

<details>
<summary>17 changes</summary>

- Add shared playback session and guest access helpers for plugins (by @marcelveldt in #4672)
- ⬆️ Update music-assistant-models to 1.1.157 (by @music-assistant-machine in #4673)
- Add diagnostics sections for core controllers and common providers (by @marcelveldt in #4675)
- ⬆️ Update music-assistant-frontend to 2.17.213 (by @music-assistant-machine in #4677)
- ⬆️ Update music-assistant-models to 1.1.158 (by @music-assistant-machine in #4678)
- ⬆️ Update music-assistant-models to 1.1.159 (by @music-assistant-machine in #4680)
- Add full-text search index for search (by @marcelveldt in #4681)
- Stabilize CodSpeed benchmark runs (by @marcelveldt in #4689)
- Remove non-deterministic macro benchmarks from CodSpeed (by @marcelveldt in #4691)
- Add issue chooser redirecting to the support repo (by @marcelveldt in #4696)
- ⬆️ Update music-assistant-frontend to 2.17.214 (by @music-assistant-machine in #4701)
- Reduce server startup time and memory usage (by @marcelveldt in #4702)
- Speed up artwork loading and refresh artwork when local files change (by @marcelveldt in #4703)
- ⬆️ Update music-assistant-frontend to 2.17.215 (by @music-assistant-machine in #4704)
- Make audio overlays audible immediately (by @marcelveldt in #4715)
- Lock in the provider config store/snapshot consistency guarantee (by @marcelveldt in #4716)
- ⬆️ Update music-assistant-frontend to 2.17.216 (by @music-assistant-machine in #4724)

</details>

## :bow: Thanks to our contributors

Special thanks to the following contributors who helped with this release:

@GiuliaPassoni, @MarvinSchenkel, @TimoPtr, @jlpouffier, @marcelveldt

## 2.9.6
- Upstream Music Assistant server (beta) update to 2.9.6

### Upstream Release Notes
## 📦 Stable Release

_Changes since [2.9.5](https://github.com/music-assistant/server/releases/tag/2.9.5)_

### 🐛 Bugfixes

- Sync groups: keep slaved followers in group member dropdown after removal (by @MarvinSchenkel in #4036)
- Improve global search reliability and database query parameter logic (by @SyedaAnshrahGillani in #4207)
- Fix AirPlay receiver advertising on the wrong network interface (by @marcelveldt in #4543)
- Remove Home Assistant musllinux wheel index from package install (by @MarvinSchenkel in #4549)
- Pace background audio analysis to stop it saturating the CPU (by @oldrobotdev in #4568)
- Fix builtin Snapserver failing to load on busy MA startup (by @OzGav in #4586)
- Prevent Qobuz credentials leaking into logs on HTTP error responses (by @OzGav in #4587)
- Snapcast fixes (by @OzGav in #4633)
- Fix Plex artist albums not loading on servers without filter metadata (by @OzGav in #4657)
- Don't auto-sync all Phish.in playlists to the library (by @OzGav in #4660)
- Fix Spotify authentication failing after recent token changes (by @marcelveldt in #4692)

### Other Changes

- Allow the Home Assistant system user to filter listings by user and remove players (by @marcelveldt in #4641)
- Add downloadable diagnostics report (backport) (by @marcelveldt in #4699)

## :bow: Thanks to our contributors

Special thanks to the following contributors who helped with this release:

@MarvinSchenkel, @OzGav, @SyedaAnshrahGillani, @marcelveldt, @oldrobotdev

## 2.10.0b4
- Upstream Music Assistant server (beta) update to 2.10.0b4

### Upstream Release Notes
## 📦 Beta Release

_Changes since [2.10.0b3](https://github.com/music-assistant/server/releases/tag/2.10.0b3)_

### 🚀 New Providers

- Add Profiler provider for on-demand performance diagnostics (by @marcelveldt in #4653)

### 🚀 Features and enhancements

- BBC Sounds: refactor for auntie-sounds 2.0 (by @kieranhogg in #4450)
- fastmcp_server: update provider to v0.13.3 (queue, library-URI, and playback tools + localizable config) (by @trudenboy in #4486)
- Use radio playlists in the MCP play_media tool (by @marcelveldt in #4501)
- Add support for authors and narrators to audiobookshelf (by @fmunkes in #4526)
- Suppress per-item media item events during library sync (by @marcelveldt in #4578)
- Make player state change detection exact and cheap (by @marcelveldt in #4579)
- Smart fades analyzer v2: frequency band envelopes, time signature and anti-aliased energy binning (by @MarvinSchenkel in #4580)
- Emby Music Provider: add last played date (by @hatharry in #4582)
- Reduce database commit overhead during library sync (by @marcelveldt in #4584)
- Remove per-track config rebuild overhead (by @marcelveldt in #4585)
- Resolve publish IP at startup instead of baking it into config entry defaults (by @marcelveldt in #4588)
- Smart crossfade: content-aware 3-band EQ from frequency band analysis (by @MarvinSchenkel in #4591)
- Add genre detection to playlist_metadata provider (by @dmoo500 in #4593)
- Implement SQL-based explicit filter for smart playlists (by @dmoo500 in #4594)
- Add explicit parameter to TracksController.library_items (by @dmoo500 in #4597)
- Populate derived_from on output protocols (by @marcelveldt in #4609)
- Add taxonomy genre icons, update genre icon image resolver (by @jozefKruszynski in #4611)
- Expose bpm, musical key and RMS waveform to the frontend (by @MarvinSchenkel in #4626)
- Speed up library matching with an indexed external ID lookup table (by @marcelveldt in #4628)
- Speed up library listings by streaming from the sort index (by @marcelveldt in #4629)
- Remove periodic garbage collection (by @marcelveldt in #4630)
- Avoid threadsafe dispatch overhead when signalling events (by @marcelveldt in #4631)
- Speed up library sync when nothing has changed (by @marcelveldt in #4632)
- Raise transient provider errors instead of caching them as negatives (by @marcelveldt in #4636)
- Fastmcp_server: Searchable log tail, whole-record tracebacks, log stats (by @trudenboy in #4640)
- Reduce image proxy-id overhead when serializing media items (by @marcelveldt in #4642)
- Make the external id lookup table the single source of truth (by @marcelveldt in #4645)
- Add diagnostics feature (by @marcelveldt in #4652)
- Add fixed genres to Phish.in tracks (by @OzGav in #4659)
- Add join code expiry lookup to auth controller (by @marcelveldt in #4663)
- Add support for sound effect media items (by @marcelveldt in #4669)

### 🐛 Bugfixes

- Sync groups: keep slaved followers in group member dropdown after removal (by @MarvinSchenkel in #4036)
- Improve global search reliability and database query parameter logic (by @SyedaAnshrahGillani in #4207)
- Prevent SSRF via attacker-controlled WebRTC HTTP proxy path (by @MarvinSchenkel in #4554)
- Harden JWT token expiration and fix guest token revocation (by @MarvinSchenkel in #4556)
- Rate-limit join code exchange and lengthen join codes (by @MarvinSchenkel in #4558)
- Prevent path traversal outside the filesystem provider base directory (by @MarvinSchenkel in #4559)
- Fix XSS and cross-host request issues in MSX Bridge web player (by @MarvinSchenkel in #4562)
- Fix playlog unique constraint errors on long-lived databases (by @MarvinSchenkel in #4567)
- Fix smart playlist artwork not displaying in recommendations (by @dmoo500 in #4571)
- Don't reinstall provider requirements with extras on every startup (by @marcelveldt in #4577)
- Fix builtin Snapserver failing to load on busy MA startup (by @OzGav in #4586)
- Prevent Qobuz credentials leaking into logs on HTTP error responses (by @OzGav in #4587)
- Sanitize all control characters in icy-name stream header (by @OzGav in #4595)
- Improve error presentation for folder playback resolution (by @OzGav in #4598)
- Prevent duplicate versions of the same song in dynamic playlist queues (by @marcelveldt in #4603)
- Fix Home Assistant integration losing authentication after restart or over time (by @MarvinSchenkel in #4620)
- Sample smart playlist seeds evenly in discover mode (by @MarvinSchenkel in #4621)
- Fix media position exceeding duration on squeezelite players (by @MarvinSchenkel in #4623)
- Shuffle smart playlist seed tracks before sampling (by @MarvinSchenkel in #4625)
- Snapcast fixes (by @OzGav in #4633)
- Preserve universal player settings during startup restore (by @SyntaxSawdust in #4634)
- Prevent universal player settings loss on startup restore (by @marcelveldt in #4643)
- Prevent syncgroup self-dissolve when recovering a stuck member (by @MarvinSchenkel in #4644)
- Advertise both IP families via mDNS and respect a specific bind IP when publishing (by @OzGav in #4646)
- Fix broken album artists filtering (by @OzGav in #4648)
- Prevent admin token leak to untrusted return_url during first-run setup (by @MarvinSchenkel in #4649)
- Fix several bugs in the Jellyfin provider (by @OzGav in #4654)
- Fix Plex artist albums not loading on servers without filter metadata (by @OzGav in #4657)
- Don't auto-sync all Phish.in playlists to the library (by @OzGav in #4660)
- Block long-lived token creation for guest accounts (by @MarvinSchenkel in #4661)
- Harden MSX bridge against host-header XSS and cross-origin fetches (by @MarvinSchenkel in #4662)

### 🎨 Frontend Changes

- Extract the player protocol section into a dedicated component (by @marcelveldt in [#2015](https://github.com/music-assistant/frontend/pull/2015))
- Extract the config entry row into a dedicated component (by @marcelveldt in [#2013](https://github.com/music-assistant/frontend/pull/2013))
- Genre taxonomy UX: add-genre, panel actions, management table, targeted restore (by @jozefKruszynski in [#1974](https://github.com/music-assistant/frontend/pull/1974))
- Fix DSP parametric EQ layout on narrow and rotated displays (by @OzGav in [#2014](https://github.com/music-assistant/frontend/pull/2014))
- Refresh library views as each media type finishes syncing (by @marcelveldt in [#2016](https://github.com/music-assistant/frontend/pull/2016))
- Add subtle grey ring to unselected editorial card checkbox (by @OzGav in [#2012](https://github.com/music-assistant/frontend/pull/2012))
- Show the base protocol for bridged outputs and explain their locked toggle (by @marcelveldt in [#2017](https://github.com/music-assistant/frontend/pull/2017))
- Exclude parent directory ("..") item from selection in browse mode (by @MarvinSchenkel in [#2029](https://github.com/music-assistant/frontend/pull/2029))
- Lokalise translations update (by @[github-actions[bot]](https://github.com/apps/github-actions) in [#2032](https://github.com/music-assistant/frontend/pull/2032))
- Fix genre merge cross taxonomy (by @jozefKruszynski in [#2031](https://github.com/music-assistant/frontend/pull/2031))
- Show a waveform progress bar in the fullscreen player (by @MarvinSchenkel in [#2035](https://github.com/music-assistant/frontend/pull/2035))
- Enhance button in fullplayer screen + add animated icons (by @stvncode in [#2036](https://github.com/music-assistant/frontend/pull/2036))
- Exit selection mode when the browse path changes (by @OzGav in [#2030](https://github.com/music-assistant/frontend/pull/2030))
- Fix long-press context menus on touch devices (by @MarvinSchenkel in [#2004](https://github.com/music-assistant/frontend/pull/2004))
- Fix audio pipeline line spacing (by @OzGav in [#2028](https://github.com/music-assistant/frontend/pull/2028))
- Extract search input component (by @GiuliaPassoni in [#1959](https://github.com/music-assistant/frontend/pull/1959))

### Other Changes

- Make Sendspin bridges first-class derived transports (by @marcelveldt in #4596)
- Add typed get_config_value helper to the config-owning base models (by @marcelveldt in #4606)
- Local Audio: promote attribution stubs to regular visible players (by @marcelveldt in #4607)
- Lokalise translations update (by @github-actions[bot] in #4639)
- Add CodSpeed performance benchmarks and CI integration (by @codspeed-hq[bot] in #4656)

### 🧰 Maintenance and dependency bumps

<details>
<summary>27 changes</summary>

- Use dedicated encryption key (by @MarvinSchenkel in #4557)
- Validate auto-merge dependency PRs via GitHub API instead of checkout (by @MarvinSchenkel in #4566)
- Isolate the hermetic e2e fixture from host audio devices (by @marcelveldt in #4583)
- ⬆️ Update music-assistant-frontend to 2.17.209 (by @music-assistant-machine in #4590)
- Bump aiohttp-asyncmdnsresolver from 0.1.1 to 0.2.0 (by @dependabot[bot] in #4599)
- Bump pre-commit from 4.5.1 to 4.6.0 (by @dependabot[bot] in #4600)
- Bump huggingface-hub from 1.12.0 to 1.22.0 (by @dependabot[bot] in #4601)
- Fix test-ordering flake caused by a leaked models global cache (by @marcelveldt in #4602)
- Fix mypy no-any-return error in Plex lyrics fetch (by @marcelveldt in #4604)
- ⬆️ Update music-assistant-models to 1.1.152 (by @music-assistant-machine in #4605)
- Isolate the unit-test `mass` fixture from host audio and default providers (by @marcelveldt in #4608)
- Add test coverage for local audio bridge-manager edge cases (by @marcelveldt in #4610)
- ⬆️ Update music-assistant-frontend to 2.17.210 (by @music-assistant-machine in #4612)
- Scope based authorization for API commands and centralized user impersonation (by @marcelveldt in #4613)
- Cache negative results in @use_cache and avoid the SWR double read (by @marcelveldt in #4616)
- Slim cache indexes, upsert in place, and clean up stale SWR rows (by @marcelveldt in #4617)
- Run dependency security checks without an untrusted privileged checkout (by @MarvinSchenkel in #4618)
- Bump API schema version for scope based authorization (by @marcelveldt in #4622)
- ⬆️ Update music-assistant-frontend to 2.17.211 (by @music-assistant-machine in #4635)
- ⬆️ Update music-assistant-models to 1.1.154 (by @music-assistant-machine in #4637)
- Auto-approve automated frontend/models bump PRs in dependency security gate (by @MarvinSchenkel in #4638)
- Add performance benchmark suite (by @marcelveldt in #4651)
- ⬆️ Update music-assistant-frontend to 2.17.212 (by @music-assistant-machine in #4655)
- Update aiodns to 4.0.4 and remove pycares pin (by @MarvinSchenkel in #4658)
- Improve Sendspin proxy error handling and quieter websocket command logging (by @marcelveldt in #4664)
- ⬆️ Update music-assistant-models to 1.1.155 (by @music-assistant-machine in #4665)
- ⬆️ Update music-assistant-models to 1.1.156 (by @music-assistant-machine in #4668)

</details>

## :bow: Thanks to our contributors

Special thanks to the following contributors who helped with this release:

@GiuliaPassoni, @MarvinSchenkel, @OzGav, @SyedaAnshrahGillani, @SyntaxSawdust, @codspeed-hq[bot], @dmoo500, @fmunkes, @hatharry, @jozefKruszynski, @kieranhogg, @marcelveldt, @stvncode, @trudenboy

## 2.10.0b3
- Upstream Music Assistant server (beta) update to 2.10.0b3

### Upstream Release Notes
## 📦 Beta Release

_Changes since [2.10.0b2](https://github.com/music-assistant/server/releases/tag/2.10.0b2)_

### 🚀 New Providers

- Add playlist_metadata plugin for auto-generating playlist artwork (by @dmoo500 in #3786)
- Add Bose SoundTouch player provider (by @Odn0 in #3891)

### 🚀 Features and enhancements

- Improve stream URL handling with failover support (by @benklop in #2996)
- Adapt artist / audiobook controller for authors and narrators (by @fmunkes in #3570)
- Extend Local Audio Out provider with PulseAudio support (by @iVolt1 in #3724)
- Plex: Add audiobook/podcast support with position sync (by @zenibako in #3748)
- Add CUE sheet support for filesystem providers (by @OzGav in #3751)
- Enhance play_media start_item parameter to allow latest podcast episode to be played and podcast/playlist to play from here (by @OzGav in #3832)
- Add birthday/memoriam recommendations via MusicBrainz (by @dmoo500 in #3833)
- Rewrite Deezer provider with GraphQL client (by @jdaberkow in #3900)
- Provide Tracking and UX for AA Failures and Retries (by @chrisuthe in #4167)
- Import additional metadata from Plex into media items (by @lebdim in #4338)
- mcp: add set_repeat tool to queue controls (by @steamEngineer in #4377)
- mcp: add explicit pause/resume playback tools (by @steamEngineer in #4390)
- mcp: add players ungroup tool  (by @steamEngineer in #4391)
- Adjust Sonic Similarity base scoring and pools to allow for better matching and more meaningful presets (by @chrisuthe in #4429)
- Improve Search results from Sonic Similarity Plugin (by @chrisuthe in #4430)
- Add native player sleep timers (by @teancom in #4432)
- Enhance and fix podcast metadata (episode descriptions, chapters, parent-podcast name) in gPodder, iTunes Podcast and Podcast RSS Feed (by @chrisuthe in #4444)
- Smart Playlist: Use library artwork from metadata providers (by @dmoo500 in #4447)
- Unload idle audio-analysis models to reclaim memory (by @marcelveldt in #4452)
- Add playlist metadata infrastructure to MetadataProvider (by @dmoo500 in #4460)
- Genre content-type awareness: create/edit safety + targeted restore (by @jozefKruszynski in #4474)
- Smart shuffle for player queues (by @marcelveldt in #4475)
- Add support for podcast chapters in Audiobookshelf (by @fmunkes in #4478)
- Bounded managed pool for radio mode (by @marcelveldt in #4479)
- Extend podcast (by @chrisuthe in #4492)
- Dynamic radio playlists (replacing radio mode) (by @marcelveldt in #4498)
- Honour the queue's recency windows in provider dynamic stations (by @marcelveldt in #4500)
- Add played_only parameter to library_items methods (by @dmoo500 in #4502)
- Play finite sources in a dynamic queue through once instead of recycling them (by @marcelveldt in #4503)
- Add AirPlay DACP replay tests and verbose traffic capture (by @MarvinSchenkel in #4507)
- Turn a queue with any dynamic source into one bounded smart-shuffled pool (by @marcelveldt in #4513)
- Add duration and last_played filters to Smart Playlist (by @dmoo500 in #4520)
- Avoid back-to-back artists in dynamic queues (by @marcelveldt in #4528)
- Smart crossfade: DJ-style bass swap EQ (by @MarvinSchenkel in #4536)
- Global defaults for queue settings with per-queue override (by @marcelveldt in #4537)
- Explain the queue Global option via a per-option description (by @marcelveldt in #4540)
- Only expose container items as player queue sources (by @marcelveldt in #4542)
- Add per-option help text to config selects (by @marcelveldt in #4546)
- Show unavailable player control and AirPlay protocol options as disabled (by @marcelveldt in #4551)
- Expose album artist on player current media (by @MarvinSchenkel in #4560)

### 🐛 Bugfixes

- Avoid syncing native parent volume to AirPlay protocols (by @jyundt in #3980)
- Apple Music: Intelligent fallback for deprecated catalog tracks (by @dmoo500 in #4109)
- Smart Playlist: Enrich library tracks with database genres for filtering (by @dmoo500 in #4175)
- Convert HTML in media descriptions to markdown (by @MarvinSchenkel in #4225)
- fastMCP Server: Connect Wizard fixes for reverse-proxy deployments (by @Sawtaytoes in #4313)
- Pre-import numpy in scoped-coverage CI to avoid py3.14 reduction break (by @chrisuthe in #4445)
- Give playback priority over realtime audio analysis (by @marcelveldt in #4449)
- Cap concurrent realtime audio analysis sessions (by @marcelveldt in #4451)
- Fix Local Audio pulse audio syncing, silence, and volume on intial playback (by @iVolt1 in #4453)
- Audiobookshelf: tolerate out-of-range podcast episode dates (by @OzGav in #4458)
- Fix smart playlist genre AND logic (by @dmoo500 in #4459)
- Fix min/max volume scaling lost on protocol/external volume redirect (by @Hopperpop in #4461)
- Unsync a player when its power is turned off externally (by @marcelveldt in #4463)
- Improve Hue entertainment start reliability for slow DTLS handshakes (by @steamEngineer in #4467)
- Fix discover page not loading due to MusicBrainz recommendation scan (by @marcelveldt in #4470)
- Prevent providers picking the same port when starting concurrently (by @marcelveldt in #4472)
- Fix the podcast's title not being used in Audiobookshelf's episode parser (by @fmunkes in #4477)
- iBroadcast mapping issue with album id's and possible other id's (by @robsonke in #4482)
- Prevent a crash when a CPU can't execute on-device analysis (by @marcelveldt in #4483)
- Fix QUIC/HTTP-3 debug log spam caused by urllib3-future override (by @MarvinSchenkel in #4485)
- Fix startup crash from provider config entry missing 'domain' (by @chrisuthe in #4488)
- Fix lrclib plain lyrics written to the synced-LRC field (by @chrisuthe in #4489)
- Fix audiobook release_date parsed but never stored (by @chrisuthe in #4490)
- Fix deezer parse_streamable returning Any from a bool function (by @chrisuthe in #4491)
- Handle Spotify's refresh-token changes (by @OzGav in #4494)
- Fix negative elapsed_time crashing clients (by @teancom in #4495)
- Catch only MusicAssistantError in playlist metadata enrichment (by @dmoo500 in #4499)
- Fix Squeezelite progress bar showing previous track position after track change (by @MarvinSchenkel in #4504)
- Detect stalled source streams when the connection drops mid-playback (by @MarvinSchenkel in #4505)
- Mark Snapcast players offline when abruptly powered off (by @MarvinSchenkel in #4506)
- Subsonic: Convert provider to StreamType.HTTP (by @khers in #4508)
- Fix first queued item being skipped when playing onto an idle queue (by @marcelveldt in #4514)
- Revert squeezelite-local media_position workaround (#4504) (by @MarvinSchenkel in #4517)
- Honour play-next under shuffle and set the current item when enqueuing onto an empty queue (by @marcelveldt in #4519)
- Don't auto-start playback when an ADD/NEXT onto an idle queue enters dynamic mode (by @marcelveldt in #4521)
- Keep the dynamic queue bounded when adding more sources (by @marcelveldt in #4522)
- Dedupe the queue's sources list so a repeated source shows once (by @marcelveldt in #4524)
- Preserve player queues and their settings across restarts (by @marcelveldt in #4529)
- Fix Spotify connect playback on some Sendspin players (by @maximmaxim345 in #4530)
- Fix complete config loss after power failure or unclean shutdown (by @MarvinSchenkel in #4534)
- Fix smart fades falling back to a hard cut when the incoming track is short (by @MarvinSchenkel in #4535)
- Fix AirPlay receiver advertising on the wrong network interface (by @marcelveldt in #4543)
- Allow smart playlists through metadata enrichment (by @dmoo500 in #4545)
- Remove Home Assistant musllinux wheel index from package install (by @MarvinSchenkel in #4549)
- Restrict the image palette API to an opaque image id (by @marcelveldt in #4550)
- Stop exposing internal error details in Plex Connect responses (by @MarvinSchenkel in #4563)
- Match NetEase image CDN hostname exactly when upgrading to https (by @MarvinSchenkel in #4564)
- Fix open redirect on login page and requirements regex char range (by @MarvinSchenkel in #4565)
- Pace background audio analysis to stop it saturating the CPU (by @oldrobotdev in #4568)

### 🎨 Frontend Changes

- Restore the player settings entry in the player menu (by @marcelveldt in [#1969](https://github.com/music-assistant/frontend/pull/1969))
- Lokalise: Translations update (by @marcelveldt in [#1971](https://github.com/music-assistant/frontend/pull/1971))
- add bitrate information to the QualityDetailsBtn.vue screen (by @Bonusbartus in [#1754](https://github.com/music-assistant/frontend/pull/1754))
- Add sleep timer support (by @marcelveldt in [#1970](https://github.com/music-assistant/frontend/pull/1970))
- Include icon aliases in IconPicker search results (by @dmoo500 in [#1972](https://github.com/music-assistant/frontend/pull/1972))
- Add missing aria labels (by @stvncode in [#1973](https://github.com/music-assistant/frontend/pull/1973))
- Upgrade eslint + add oxlint (by @stvncode in [#1958](https://github.com/music-assistant/frontend/pull/1958))
- Add smart shuffle indicator to the player (by @marcelveldt in [#1987](https://github.com/music-assistant/frontend/pull/1987))
- Provide Tracking and UX for AA Failures and Retries (by @chrisuthe in [#1907](https://github.com/music-assistant/frontend/pull/1907))
- Restore timeline progress bar spacing in the player bar (by @MarvinSchenkel in [#1994](https://github.com/music-assistant/frontend/pull/1994))
- Lokalise translations update (by @[github-actions[bot]](https://github.com/apps/github-actions) in [#1989](https://github.com/music-assistant/frontend/pull/1989))
- Adopt dynamic radio playlists (replace radio mode) (by @marcelveldt in [#1995](https://github.com/music-assistant/frontend/pull/1995))
- Declutter the player queue list item layout (by @MarvinSchenkel in [#1988](https://github.com/music-assistant/frontend/pull/1988))
- Fix main listing search stealing focus from other inputs (by @OzGav in [#1991](https://github.com/music-assistant/frontend/pull/1991))
- Center the play button in the fullscreen player controls (by @MarvinSchenkel in [#1993](https://github.com/music-assistant/frontend/pull/1993))
- Fix buffered icon spacing in the player queue list (by @MarvinSchenkel in [#1992](https://github.com/music-assistant/frontend/pull/1992))
- Fix browse sort/view settings not persisting per folder (by @OzGav in [#1990](https://github.com/music-assistant/frontend/pull/1990))
- Remove the smart playlist 'do not repeat' control (by @marcelveldt in [#1996](https://github.com/music-assistant/frontend/pull/1996))
- Restore progress bar fill thickness and time-label spacing (by @MarvinSchenkel in [#1997](https://github.com/music-assistant/frontend/pull/1997))
- Improve fullscreen player controls and lyrics/queue behavior (by @marcelveldt in [#1999](https://github.com/music-assistant/frontend/pull/1999))
- Show per-option description in config-entry select (by @marcelveldt in [#2003](https://github.com/music-assistant/frontend/pull/2003))
- Convert player protocol section to a shadcn accordion (by @marcelveldt in [#2011](https://github.com/music-assistant/frontend/pull/2011))

### Other Changes

- Lokalise translations update (by @github-actions[bot] in #4454)
- Split config controller into a package (by @MarvinSchenkel in #4484)
- Lokalise translations update (by @github-actions[bot] in #4497)
- Refactor player-queues controller (by @marcelveldt in #4509)
- Refactor smart fades into a plan/render architecture (by @MarvinSchenkel in #4532)

### 🧰 Maintenance and dependency bumps

<details>
<summary>28 changes</summary>

- Refactor MusicBrainz provider into multi-file package (by @dmoo500 in #3905)
- Update srptools requirement from >=1.0.0 to >=1.0.1 (by @dependabot[bot] in #4234)
- Bump torch from 2.11.0 to 2.12.1+cpu (by @dependabot[bot] in #4403)
- ⬆️ Update music-assistant-frontend to 2.17.201 (by @music-assistant-machine in #4448)
- ⬆️ Update music-assistant-frontend to 2.17.202 (by @music-assistant-machine in #4455)
- Document provider_mappings database structure (by @dmoo500 in #4466)
- ⬆️ Update music-assistant-frontend to 2.17.203 (by @music-assistant-machine in #4468)
- Auto-sync provider manifests on Dependabot PRs (by @marcelveldt in #4471)
- Replace obfuscated app_vars with build-time secret injection (by @marcelveldt in #4473)
- ⬆️ Update music-assistant-models to 1.1.145 (by @music-assistant-machine in #4476)
- Clarify supported installation methods in README (by @marcelveldt in #4480)
- Bump wiim from 0.1.4 to 0.1.5 (by @dependabot[bot] in #4481)
- ⬆️ Update music-assistant-frontend to 2.17.204 (by @music-assistant-machine in #4496)
- ⬆️ Update music-assistant-frontend to 2.17.205 (by @music-assistant-machine in #4511)
- Fix stale docs in the player-queues package (by @marcelveldt in #4518)
- Bump docker/build-push-action from 7.2.0 to 7.3.0 (by @dependabot[bot] in #4523)
- ⬆️ Update music-assistant-models to 1.1.147 (by @music-assistant-machine in #4525)
- ⬆️ Update music-assistant-frontend to 2.17.206 (by @music-assistant-machine in #4527)
- ⬆️ Update music-assistant-models to 1.1.149 (by @music-assistant-machine in #4539)
- Bump aioslimproto to 3.1.9 (by @MarvinSchenkel in #4541)
- Remove the deprecated legacy image proxy endpoint (by @marcelveldt in #4544)
- Bump docker/login-action from 4.2.0 to 4.3.0 (by @dependabot[bot] in #4547)
- Bump docker/setup-buildx-action from 4.1.0 to 4.2.0 (by @dependabot[bot] in #4548)
- ⬆️ Update music-assistant-frontend to 2.17.207 (by @music-assistant-machine in #4552)
- ⬆️ Update music-assistant-models to 1.1.150 (by @music-assistant-machine in #4553)
- ⬆️ Update music-assistant-models to 1.1.151 (by @music-assistant-machine in #4569)
- Bump docker/login-action from 4.3.0 to 4.4.0 (by @dependabot[bot] in #4574)
- ⬆️ Update music-assistant-frontend to 2.17.208 (by @music-assistant-machine in #4575)

</details>

## :bow: Thanks to our contributors

Special thanks to the following contributors who helped with this release:

@Bonusbartus, @Hopperpop, @MarvinSchenkel, @Odn0, @OzGav, @Sawtaytoes, @benklop, @chrisuthe, @dmoo500, @fmunkes, @iVolt1, @jdaberkow, @jozefKruszynski, @jyundt, @khers, @lebdim, @marcelveldt, @maximmaxim345, @oldrobotdev, @robsonke, @steamEngineer, @stvncode, @teancom, @zenibako

## 2.9.5
- Upstream Music Assistant server (beta) update to 2.9.5

### Upstream Release Notes
## 📦 Stable Release

_Changes since [2.9.4](https://github.com/music-assistant/server/releases/tag/2.9.4)_

### 🚀 Features and enhancements

- Add AirPlay DACP replay tests and verbose traffic capture (by @MarvinSchenkel in #4507)

### 🐛 Bugfixes

- Avoid syncing native parent volume to AirPlay protocols (by @jyundt in #3980)
- Audiobookshelf: tolerate out-of-range podcast episode dates (by @OzGav in #4458)
- Fix smart playlist genre AND logic (by @dmoo500 in #4459)
- Fix min/max volume scaling lost on protocol/external volume redirect (by @Hopperpop in #4461)
- Improve Hue entertainment start reliability for slow DTLS handshakes (by @steamEngineer in #4467)
- Fix the podcast's title not being used in Audiobookshelf's episode parser (by @fmunkes in #4477)
- Prevent a crash when a CPU can't execute on-device analysis (by @marcelveldt in #4483)
- Fix startup crash from provider config entry missing 'domain' (by @chrisuthe in #4488)
- Fix negative elapsed_time crashing clients (by @teancom in #4495)
- Mark Snapcast players offline when abruptly powered off (by @MarvinSchenkel in #4506)
- Fix first queued item being skipped when playing onto an idle queue (backport) (by @marcelveldt in #4515)
- Handle expired/revoked Spotify refresh tokens and missing rotation - stable branch (by @OzGav in #4516)

### Other Changes

- Allow Don't stop the music with metadata/plugin similar-track providers (by @OzGav in #4512)

## :bow: Thanks to our contributors

Special thanks to the following contributors who helped with this release:

@Hopperpop, @MarvinSchenkel, @OzGav, @chrisuthe, @dmoo500, @fmunkes, @jyundt, @marcelveldt, @steamEngineer, @teancom

## 2.10.0b2
- Upstream Music Assistant server (beta) update to 2.10.0b2

### Upstream Release Notes
## 📦 Beta Release

_Changes since [2.10.0b1](https://github.com/music-assistant/server/releases/tag/2.10.0b1)_

### 🚀 New Providers

- Add Sveriges Radio provider (by @romany in #2974)
- Add Pocket Casts Provider (by @yfhyou in #3127)

### 🚀 Features and enhancements

- Add favorites support to Digitally Incorporated provider (by @benklop in #3458)
- feat(spotify): add curated browse for new releases and genres (by @x-ingo in #4177)
- Rename 'don't stop the music' to 'autoplay' (by @marcelveldt in #4404)
- Transfer playback to a new leader when unjoining a sync group leader (by @marcelveldt in #4412)
- Support `seek` Sendspin controller commands (by @maximmaxim345 in #4417)
- Resolve player palette only on the media owner, not per grouped member (by @marcelveldt in #4425)
- Make the demo player provider a groupable end-to-end test bed (by @marcelveldt in #4428)
- Add content_type to Genre schema with migration (by @jozefKruszynski in #4435)
- Configurable Autoplay with similar / library / playlist modes (by @marcelveldt in #4446)

### 🐛 Bugfixes

- Validate return_url before appending JWT token (by @s0yd4RK in #4272)
- Fix Spotify playback failing on broken Spotify CDN URLs (by @marcelveldt in #4398)
- Handle deleted image files with a typed not-found error (by @OzGav in #4400)
- Pause external sources instead of stopping them (by @marcelveldt in #4401)
- Fix unjoining a syncgroup member that joined the leader externally (by @marcelveldt in #4405)
- Recover flow stream restart on Cast groups (players that don't report idle) (by @OzGav in #4406)
- Keep universal player when its protocol links can't migrate to the native player (by @maximmaxim345 in #4413)
- Fix Home Assistant control of universal players running an external source (by @maximmaxim345 in #4415)
- Prevent a player from linking to itself on player type change (by @maximmaxim345 in #4416)
- Don't switch a playing group's output protocol when joining a player (by @marcelveldt in #4419)
- Keep radio/live streams restartable after a mid-stream disconnect (by @marcelveldt in #4421)
- Reconnect ICY radio streams on disconnect (by @marcelveldt in #4422)
- Keep AirPlay sync group playing when the leader's stream process crashes (by @marcelveldt in #4424)
- Fix WiiM UPnP event-callback binding on multi-homed / containerized hosts (by @rwlove in #4434)
- fix(snapcast): fix ~65s stop delay caused by spurious inactivity timer (by @vintvinst in #4436)
- Make live audio analysis a passive observer so it can never stall playback (by @chrisuthe in #4442)

### 🎨 Frontend Changes

- Always expand players when clicking the player button from the 'now playing' screen ([#60](https://github.com/music-assistant/frontend/pull/60)) (by @joperafe in [#1944](https://github.com/music-assistant/frontend/pull/1944))
- Add crossfade control to the player and a per-queue settings page (by @marcelveldt in [#1942](https://github.com/music-assistant/frontend/pull/1942))
- Pnpm switch (by @stvncode in [#1951](https://github.com/music-assistant/frontend/pull/1951))
- Revamp the fullscreen player header controls (by @marcelveldt in [#1945](https://github.com/music-assistant/frontend/pull/1945))
- Lokalise translations update (by @[github-actions[bot]](https://github.com/apps/github-actions) in [#1955](https://github.com/music-assistant/frontend/pull/1955))
- Possibility to hide/show browse by genre in discover page (by @stvncode in [#1957](https://github.com/music-assistant/frontend/pull/1957))
- Allow unjoining the sync group leader to hand off playback (by @marcelveldt in [#1956](https://github.com/music-assistant/frontend/pull/1956))
- Genre media type filtering (by @jozefKruszynski in [#1952](https://github.com/music-assistant/frontend/pull/1952))
- Rename 'auto play' to 'autoplay' and use the new queue command (by @marcelveldt in [#1953](https://github.com/music-assistant/frontend/pull/1953))
- Fix favorite heart state resetting on queue updates for radio and provider items (by @dmoo500 in [#1725](https://github.com/music-assistant/frontend/pull/1725))
- Add Start Radio to the queue item menu and drop redundant move up/down (by @marcelveldt in [#1963](https://github.com/music-assistant/frontend/pull/1963))
- Drag to reorder up next items in the fullscreen queue (by @marcelveldt in [#1961](https://github.com/music-assistant/frontend/pull/1961))
- Redesign the fullscreen player queue as a single scrollable list (by @marcelveldt in [#1960](https://github.com/music-assistant/frontend/pull/1960))
- Migrate timeline slider to reka-ui, fix tap not skipping correctly (by @pierosavi in [#1857](https://github.com/music-assistant/frontend/pull/1857))
- Extract the fullscreen queue item context menu into a helper (by @marcelveldt in [#1962](https://github.com/music-assistant/frontend/pull/1962))
- Add Lucide icon picker with custom MA device icons for player settings (by @dmoo500 in [#1779](https://github.com/music-assistant/frontend/pull/1779))
- Add a queue mode banner to surface radio and autoplay (by @marcelveldt in [#1966](https://github.com/music-assistant/frontend/pull/1966))
- Update context menu with shadcn comp and lucide icons (by @stvncode in [#1964](https://github.com/music-assistant/frontend/pull/1964))
- Streamline fullscreen player header controls (by @marcelveldt in [#1965](https://github.com/music-assistant/frontend/pull/1965))
- Fix rectangle art album not well displayed in the now playing bottom ([#66](https://github.com/music-assistant/frontend/pull/66)) (by @joperafe in [#1940](https://github.com/music-assistant/frontend/pull/1940))
- Fix drodpdown offset + width (by @stvncode in [#1968](https://github.com/music-assistant/frontend/pull/1968))

### Other Changes

- Lokalise translations update (by @github-actions[bot] in #4411)
- Extract library-sync config-entry building into a helper (by @zenibako in #4414)
- Share UPnP source-IP resolution across AirPlay and WiiM (by @rwlove in #4443)

### 🧰 Maintenance and dependency bumps

<details>
<summary>18 changes</summary>

- Bump ytmusicapi from 1.11.5 to 1.12.1 (by @dependabot[bot] in #4235)
- Enable RUF006 and fix unstored asyncio tasks (by @OzGav in #4393)
- Enable RUF012 (by @OzGav in #4394)
- Enable PYI034 (return Self from __aenter__/__new__) (by @OzGav in #4395)
- ⬆️ Update music-assistant-frontend to 2.17.195 (by @music-assistant-machine in #4396)
- Enable S307 rule - possibly insecure function (by @OzGav in #4397)
- ⬆️ Update music-assistant-frontend to 2.17.196 (by @music-assistant-machine in #4407)
- Bump zeroconf from 0.149.12 to 0.149.16 (by @dependabot[bot] in #4408)
- Move private methods to the bottom in the PocketCasts provider (by @OzGav in #4418)
- Bump actions/cache from 5 to 6 (by @dependabot[bot] in #4420)
- Dynamically update group leader capability on a zone player in MusicCast (by @fmunkes in #4423)
- ⬆️ Update music-assistant-frontend to 2.17.197 (by @music-assistant-machine in #4427)
- Bump actions/setup-python from 6.2.0 to 6.3.0 (by @dependabot[bot] in #4431)
- ⬆️ Update music-assistant-models to 1.1.144 (by @music-assistant-machine in #4433)
- ⬆️ Update music-assistant-frontend to 2.17.198 (by @music-assistant-machine in #4437)
- ⬆️ Update music-assistant-frontend to 2.17.199 (by @music-assistant-machine in #4438)
- ⬆️ Update music-assistant-frontend to 2.17.200 (by @music-assistant-machine in #4439)
- Enhance Audio Analysis Logging (by @chrisuthe in #4440)

</details>

## :bow: Thanks to our contributors

Special thanks to the following contributors who helped with this release:

@OzGav, @benklop, @chrisuthe, @dmoo500, @fmunkes, @joperafe, @jozefKruszynski, @marcelveldt, @maximmaxim345, @pierosavi, @romany, @rwlove, @s0yd4RK, @stvncode, @vintvinst, @x-ingo, @yfhyou, @zenibako

## 2.10.0b1
- Upstream Music Assistant server (beta) update to 2.10.0b1

### Upstream Release Notes
## 📦 Beta Release

_Changes since [2.10.0b0](https://github.com/music-assistant/server/releases/tag/2.10.0b0)_

### 🚀 Features and enhancements

- Allow Bandcamp feed and wishlist to be playable. (by @rnewman in #4371)
- Move queue-scoped settings (crossfade, volume normalization) to the queue (by @marcelveldt in #4373)
- Use ICY StreamUrl cover art for radio streams when it is an image (by @OzGav in #4379)
- Migrate Spotify Connect to go-librespot (by @marcelveldt in #4384)

### 🐛 Bugfixes

- Fix Party URL when webserver URL has trailing / (by @OzGav in #4375)
- Fix white noise bug in Jellyfin (by @OzGav in #4378)
- Fix next-track preload crash for fractional track durations (by @marcelveldt in #4380)
- Fix elapsed time drift for live sources played to a sync group (by @marcelveldt in #4385)
- Plex: fix track sync re-scanning the whole library on every page (by @marcelveldt in #4386)

### 🧰 Maintenance and dependency bumps

<details>
<summary>4 changes</summary>

- ⬆️ Update music-assistant-models to 1.1.140 (by @music-assistant-machine in #4374)
- ⬆️ Update music-assistant-models to 1.1.141 (by @music-assistant-machine in #4381)
- ⬆️ Update music-assistant-models to 1.1.142 (by @music-assistant-machine in #4382)
- Update BASE_IMAGE_VERSION for beta and nightly (by @marcelveldt in #4387)

</details>

## :bow: Thanks to our contributors

Special thanks to the following contributors who helped with this release:

@OzGav, @marcelveldt, @rnewman

## 2.10.0b0
- Upstream Music Assistant server (beta) update to 2.10.0b0

### Upstream Release Notes
## 📦 Beta Release

_Changes since [2.9.0rc7](https://github.com/music-assistant/server/releases/tag/2.9.0rc7)_

### 🚀 New Providers

- feat(provider): Add Amplipi provider (by @mcaulifn in #4110)

### 🚀 Features and enhancements

- Add support for audiobook collections (by @fmunkes in #3569)
- feat(audible): resume playback position from Audible Whispersync (by @scootaash in #3893)
- Adapt core methods to allow providing a username for item retrieval (by @fmunkes in #4015)
- Add explicit filter to smart playlist rules (by @dmoo500 in #4095)
- Improve smart crossfade audio quality: true frequency sweep and equal-power curves (by @MarvinSchenkel in #4158)
- Automatically check if CPU is supported for Audio Analysis (by @chrisuthe in #4166)
- Smart crossfade: transition on audible content instead of silent outros (by @MarvinSchenkel in #4178)
- Add API command to get the color palette for any image (by @marcelveldt in #4193)
- Localize server-provided strings (by @marcelveldt in #4200)
- Localized-name search for genres and playlists (by @marcelveldt in #4212)
- Key media item translation names by media type (by @marcelveldt in #4216)
- Localize genre descriptions server-side (by @marcelveldt in #4227)
- Localize error messages sent to API clients (by @marcelveldt in #4228)
- Localize provider-sync background-task names server-side (by @marcelveldt in #4238)
- Wire up provider status reporting (structured errors + derived status) (by @marcelveldt in #4242)
- Relax resource requirements for audio analysis providers (by @marcelveldt in #4249)
- Localize UnsupportedSystemError messages (by @marcelveldt in #4255)
- Localize user-facing provider error messages (by @marcelveldt in #4259)
- Localize core module names & descriptions server-side (by @marcelveldt in #4261)
- Localize player option labels server-side (by @marcelveldt in #4262)
- Relax 'Maximum' buffer tier to 7GB RAM (by @marcelveldt in #4268)
- Respect container cgroup memory limits when detecting system memory (by @marcelveldt in #4269)
- Persist playback speed for audiobooks and podcast episodes (by @OzGav in #4270)
- Localize Last.fm recommendation row titles and subtitles (by @marcelveldt in #4276)
- Translate nugs recommendation folder names (by @marcelveldt in #4277)
- Make NicoVideo recommendation labels translatable (by @marcelveldt in #4279)
- Make Audible root browse-folder labels translatable (by @marcelveldt in #4281)
- Make Bandcamp recommendation and collection folder labels translatable (by @marcelveldt in #4282)
- Localize NetEase Cloud Music recommendation and playlist labels (by @marcelveldt in #4283)
- Enable multi-instance support for Pandora (by @mcaulifn in #4284)
- Localize Deezer browse and virtual-playlist labels (by @marcelveldt in #4285)
- Localize Yandex Music browse labels via the server translation system (by @marcelveldt in #4286)
- Localize Podcast Index browse folder labels (by @marcelveldt in #4287)
- Make Phish.in browse-folder labels translatable (by @marcelveldt in #4288)
- KION Music: localize browse & recommendation labels via server translations (by @marcelveldt in #4289)
- Lazy-import chardet to lower idle memory (by @marcelveldt in #4291)
- Support common-string references in the translations build (by @marcelveldt in #4298)
- Guard against hardcoded ConfigEntry strings (by @marcelveldt in #4304)
- Extract CLAP scalar scoring into pure score_scalars() (by @chrisuthe in #4307)
- Import genres from Plex into media item metadata (by @lebdim in #4312)
- Skip dynamic playlists in refresh scan, sync provider-owned name/images (by @mcaulifn in #4326)
- Persist localized playlist names so they survive the library (by @marcelveldt in #4341)
- Fix config entry categories: use translation keys instead of raw English strings (by @marcelveldt in #4349)
- Parse "Track" by Artist radio stream titles and use album for artwork (by @OzGav in #4364)
- Move volume normalization target level to streams global setting (by @marcelveldt in #4369)

### 🐛 Bugfixes

- Fix Tidal DASH playback stuttering by serving manifests as HTTP routes (by @libre-7 in #4062)
- Fix Universal Group Player producing no audio on some members (by @OzGav in #4116)
- fix(alexa): include track metadata in the initial play_media push (by @croll83 in #4168)
- Fix Sendspin grouping with Cast devices (by @maximmaxim345 in #4170)
- Restore 'ignore volume reports' setting for AirPlay players (by @MarvinSchenkel in #4172)
- Fix track duration shrinking when seeking near the end with smart crossfade (by @MarvinSchenkel in #4176)
- Plex: fix bugs, remove dead code and reduce repetition (by @anatosun in #4179)
- Alexa: Fix restore saved session after aiohttp update (by @Joshi425 in #4181)
- Fix invalid scope error when adding a custom Spotify client ID (by @marcelveldt in #4182)
- Remove local providers without wiping the entire library (by @marcelveldt in #4183)
- Fix ISRC lookups failing for Last.fm track MBIDs (by @OzGav in #4185)
- Fix Last.fm Discover rows showing owned tracks under a different version name (by @OzGav in #4186)
- Derive Last.fm genre rows from listening history, not manual tags (by @OzGav in #4187)
- Fix now-playing artwork showing a solid background for transparent logos (by @OzGav in #4188)
- Fix sync group member playing out of sync after concurrent group changes (by @marcelveldt in #4189)
- Drop per-track MusicBrainz ISRC lookups from Last.fm recommendations (by @OzGav in #4190)
- Skip stale artist paths during filesystem track parsing (by @chrisuthe in #4191)
- Fix high idle memory usage (by @marcelveldt in #4198)
- Add correct playlog information when retrieving audiobooks in audiobooks controller (by @fmunkes in #4199)
- Fix translations in Audiobookshelf and iTunes podcasts (by @fmunkes in #4210)
- Translate RadioBrowser browse folder names (by @marcelveldt in #4223)
- Fix Cast Group mDNS for Nest Mini stereo pairs (cast_port/leader rename) (by @goodlucknow in #4224)
- Skip multichannel files in AcoustID scan instead of crashing (by @OzGav in #4230)
- Fix progress report when transitioning from idle or paused (by @fmunkes in #4236)
- Fix Sonos abrupt track switches when reordering an active queue (by @marcelveldt in #4237)
- Trim Provider.to_dict() to match the ProviderInstance schema (by @marcelveldt in #4239)
- Fix image download from CDNs that reject our User-Agent (by @OzGav in #4243)
- Backfill missing album on provider album tracks (by @OzGav in #4244)
- Fix standard crossfade falling back to a hard cut on some tracks (by @marcelveldt in #4253)
- Bound audio-analysis CPU usage and silence NNPACK spam on ARM (by @marcelveldt in #4257)
- Record explicit album/artist/track plays as user-initiated (by @chrisuthe in #4260)
- Localize MusicMe browse and recommendation section labels (by @marcelveldt in #4278)
- Translate Zvuk Music browse/recommendation labels (by @marcelveldt in #4280)
- Localize hardcoded provider browse and recommendation labels (by @marcelveldt in #4290)
- Release drained audio buffers in the inactivity monitor (by @marcelveldt in #4294)
- Admit genuine 4GB hosts via a shared RAM reporting tolerance (by @marcelveldt in #4301)
- Remove stale Cast players that are actually passive multichannel endpoints (by @marcelveldt in #4302)
- Fix live metadata not refreshing for grouped AirPlay players (by @marcelveldt in #4303)
- Pace audio analysis and cap it to half the CPU cores (by @marcelveldt in #4311)
- Fix protocol player settings not reverting to their default value (by @marcelveldt in #4314)
- Fix WebDAV sync failing on folder names with special characters (by @marcelveldt in #4315)
- Fix podcast episode lookup and a queue preload crash on a drained queue (by @marcelveldt in #4318)
- Preserve percent-encoding when fetching radio/HTTP stream URLs (by @OzGav in #4319)
- Localize injected protocol output config entries (by @marcelveldt in #4322)
- Fix podcast episode lookup in gpodder (by @fmunkes in #4323)
- Fix playback of multipart files with apostrophes in path (by @OzGav in #4329)
- Fix WebDAV auth deprecation warning (by @OzGav in #4330)
- Raise open-file soft limit at startup (by @OzGav in #4332)

### 🎨 Frontend Changes

- Add scroll to description dialog for long descriptions (by @dmoo500 in [#1908](https://github.com/music-assistant/frontend/pull/1908))
- Add field icons to smart playlist rules (by @dmoo500 in [#1866](https://github.com/music-assistant/frontend/pull/1866))
- Fix settings breadcrumb for disabled provider instances (by @OzGav in [#1909](https://github.com/music-assistant/frontend/pull/1909))
- Consume server-resolved translations for server-provided strings (by @marcelveldt in [#1911](https://github.com/music-assistant/frontend/pull/1911))
- Add explicit_only filter to smart playlist rules (by @dmoo500 in [#1865](https://github.com/music-assistant/frontend/pull/1865))
- Remove server-resolved strings from the locale files (by @marcelveldt in [#1912](https://github.com/music-assistant/frontend/pull/1912))
- Use ExplicitIcon for explicit content field in smart playlist rules (by @dmoo500 in [#1924](https://github.com/music-assistant/frontend/pull/1924))
- Use server-provided genre descriptions (by @marcelveldt in [#1923](https://github.com/music-assistant/frontend/pull/1923))
- Reconnect the built-in player after a dropped connection (by @marcelveldt in [#1910](https://github.com/music-assistant/frontend/pull/1910))
- Use server-resolved background-task names (drop client-side translation) (by @marcelveldt in [#1925](https://github.com/music-assistant/frontend/pull/1925))
- Render player option and sound mode labels localized by the server (by @marcelveldt in [#1932](https://github.com/music-assistant/frontend/pull/1932))
- Use toast notifications for config flow errors instead of browser alerts (by @marcelveldt in [#1929](https://github.com/music-assistant/frontend/pull/1929))
- Provider status indicator and clearer error reporting (by @marcelveldt in [#1927](https://github.com/music-assistant/frontend/pull/1927))
- Drop server-stripped translation fields from frontend types (by @marcelveldt in [#1931](https://github.com/music-assistant/frontend/pull/1931))
- Remove leftover and dead translation keys from the frontend (by @marcelveldt in [#1933](https://github.com/music-assistant/frontend/pull/1933))
- fix(i18n): replace edit by save (by @kissu in [#1856](https://github.com/music-assistant/frontend/pull/1856))
- Move "refresh" button to the toolbar for playlists (by @ijc in [#1930](https://github.com/music-assistant/frontend/pull/1930))
- Localize frontend-injected config entry categories (by @marcelveldt in [#1938](https://github.com/music-assistant/frontend/pull/1938))
- Stop play button animation with external source (by @OzGav in [#1935](https://github.com/music-assistant/frontend/pull/1935))

### Other Changes

- Lokalise translations update (by @github-actions[bot] in #4219)
- Lokalise translations update (by @github-actions[bot] in #4252)
- Refactor player_queues controller into a package (by @marcelveldt in #4263)
- Refactor metadata controller into a package (by @marcelveldt in #4265)
- Refactor music controller into its own package (by @marcelveldt in #4266)
- Move player_queues config-entry strings into the controller's strings.json (by @marcelveldt in #4267)
- Revert "Respect container cgroup memory limits" (#4269) (by @marcelveldt in #4274)
- Lokalise translations update (by @github-actions[bot] in #4296)
- Move core-owned strings out of the common translations (by @marcelveldt in #4299)
- Use bare keys for all translation_key overrides (ConfigEntry + media) (by @marcelveldt in #4310)
- Deduplicate strings via common-string references (by @marcelveldt in #4327)
- Lokalise translations update (by @github-actions[bot] in #4340)
- Use the shared datetime helpers instead of calling datetime directly (by @marcelveldt in #4352)
- Move private methods to the bottom of the class in a few small providers (by @marcelveldt in #4353)
- Move private methods to the bottom of the class in the music media controllers (by @marcelveldt in #4354)
- Lokalise translations update (by @github-actions[bot] in #4357)

### 🧰 Maintenance and dependency bumps

<details>
<summary>59 changes</summary>

- Fix release notes for minor releases skipping most changes (by @MarvinSchenkel in #4171)
- Bump zeroconf from 0.149.7 to 0.149.12 (by @dependabot[bot] in #4174)
- Remove Dashie Kiosk player provider (by @jwlerch78 in #4192)
- ⬆️ Update music-assistant-frontend to 2.17.187 (by @music-assistant-machine in #4195)
- Vectorize weighted distance in the sonic similarity provider (by @marcelveldt in #4203)
- Use threading.get_ident() instead of asyncio's private _thread_id (by @marcelveldt in #4205)
- ⬆️ Update music-assistant-frontend to 2.17.188 (by @music-assistant-machine in #4208)
- Lokalise translations update (by @github-actions[bot] in #4209)
- Adapt QQ Music provider to qqmusic-api 0.6 (by @xiasi0 in #4211)
- Reduce idle memory usage by tuning jemalloc (by @marcelveldt in #4213)
- Don't lint downloaded translation files for spelling/EOF (by @marcelveldt in #4215)
- Lokalise translations update (by @github-actions[bot] in #4221)
- ⬆️ Update music-assistant-frontend to 2.17.189 (by @music-assistant-machine in #4222)
- Replace broad except in scrobbler with per-client exceptions (by @OzGav in #4226)
- Remove stale Deezer disc/track number TODO (by @OzGav in #4229)
- Bump actions/checkout from 4 to 6 (by @dependabot[bot] in #4232)
- Bump cryptography from 46.0.7 to 49.0.0 (by @dependabot[bot] in #4233)
- ⬆️ Update music-assistant-models to 1.1.133 (by @music-assistant-machine in #4240)
- Bump aiohttp from 3.14.0 to 3.14.1 (by @dependabot[bot] in #4241)
- Type ytmusic search filter as a Literal (unblock ytmusicapi 1.12.1 mypy) (by @OzGav in #4245)
- ⬆️ Update music-assistant-frontend to 2.17.190 (by @music-assistant-machine in #4248)
- Target Python 3.14 for lint and type-checking (by @marcelveldt in #4254)
- ⬆️ Update music-assistant-models to 1.1.134 (by @music-assistant-machine in #4258)
- ⬆️ Update music-assistant-models to 1.1.135 (by @music-assistant-machine in #4264)
- ⬆️ Update music-assistant-frontend to 2.17.191 (by @music-assistant-machine in #4271)
- ⬆️ Update music-assistant-models to 1.1.136 (by @music-assistant-machine in #4273)
- Avoid loading aiortc/PyAV when remote access is disabled (by @marcelveldt in #4292)
- Make SQLite page-cache and mmap RAM-aware (by @marcelveldt in #4293)
- Cut repeated reflection on hot cache-hit and event-dispatch paths (by @marcelveldt in #4295)
- ⬆️ Update music-assistant-frontend to 2.17.192 (by @music-assistant-machine in #4309)
- ⬆️ Update music-assistant-models to 1.1.137 (by @music-assistant-machine in #4316)
- Fix unreachable statement in player_queues controller (by @Copilot in #4320)
- Bump actions/checkout from 6 to 7 (by @dependabot[bot] in #4321)
- Remove ffmpeg install from lint CI job (by @marcelveldt in #4324)
- Speed up CI test jobs (split ffmpeg tests + skip on non-code PRs) (by @marcelveldt in #4325)
- Add Amplipi SVGs (by @OzGav in #4331)
- ⬆️ Update music-assistant-frontend to 2.17.193 (by @music-assistant-machine in #4333)
- Fix test suite hanging without ffmpeg + cap test jobs at 30min (by @marcelveldt in #4334)
- Run only affected providers' tests on PRs (HA-style), with Codecov (by @marcelveldt in #4335)
- Clarify the audio-analysis CPU requirement (AVX2 on x86, NEON on ARM) (by @marcelveldt in #4336)
- Mirror the source tree in tests/ (controller tests → folders, utils → tests/helpers/) (by @marcelveldt in #4337)
- Smarter CI test selection: scope coverage on partial runs + skip translation-only PRs (by @marcelveldt in #4339)
- Add provider-focused lint checks to pre-commit and CI (by @marcelveldt in #4343)
- ⬆️ Update music-assistant-models to 1.1.139 (by @music-assistant-machine in #4345)
- Bump codecov/codecov-action from 5 to 7 (by @dependabot[bot] in #4346)
- Enforce multi-line docstring summary on the second line (by @marcelveldt in #4347)
- Enforce private methods at the bottom of a class (by @marcelveldt in #4350)
- Validate ConfigEntry.category against strings.json in pre-commit check (by @marcelveldt in #4351)
- Fix incorrect docstrings and comment in the music media controllers (by @marcelveldt in #4355)
- Move private methods to the bottom of the class in the webserver controllers (by @marcelveldt in #4356)
- Move private methods to the bottom of the class in the streams controllers (by @marcelveldt in #4358)
- Move private methods to the bottom of the class in the music controller (by @marcelveldt in #4359)
- Move private methods to the bottom of the class in the player queues controller (by @marcelveldt in #4360)
- Move private methods to the bottom of the class in the players controller (by @marcelveldt in #4361)
- Move private methods to the bottom of the class in the tasks controller (by @marcelveldt in #4362)
- Move private methods to the bottom of the class in core misc files (by @marcelveldt in #4363)
- Move private methods to the bottom of the class in team-maintained providers (by @marcelveldt in #4365)
- ⬆️ Update music-assistant-frontend to 2.17.194 (by @music-assistant-machine in #4366)
- Fix Auto Release workflow failing at startup due to missing PR permission (by @marcelveldt in #4368)

</details>

## :bow: Thanks to our contributors

Special thanks to the following contributors who helped with this release:

@Copilot, @Joshi425, @MarvinSchenkel, @OzGav, @anatosun, @chrisuthe, @croll83, @dmoo500, @fmunkes, @goodlucknow, @ijc, @jwlerch78, @kissu, @lebdim, @libre-7, @marcelveldt, @maximmaxim345, @mcaulifn, @scootaash, @xiasi0

## 2.9.0b0
- Upstream Music Assistant server (beta) update to 2.9.0b0

### Upstream Release Notes
## 📦 Beta Release

_Changes since [2.9.0rc7](https://github.com/music-assistant/server/releases/tag/2.9.0rc7)_

### 🚀 New Providers

- feat(provider): Add Amplipi provider (by @mcaulifn in #4110)

### 🚀 Features and enhancements

- Add support for audiobook collections (by @fmunkes in #3569)
- feat(audible): resume playback position from Audible Whispersync (by @scootaash in #3893)
- Adapt core methods to allow providing a username for item retrieval (by @fmunkes in #4015)
- Add explicit filter to smart playlist rules (by @dmoo500 in #4095)
- Improve smart crossfade audio quality: true frequency sweep and equal-power curves (by @MarvinSchenkel in #4158)
- Automatically check if CPU is supported for Audio Analysis (by @chrisuthe in #4166)
- Smart crossfade: transition on audible content instead of silent outros (by @MarvinSchenkel in #4178)
- Add API command to get the color palette for any image (by @marcelveldt in #4193)
- Localize server-provided strings (by @marcelveldt in #4200)
- Localized-name search for genres and playlists (by @marcelveldt in #4212)
- Key media item translation names by media type (by @marcelveldt in #4216)
- Localize genre descriptions server-side (by @marcelveldt in #4227)
- Localize error messages sent to API clients (by @marcelveldt in #4228)
- Localize provider-sync background-task names server-side (by @marcelveldt in #4238)
- Wire up provider status reporting (structured errors + derived status) (by @marcelveldt in #4242)
- Relax resource requirements for audio analysis providers (by @marcelveldt in #4249)
- Localize UnsupportedSystemError messages (by @marcelveldt in #4255)
- Localize user-facing provider error messages (by @marcelveldt in #4259)
- Localize core module names & descriptions server-side (by @marcelveldt in #4261)
- Localize player option labels server-side (by @marcelveldt in #4262)
- Relax 'Maximum' buffer tier to 7GB RAM (by @marcelveldt in #4268)
- Respect container cgroup memory limits when detecting system memory (by @marcelveldt in #4269)
- Persist playback speed for audiobooks and podcast episodes (by @OzGav in #4270)
- Localize Last.fm recommendation row titles and subtitles (by @marcelveldt in #4276)
- Translate nugs recommendation folder names (by @marcelveldt in #4277)
- Make NicoVideo recommendation labels translatable (by @marcelveldt in #4279)
- Make Audible root browse-folder labels translatable (by @marcelveldt in #4281)
- Make Bandcamp recommendation and collection folder labels translatable (by @marcelveldt in #4282)
- Localize NetEase Cloud Music recommendation and playlist labels (by @marcelveldt in #4283)
- Localize Deezer browse and virtual-playlist labels (by @marcelveldt in #4285)
- Localize Yandex Music browse labels via the server translation system (by @marcelveldt in #4286)
- Localize Podcast Index browse folder labels (by @marcelveldt in #4287)
- Make Phish.in browse-folder labels translatable (by @marcelveldt in #4288)
- KION Music: localize browse & recommendation labels via server translations (by @marcelveldt in #4289)
- Lazy-import chardet to lower idle memory (by @marcelveldt in #4291)
- Support common-string references in the translations build (by @marcelveldt in #4298)
- Guard against hardcoded ConfigEntry strings (by @marcelveldt in #4304)
- Extract CLAP scalar scoring into pure score_scalars() (by @chrisuthe in #4307)
- Import genres from Plex into media item metadata (by @lebdim in #4312)
- Skip dynamic playlists in refresh scan, sync provider-owned name/images (by @mcaulifn in #4326)
- Persist localized playlist names so they survive the library (by @marcelveldt in #4341)
- Fix config entry categories: use translation keys instead of raw English strings (by @marcelveldt in #4349)
- Parse "Track" by Artist radio stream titles and use album for artwork (by @OzGav in #4364)
- Move volume normalization target level to streams global setting (by @marcelveldt in #4369)

### 🐛 Bugfixes

- Fix Tidal DASH playback stuttering by serving manifests as HTTP routes (by @libre-7 in #4062)
- Fix Universal Group Player producing no audio on some members (by @OzGav in #4116)
- fix(alexa): include track metadata in the initial play_media push (by @croll83 in #4168)
- Fix Sendspin grouping with Cast devices (by @maximmaxim345 in #4170)
- Restore 'ignore volume reports' setting for AirPlay players (by @MarvinSchenkel in #4172)
- Fix track duration shrinking when seeking near the end with smart crossfade (by @MarvinSchenkel in #4176)
- Plex: fix bugs, remove dead code and reduce repetition (by @anatosun in #4179)
- Alexa: Fix restore saved session after aiohttp update (by @Joshi425 in #4181)
- Fix invalid scope error when adding a custom Spotify client ID (by @marcelveldt in #4182)
- Remove local providers without wiping the entire library (by @marcelveldt in #4183)
- Fix ISRC lookups failing for Last.fm track MBIDs (by @OzGav in #4185)
- Fix Last.fm Discover rows showing owned tracks under a different version name (by @OzGav in #4186)
- Derive Last.fm genre rows from listening history, not manual tags (by @OzGav in #4187)
- Fix now-playing artwork showing a solid background for transparent logos (by @OzGav in #4188)
- Fix sync group member playing out of sync after concurrent group changes (by @marcelveldt in #4189)
- Drop per-track MusicBrainz ISRC lookups from Last.fm recommendations (by @OzGav in #4190)
- Skip stale artist paths during filesystem track parsing (by @chrisuthe in #4191)
- Fix high idle memory usage (by @marcelveldt in #4198)
- Add correct playlog information when retrieving audiobooks in audiobooks controller (by @fmunkes in #4199)
- Fix translations in Audiobookshelf and iTunes podcasts (by @fmunkes in #4210)
- Translate RadioBrowser browse folder names (by @marcelveldt in #4223)
- Fix Cast Group mDNS for Nest Mini stereo pairs (cast_port/leader rename) (by @goodlucknow in #4224)
- Skip multichannel files in AcoustID scan instead of crashing (by @OzGav in #4230)
- Fix progress report when transitioning from idle or paused (by @fmunkes in #4236)
- Fix Sonos abrupt track switches when reordering an active queue (by @marcelveldt in #4237)
- Trim Provider.to_dict() to match the ProviderInstance schema (by @marcelveldt in #4239)
- Fix image download from CDNs that reject our User-Agent (by @OzGav in #4243)
- Backfill missing album on provider album tracks (by @OzGav in #4244)
- Fix standard crossfade falling back to a hard cut on some tracks (by @marcelveldt in #4253)
- Bound audio-analysis CPU usage and silence NNPACK spam on ARM (by @marcelveldt in #4257)
- Record explicit album/artist/track plays as user-initiated (by @chrisuthe in #4260)
- Localize MusicMe browse and recommendation section labels (by @marcelveldt in #4278)
- Translate Zvuk Music browse/recommendation labels (by @marcelveldt in #4280)
- Localize hardcoded provider browse and recommendation labels (by @marcelveldt in #4290)
- Release drained audio buffers in the inactivity monitor (by @marcelveldt in #4294)
- Admit genuine 4GB hosts via a shared RAM reporting tolerance (by @marcelveldt in #4301)
- Remove stale Cast players that are actually passive multichannel endpoints (by @marcelveldt in #4302)
- Fix live metadata not refreshing for grouped AirPlay players (by @marcelveldt in #4303)
- Pace audio analysis and cap it to half the CPU cores (by @marcelveldt in #4311)
- Fix protocol player settings not reverting to their default value (by @marcelveldt in #4314)
- Fix WebDAV sync failing on folder names with special characters (by @marcelveldt in #4315)
- Fix podcast episode lookup and a queue preload crash on a drained queue (by @marcelveldt in #4318)
- Preserve percent-encoding when fetching radio/HTTP stream URLs (by @OzGav in #4319)
- Localize injected protocol output config entries (by @marcelveldt in #4322)
- Fix podcast episode lookup in gpodder (by @fmunkes in #4323)
- Fix playback of multipart files with apostrophes in path (by @OzGav in #4329)
- Fix WebDAV auth deprecation warning (by @OzGav in #4330)
- Raise open-file soft limit at startup (by @OzGav in #4332)

### 🎨 Frontend Changes

- Add scroll to description dialog for long descriptions (by @dmoo500 in [#1908](https://github.com/music-assistant/frontend/pull/1908))
- Add field icons to smart playlist rules (by @dmoo500 in [#1866](https://github.com/music-assistant/frontend/pull/1866))
- Fix settings breadcrumb for disabled provider instances (by @OzGav in [#1909](https://github.com/music-assistant/frontend/pull/1909))
- Consume server-resolved translations for server-provided strings (by @marcelveldt in [#1911](https://github.com/music-assistant/frontend/pull/1911))
- Add explicit_only filter to smart playlist rules (by @dmoo500 in [#1865](https://github.com/music-assistant/frontend/pull/1865))
- Remove server-resolved strings from the locale files (by @marcelveldt in [#1912](https://github.com/music-assistant/frontend/pull/1912))
- Use ExplicitIcon for explicit content field in smart playlist rules (by @dmoo500 in [#1924](https://github.com/music-assistant/frontend/pull/1924))
- Use server-provided genre descriptions (by @marcelveldt in [#1923](https://github.com/music-assistant/frontend/pull/1923))
- Reconnect the built-in player after a dropped connection (by @marcelveldt in [#1910](https://github.com/music-assistant/frontend/pull/1910))
- Use server-resolved background-task names (drop client-side translation) (by @marcelveldt in [#1925](https://github.com/music-assistant/frontend/pull/1925))
- Render player option and sound mode labels localized by the server (by @marcelveldt in [#1932](https://github.com/music-assistant/frontend/pull/1932))
- Use toast notifications for config flow errors instead of browser alerts (by @marcelveldt in [#1929](https://github.com/music-assistant/frontend/pull/1929))
- Provider status indicator and clearer error reporting (by @marcelveldt in [#1927](https://github.com/music-assistant/frontend/pull/1927))
- Drop server-stripped translation fields from frontend types (by @marcelveldt in [#1931](https://github.com/music-assistant/frontend/pull/1931))
- Remove leftover and dead translation keys from the frontend (by @marcelveldt in [#1933](https://github.com/music-assistant/frontend/pull/1933))
- fix(i18n): replace edit by save (by @kissu in [#1856](https://github.com/music-assistant/frontend/pull/1856))
- Move "refresh" button to the toolbar for playlists (by @ijc in [#1930](https://github.com/music-assistant/frontend/pull/1930))
- Localize frontend-injected config entry categories (by @marcelveldt in [#1938](https://github.com/music-assistant/frontend/pull/1938))
- Stop play button animation with external source (by @OzGav in [#1935](https://github.com/music-assistant/frontend/pull/1935))

### Other Changes

- Lokalise translations update (by @github-actions[bot] in #4219)
- Lokalise translations update (by @github-actions[bot] in #4252)
- Refactor player_queues controller into a package (by @marcelveldt in #4263)
- Refactor metadata controller into a package (by @marcelveldt in #4265)
- Refactor music controller into its own package (by @marcelveldt in #4266)
- Move player_queues config-entry strings into the controller's strings.json (by @marcelveldt in #4267)
- Revert "Respect container cgroup memory limits" (#4269) (by @marcelveldt in #4274)
- Lokalise translations update (by @github-actions[bot] in #4296)
- Move core-owned strings out of the common translations (by @marcelveldt in #4299)
- Use bare keys for all translation_key overrides (ConfigEntry + media) (by @marcelveldt in #4310)
- Deduplicate strings via common-string references (by @marcelveldt in #4327)
- Lokalise translations update (by @github-actions[bot] in #4340)
- Use the shared datetime helpers instead of calling datetime directly (by @marcelveldt in #4352)
- Move private methods to the bottom of the class in a few small providers (by @marcelveldt in #4353)
- Move private methods to the bottom of the class in the music media controllers (by @marcelveldt in #4354)
- Lokalise translations update (by @github-actions[bot] in #4357)

### 🧰 Maintenance and dependency bumps

<details>
<summary>59 changes</summary>

- Fix release notes for minor releases skipping most changes (by @MarvinSchenkel in #4171)
- Bump zeroconf from 0.149.7 to 0.149.12 (by @dependabot[bot] in #4174)
- Remove Dashie Kiosk player provider (by @jwlerch78 in #4192)
- ⬆️ Update music-assistant-frontend to 2.17.187 (by @music-assistant-machine in #4195)
- Vectorize weighted distance in the sonic similarity provider (by @marcelveldt in #4203)
- Use threading.get_ident() instead of asyncio's private _thread_id (by @marcelveldt in #4205)
- ⬆️ Update music-assistant-frontend to 2.17.188 (by @music-assistant-machine in #4208)
- Lokalise translations update (by @github-actions[bot] in #4209)
- Adapt QQ Music provider to qqmusic-api 0.6 (by @xiasi0 in #4211)
- Reduce idle memory usage by tuning jemalloc (by @marcelveldt in #4213)
- Don't lint downloaded translation files for spelling/EOF (by @marcelveldt in #4215)
- Lokalise translations update (by @github-actions[bot] in #4221)
- ⬆️ Update music-assistant-frontend to 2.17.189 (by @music-assistant-machine in #4222)
- Replace broad except in scrobbler with per-client exceptions (by @OzGav in #4226)
- Remove stale Deezer disc/track number TODO (by @OzGav in #4229)
- Bump actions/checkout from 4 to 6 (by @dependabot[bot] in #4232)
- Bump cryptography from 46.0.7 to 49.0.0 (by @dependabot[bot] in #4233)
- ⬆️ Update music-assistant-models to 1.1.133 (by @music-assistant-machine in #4240)
- Bump aiohttp from 3.14.0 to 3.14.1 (by @dependabot[bot] in #4241)
- Type ytmusic search filter as a Literal (unblock ytmusicapi 1.12.1 mypy) (by @OzGav in #4245)
- ⬆️ Update music-assistant-frontend to 2.17.190 (by @music-assistant-machine in #4248)
- Target Python 3.14 for lint and type-checking (by @marcelveldt in #4254)
- ⬆️ Update music-assistant-models to 1.1.134 (by @music-assistant-machine in #4258)
- ⬆️ Update music-assistant-models to 1.1.135 (by @music-assistant-machine in #4264)
- ⬆️ Update music-assistant-frontend to 2.17.191 (by @music-assistant-machine in #4271)
- ⬆️ Update music-assistant-models to 1.1.136 (by @music-assistant-machine in #4273)
- Avoid loading aiortc/PyAV when remote access is disabled (by @marcelveldt in #4292)
- Make SQLite page-cache and mmap RAM-aware (by @marcelveldt in #4293)
- Cut repeated reflection on hot cache-hit and event-dispatch paths (by @marcelveldt in #4295)
- ⬆️ Update music-assistant-frontend to 2.17.192 (by @music-assistant-machine in #4309)
- ⬆️ Update music-assistant-models to 1.1.137 (by @music-assistant-machine in #4316)
- Fix unreachable statement in player_queues controller (by @Copilot in #4320)
- Bump actions/checkout from 6 to 7 (by @dependabot[bot] in #4321)
- Remove ffmpeg install from lint CI job (by @marcelveldt in #4324)
- Speed up CI test jobs (split ffmpeg tests + skip on non-code PRs) (by @marcelveldt in #4325)
- Add Amplipi SVGs (by @OzGav in #4331)
- ⬆️ Update music-assistant-frontend to 2.17.193 (by @music-assistant-machine in #4333)
- Fix test suite hanging without ffmpeg + cap test jobs at 30min (by @marcelveldt in #4334)
- Run only affected providers' tests on PRs (HA-style), with Codecov (by @marcelveldt in #4335)
- Clarify the audio-analysis CPU requirement (AVX2 on x86, NEON on ARM) (by @marcelveldt in #4336)
- Mirror the source tree in tests/ (controller tests → folders, utils → tests/helpers/) (by @marcelveldt in #4337)
- Smarter CI test selection: scope coverage on partial runs + skip translation-only PRs (by @marcelveldt in #4339)
- Add provider-focused lint checks to pre-commit and CI (by @marcelveldt in #4343)
- ⬆️ Update music-assistant-models to 1.1.139 (by @music-assistant-machine in #4345)
- Bump codecov/codecov-action from 5 to 7 (by @dependabot[bot] in #4346)
- Enforce multi-line docstring summary on the second line (by @marcelveldt in #4347)
- Enforce private methods at the bottom of a class (by @marcelveldt in #4350)
- Validate ConfigEntry.category against strings.json in pre-commit check (by @marcelveldt in #4351)
- Fix incorrect docstrings and comment in the music media controllers (by @marcelveldt in #4355)
- Move private methods to the bottom of the class in the webserver controllers (by @marcelveldt in #4356)
- Move private methods to the bottom of the class in the streams controllers (by @marcelveldt in #4358)
- Move private methods to the bottom of the class in the music controller (by @marcelveldt in #4359)
- Move private methods to the bottom of the class in the player queues controller (by @marcelveldt in #4360)
- Move private methods to the bottom of the class in the players controller (by @marcelveldt in #4361)
- Move private methods to the bottom of the class in the tasks controller (by @marcelveldt in #4362)
- Move private methods to the bottom of the class in core misc files (by @marcelveldt in #4363)
- Move private methods to the bottom of the class in team-maintained providers (by @marcelveldt in #4365)
- ⬆️ Update music-assistant-frontend to 2.17.194 (by @music-assistant-machine in #4366)
- Fix Auto Release workflow failing at startup due to missing PR permission (by @marcelveldt in #4368)

</details>

## :bow: Thanks to our contributors

Special thanks to the following contributors who helped with this release:

@Copilot, @Joshi425, @MarvinSchenkel, @OzGav, @anatosun, @chrisuthe, @croll83, @dmoo500, @fmunkes, @goodlucknow, @ijc, @jwlerch78, @kissu, @lebdim, @libre-7, @marcelveldt, @maximmaxim345, @mcaulifn, @scootaash, @xiasi0

## 2.9.2
- Upstream Music Assistant server (beta) update to 2.9.2

### Upstream Release Notes
## 📦 Stable Release

_Changes since [2.9.1](https://github.com/music-assistant/server/releases/tag/2.9.1)_

### 🚀 Features and enhancements

- Relax resource requirements for audio analysis providers (by @marcelveldt in #4249)
- Relax 'Maximum' buffer tier to 7GB RAM (by @marcelveldt in #4268)

### 🐛 Bugfixes

- Alexa: Fix restore saved session after aiohttp update (by @Joshi425 in #4181)
- Add correct playlog information when retrieving audiobooks in audiobooks controller (by @fmunkes in #4199)
- Fix Cast Group mDNS for Nest Mini stereo pairs (cast_port/leader rename) (by @goodlucknow in #4224)
- Skip multichannel files in AcoustID scan instead of crashing (by @OzGav in #4230)
- Fix progress report when transitioning from idle or paused (by @fmunkes in #4236)
- Fix image download from CDNs that reject our User-Agent (by @OzGav in #4243)
- Backfill missing album on provider album tracks (by @OzGav in #4244)
- Fix standard crossfade falling back to a hard cut on some tracks (by @marcelveldt in #4253)
- Bound audio-analysis CPU usage and silence NNPACK spam on ARM (by @marcelveldt in #4257)
- Record explicit album/artist/track plays as user-initiated (by @chrisuthe in #4260)
- Release drained audio buffers in the inactivity monitor (by @marcelveldt in #4294)

### 🧰 Maintenance and dependency bumps

<details>
<summary>5 changes</summary>

- Vectorize weighted distance in the sonic similarity provider (by @marcelveldt in #4203)
- Bump aiohttp from 3.14.0 to 3.14.1 (by @dependabot[bot] in #4241)
- Type ytmusic search filter as a Literal (unblock ytmusicapi 1.12.1 mypy) (by @OzGav in #4245)
- Accept Python 3.14 syntax in backports without reformatting stable (by @marcelveldt in #4256)
- Make SQLite page-cache and mmap RAM-aware (by @marcelveldt in #4293)

</details>

## :bow: Thanks to our contributors

Special thanks to the following contributors who helped with this release:

@Joshi425, @OzGav, @chrisuthe, @fmunkes, @goodlucknow, @marcelveldt

## 2.9.1
- Upstream Music Assistant server (beta) update to 2.9.1

### Upstream Release Notes
## 📦 Stable Release

_Changes since [2.9.0](https://github.com/music-assistant/server/releases/tag/2.9.0)_

### 🚀 Features and enhancements

- Improve smart crossfade audio quality: true frequency sweep and equal-power curves (by @MarvinSchenkel in #4158)
- Automatically check if CPU is supported for Audio Analysis (by @chrisuthe in #4166)

### 🐛 Bugfixes

- Fix Universal Group Player producing no audio on some members (by @OzGav in #4116)
- fix(alexa): include track metadata in the initial play_media push (by @croll83 in #4168)
- Fix Sendspin grouping with Cast devices (by @maximmaxim345 in #4170)
- Restore 'ignore volume reports' setting for AirPlay players (by @MarvinSchenkel in #4172)
- Fix track duration shrinking when seeking near the end with smart crossfade (by @MarvinSchenkel in #4176)
- Fix invalid scope error when adding a custom Spotify client ID (by @marcelveldt in #4182)
- Remove local providers without wiping the entire library (by @marcelveldt in #4183)
- Fix ISRC lookups failing for Last.fm track MBIDs (by @OzGav in #4185)
- Fix Last.fm Discover rows showing owned tracks under a different version name (by @OzGav in #4186)
- Derive Last.fm genre rows from listening history, not manual tags (by @OzGav in #4187)
- Fix now-playing artwork showing a solid background for transparent logos (by @OzGav in #4188)
- Fix sync group member playing out of sync after concurrent group changes (by @marcelveldt in #4189)
- Drop per-track MusicBrainz ISRC lookups from Last.fm recommendations (by @OzGav in #4190)
- Skip stale artist paths during filesystem track parsing (by @chrisuthe in #4191)
- Fix high idle memory usage (by @marcelveldt in #4198)

### 🧰 Maintenance and dependency bumps

- Reduce idle memory usage by tuning jemalloc (by @marcelveldt in #4213)

## :bow: Thanks to our contributors

Special thanks to the following contributors who helped with this release:

@MarvinSchenkel, @OzGav, @chrisuthe, @croll83, @marcelveldt, @maximmaxim345

## 2.9.0
- Upstream Music Assistant server (beta) update to 2.9.0

### Upstream Release Notes
## 📦 Stable Release

_Changes since [2.8.9](https://github.com/music-assistant/server/releases/tag/2.8.9)_

### 🚀 Features and enhancements

- Separate library artist views from per-provider artist listings (by @marcelveldt in #4039)
- Add Settings to allow Control of default similar_track action (by @chrisuthe in #4053)
- Add album_type filter to smart playlist rules (by @dmoo500 in #4059)
- Cache recommendations() for sonic_similarity and audiobookshelf (by @MarvinSchenkel in #4099)
- Speed up YouTube Music recommendations loading (by @MarvinSchenkel in #4120)
- Spread metadata maintenance schedule across the day (by @MarvinSchenkel in #4126)
- Add get_artist_toptracks to lastfm recommendations provider (by @OzGav in #4141)
- Enable WiiM and Last.fm Recommendations by default (by @MarvinSchenkel in #4142)
- Smart playlists: optional AI-generated descriptions (by @MarvinSchenkel in #4144)
- Lastfm improvements (by @OzGav in #4148)
- Improve playlog for artists and albums (by @chrisuthe in #4149)
- ACoustID Switch to shared API key by default (by @OzGav in #4154)
- Default artist fix (by @chrisuthe in #4163)
- Add unofficial-integration disclaimer to streaming provider settings (by @marcelveldt in #4164)

### 🐛 Bugfixes

- Plex Connect: refactor and fixes plugin (by @anatosun in #3510)
- Make universal player merge deterministic when link counts tie (by @sdhomecode in #4017)
- Fix AcoustID scan coverage stalling (by @OzGav in #4070)
- Fix smart playlist dedup for streaming (non-library) tracks (by @MarvinSchenkel in #4082)
- Fix genre icons disappearing after install path changes (by @MarvinSchenkel in #4083)
- Fix YouTube Music search() signature (by @OzGav in #4085)
- Fix WiiM volume_set by using HTTP command instead of UPnP (by @MarvinSchenkel in #4086)
- Reconcile smart playlist library entries on load to recover after DB reset (by @dmoo500 in #4088)
- Apple Music: stream library tracks and harden transient-error handling (by @teancom in #4089)
- Fix YTMusic provider not retrying when PO Token server is slow to start (by @CodeCommander in #4093)
- Fix radio station logos rendering as black or failing to load (by @OzGav in #4094)
- Phishin Change fallback album image URL (by @OzGav in #4097)
- AirPlay: fix mDNS cross-match when device name is substring of another device name (by @MarvinSchenkel in #4098)
- Fix None handling in music controller track/resume lookups (by @OzGav in #4102)
- Avoid event loop block in YouTube Music recommendations and skip SoundCloud default avatar (by @MarvinSchenkel in #4104)
- Only advertise extended ICY headers on flow stream when ICY metadata is requested (by @mcaulifn in #4105)
- Fix Apple Music library-only album artwork by caching blobstore URLs (by @dmoo500 in #4106)
- Added None guard (by @anatosun in #4107)
- Fix library-only tracks/albums showing as unavailable in shared playlists (by @dmoo500 in #4108)
- Fix transfer_queue losing position when source queue is paused/idle (by @OzGav in #4115)
- AirPlay: Ignore mDNS address updates that replace a routable IP with a Docker bridge address (by @MarvinSchenkel in #4117)
- Re-add configurable output buffer for AirPlay 1 (RAOP) players (by @MarvinSchenkel in #4118)
- Fix version parsing for titles with nested parentheses (by @OzGav in #4119)
- Audio analysis: re-scan stale-version tracks in background scan (by @chrisuthe in #4123)
- Don't enqueue next track onto a stopped queue (by @MarvinSchenkel in #4127)
- Bump `aiosendspin` to 6.0.2 to fix spec conformance issues (by @maximmaxim345 in #4128)
- Fix volume jump when crossfade intro and body normalize differently (by @MarvinSchenkel in #4129)
- Send Sendspin album artwork for radio and Spotify Connect streams (by @maximmaxim345 in #4130)
- Adjust Chromecast playback defaults (HTTP Profile 3 + flow mode) (by @MarvinSchenkel in #4133)
- Fix misleading smart-crossfade FFmpeg failure log message (by @MarvinSchenkel in #4139)
- Separate Phish.in artist tracks from top tracks (by @OzGav in #4140)
- Fix disappearing Sendspin Visualizer clients (by @maximmaxim345 in #4143)
- Align MusicBrainz throttler with mirror rate limit (by @MarvinSchenkel in #4146)
- Fix Sendspin not playing when grouping ESPHome devices (by @maximmaxim345 in #4147)
- end of queue results in track being reported as played twice (by @chrisuthe in #4150)
- Fix sendspin unmute (by @OzGav in #4151)
- Cap concurrent MusicBrainz ISRC lookups in Last.fm recommendations (by @OzGav in #4155)
- Fix cache cleanup missing most records and skip needless startup vacuum (by @MarvinSchenkel in #4156)
- Last.fm provider search bug fixes (by @OzGav in #4159)
- Fix 30s delay when grouping some Sendspin devices (by @maximmaxim345 in #4160)
- Prevent out-of-memory crash when compacting the library database (by @MarvinSchenkel in #4161)

### 🎨 Frontend Changes

- Show Smart Playlist provider in playlists provider filter (by @dmoo500 in [#1848](https://github.com/music-assistant/frontend/pull/1848))
- Fanart for top picks (by @stvncode in [#1854](https://github.com/music-assistant/frontend/pull/1854))
- Fix play button centering + banner behind tile (by @stvncode in [#1852](https://github.com/music-assistant/frontend/pull/1852))
- Prune stale provider ids from stored listing filters (by @OzGav in [#1727](https://github.com/music-assistant/frontend/pull/1727))
- Derive library membership from in_library flag (by @OzGav in [#1810](https://github.com/music-assistant/frontend/pull/1810))
- fix(theme): fix dark-mode rendering (by @teancom in [#1811](https://github.com/music-assistant/frontend/pull/1811))
- Show catalog providers in library provider filter (by @OzGav in [#1851](https://github.com/music-assistant/frontend/pull/1851))
- Fix album/playlist track order when played directly from a list (by @OzGav in [#1850](https://github.com/music-assistant/frontend/pull/1850))
- Lower smart playlist dedup_hours max to 2160h (90 days) (by @MarvinSchenkel in [#1861](https://github.com/music-assistant/frontend/pull/1861))
- Always show lights and visualisers in the group list (by @OzGav in [#1860](https://github.com/music-assistant/frontend/pull/1860))
- Add link to background analysis Concurrency Setting (by @chrisuthe in [#1830](https://github.com/music-assistant/frontend/pull/1830))
- Add back provider icon in discover pge + fix fanart (by @stvncode in [#1859](https://github.com/music-assistant/frontend/pull/1859))
- Add back provider icon in discover pge + fix fanart (by @stvncode in [#1859](https://github.com/music-assistant/frontend/pull/1859))
- Fix genre display in smart playlist rule picker (by @dmoo500 in [#1864](https://github.com/music-assistant/frontend/pull/1864))
- Put play button to the right for consistency (by @stvncode in [#1868](https://github.com/music-assistant/frontend/pull/1868))
- Hide/Show top picks and replace v-btn by shadcn one (by @stvncode in [#1867](https://github.com/music-assistant/frontend/pull/1867))
- Add album type filter to smart playlist rules (by @dmoo500 in [#1847](https://github.com/music-assistant/frontend/pull/1847))
- Fix server spam for fresh recommandation with debounce (by @stvncode in [#1869](https://github.com/music-assistant/frontend/pull/1869))
- Fix erroneous underline on Audio Analysis concurrency link (by @chrisuthe in [#1872](https://github.com/music-assistant/frontend/pull/1872))
- Only refetch recommendations on track end, not periodic progress (by @stvncode in [#1870](https://github.com/music-assistant/frontend/pull/1870))
- Lokalise: Translations update (by @marcelveldt in [#1875](https://github.com/music-assistant/frontend/pull/1875))
- Fix queue items disappearing in fullscreen player (by @MarvinSchenkel in [#1874](https://github.com/music-assistant/frontend/pull/1874))
- Single artist detail view with provider filter (by @marcelveldt in [#1829](https://github.com/music-assistant/frontend/pull/1829))
- Fix: Update overflow menu on shortcuts change and album tracks on navigation (by @dmoo500 in [#1892](https://github.com/music-assistant/frontend/pull/1892))
- Add refresh top picks + Fix two shorcut bugs (by @stvncode in [#1901](https://github.com/music-assistant/frontend/pull/1901))
- Store some settings per user (by @OzGav in [#1335](https://github.com/music-assistant/frontend/pull/1335))
- Lokalise: Translations update (by @marcelveldt in [#1904](https://github.com/music-assistant/frontend/pull/1904))

### 🧰 Maintenance and dependency bumps

<details>
<summary>37 changes</summary>

- Bump stages on 2.9 release (by @OzGav in #3942)
- Treat Retry-After as a floor for rate limits, not an exact target (by @rnewman in #4067)
- Some Typing fixes for Apple Music (by @OzGav in #4073)
- Final Typing fixes for Bluesound provider (by @OzGav in #4074)
- Add PGH003 mypy rule (by @OzGav in #4075)
- ⬆️ Update music-assistant-models to 1.1.129 (by @music-assistant-machine in #4076)
- ⬆️ Update music-assistant-frontend to 2.17.175 (by @music-assistant-machine in #4077)
- Further typing fixes for Apple Music (by @OzGav in #4078)
- Bump aiohttp from 3.13.5 to 3.14.0 (by @dependabot[bot] in #4079)
- Remove ignore from Bluesound player.py (by @OzGav in #4080)
- Type throttle_with_retries via Protocol instead of Provider bound (by @OzGav in #4081)
- Final typing fixes for Apple Music (by @OzGav in #4084)
- Some typing fixes for the YouTube Music provider (by @OzGav in #4087)
- Final typing fixes for YouTube Music (by @OzGav in #4090)
- Type-check plex and plex_connect providers, treat plexapi as untyped (by @OzGav in #4091)
- Typing fixes for the music controller - stage 1 (by @OzGav in #4092)
- ⬆️ Update music-assistant-frontend to 2.17.176 (by @music-assistant-machine in #4096)
- ⬆️ Update music-assistant-frontend to 2.17.177 (by @music-assistant-machine in #4100)
- Typing fixes for the music controller stage 2 (by @OzGav in #4101)
- Enable ruff UP043 and drop unnecessary default type arguments (by @OzGav in #4103)
- ⬆️ Update music-assistant-frontend to 2.17.178 (by @music-assistant-machine in #4111)
- ⬆️ Update music-assistant-frontend to 2.17.179 (by @music-assistant-machine in #4113)
- Final typing fixes for the Music controller (by @OzGav in #4114)
- Add translation_key to builtin playlists (by @OzGav in #4122)
- ⬆️ Update music-assistant-frontend to 2.17.180 (by @music-assistant-machine in #4125)
- Pin Sendspin Cast app id to the frozen `ma-2.9` channel (by @maximmaxim345 in #4131)
- ⬆️ Update music-assistant-frontend to 2.17.181 (by @music-assistant-machine in #4132)
- Bump pyblu from 2.0.7 to 2.0.8 (by @dependabot[bot] in #4134)
- Bump lyricsgenius from 3.11.0 to 3.12.2 (by @dependabot[bot] in #4136)
- ⬆️ Update music-assistant-frontend to 2.17.182 (by @music-assistant-machine in #4137)
- Add more translation keys (by @OzGav in #4138)
- ⬆️ Update music-assistant-frontend to 2.17.183 (by @music-assistant-machine in #4145)
- Use the standalone hue-entertainment library in the Hue Lights Sync plugin (by @marcelveldt in #4152)
- Fix guard_single_request type-var bound so media controllers don't need ignores (by @OzGav in #4153)
- ⬆️ Update music-assistant-frontend to 2.17.184 (by @music-assistant-machine in #4157)
- ⬆️ Update music-assistant-frontend to 2.17.185 (by @music-assistant-machine in #4162)
- ⬆️ Update music-assistant-frontend to 2.17.186 (by @music-assistant-machine in #4165)

</details>

## :bow: Thanks to our contributors

Special thanks to the following contributors who helped with this release:

@CodeCommander, @MarvinSchenkel, @OzGav, @anatosun, @chrisuthe, @dmoo500, @marcelveldt, @maximmaxim345, @mcaulifn, @rnewman, @sdhomecode, @stvncode, @teancom

## 2.9.0rc6
- Upstream Music Assistant server (beta) update to 2.9.0rc6

### Upstream Release Notes
## 📦 RC Release

_Changes since [2.9.0rc5](https://github.com/music-assistant/server/releases/tag/2.9.0rc5)_

### 🐛 Bugfixes

- Last.fm provider search bug fixes (by @OzGav in #4159)
- Fix 30s delay when grouping some Sendspin devices (by @maximmaxim345 in #4160)
- Prevent out-of-memory crash when compacting the library database (by @MarvinSchenkel in #4161)

### 🎨 Frontend Changes

- Store some settings per user (by @OzGav in [#1335](https://github.com/music-assistant/frontend/pull/1335))
- Fix heart icon spacing in list view and keep listing search visible (by @MarvinSchenkel in [#1903](https://github.com/music-assistant/frontend/pull/1903))

### 🧰 Maintenance and dependency bumps

- ⬆️ Update music-assistant-frontend to 2.17.185 (by @music-assistant-machine in #4162)

## :bow: Thanks to our contributors

Special thanks to the following contributors who helped with this release:

@MarvinSchenkel, @OzGav, @maximmaxim345

## 2.9.0rc4
- Upstream Music Assistant server (beta) update to 2.9.0rc4

### Upstream Release Notes
## 📦 RC Release

_Changes since [2.9.0rc3](https://github.com/music-assistant/server/releases/tag/2.9.0rc3)_

### 🚀 Features and enhancements

- Spread metadata maintenance schedule across the day (by @MarvinSchenkel in #4126)
- Add get_artist_toptracks to lastfm recommendations provider (by @OzGav in #4141)
- Enable WiiM and Last.fm Recommendations by default (by @MarvinSchenkel in #4142)
- Smart playlists: optional AI-generated descriptions (by @MarvinSchenkel in #4144)

### 🐛 Bugfixes

- Fix AcoustID scan coverage stalling (by @OzGav in #4070)
- Fix radio station logos rendering as black or failing to load (by @OzGav in #4094)
- AirPlay: Ignore mDNS address updates that replace a routable IP with a Docker bridge address (by @MarvinSchenkel in #4117)
- Send Sendspin album artwork for radio and Spotify Connect streams (by @maximmaxim345 in #4130)
- Fix misleading smart-crossfade FFmpeg failure log message (by @MarvinSchenkel in #4139)
- Separate Phish.in artist tracks from top tracks (by @OzGav in #4140)
- Fix disappearing Sendspin Visualizer clients (by @maximmaxim345 in #4143)
- Align MusicBrainz throttler with mirror rate limit (by @MarvinSchenkel in #4146)
- Fix Sendspin not playing when grouping ESPHome devices (by @maximmaxim345 in #4147)

### 🎨 Frontend Changes

- Fix: Update overflow menu on shortcuts change and album tracks on navigation (by @dmoo500 in [#1892](https://github.com/music-assistant/frontend/pull/1892))
- Lokalise translations update (by @[github-actions[bot]](https://github.com/apps/github-actions) in [#1894](https://github.com/music-assistant/frontend/pull/1894))
- Update `sendspin-js` to improve playback stability of radio streams for web players (by @maximmaxim345 in [#1899](https://github.com/music-assistant/frontend/pull/1899))
- Enhance the height of the context menu dialog (by @stvncode in [#1898](https://github.com/music-assistant/frontend/pull/1898))
- Improve listing empty states and declutter the action toolbar (by @marcelveldt in [#1897](https://github.com/music-assistant/frontend/pull/1897))
- Align heart icon in list view (by @stvncode in [#1896](https://github.com/music-assistant/frontend/pull/1896))
- Add more translations (by @OzGav in [#1895](https://github.com/music-assistant/frontend/pull/1895))

### 🧰 Maintenance and dependency bumps

- Add more translation keys (by @OzGav in #4138)
- ⬆️ Update music-assistant-frontend to 2.17.183 (by @music-assistant-machine in #4145)

## :bow: Thanks to our contributors

Special thanks to the following contributors who helped with this release:

@MarvinSchenkel, @OzGav, @dmoo500, @marcelveldt, @maximmaxim345, @stvncode

## 2.9.0rc3
- Upstream Music Assistant server (beta) update to 2.9.0rc3

### Upstream Release Notes
## 📦 RC Release

_Changes since [2.9.0rc2](https://github.com/music-assistant/server/releases/tag/2.9.0rc2)_

### 🚀 Features and enhancements

- Separate library artist views from per-provider artist listings (by @marcelveldt in #4039)
- Speed up YouTube Music recommendations loading (by @MarvinSchenkel in #4120)

### 🐛 Bugfixes

- Make universal player merge deterministic when link counts tie (by @sdhomecode in #4017)
- Fix YTMusic provider not retrying when PO Token server is slow to start (by @CodeCommander in #4093)
- Fix None handling in music controller track/resume lookups (by @OzGav in #4102)
- Avoid event loop block in YouTube Music recommendations and skip SoundCloud default avatar (by @MarvinSchenkel in #4104)
- Only advertise extended ICY headers on flow stream when ICY metadata is requested (by @mcaulifn in #4105)
- Fix Apple Music library-only album artwork by caching blobstore URLs (by @dmoo500 in #4106)
- Added None guard (by @anatosun in #4107)
- Fix library-only tracks/albums showing as unavailable in shared playlists (by @dmoo500 in #4108)
- Fix transfer_queue losing position when source queue is paused/idle (by @OzGav in #4115)
- Re-add configurable output buffer for AirPlay 1 (RAOP) players (by @MarvinSchenkel in #4118)
- Fix version parsing for titles with nested parentheses (by @OzGav in #4119)
- Audio analysis: re-scan stale-version tracks in background scan (by @chrisuthe in #4123)
- Don't enqueue next track onto a stopped queue (by @MarvinSchenkel in #4127)
- Bump `aiosendspin` to 6.0.2 to fix spec conformance issues (by @maximmaxim345 in #4128)
- Fix volume jump when crossfade intro and body normalize differently (by @MarvinSchenkel in #4129)
- Adjust Chromecast playback defaults (HTTP Profile 3 + flow mode) (by @MarvinSchenkel in #4133)

### 🎨 Frontend Changes

- Fix erroneous underline on Audio Analysis concurrency link (by @chrisuthe in [#1872](https://github.com/music-assistant/frontend/pull/1872))
- Only refetch recommendations on track end, not periodic progress (by @stvncode in [#1870](https://github.com/music-assistant/frontend/pull/1870))
- Remove animation when changing volume for group player (by @stvncode in [#1871](https://github.com/music-assistant/frontend/pull/1871))
- Fix background task copy (by @stvncode in [#1873](https://github.com/music-assistant/frontend/pull/1873))
- Lokalise: Translations update (by @marcelveldt in [#1875](https://github.com/music-assistant/frontend/pull/1875))
- Fix queue items disappearing in fullscreen player (by @MarvinSchenkel in [#1874](https://github.com/music-assistant/frontend/pull/1874))
- Add translation key for now playing badge (by @MarvinSchenkel in [#1889](https://github.com/music-assistant/frontend/pull/1889))
- Refactor heart icon and add it to the artist page (by @stvncode in [#1891](https://github.com/music-assistant/frontend/pull/1891))
- Add back subtitle for discover page (by @stvncode in [#1890](https://github.com/music-assistant/frontend/pull/1890))
- Bigger tiles on mobile (by @stvncode in [#1887](https://github.com/music-assistant/frontend/pull/1887))
- Fix self-sustaining WebRTC reconnect storm in remote transport (by @MarvinSchenkel in [#1888](https://github.com/music-assistant/frontend/pull/1888))
- Subtle placeholder for both dark and light mode (by @stvncode in [#1886](https://github.com/music-assistant/frontend/pull/1886))
- Add built-in playlists for favorites and random tracks (by @OzGav in [#1876](https://github.com/music-assistant/frontend/pull/1876))
- Single artist detail view with provider filter (by @marcelveldt in [#1829](https://github.com/music-assistant/frontend/pull/1829))
- Single artist detail view with provider filter (by @marcelveldt in [#1829](https://github.com/music-assistant/frontend/pull/1829))

### 🧰 Maintenance and dependency bumps

<details>
<summary>13 changes</summary>

- Bump stages on 2.9 release (by @OzGav in #3942)
- Typing fixes for the music controller stage 2 (by @OzGav in #4101)
- Enable ruff UP043 and drop unnecessary default type arguments (by @OzGav in #4103)
- ⬆️ Update music-assistant-frontend to 2.17.178 (by @music-assistant-machine in #4111)
- ⬆️ Update music-assistant-frontend to 2.17.179 (by @music-assistant-machine in #4113)
- Final typing fixes for the Music controller (by @OzGav in #4114)
- Add translation_key to builtin playlists (by @OzGav in #4122)
- ⬆️ Update music-assistant-frontend to 2.17.180 (by @music-assistant-machine in #4125)
- Pin Sendspin Cast app id to the frozen `ma-2.9` channel (by @maximmaxim345 in #4131)
- ⬆️ Update music-assistant-frontend to 2.17.181 (by @music-assistant-machine in #4132)
- Bump pyblu from 2.0.7 to 2.0.8 (by @dependabot[bot] in #4134)
- Bump lyricsgenius from 3.11.0 to 3.12.2 (by @dependabot[bot] in #4136)
- ⬆️ Update music-assistant-frontend to 2.17.182 (by @music-assistant-machine in #4137)

</details>

## :bow: Thanks to our contributors

Special thanks to the following contributors who helped with this release:

@CodeCommander, @MarvinSchenkel, @OzGav, @anatosun, @chrisuthe, @dmoo500, @marcelveldt, @maximmaxim345, @mcaulifn, @sdhomecode, @stvncode

## 2.9.0rc2
- Upstream Music Assistant server (beta) update to 2.9.0rc2

### Upstream Release Notes
## 📦 RC Release

_Changes since [2.9.0rc1](https://github.com/music-assistant/server/releases/tag/2.9.0rc1)_

### 🚀 Features and enhancements

- Add album_type filter to smart playlist rules (by @dmoo500 in #4059)
- Cache recommendations() for sonic_similarity and audiobookshelf (by @MarvinSchenkel in #4099)

### 🐛 Bugfixes

- Plex Connect: refactor and fixes plugin (by @anatosun in #3510)
- Fix smart playlist dedup for streaming (non-library) tracks (by @MarvinSchenkel in #4082)
- Fix genre icons disappearing after install path changes (by @MarvinSchenkel in #4083)
- Fix YouTube Music search() signature (by @OzGav in #4085)
- Fix WiiM volume_set by using HTTP command instead of UPnP (by @MarvinSchenkel in #4086)
- Reconcile smart playlist library entries on load to recover after DB reset (by @dmoo500 in #4088)
- Apple Music: stream library tracks and harden transient-error handling (by @teancom in #4089)
- Phishin Change fallback album image URL (by @OzGav in #4097)

### 🎨 Frontend Changes

- Lower smart playlist dedup_hours max to 2160h (90 days) (by @MarvinSchenkel in [#1861](https://github.com/music-assistant/frontend/pull/1861))
- Always show lights and visualisers in the group list (by @OzGav in [#1860](https://github.com/music-assistant/frontend/pull/1860))
- Add link to background analysis Concurrency Setting (by @chrisuthe in [#1830](https://github.com/music-assistant/frontend/pull/1830))
- Add back provider icon in discover pge + fix fanart (by @stvncode in [#1859](https://github.com/music-assistant/frontend/pull/1859))
- Add back provider icon in discover pge + fix fanart (by @stvncode in [#1859](https://github.com/music-assistant/frontend/pull/1859))
- Fix genre display in smart playlist rule picker (by @dmoo500 in [#1864](https://github.com/music-assistant/frontend/pull/1864))
- Put play button to the right for consistency (by @stvncode in [#1868](https://github.com/music-assistant/frontend/pull/1868))
- Hide/Show top picks and replace v-btn by shadcn one (by @stvncode in [#1867](https://github.com/music-assistant/frontend/pull/1867))
- Add album type filter to smart playlist rules (by @dmoo500 in [#1847](https://github.com/music-assistant/frontend/pull/1847))
- Fix server spam for fresh recommandation with debounce (by @stvncode in [#1869](https://github.com/music-assistant/frontend/pull/1869))

### 🧰 Maintenance and dependency bumps

<details>
<summary>12 changes</summary>

- Treat Retry-After as a floor for rate limits, not an exact target (by @rnewman in #4067)
- Further typing fixes for Apple Music (by @OzGav in #4078)
- Bump aiohttp from 3.13.5 to 3.14.0 (by @dependabot[bot] in #4079)
- Remove ignore from Bluesound player.py (by @OzGav in #4080)
- Type throttle_with_retries via Protocol instead of Provider bound (by @OzGav in #4081)
- Final typing fixes for Apple Music (by @OzGav in #4084)
- Some typing fixes for the YouTube Music provider (by @OzGav in #4087)
- Final typing fixes for YouTube Music (by @OzGav in #4090)
- Type-check plex and plex_connect providers, treat plexapi as untyped (by @OzGav in #4091)
- Typing fixes for the music controller - stage 1 (by @OzGav in #4092)
- ⬆️ Update music-assistant-frontend to 2.17.176 (by @music-assistant-machine in #4096)
- ⬆️ Update music-assistant-frontend to 2.17.177 (by @music-assistant-machine in #4100)

</details>

## :bow: Thanks to our contributors

Special thanks to the following contributors who helped with this release:

@MarvinSchenkel, @OzGav, @anatosun, @chrisuthe, @dmoo500, @rnewman, @stvncode, @teancom

## 2.9.0rc1
- Upstream Music Assistant server (beta) update to 2.9.0rc1

### Upstream Release Notes
## 📦 RC Release

_Changes since [2.9.0b16](https://github.com/music-assistant/server/releases/tag/2.9.0b16)_

### 🚀 Features and enhancements

- Add Bandcamp feed and wishlist recommendations (by @rnewman in #4047)
- Add Settings to allow Control of default similar_track action (by @chrisuthe in #4053)
- Support changing audiobook covers (by @OzGav in #4055)

### 🐛 Bugfixes

- Fix dynamic smart playlist cache leaking across users with different provider filters (by @dmoo500 in #4061)
- Phishin fixes and optimisations (by @OzGav in #4066)
- Fix Bluesound ungroup crashing on non-existent pyblu client attributes (by @OzGav in #4072)

### 🎨 Frontend Changes

- Fix: Mobile issues for discover page and bg for genre and placeholder (by @stvncode in [#1849](https://github.com/music-assistant/frontend/pull/1849))
- Fix: Mobile issues for discover page and bg for genre and placeholder (by @stvncode in [#1849](https://github.com/music-assistant/frontend/pull/1849))
- Show Smart Playlist provider in playlists provider filter (by @dmoo500 in [#1848](https://github.com/music-assistant/frontend/pull/1848))
- Fanart for top picks (by @stvncode in [#1854](https://github.com/music-assistant/frontend/pull/1854))
- Fix play button centering + banner behind tile (by @stvncode in [#1852](https://github.com/music-assistant/frontend/pull/1852))
- Prune stale provider ids from stored listing filters (by @OzGav in [#1727](https://github.com/music-assistant/frontend/pull/1727))
- Derive library membership from in_library flag (by @OzGav in [#1810](https://github.com/music-assistant/frontend/pull/1810))
- fix(theme): fix dark-mode rendering (by @teancom in [#1811](https://github.com/music-assistant/frontend/pull/1811))
- Show catalog providers in library provider filter (by @OzGav in [#1851](https://github.com/music-assistant/frontend/pull/1851))
- Fix album/playlist track order when played directly from a list (by @OzGav in [#1850](https://github.com/music-assistant/frontend/pull/1850))

### 🧰 Maintenance and dependency bumps

<details>
<summary>11 changes</summary>

- Bump usearch from 2.25.2 to 2.25.3 (by @dependabot[bot] in #4063)
- Bump bandcamp-async-api from 0.2.1 to 0.2.2 (by @dependabot[bot] in #4064)
- Bump soco from 0.31.0 to 0.31.1 (by @dependabot[bot] in #4065)
- Treat Retry-After as a floor for rate limits, not an exact target (by @rnewman in #4067)
- ⬆️ Update music-assistant-frontend to 2.17.174 (by @music-assistant-machine in #4069)
- Typing fixes for Bluesound provider.py (by @OzGav in #4071)
- Some Typing fixes for Apple Music (by @OzGav in #4073)
- Final Typing fixes for Bluesound provider (by @OzGav in #4074)
- Add PGH003 mypy rule (by @OzGav in #4075)
- ⬆️ Update music-assistant-models to 1.1.129 (by @music-assistant-machine in #4076)
- ⬆️ Update music-assistant-frontend to 2.17.175 (by @music-assistant-machine in #4077)

</details>

## :bow: Thanks to our contributors

Special thanks to the following contributors who helped with this release:

@OzGav, @chrisuthe, @dmoo500, @rnewman, @stvncode, @teancom

## 2.8.9
- Upstream Music Assistant server (beta) update to 2.8.9

### Upstream Release Notes
## 📦 Stable Release

_Changes since [2.8.8](https://github.com/music-assistant/server/releases/tag/2.8.8)_

### 🐛 Bugfixes

- Resolve universal_player wrappers in UGP stream handler (by @OzGav in #3952)
- Skip DSP-triggered playback restart when DSP was and remains disabled (by @MarvinSchenkel in #3988)
- Fix Deezer playback stalling on tracks with insufficient rights (error 2002) (by @MarvinSchenkel in #4048)
- Phishin fixes and optimisations (by @OzGav in #4066)
- Fix Bluesound ungroup crashing on non-existent pyblu client attributes (by @OzGav in #4072)

### 🧰 Maintenance and dependency bumps

- Revert "Resolve universal_player wrappers in UGP stream handler" (by @OzGav in #3956)

## :bow: Thanks to our contributors

Special thanks to the following contributors who helped with this release:

@MarvinSchenkel, @OzGav

## 2.9.0b16
- Upstream Music Assistant server (beta) update to 2.9.0b16

### Upstream Release Notes
## 📦 Beta Release

_Changes since [2.9.0b15](https://github.com/music-assistant/server/releases/tag/2.9.0b15)_

### 🚀 Features and enhancements

- fast MCP server: debug & config namespaces, external-source playback, OpenClaw/Hermes presets (v0.7.1) (by @trudenboy in #4019)
- Show real source format for piped AudioSource providers (by @marcelveldt in #4027)
- Implement the Sendspin `visualizer@v1` role and rework Hue Lights Sync (by @maximmaxim345 in #4042)
- Import album tracks when manually adding an album and Import Album Tracks setting enabled (by @OzGav in #4046)

### 🐛 Bugfixes

- Spotify Connect: clearer transport errors and automatic stall recovery (by @marcelveldt in #4010)
- Sonic Similarity: relax depends_on timing check + document smart_fades requirement (by @chrisuthe in #4016)
- Fix KeyError for CONF_SMART_FADES_MODE on protocol-type players (by @MarvinSchenkel in #4020)
- Fix queue cleared prematurely when radio follows tracks in flow stream (by @marcelveldt in #4021)
- AcoustID Skip processing if track has an ISRC (by @OzGav in #4022)
- Optimize size of provider icons (by @MarvinSchenkel in #4023)
- Fix smart playlist track evaluation from Discover and background queue context (by @dmoo500 in #4025)
- Fix Apple music library album tracks not showing up (by @dmoo500 in #4028)
- Fix Apple Music playlist add for catalog-backed library playlists (by @dmoo500 in #4032)
- Fix KeyError for CONF_SMART_FADES_MODE in streams controller get_value calls (by @MarvinSchenkel in #4033)
- Fix smart playlist GUID lookup when called with library IDs (by @dmoo500 in #4037)
- Add error handling for provider search (by @OzGav in #4044)
- Hide HTTP profile and ICY metadata config entries for Samsung WAM (by @Oliver-Stevens in #4045)
- Fix Deezer playback stalling on tracks with insufficient rights (error 2002) (by @MarvinSchenkel in #4048)
- Prevent duplicate songs in smart playlist dedup window (by @dmoo500 in #4052)
- Fix loudness volume jumps: scope audio-analysis reads to the authoritative provider (by @MarvinSchenkel in #4057)

### 🎨 Frontend Changes

- Fix smart playlist operator label after field switch (by @dmoo500 in [#1820](https://github.com/music-assistant/frontend/pull/1820))
- Smart Playlist: search UX & dynamic playlist provider details (by @MarvinSchenkel in [#1821](https://github.com/music-assistant/frontend/pull/1821))
- Remove padding for settings proivders on mobile (by @stvncode in [#1825](https://github.com/music-assistant/frontend/pull/1825))
- Fix some mobile issues for smart playlist mobile (by @stvncode in [#1824](https://github.com/music-assistant/frontend/pull/1824))
- Skip getSmartPlaylistRules call for non-smart playlists (by @dmoo500 in [#1822](https://github.com/music-assistant/frontend/pull/1822))
- Remove warning on dev (by @stvncode in [#1827](https://github.com/music-assistant/frontend/pull/1827))
- Match now-playing typography to new discover tiles (by @MarvinSchenkel in [#1846](https://github.com/music-assistant/frontend/pull/1846))
- Lokalise translations update (by @[github-actions[bot]](https://github.com/apps/github-actions) in [#1845](https://github.com/music-assistant/frontend/pull/1845))
- Add shortcut ordering actions (by @dmoo500 in [#1826](https://github.com/music-assistant/frontend/pull/1826))
- Remove redundant information from the Album overview page (by @MarvinSchenkel in [#1828](https://github.com/music-assistant/frontend/pull/1828))
- Discover refactor (by @stvncode in [#1842](https://github.com/music-assistant/frontend/pull/1842))
- Keep shortcuts in sync after delete and update events (by @dmoo500 in [#1819](https://github.com/music-assistant/frontend/pull/1819))
- Hide player in more places (by @OzGav in [#1711](https://github.com/music-assistant/frontend/pull/1711))

### 🧰 Maintenance and dependency bumps

<details>
<summary>13 changes</summary>

- Subsonic: Update py-opensonic library (by @khers in #4018)
- Drop redundant per-player throttler and harden the command lock (by @marcelveldt in #4024)
- ⬆️ Update music-assistant-models to 1.1.127 (by @music-assistant-machine in #4026)
- Bump zeroconf from 0.148.0 to 0.149.7 (by @dependabot[bot] in #4030)
- ⬆️ Update music-assistant-frontend to 2.17.169 (by @music-assistant-machine in #4031)
- Improve icons (by @OzGav in #4034)
- ⬆️ Update music-assistant-frontend to 2.17.170 (by @music-assistant-machine in #4035)
- ⬆️ Update music-assistant-models to 1.1.128 (by @music-assistant-machine in #4038)
- Bump aioaudiobookshelf to 0.1.21 (by @fmunkes in #4040)
- ⬆️ Update music-assistant-frontend to 2.17.171 (by @music-assistant-machine in #4049)
- Add checklist for documentation PR submissions (by @OzGav in #4051)
- ⬆️ Update music-assistant-frontend to 2.17.172 (by @music-assistant-machine in #4056)
- ⬆️ Update music-assistant-frontend to 2.17.173 (by @music-assistant-machine in #4060)

</details>

## :bow: Thanks to our contributors

Special thanks to the following contributors who helped with this release:

@MarvinSchenkel, @Oliver-Stevens, @OzGav, @chrisuthe, @dmoo500, @fmunkes, @khers, @marcelveldt, @maximmaxim345, @stvncode, @trudenboy

## 2.9.0b15
- Upstream Music Assistant server (beta) update to 2.9.0b15

### Upstream Release Notes
## 📦 Beta Release

_Changes since [2.9.0b14](https://github.com/music-assistant/server/releases/tag/2.9.0b14)_

### 🚀 New Providers

- Add Yandex Music Connect (Ynison) (by @trudenboy in #3856)
- Add Wikipedia provider and associated plumbing (by @OzGav in #3972)

### 🚀 Features and enhancements

- Use MB lookup to resolve ambiguous artist names (by @OzGav in #3862)
- Sonic Similarity Plugin (by @chrisuthe in #3943)
- Return a track sample for dynamic playlists when browsing (by @MarvinSchenkel in #4004)
- Emby Music Provider: add genres (by @hatharry in #4005)
- Smart Playlist: multi-seed support with album/playlist seeds (by @MarvinSchenkel in #4012)

### 🐛 Bugfixes

- Fix AirPlay receiver album artwork stuck after first track (by @MarvinSchenkel in #3945)
- Fix lyrics out-of-sync after smart crossfade (by @MarvinSchenkel in #3990)
- Yandex Music: bump to v3.5.14 — rate-limit mitigation, resilience hardening, security hygiene (by @trudenboy in #3996)
- Skip non-music providers in library update callback dispatch (by @dmoo500 in #3999)
- Fix Spotify Connect playback control reliability and error reporting (by @marcelveldt in #4001)
- Keep plugin playlist items visible for users with provider filters (by @dmoo500 in #4002)
- Improve Apple Music library album mapping and recommendation fallback (by @dmoo500 in #4006)
- fastMCP Server: sync 0.3.20→0.3.33 (security, fixes, tests) (by @trudenboy in #4007)
- Yandex Music: bump to v3.5.15 — captcha mitigation, faster recovery, datacenter safe-mode (by @trudenboy in #4011)
- fastMCP Server : sync 0.3.33→0.3.35 (synced state + group_volume) (by @trudenboy in #4013)

### 🎨 Frontend Changes

- Fix Smart Playlist seed picker dropping all results when only plugin providers supply SIMILAR_TRACKS (by @chrisuthe in [#1813](https://github.com/music-assistant/frontend/pull/1813))
- Fix config key default enqueue option radio (by @stvncode in [#1814](https://github.com/music-assistant/frontend/pull/1814))
- Add confirmation dialog for remove from library (by @stvncode in [#1812](https://github.com/music-assistant/frontend/pull/1812))
- Smart playlist: Let the user add multiple seeds (by @stvncode in [#1818](https://github.com/music-assistant/frontend/pull/1818))
- Refactor smart playlist (by @stvncode in [#1817](https://github.com/music-assistant/frontend/pull/1817))
- Update dynamic playlist overview (by @stvncode in [#1815](https://github.com/music-assistant/frontend/pull/1815))
- Update modal for add item from URL (by @stvncode in [#1816](https://github.com/music-assistant/frontend/pull/1816))

### 🧰 Maintenance and dependency bumps

<details>
<summary>5 changes</summary>

- Refactor Fully Kiosk to single-instance (by @OzGav in #3849)
- Update log messages (by @OzGav in #4000)
- Title-case the default genre aliases (by @OzGav in #4003)
- ⬆️ Update music-assistant-frontend to 2.17.167 (by @music-assistant-machine in #4008)
- ⬆️ Update music-assistant-frontend to 2.17.168 (by @music-assistant-machine in #4014)

</details>

## :bow: Thanks to our contributors

Special thanks to the following contributors who helped with this release:

@MarvinSchenkel, @OzGav, @chrisuthe, @dmoo500, @hatharry, @marcelveldt, @stvncode, @trudenboy

## 2.9.0b14
- Upstream Music Assistant server (beta) update to 2.9.0b14

### Upstream Release Notes
## 📦 Beta Release

_Changes since [2.9.0b13](https://github.com/music-assistant/server/releases/tag/2.9.0b13)_

### ⚠ Breaking Changes

- Refactor plugin sources to first-class AudioSource MediaItems (by @marcelveldt in #3938)

### 🚀 New Providers

- Smart playlist plugin (by @dmoo500 in #3630)
- Add MCP-spec-compliant FastMCP server provider v0.3.20 (by @trudenboy in #3858)
- Add Acoustid audio analysis provider (by @OzGav in #3892)

### 🚀 Features and enhancements

- Add support for legacy Shoutcast servers using ICY protocol (by @OzGav in #3386)
- audio_analysis: add coverage endpoint + bulk merged accessor for sonic_similarity (by @chrisuthe in #3851)
- Set PlayerQueue.is_dynamic when radio_source changes (by @dmoo500 in #3886)
- Add variable playback speed for audiobooks and podcasts (by @OzGav in #3939)
- Add stale-while-revalidate option to @use_cache (by @MarvinSchenkel in #3946)
- Stabilize group players: session-lifecycle instead of mandatory power (by @marcelveldt in #3947)
- Detect source audio format from ffmpeg log output (by @marcelveldt in #3950)
- Add Flow Mode sample-rate selection and per-player declared rates (by @marcelveldt in #3951)
- Improve imageproxy (by @marcelveldt in #3960)
- AudioSource follow-up (by @marcelveldt in #3964)
- Use passthrough PCM format for realtime AudioSource items (by @marcelveldt in #3969)
- Allow scrobble providers to filter by media_type (by @Tommatheussen in #3975)
- Allow Plugin Providers to implement ProviderFeature.SEARCH (by @MarvinSchenkel in #3978)

### 🐛 Bugfixes

- Fix genre movements when genres are promoted or deleted (by @OzGav in #3923)
- Squeezelite: Honor per-player output_codec in multi-client sync URL (by @MarvinSchenkel in #3924)
- Fix HEOS queue cleanup slowing down other commands (by @Tommatheussen in #3932)
- Fix browse and recommendations not applying user filters (by @MarvinSchenkel in #3934)
- Restore PlayerQueue.is_dynamic after loading queue from cache (by @dmoo500 in #3948)
- Resolve universal_player wrappers in UGP stream handler (by @OzGav in #3952)
- Fix stale Sonos cloud queue items and idle radio prebuffer (by @marcelveldt in #3957)
- Fix invalid imageproxy size on PlayerMedia URLs (by @marcelveldt in #3966)
- Prevent server crash on malformed player config entries (by @marcelveldt in #3967)
- Musiccast stability fixes (by @jhbruhn in #3977)
- Skip DSP-triggered playback restart when DSP was and remains disabled (by @MarvinSchenkel in #3988)
- Avoid KeyError when prefetching next-item palette for a player without a queue (by @marcelveldt in #3992)
- Disable linked protocol players when their parent is disabled (by @marcelveldt in #3993)
- Emby Music Provider: fix album art (by @hatharry in #3995)
- Scale background audio-analysis timeout to track duration (by @chrisuthe in #3997)

### 🎨 Frontend Changes

- Fix auto-refresh toggle on server logs page (by @OzGav in [#1784](https://github.com/music-assistant/frontend/pull/1784))
- Use server-derived color palette via `MediaItemPalette` (by @maximmaxim345 in [#1782](https://github.com/music-assistant/frontend/pull/1782))
- i18n: add 'inspired_by_recently_played' recommendations key (by @chrisuthe in [#1791](https://github.com/music-assistant/frontend/pull/1791))
- Add AudioSource media type for plugin sources (by @marcelveldt in [#1786](https://github.com/music-assistant/frontend/pull/1786))
- Fix copy to clipboard (by @OzGav in [#1742](https://github.com/music-assistant/frontend/pull/1742))
- Support new opaque-id imageproxy endpoint (by @marcelveldt in [#1792](https://github.com/music-assistant/frontend/pull/1792))
- Add "hide fully-played episodes" toggle to podcast details (by @teancom in [#1743](https://github.com/music-assistant/frontend/pull/1743))
- AudioSource follow-up: treat as in-queue infinite stream (by @marcelveldt in [#1793](https://github.com/music-assistant/frontend/pull/1793))
- Use PlayerQueue.is_dynamic directly (by @dmoo500 in [#1773](https://github.com/music-assistant/frontend/pull/1773))
- Add audio-analysis page with coverage information to system-> settings (by @chrisuthe in [#1783](https://github.com/music-assistant/frontend/pull/1783))
- Add sidebar shortcuts for playlists, artists, albums, tracks, radios, podcasts and audiobooks (by @dmoo500 in [#1780](https://github.com/music-assistant/frontend/pull/1780))
- Add support for variable playback speed (by @OzGav in [#1787](https://github.com/music-assistant/frontend/pull/1787))
- Hide group count badge on standalone players when not synced (by @KealanAU in [#1790](https://github.com/music-assistant/frontend/pull/1790))
- Reduce items-per-row at large screen widths (by @MarvinSchenkel in [#1806](https://github.com/music-assistant/frontend/pull/1806))
- Proposition for menu sections (by @stvncode in [#1808](https://github.com/music-assistant/frontend/pull/1808))
- Smart playlist UI (by @dmoo500 in [#1693](https://github.com/music-assistant/frontend/pull/1693))

### Other Changes

- Add PR template and auto-label from Types of changes checkbox (by @MarvinSchenkel in #3959)

### 🧰 Maintenance and dependency bumps

<details>
<summary>24 changes</summary>

- Add DTZ006 mypy rule (by @OzGav in #3525)
- Surface MusicBrainz artist URL relations as MediaItemLinks (by @OzGav in #3899)
- ⬆️ Update music-assistant-models to 1.1.120 (by @music-assistant-machine in #3937)
- ⬆️ Update music-assistant-frontend to 2.17.161 (by @music-assistant-machine in #3940)
- Bump docker/build-push-action from 7.1.0 to 7.2.0 (by @dependabot[bot] in #3941)
- ⬆️ Update music-assistant-models to 1.1.121 (by @music-assistant-machine in #3944)
- Add multiroom transition debug logs to WiiM provider (by @MarvinSchenkel in #3949)
- ⬆️ Update music-assistant-frontend to 2.17.162 (by @music-assistant-machine in #3954)
- Revert "Resolve universal_player wrappers in UGP stream handler" (by @OzGav in #3956)
- ⬆️ Update music-assistant-models to 1.1.122 (by @music-assistant-machine in #3958)
- ⬆️ Update music-assistant-models to 1.1.124 (by @music-assistant-machine in #3962)
- ⬆️ Update music-assistant-frontend to 2.17.163 (by @music-assistant-machine in #3963)
- Use Protocol-bounded TypeVar for @use_cache decorator (by @jdaberkow in #3965)
- ⬆️ Update music-assistant-frontend to 2.17.164 (by @music-assistant-machine in #3968)
- audiobookshelf: use from_utc_timestamp helper for ms-epoch conversions (by @OzGav in #3970)
- ⬆️ Update music-assistant-models to 1.1.125 (by @music-assistant-machine in #3973)
- Fix audio analysis documentation links (by @SuperSandro2000 in #3981)
- Bump docker/login-action from 4.1.0 to 4.2.0 (by @dependabot[bot] in #3982)
- Bump docker/setup-buildx-action from 4.0.0 to 4.1.0 (by @dependabot[bot] in #3983)
- Bump bandcamp-async-api from 0.1.1 to 0.2.1 (by @dependabot[bot] in #3984)
- Bump py-opensonic from 9.1.0 to 9.2.0 (by @dependabot[bot] in #3985)
- Bump pychromecast from 14.0.9 to 14.0.10 (by @dependabot[bot] in #3986)
- ⬆️ Update music-assistant-frontend to 2.17.165 (by @music-assistant-machine in #3987)
- ⬆️ Update music-assistant-frontend to 2.17.166 (by @music-assistant-machine in #3998)

</details>

## :bow: Thanks to our contributors

Special thanks to the following contributors who helped with this release:

@KealanAU, @MarvinSchenkel, @OzGav, @SuperSandro2000, @Tommatheussen, @chrisuthe, @dmoo500, @hatharry, @jdaberkow, @jhbruhn, @marcelveldt, @maximmaxim345, @stvncode, @teancom, @trudenboy

## 2.8.8
- Upstream Music Assistant server (beta) update to 2.8.8

### Upstream Release Notes
## 📦 Stable Release

_Changes since [2.8.7](https://github.com/music-assistant/server/releases/tag/2.8.7)_

### 🚀 Features and enhancements

- Support German radio station metadata (by @OzGav in #3881)

### 🐛 Bugfixes

- Fix protocol recovery with missing cached parent (by @prydie in #3829)
- Fix output bit depth ignoring supported sample-rate/bit-depth pairs in player settings (by @OzGav in #3842)
- Fix imageproxy URL encoding for paths containing only spaces (by @OzGav in #3863)
- Tolerate non-UTF-8 metadata in DLNA SOAP/NOTIFY responses (by @OzGav in #3864)
- Disable zone handling for a disabled player in MusicCast (by @fmunkes in #3872)
- Fix media progress retrieval for open sessions in Audiobookshelf (by @fmunkes in #3879)
- Fix Airplay not stopping stream on some devices. (by @MarvinSchenkel in #3903)
- Squeezelite: Honor per-player output_codec in multi-client sync URL (by @MarvinSchenkel in #3924)
- Sonos S1: Implement select_source for line-in support (by @MarvinSchenkel in #3925)
- Streams: Handle empty supported_sample_rates in get_output_format (by @MarvinSchenkel in #3926)
- Fix HEOS showing incorrect Now Playing (by @Tommatheussen in #3928)
- Close coroutines when submitted in rapid succession (by @MarvinSchenkel in #3929)
- Fix HEOS queue cleanup slowing down other commands (by @Tommatheussen in #3932)

## :bow: Thanks to our contributors

Special thanks to the following contributors who helped with this release:

@MarvinSchenkel, @OzGav, @Tommatheussen, @fmunkes, @prydie

## 2.9.0b13
- Upstream Music Assistant server (beta) update to 2.9.0b13

### Upstream Release Notes
## 📦 Beta Release

_Changes since [2.9.0b12](https://github.com/music-assistant/server/releases/tag/2.9.0b12)_

### 🐛 Bugfixes

- Remove initial_delay to fix duplicate lastfm recommendation rows (by @OzGav in #3920)
- Fix server crash on non-RGB cover art in palette extractor (by @OzGav in #3921)
- Sonos S1: Implement select_source for line-in support (by @MarvinSchenkel in #3925)
- Streams: Handle empty supported_sample_rates in get_output_format (by @MarvinSchenkel in #3926)
- Fix HEOS showing incorrect Now Playing (by @Tommatheussen in #3928)
- Close coroutines when submitted in rapid succession (by @MarvinSchenkel in #3929)
- Fix issues with M4B audiobooks (by @OzGav in #3930)

### 🎨 Frontend Changes

- Fix Audio Pipeline volume normalisation line (by @OzGav in [#1752](https://github.com/music-assistant/frontend/pull/1752))
- Fix genre casing (by @OzGav in [#1744](https://github.com/music-assistant/frontend/pull/1744))

### 🧰 Maintenance and dependency bumps

- Improve lastfm recommendations (by @OzGav in #3922)
- ⬆️ Update music-assistant-frontend to 2.17.160 (by @music-assistant-machine in #3927)

## :bow: Thanks to our contributors

Special thanks to the following contributors who helped with this release:

@MarvinSchenkel, @OzGav, @Tommatheussen

## 2.9.0b12
- Upstream Music Assistant server (beta) update to 2.9.0b12

### Upstream Release Notes
## 📦 Beta Release

_Changes since [2.9.0b11](https://github.com/music-assistant/server/releases/tag/2.9.0b11)_

### 🚀 New Providers

- Add Last.fm Recommendations metadata provider (by @OzGav in #3020)
- Add Samsung WAM player provider (by @Oliver-Stevens in #3334)
- Add Sonic Analysis audio-analysis provider (CLAP-driven scalars + embedding) (by @chrisuthe in #3795)

### 🚀 Features and enhancements

- Allow Plugin Providers and Metadata providers to implement music related ProviderFeatures (by @MarvinSchenkel in #3811)
- Fix double sendspin bridges for devices with both Airplay and Cast (by @MarvinSchenkel in #3854)
- Apple Music similar artists via views=similar-artists API (by @dmoo500 in #3861)
- Support German radio station metadata (by @OzGav in #3881)
- Improve Listenbrainz multi-artist track scrobbles (by @Tommatheussen in #3887)
- Improve UX of Sync groups (by @MarvinSchenkel in #3897)
- Subsonic: Provide close implementation that cleans up (by @khers in #3906)
- Implement the `color@v1` Sendspin role (by @maximmaxim345 in #3917)
- Fix WiiM external source reporting (by @MarvinSchenkel in #3918)

### 🐛 Bugfixes

- Yandex music: captcha-aware 429 handling, per-kind throttling, file-info cache (v3.5.4) (by @trudenboy in #3882)
- Preserve propagated artist / album genres across refreshes (by @OzGav in #3883)
- Apple Music: fix rotating IDs for recommendation folders and personal stations (by @dmoo500 in #3895)
- Fix Airplay not stopping stream on some devices. (by @MarvinSchenkel in #3903)
- Fix Hue sync bridge not being able to join to players with a sendspin bridge (by @MarvinSchenkel in #3904)
- Fix Apple Music library_add errors (by @dmoo500 in #3907)

### 🎨 Frontend Changes

- Enable asynchronous download in lokalise workflow (by @OzGav in [#1766](https://github.com/music-assistant/frontend/pull/1766))
- Lokalise: Translations update (by @marcelveldt in [#1769](https://github.com/music-assistant/frontend/pull/1769))
- Bump PWA precache limit to 5 MiB for larger translation bundle (by @OzGav in [#1772](https://github.com/music-assistant/frontend/pull/1772))
- A11Y - Improve spoken search clear button label (by @bartbunting in [#1777](https://github.com/music-assistant/frontend/pull/1777))
- Toggle homescreen edit mode label in user menu (by @dmoo500 in [#1768](https://github.com/music-assistant/frontend/pull/1768))
- Remove border-radius from sidebar header logo (by @remon1496 in [#1758](https://github.com/music-assistant/frontend/pull/1758))
- Add translation keys for Recommendations plugin provider (by @dmoo500 in [#1774](https://github.com/music-assistant/frontend/pull/1774))
- Add Bulgarian translation (by @OzGav in [#1771](https://github.com/music-assistant/frontend/pull/1771))
- Lokalise translations update (by @[github-actions[bot]](https://github.com/apps/github-actions) in [#1781](https://github.com/music-assistant/frontend/pull/1781))
- Show similar artists section on artist detail view (by @dmoo500 in [#1760](https://github.com/music-assistant/frontend/pull/1760))
- Show similar tracks section on TrackDetails view (by @dmoo500 in [#1776](https://github.com/music-assistant/frontend/pull/1776))
- Add Lyrics offset functionality (by @OzGav in [#1755](https://github.com/music-assistant/frontend/pull/1755))

### 🧰 Maintenance and dependency bumps

<details>
<summary>15 changes</summary>

- Bump plexapi from 4.17.2 to 4.18.1 (by @dependabot[bot] in #3598)
- Add DTZ005 mypy rule (by @OzGav in #3770)
- ⬆️ Update music-assistant-frontend to 2.17.156 (by @music-assistant-machine in #3884)
- ⬆️ Update music-assistant-models to 1.1.118 (by @music-assistant-machine in #3888)
- ⬆️ Update music-assistant-frontend to 2.17.157 (by @music-assistant-machine in #3889)
- Add WeChat QR login for QQ Music (by @xiasi0 in #3898)
- Fix support for `Literal` handling in OpenAPI generation (by @loopj in #3908)
- Bump snapcast from 2.3.7 to 2.3.8 (by @dependabot[bot] in #3909)
- Bump syrupy from 5.1.0 to 5.2.0 (by @dependabot[bot] in #3910)
- Bump codespell from 2.4.1 to 2.4.2 (by @dependabot[bot] in #3911)
- ⬆️ Update music-assistant-frontend to 2.17.158 (by @music-assistant-machine in #3912)
- Remove Sonos from mypy excludes (by @OzGav in #3914)
- Compute the artwork-derived color palette in the backend (by @maximmaxim345 in #3915)
- ⬆️ Update music-assistant-models to 1.1.119 (by @music-assistant-machine in #3916)
- ⬆️ Update music-assistant-frontend to 2.17.159 (by @music-assistant-machine in #3919)

</details>

## :bow: Thanks to our contributors

Special thanks to the following contributors who helped with this release:

@MarvinSchenkel, @Oliver-Stevens, @OzGav, @Tommatheussen, @bartbunting, @chrisuthe, @dmoo500, @khers, @loopj, @marcelveldt, @maximmaxim345, @remon1496, @trudenboy, @xiasi0

## 2.9.0b11
- Upstream Music Assistant server (beta) update to 2.9.0b11

### Upstream Release Notes
## 📦 Beta Release

_Changes since [2.9.0b10](https://github.com/music-assistant/server/releases/tag/2.9.0b10)_

### 🚀 Features and enhancements

- Add player filter to scrobble providers (by @Tommatheussen in #3823)
- Add manual IP addresses setting to the Sendspin provider (by @staticdev in #3846)
- Detect Sendspin Cast Receiver failures and show them in the frontend (by @maximmaxim345 in #3853)
- TuneIn: add translation_key to trending recommendations folder (by @dmoo500 in #3865)
- TuneIn: store image URLs as HTTPS instead of HTTP (by @dmoo500 in #3868)

### 🐛 Bugfixes

- Workaround for "Youtube Music playlist stalls on uploaded music" music-assistant/support#4469 (by @whitty in #3156)
- Fix protocol recovery with missing cached parent (by @prydie in #3829)
- Set NTS stations + mixtape images to square aspect (by @mike-sheppard in #3850)
- Fix imageproxy URL encoding for paths containing only spaces (by @OzGav in #3863)
- Tolerate non-UTF-8 metadata in DLNA SOAP/NOTIFY responses (by @OzGav in #3864)
- Fix event loop blocks when building the crossfade buffer (by @MarvinSchenkel in #3867)
- Emby Music Provider: scrobble tracks only (by @hatharry in #3871)
- Disable zone handling for a disabled player in MusicCast (by @fmunkes in #3872)
- Fix AA Background Processing to not Monopolize CPU (by @chrisuthe in #3873)
- Fix media progress retrieval for open sessions in Audiobookshelf (by @fmunkes in #3879)
- Fix silence after warmup buffer period (by @MarvinSchenkel in #3880)

### 🎨 Frontend Changes

- Add trending_stations translation key for TuneIn recommendations (by @dmoo500 in [#1765](https://github.com/music-assistant/frontend/pull/1765))

### 🧰 Maintenance and dependency bumps

<details>
<summary>4 changes</summary>

- Eliminate unused referencs to sync adjust.  (by @bradkeifer in #3852)
- Bump python-fullykiosk from 0.0.14 to 0.0.15 (by @dependabot[bot] in #3876)
- Bump mypy from 1.19.1 to 2.1.0 (by @dependabot[bot] in #3877)
- ⬆️ Update music-assistant-frontend to 2.17.155 (by @music-assistant-machine in #3878)

</details>

## :bow: Thanks to our contributors

Special thanks to the following contributors who helped with this release:

@MarvinSchenkel, @OzGav, @Tommatheussen, @bradkeifer, @chrisuthe, @dmoo500, @fmunkes, @hatharry, @maximmaxim345, @mike-sheppard, @prydie, @staticdev, @whitty

## 2.8.7
- Upstream Music Assistant server (beta) update to 2.8.7

### Upstream Release Notes
## 📦 Stable Release

_Changes since [2.8.6](https://github.com/music-assistant/server/releases/tag/2.8.6)_

### 🚀 Features and enhancements

- Emby Music Provider: add audio format to stream details (by @hatharry in #3796)

### 🐛 Bugfixes

- Workaround for "Youtube Music playlist stalls on uploaded music" music-assistant/support#4469 (by @whitty in #3156)
- Fix volume of Sendspin bridge players defaulting to 100% (by @maximmaxim345 in #3782)
- Suppress `StreamStoppedError` when skipping tracks with Sendspin (by @maximmaxim345 in #3783)
- Fix YTMusic stream format selection (by @greenmansuperhero in #3784)
- Update MASS_LOGO_ONLINE URL to raw GitHub link (by @h4de5 in #3797)
- Fix library sync deletion for non-streaming providers (by @OzGav in #3806)
- bbc_sounds: use LiveStation.id for station identifier (by @MacTheFork in #3807)
- YTMusic: Add auto mixes to recommendations. (by @MarvinSchenkel in #3816)
- Airplay: Add debounce to prevent-playback=1 commands (by @MarvinSchenkel in #3817)
- Fix Spotify playlists failing when track count is a multiple of 50 (by @gitviola in #3818)
- Snapcast: Adopt orphaned snapserver streams on name collision instead of misreporting as no-free-port (by @PeterPalenik in #3830)
- Fix output bit depth ignoring supported sample-rate/bit-depth pairs in player settings (by @OzGav in #3842)

### 🧰 Maintenance and dependency bumps

- Use /playlists/{id}/items endpoint (Spotify Feb 2026 API change) (by @Yipsh in #3436)
- Spotify: Update get_artist_albums limit, log error messages, guard methods (by @delatt in #3762)

## :bow: Thanks to our contributors

Special thanks to the following contributors who helped with this release:

@MacTheFork, @MarvinSchenkel, @OzGav, @PeterPalenik, @Yipsh, @delatt, @gitviola, @greenmansuperhero, @h4de5, @hatharry, @maximmaxim345, @whitty

## 2.9.0b10
- Upstream Music Assistant server (beta) update to 2.9.0b10

### Upstream Release Notes
## 📦 Beta Release

_Changes since [2.9.0b9](https://github.com/music-assistant/server/releases/tag/2.9.0b9)_

### 🚀 New Providers

- Add Yandex Music Connect (Ynison) plugin provider (by @trudenboy in #3614)
- Add NTS Radio (Music Provider) (by @mike-sheppard in #3722)

### 🚀 Features and enhancements

- kion_music: upgrade to yandex-music v3 - raw/enc FLAC, lyrics, similar artists, browse (by @trudenboy in #3234)
- Yandex Music: rotor session API, Wave Modes, user presets, library sync improvements (by @trudenboy in #3606)
- Update yandex_smarthome provider to v1.4.5 — auto-create skill flow (by @trudenboy in #3785)
- Enrich Sendspin metadata with track number, year, album artist, and artist artwork (by @OnFreund in #3788)
- Set PlayerFeature.SELECT_SOURCE when the FINAL source list is multi-entry (by @rnewman in #3789)
- Add custom playlist image functionality to local file provider (by @OzGav in #3794)
- Emby Music Provider: add audio format to stream details (by @hatharry in #3796)
- Emby Music Provider: add on played event handler (by @hatharry in #3805)
- Throttle torch to max 25% of CPU to prevent spikes during analysis (by @MarvinSchenkel in #3808)
- Add option to use local genre metadata only when available (by @OzGav in #3815)

### 🐛 Bugfixes

- Neteasecloudmusic: Stabilize login, recommendations, and dynamic radio playback (by @xiasi0 in #3761)
- Handle syncing for cases where session establishment is both early and late for adhering to required ntpstart value (by @bradkeifer in #3776)
- Fix volume of Sendspin bridge players defaulting to 100% (by @maximmaxim345 in #3782)
- Suppress `StreamStoppedError` when skipping tracks with Sendspin (by @maximmaxim345 in #3783)
- Fix YTMusic stream format selection (by @greenmansuperhero in #3784)
- Nicovideo: Fix watch history API endpoint (v1 → v2) (by @Shi-553 in #3791)
- Update MASS_LOGO_ONLINE URL to raw GitHub link (by @h4de5 in #3797)
- WiiM: Set the default max sample rate to 96kHz (by @teancom in #3798)
- Bump wiim SDK to 0.1.4 to fix track transition tracking (by @teancom in #3801)
- Fix library sync deletion for non-streaming providers (by @OzGav in #3806)
- bbc_sounds: use LiveStation.id for station identifier (by @MacTheFork in #3807)
- Decrease buffer warmup duration to 8s (by @MarvinSchenkel in #3814)
- YTMusic: Add auto mixes to recommendations. (by @MarvinSchenkel in #3816)
- Airplay: Add debounce to prevent-playback=1 commands (by @MarvinSchenkel in #3817)
- Fix Spotify playlists failing when track count is a multiple of 50 (by @gitviola in #3818)
- Fix queue restore: call from_cache to reconstruct radio_source and enqueued_media_items (by @dmoo500 in #3827)
- Snapcast: Adopt orphaned snapserver streams on name collision instead of misreporting as no-free-port (by @PeterPalenik in #3830)
- Fix sync issues with Sendspin players (by @maximmaxim345 in #3840)
- Fix Sendspin Cast bridge silently failing to set up (by @maximmaxim345 in #3841)
- Fix output bit depth ignoring supported sample-rate/bit-depth pairs in player settings (by @OzGav in #3842)
- Bump `aiosendspin` to 5.2.0 to fix slow desyncing at some player sample rates (by @maximmaxim345 in #3845)
- Allow AirPlay2 devices to be selected for synchronised playback (by @bradkeifer in #3847)

### Other Changes

- Stream PCM to audio analysis providers during background scan (by @chrisuthe in #3821)

### 🧰 Maintenance and dependency bumps

<details>
<summary>20 changes</summary>

- Spotify: Update get_artist_albums limit, log error messages, guard methods (by @delatt in #3762)
- Rename icon in audio analysis manifest.json (by @OzGav in #3781)
- Add comments to demo player provider for sound modes and player options (by @fmunkes in #3790)
- Add description for "Hide player in UI" setting (by @OzGav in #3792)
- Bump deno from 2.7.4 to 2.7.12 (by @dependabot[bot] in #3799)
- ⬆️ Update music-assistant-frontend to 2.17.153 (by @music-assistant-machine in #3802)
- Bump pytest from 9.0.2 to 9.0.3 (by @dependabot[bot] in #3803)
- Maintenance: sort provider dirs in gen_requirements_all for deterministic output (by @trudenboy in #3804)
- Refine description for 'Hide in UI' config entry (by @OzGav in #3809)
- ⬆️ Update music-assistant-models to 1.1.116 (by @music-assistant-machine in #3810)
- ⬆️ Update music-assistant-frontend to 2.17.154 (by @music-assistant-machine in #3812)
- Bump actions/download-artifact from 4 to 8 (by @dependabot[bot] in #3819)
- Bump actions/upload-artifact from 4 to 7 (by @dependabot[bot] in #3820)
- Revert "Remaintain jellyfin (#3528)" (by @staticdev in #3822)
- VBAN Receiver update (by @sprocket-9 in #3825)
- Radio Paradise small cleanup (by @teancom in #3826)
- Change Snapcast stage from stable to unmaintained (by @OzGav in #3835)
- Enhance warning for Spotify top tracks fetch failure (by @OzGav in #3837)
- Bump soco from 0.30.14 to 0.31.0 (by @dependabot[bot] in #3838)
- ⬆️ Update music-assistant-models to 1.1.117 (by @music-assistant-machine in #3839)

</details>

## :bow: Thanks to our contributors

Special thanks to the following contributors who helped with this release:

@MacTheFork, @MarvinSchenkel, @OnFreund, @OzGav, @PeterPalenik, @Shi-553, @bradkeifer, @chrisuthe, @delatt, @dmoo500, @fmunkes, @gitviola, @greenmansuperhero, @h4de5, @hatharry, @maximmaxim345, @mike-sheppard, @rnewman, @sprocket-9, @staticdev, @teancom, @trudenboy, @xiasi0

## 2.9.0b9
- Upstream Music Assistant server update to 2.9.0b9

### Upstream Release Notes
## 📦 Beta Release

_Changes since [2.9.0b8](https://github.com/music-assistant/server/releases/tag/2.9.0b8)_

### 🚀 Features and enhancements

- Improve TuneIn browse, search and add recommendations (by @dmoo500 in #3764)
- Add recommendation translation keys for QQ and NetEase (by @xiasi0 in #3778)
- Revert "AirPlay 2 provider now supports sync" (by @MarvinSchenkel in #3780)

### 🐛 Bugfixes

- Force imageproxy over streamserver for Airplay artwork (by @MarvinSchenkel in #3763)
- Fix tidal recommendations (by @jozefKruszynski in #3767)
- Change heartbeat of websocket and sendspin proxy socket to 25s (by @MarvinSchenkel in #3769)
- Fix 30s delay after switching tracks on Sendspin (by @maximmaxim345 in #3777)

### 🎨 Frontend Changes

- Remove size restriction for volume slider + refacto old ui for player controls (by @stvncode in [#1726](https://github.com/music-assistant/frontend/pull/1726))

### 🧰 Maintenance and dependency bumps

<details>
<summary>5 changes</summary>

- Bump ya-passport-auth to 1.3.0 for Yandex Smart Home provider (by @trudenboy in #3746)
- Consolidate tidal constants for urls and paths (by @jozefKruszynski in #3768)
- Resolve TODOs in metadata controller (by @OzGav in #3771)
- Remove code in the config controller commented for removal post the 2.8 release  (by @OzGav in #3772)
- ⬆️ Update music-assistant-frontend to 2.17.152 (by @music-assistant-machine in #3775)

</details>

## :bow: Thanks to our contributors

Special thanks to the following contributors who helped with this release:

@MarvinSchenkel, @OzGav, @dmoo500, @jozefKruszynski, @maximmaxim345, @stvncode, @trudenboy, @xiasi0

## 2.8.6
- Upstream Music Assistant server update to 2.8.6

### Upstream Release Notes
## 📦 Stable Release

_Changes since [2.8.5](https://github.com/music-assistant/server/releases/tag/2.8.5)_

### 🐛 Bugfixes

- Fix ffmpeg process leak in smart fades mixer on aborted playback (by @marcelveldt in #3725)
- Harden AirPlay STOP command delivery and add teardown logging (by @marcelveldt in #3729)
- Prevent concurrent flow-stream producers from corrupting the playlog (by @marcelveldt in #3731)
- Guard Sonos volume attribute update against uninitialized state (by @marcelveldt in #3732)
- Fix ORF Radiothek browse reverting to top level (by @OzGav in #3733)
- Preserve multi-value album type across all tag parsers (by @OzGav in #3743)
- [Soundcloud]: improving search (by @fionn-r in #3745)
- Fix enqueue action 'replace' stopping the music (by @MarvinSchenkel in #3753)
- Qobuz: fix credential leak on 401 and populate date_added (by @OzGav in #3754)
- Implement power control function for squeezelite (by @MarvinSchenkel in #3755)
- Fix manual genres disappearing after a cleanup run (by @MarvinSchenkel in #3757)
- Force imageproxy over streamserver for Airplay artwork (by @MarvinSchenkel in #3763)
- Fix tidal recommendations (by @jozefKruszynski in #3767)
- Change heartbeat of websocket and sendspin proxy socket to 25s (by @MarvinSchenkel in #3769)
- Fix 30s delay after switching tracks on Sendspin (by @maximmaxim345 in #3777)

### 🧰 Maintenance and dependency bumps

- Bump auntie-sounds to 1.1.8 (by @kieranhogg in #3723)

## :bow: Thanks to our contributors

Special thanks to the following contributors who helped with this release:

@MarvinSchenkel, @OzGav, @fionn-r, @jozefKruszynski, @kieranhogg, @marcelveldt, @maximmaxim345

## 2.8.5
- Upstream Music Assistant server update to 2.8.5

### Upstream Release Notes
## 📦 Stable Release

_Changes since [2.8.4](https://github.com/music-assistant/server/releases/tag/2.8.4)_

### 🚀 Features and enhancements

- Apple Music: Add Unicode NFC normalization for artist/album/track names (by @jasonhollis in #2631)
- Apple Music: Add content rating check for explicit tracks (by @LosCV29 in #3514)
- Apple Music: Add content rating check for explicit tracks (by @LosCV29 in #3669)

### 🐛 Bugfixes

- Fix AirPlay DACP volume control for Sonos speakers (by @marcelveldt in #3654)
- Fix queue items showing zero/unknown duration (by @marcelveldt in #3668)
- Tweak imageproxy (by @MarvinSchenkel in #3671)
- Several fixes for synced playback stability (by @marcelveldt in #3672)
- Filter stale podcast episodes (by @OzGav in #3673)
- Sendspin: guard against negative track_progress in metadata (by @marcelveldt in #3681)
- Fix sync group session lifecycle and AirPlay late joiner sync (by @marcelveldt in #3682)
- Automatically clean up loudness measurements on media item deletion (by @MarvinSchenkel in #3687)
- Fix multiple (virtual) devices on the same host being merged. (by @MarvinSchenkel in #3688)
- Fix sync group dissolve+reform race with async providers (by @marcelveldt in #3691)
- Fix Jellyfin multidisc albums with same named tracks (by @MarvinSchenkel in #3692)
- Fix Volume control for Bluesound native devices (by @MarvinSchenkel in #3693)
- Fix race condition in AirPlay stream session client removal (by @marcelveldt in #3698)
- Improve loudness measurement robustness (by @marcelveldt in #3703)
- Fix smart fades mixer sometimes choking up the flow stream + Smart Fades provider not starting on ARM (by @MarvinSchenkel in #3706)
- Bump aiohttp to 3.13.5 and ibroadcastaio to 0.6.0 (by @staticdev in #3707)
- Fix syncgroup state derivation and tighten lifecycle handling (by @marcelveldt in #3709)
- Fix duration parsing for M3U playlist items (by @marcelveldt in #3714)
- Fix AirPlay cleanup idling re-added clients (by @marcelveldt in #3716)
- Fix sync leader child state forwarding (by @marcelveldt in #3717)
- Forward syncgroup join/unjoin to the syncgroup player (by @marcelveldt in #3718)
- Fix audiobook controller not using userid in library_items call (by @fmunkes in #3719)

### 🧰 Maintenance and dependency bumps

<details>
<summary>4 changes</summary>

- [Backport to stable] 2.8.2 (by @marcelveldt in #3564)
- Add diagnostics for AirPlay stream stalls and increase flow buffer (by @marcelveldt in #3696)
- Remove temporary airplay diagnostics (by @marcelveldt in #3720)
- Fix power control for squeezelite (by @marcelveldt in #3721)

</details>

## :bow: Thanks to our contributors

Special thanks to the following contributors who helped with this release:

@LosCV29, @MarvinSchenkel, @OzGav, @fmunkes, @jasonhollis, @marcelveldt, @staticdev

## 2.8.4
- Upstream Music Assistant server update to 2.8.4

### Upstream Release Notes
## 📦 Stable Release

_Changes since [2.8.3](https://github.com/music-assistant/server/releases/tag/2.8.3)_

### Other Changes

- [Backport to stable] 2.8.4 (by @github-actions[bot] in #3634)


## 2.8.3
- Upstream Music Assistant server update to 2.8.3

### Upstream Release Notes
## 📦 Stable Release

_Changes since [2.8.2](https://github.com/music-assistant/server/releases/tag/2.8.2)_

### 🐛 Bugfixes

- Rewrite tidal stream behaviour to avoid premature cutoff (by @jozefKruszynski in #3369)
- YT Music: Fix syncing 'Episodes for later' in podcast library sync (by @teancom in #3582)
- Fix flow stream playlog pre-count and use 50/50 crossfade split (by @marcelveldt in #3587)
- Fix sync group player desynchronization and add dynamic leader switching (by @marcelveldt in #3591)
- Revert "Rewrite tidal stream behaviour to avoid premature cutoff (#3369)" (by @jozefKruszynski in #3593)
- Fix sync group regressions: proper locking and dynamic leader switch (by @marcelveldt in #3594)
- Include missing description in automatic artist metadata scan (by @OzGav in #3595)
- Add protocol awareness and transition guards to sync group player (by @marcelveldt in #3600)
- Fix party duplicate prevention race (by @marcelveldt in #3601)
- Subsonic: Fix structured lyrics yet again (by @khers in #3604)
- Fix player/queue deadlock on multiple simultane (play) actions (by @marcelveldt in #3624)
- Fix AirPlay late joiner out-of-sync when joining a sync group (by @marcelveldt in #3625)
- Fix flow mode queue tracking drift on AirPlay dynamic leader switch (by @marcelveldt in #3628)

### 🧰 Maintenance and dependency bumps

- Consolidate smart fades analyzer thread calls to fix asyncio slow-task warning (by @marcelveldt in #3588)

## :bow: Thanks to our contributors

Special thanks to the following contributors who helped with this release:

@OzGav, @jozefKruszynski, @khers, @marcelveldt, @teancom

## 2.8.2
- Upstream Music Assistant server update to 2.8.2

### Upstream Release Notes
## 📦 Stable Release

_Changes since [2.8.1](https://github.com/music-assistant/server/releases/tag/2.8.1)_

### 🚀 New Providers

- Add Coverart Archive metadata provider (by @OzGav in #3523)

### 🚀 Features and enhancements

- Allow use of a personal client id for Spotify (by @marcelveldt in #1536)
- Try parsing track number from the filename (by @marcelveldt in #1663)
- A few small bugfixes and enhancements to playback and enqueuing  (by @marcelveldt in #1670)
- Fix IPv6 support across core and providers (by @fmurodov in #3235)
- Support playback of radio station PLS playlist URLs with query parameters (by @OzGav in #3419)
- Open Subsonic Lyric support (by @khers in #3424)
- Add optional timestamp to get_resume_position (by @fmunkes in #3505)
- Add Socks proxy option for Pandora (by @TermeHansen in #3513)
- Dynamic playlist queue support for is_dynamic playlists (by @dmoo500 in #3527)
- Fix group volume balance drift with interpolation-based scaling (by @marcelveldt in #3548)
- Add config for show progress bar in party mode (by @Awashcard0 in #3549)
- Add Canada in UI for Alexa provider (by @EricLabranche in #3568)
- Add duplicate track prevention and empty default for party name/QR text (by @apophisnow in #3576)

### 🐛 Bugfixes

- Apple Music: Various fixes (by @MarvinSchenkel in #1652)
- Fix cast/dlna player stops playing after 1 or 2 tracks of a playlist (by @marcelveldt in #1658)
- Bluesound: fixed deprecated enqueue next issue, announcements removed (by @Cyanogenbot in #1659)
- Create new session so Pandora fetches fresh tracks (by @OzGav in #3493)
- Fix podcasts from filesystem source not appearing in library (by @teancom in #3494)
- Fix Bandcamp provider not having pagination (by @teancom in #3496)
- Fix output format reporting for protocol and sendspin players (by @marcelveldt in #3498)
- Fix player controls configuration (by @marcelveldt in #3503)
- Improve audio buffering in streams controller (by @marcelveldt in #3507)
- Improve Qobuz API rate limiting, backoff, and sync efficiency (by @teancom in #3515)
- Fix jellyfin get_artist_albums always returning empty list (by @TastyPi in #3521)
- Several small bugfixes and stability enhancements related to streaming (by @marcelveldt in #3522)
- Fix Sonos not unmuting when playing via Airplay (by @MarvinSchenkel in #3529)
- Bump aioslimproto to 3.1.8. (by @MarvinSchenkel in #3530)
- Subsonic: Include bookmark creation date if available (by @khers in #3531)
- Fix player controls for non-native players (by @marcelveldt in #3532)
- Fix: select_source should ungroup a player if its grouped/synced (by @marcelveldt in #3534)
- Guard against non-UTF-8 filenames in file system providers (by @OzGav in #3539)
- Fix syncgroup ungroup command silently ignored due to stale state (by @marcelveldt in #3540)
- Fix AirPlay mDNS discovery race between RAOP and AirPlay services (by @marcelveldt in #3546)
- Fix AirPlay Sendspin bridge audio sync and re-enable AirPlay2 (by @marcelveldt in #3547)
- Fix filesystem provider sync config checkboxes not being respected (by @teancom in #3550)
- Fix plugin source volume feedback loop with group players (by @marcelveldt in #3556)
- Fix player queue stuck on play_action_in_progress (by @marcelveldt in #3557)
- Subsonic: Bump py-opensonic for lyrics fix (by @khers in #3559)
- A few fixes for audio streaming (by @marcelveldt in #3560)
- Plex: fix streaming of newly added Plex tracks (by @anatosun in #3561)
- Fix Universal Group Player playback issues (by @marcelveldt in #3562)
- Fix high CPU usage during audio streaming on low-power devices (by @marcelveldt in #3567)
- Fix external source reporting on Universal Players (by @marcelveldt in #3571)
- Fix sync group player features not available when idle (by @marcelveldt in #3572)
- Fix scheduled sync task settings not persisting across restarts (by @marcelveldt in #3574)
- Fix plugin source players stuck in PLAYING state after disconnect (by @marcelveldt in #3579)
- Fix AirPlay late-join timing and remove oversized pipe buffers (by @marcelveldt in #3581)
- Fix AirPlay late-join sync: start_at must match first byte stream position (by @marcelveldt in #3583)
- Restore flow stream buffering for smart fades headroom (by @marcelveldt in #3584)
- Fix flow stream UI showing next track too early during crossfade (by @marcelveldt in #3586)

### 🎨 Frontend Changes

- Accept frameless query param without requiring a value (by @apophisnow in [#1650](https://github.com/music-assistant/frontend/pull/1650))
- Fix Party dashboard QR color and track sizing (by @apophisnow in [#1649](https://github.com/music-assistant/frontend/pull/1649))
- Add import playlist feature (by @chrisuthe in [#1662](https://github.com/music-assistant/frontend/pull/1662))
- Add progress bar for current track in party mode (by @Awashcard0 in [#1664](https://github.com/music-assistant/frontend/pull/1664))
- Disable shuffle and repeat buttons for dynamic playlists (by @dmoo500 in [#1667](https://github.com/music-assistant/frontend/pull/1667))
- Add favorite button to player bar (by @dmoo500 in [#1666](https://github.com/music-assistant/frontend/pull/1666))
- Player menu enhancements (by @radiohe4d in [#1536](https://github.com/music-assistant/frontend/pull/1536))
- Add translation strings for player options (by @fmunkes in [#1663](https://github.com/music-assistant/frontend/pull/1663))
- Add track action menu to player bar (by @dmoo500 in [#1669](https://github.com/music-assistant/frontend/pull/1669))
- Party duplicate prevention (by @apophisnow in [#1670](https://github.com/music-assistant/frontend/pull/1670))
- Party duplicate prevention (by @apophisnow in [#1670](https://github.com/music-assistant/frontend/pull/1670))

### Other Changes

- Fix: Handle radio stations providing non utf-8 in streamtitle (by @marcelveldt in #1664)
- Adding missing icon for the Soundcloud music provider (by @robsonke in #1665)
- Fix loading state from cache when connecting to slimproto players (by @kepstin in #1666)

### 🧰 Maintenance and dependency bumps

<details>
<summary>34 changes</summary>

- Split up build workflow to use intermediate base image (by @marcelveldt in #1647)
- Bump zeroconf from 0.133.0 to 0.134.0 (by @dependabot[bot] in #1656)
- Bump ruff from 0.6.4 to 0.6.5 (by @dependabot[bot] in #1667)
- Bump pyblu from 0.4.0 to 1.0.2 (by @dependabot[bot] in #1669)
- Bump lyricsgenius from 3.7.5 to 3.11.0 (by @dependabot[bot] in #3405)
- Bump ruff from 0.14.13 to 0.15.6 (by @dependabot[bot] in #3406)
- Add support for dynamic playlists to the Queue controller (by @dmoo500 in #3432)
- AirPlay improvements for pre-4K devices and interface resolution in Docker (by @dmoo500 in #3434)
- Rename music provider to source (by @OzGav in #3480)
- Add pkce to spotify_connect (by @SuperSandro2000 in #3485)
- ⬆️ Update music-assistant-frontend to 2.17.135 (by @music-assistant-machine in #3500)
- Bump cryptography from 46.0.5 to 46.0.6 (by @dependabot[bot] in #3501)
- ⬆️ Update music-assistant-models to 1.1.109 (by @music-assistant-machine in #3502)
- ⬆️ Update music-assistant-frontend to 2.17.136 (by @music-assistant-machine in #3504)
- ⬆️ Update music-assistant-frontend to 2.17.137 (by @music-assistant-machine in #3517)
- ⬆️ Update music-assistant-models to 1.1.110 (by @music-assistant-machine in #3519)
- Add PTH119 and PTH116 mypy rules (by @OzGav in #3526)
- Remaintain jellyfin (by @staticdev in #3528)
- Bump aiohttp from 3.13.3 to 3.13.4 (by @dependabot[bot] in #3533)
- fix(alexa): Fix issue with language on alexa skills for french and english canada (by @EricLabranche in #3535)
- ⬆️ Update music-assistant-frontend to 2.17.139 (by @music-assistant-machine in #3536)
- Standardise icons for remote filesystem providers (by @OzGav in #3537)
- Replace blind asyncio.sleep calls with event-based state waiting (by @marcelveldt in #3541)
- Fix cache controller to enforce consistent JSON serialization (by @marcelveldt in #3542)
- Stream smart fades FFmpeg output instead of buffering (by @marcelveldt in #3543)
- Bump hass client to 1.2.3. (by @MarvinSchenkel in #3544)
- Bump docker/login-action from 4.0.0 to 4.1.0 (by @dependabot[bot] in #3545)
- Copy queue items list before mutation in delete_item for consistency (by @teancom in #3551)
- Bandcamp: fix Liskov substitution violation in get_artist signature (by @teancom in #3552)
- ⬆️ Update music-assistant-frontend to 2.17.140 (by @music-assistant-machine in #3553)
- Clean up leaked throttlers, command locks, and protocol evaluations on player unregister (by @teancom in #3554)
- Add MusicCast player options translation keys (by @fmunkes in #3558)
- ⬆️ Update music-assistant-frontend to 2.17.141 (by @music-assistant-machine in #3565)
- ⬆️ Update music-assistant-frontend to 2.17.142 (by @music-assistant-machine in #3578)

</details>

## :bow: Thanks to our contributors

Special thanks to the following contributors who helped with this release:

@Awashcard0, @Cyanogenbot, @EricLabranche, @MarvinSchenkel, @OzGav, @SuperSandro2000, @TastyPi, @TermeHansen, @anatosun, @apophisnow, @chrisuthe, @dmoo500, @fmunkes, @fmurodov, @kepstin, @khers, @marcelveldt, @radiohe4d, @robsonke, @staticdev, @teancom

## 2.8.1-patch.f02c3bf
- Better playback, format selection, retry logic

## 2.8.1-patch.47be7c5
- Upstream pipeline fix

## 2.8.1
- Upstream Music Assistant server update to 2.8.1

### Upstream Release Notes
## 📦 Stable Release

_Changes since [2.8.0](https://github.com/music-assistant/server/releases/tag/2.8.0)_

### 🐛 Bugfixes

- Fix race condition when calling stop/pause on an already stopped Universal Player (by @MarvinSchenkel in #3481)
- Emby Music Provider: fix artist endpoint, image remote accessibility and album artwork (by @hatharry in #3482)
- Fix plex SSL warning polluting the log (by @MarvinSchenkel in #3486)
- Fix filesystem playlists not showing up in the library (by @MarvinSchenkel in #3487)
- Fix not being able to edit Apple Music playlist tracks (by @MarvinSchenkel in #3488)
- Fix tracks from Sonos not being reported as played (by @MarvinSchenkel in #3489)
- Fix dlna not playing on some devices (by @MarvinSchenkel in #3490)

### 🎨 Frontend Changes

- Fix widget rows reloading when toggling the player bar (by @MarvinSchenkel in [#1646](https://github.com/music-assistant/frontend/pull/1646))

### 🧰 Maintenance and dependency bumps

- ⬆️ Update music-assistant-frontend to 2.17.134 (by @music-assistant-machine in #3491)

## :bow: Thanks to our contributors

Special thanks to the following contributors who helped with this release:

@MarvinSchenkel, @hatharry

## 2.8.0-patch.ecf1b23
- Fix workflow for upstream updates, add changelog

## 2.8.0
- Upstream Music Assistant server update to 2.8.0
