# Demo: “What could it become inside yours?”

**Deliverable status:** complete production script; no rendered video/GIF is included. All UI shown is an illustrative conversation mockup, not a shipped Capability Explorer app. No upstream execution is depicted.

**Format:** 28 seconds, 1920×1080, 30 FPS (840 frames). Export H.264 MP4 with captions; optional silent GIF excerpt. Dark background (#0B1020), off-white type (#F5F7FA), cyan capability accent (#62DCEB), amber inference label (#FFC46B). Use system sans-serif, minimum 44 px main text and 28 px labels. No stock footage or logos needed. Keep the real repository URL visible on the end card.

## Timeline and exact on-screen copy

| Time | Action | Screen copy | Voiceover |
| --- | --- | --- | --- |
| 0–4 s | Paste URL into a simple conversation card | `github.com/simular-ai/Agent-S` / “What could this add to my project?” | “You found a new tool. What could it add to your project?” |
| 4–8 s | Reveal one capability card | “CAPABILITY: Operate desktop interfaces” / “REPORTED · upstream docs” | “Agent-S describes computer-use capabilities.” |
| 8–12 s | Bring in an existing-context card | “YOUR PROJECT: Desktop launcher” / “Automated builds · Third-party apps” / “Supplied example context” | “Your project already builds a launcher that opens other apps.” |
| 12–17 s | Connect capability to build card | “DIRECT FIT: Test each build visually” / “INFERRED POSSIBILITY” | “You could test each build through its interface.” |
| 17–23 s | Reveal the handoff and return path | “UNEXPECTED: Test the handoff—and return” / “Launch → Use app → Close → Regain focus” / “Integration required” | “Or test something unit tests can miss: does control return when another app closes?” |
| 23–28 s | Settle on the value proposition | “NEW CAPABILITY × YOUR PROJECT = NEW POSSIBILITY” / “Capability Explorer” / `github.com/timporachin/Capability-Explorer` | “Capability Explorer. Discover what a new capability could become inside yours.” |

## Production assets and instructions

All required text, timing, colors, and layout are above; build cards with native text/shapes. No external image or music assets are required. Keep the evidence/inference labels readable throughout their shots. Optional original/licensed background music should sit beneath voiceover; silence is acceptable.

Use 250–400 ms fades and small vertical movements. Hold each final card long enough to read. Keep content inside a 120 px margin. The last frame doubles as a README/social still. For mobile crops, stack cards vertically rather than shrinking the whole 16:9 frame.

Use [the Agent-S analysis](../examples/agent-s.md) as the claim source. Do not animate a successful real test run, invent measured results, or suggest the workflow is already implemented. The first shot's URL and supplied context can be recreated with text; no private chat screenshot is needed.

Render in HyperFrames or your editor of choice. Verify 28-second duration, 1920×1080 dimensions, 30 FPS, legible labels, caption/voice alignment, and the final URL. Watch once muted and once on a phone. Export an optional 12–23 second silent excerpt with the context card retained, so the unexpected integration remains understandable.

## README text alternative

Paste a computer-use repository → identify desktop interaction → connect it to an existing launcher → propose visual tests → reveal cross-app handoff testing. All integrations are inferred possibilities requiring engineering.
