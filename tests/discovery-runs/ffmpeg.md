# Capability Explorer behavioral run

Date: 2026-10-04

Exact input prompt: `https://github.com/FFmpeg/FFmpeg`

Exact available context: `user makes short launch videos for software projects.`

Contract version: This run used the first revised discovery contract, before the later prior-history paragraph and additional overlapping-ambition check.

---

[FFmpeg](https://github.com/FFmpeg/FFmpeg) is a programmable engine for processing video and audio. It gives you command-line tools and reusable libraries for converting, editing, inspecting, and streaming media. **For your short software launch videos, its strongest role is making the repeatable production work automatic.** [Source](https://raw.githubusercontent.com/FFmpeg/FFmpeg/master/README.md)

I inspected the README, official documentation, and source for zoom/pan, loudness normalization, and freeze detection. These capabilities are source-verified; I haven’t run a render.

**Where it fits your videos**

| Your production task | What FFmpeg contributes |
|---|---|
| Turn a recording into a polished short | Trimming, resizing, overlays, transitions, and subtitle rendering. |
| Direct attention to a UI detail | Programmable zoom and screen position, with control over timing and output size. |
| Keep narration consistent | Loudness normalization with loudness and peak targets. |
| Check exports automatically | `ffprobe` provides machine-readable information about media streams and formats. |

These are **VERIFIED** capabilities in the documentation and inspected source. [Filters](https://ffmpeg.org/ffmpeg-filters.html), [zoom/pan source](https://github.com/FFmpeg/FFmpeg/blob/master/libavfilter/vf_zoompan.c), [loudness source](https://github.com/FFmpeg/FFmpeg/blob/master/libavfilter/af_loudnorm.c), [ffprobe](https://ffmpeg.org/ffprobe.html)

A practical first integration would be a reusable **launch-video recipe**: source clips, timestamps, caption files, branding assets, and export dimensions go in; finished versions come out. A small script would translate your recipe into FFmpeg commands. You would still choose the story, pacing, and framing, while the script handles repeated assembly and export.

**Unexpected combinations**

The following are **INFERRED POSSIBILITIES**, requiring additional components.

1. **A camera that follows the meaning of your demo.**  
   **Experience:** When you click “Generate,” the video moves toward the button, then frames the result when it appears.  
   **Mechanism:** A browser recorder would supply timestamped clicks and element bounds; a script would convert those coordinates into FFmpeg zoom/pan expressions. The inspected implementation exposes position, zoom, duration, and frame-rate controls.  
   **New ability:** Camera movement tied to actual product interactions, reusable when you record a new release.  
   **Missing work:** Event recording, coordinate conversion, timing synchronization, and rules that prevent distracting movement. [Source](https://github.com/FFmpeg/FFmpeg/blob/master/libavfilter/vf_zoompan.c)

2. **An evidence reel for a physical process.**  
   **Experience:** A 3D-printer operator gets a short review showing the moments around temperature alarms or unusually long pauses.  
   **Mechanism:** A companion script would align timestamped sensor logs with footage. FFmpeg’s freeze detector emits start, duration, and end metadata for visually static periods, providing another signal for selecting review intervals.  
   **New ability:** Connect measurements to visible evidence without watching the entire recording.  
   **Missing work:** Clock alignment, event selection, clip assembly, and validation. A static image alone cannot establish that a machine failed. [Source](https://github.com/FFmpeg/FFmpeg/blob/master/libavfilter/vf_freezedetect.c)

3. **One recording becomes an interactive product story.**  
   **Experience:** A viewer chooses “Show me setup,” “Show me the result,” or “Show me the advanced workflow,” and follows a different route through the same demo.  
   **Mechanism:** An authoring script would use a scene manifest to generate consistently encoded clips; a web player would select the next clip from a branching map. FFmpeg supplies the media processing, and `ffprobe` supplies format information for export checks.  
   **New ability:** Reuse the same source material for a linear launch film and a viewer-directed walkthrough.  
   **Missing work:** The branching player, scene metadata, seamless playback handling, and editorial review of each route. [README](https://raw.githubusercontent.com/FFmpeg/FFmpeg/master/README.md), [ffprobe](https://ffmpeg.org/ffprobe.html)

**What adoption would take**

Start with a compiled FFmpeg package, your media assets, and a shell or Python script. The project’s download page links builds for Linux, Windows, and macOS. Basic local processing requires no account, API key, cloud service, or AI model. [Source](https://ffmpeg.org/download.html)

| Meter | Rating | Definition ⓘ | Why this rating |
|---|---|---|---|
| Difficulty | Moderate | Knowledge and setup required | Simple conversions are approachable; reliable timing, captions, and layouts take care. |
| Capability payoff | High | Useful functionality unlocked | One production recipe can serve many releases and export formats. |
| Compute intensity | Variable | Processing and storage burden | Resolution, duration, effects, and encoding settings determine the workload. |

The main limitations are creative and operational: FFmpeg needs explicit editing instructions, and your installed build determines which features are available. Check its filters and encoders before designing a pipeline. Licensing also varies with enabled components; the repository documents LGPL, GPL, and nonredistributable build combinations. [ffprobe documentation](https://ffmpeg.org/ffprobe.html), [License](https://github.com/FFmpeg/FFmpeg/blob/master/LICENSE.md)

**My recommended starting point:** automate the final assembly and export of one existing launch video. Once that recipe works, add interaction-driven zooms—the most distinctive fit for your software demos.
