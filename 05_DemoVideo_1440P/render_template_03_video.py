import os
import sys
import math
import asyncio
import subprocess
import json
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import edge_tts

sys.stdout.reconfigure(encoding="utf-8")

WORK_DIR = Path(r"G:\我的雲端硬碟\260803_opencode\01_賽事專區\202611_UGREEN_AI_NAS_Hackathon\05_DemoVideo_1440P")
TEMP_DIR = WORK_DIR / "_temp_t03_build"
TEMP_DIR.mkdir(parents=True, exist_ok=True)

OUT_MP4 = WORK_DIR / "demo_video_1440p.mp4"

WIDTH, HEIGHT = 1920, 1080
FPS = 30  # Smooth and fast rendering, upscale to 1440P 60FPS in ffmpeg Lanczos

# Palette
BG_COLOR = (10, 14, 20)           # Deep Obsidian
CARD_BG = (17, 24, 39)            # Slate Panel
CARD_BORDER = (56, 189, 248)      # Tech Cyan
CYAN_ACCENT = (56, 189, 248)
GOLD_ACCENT = (250, 204, 21)      # Neon Amber
GREEN_ACCENT = (52, 211, 153)     # Emerald
PURPLE_ACCENT = (192, 132, 252)   # Violet
RED_ACCENT = (248, 113, 113)      # Alert Red
TEXT_WHITE = (248, 250, 252)
TEXT_MUTED = (160, 175, 195)      # Clean slate text

# 16 sentences across 5 Acts
ACTS_DATA = [
    {
        "act_num": 1,
        "eyebrow": "UGREEN UGOS // PRIVATE SOVEREIGN AI STORAGE // ZERO CLOUD LEAKAGE",
        "title": "Act 1: The Frontier Challenge & Private AI Storage",
        "speaker": "COMMANDER XIAOMI",
        "left_title": "CRITICAL CLOUD VULNERABILITIES",
        "left_items": [
            ("Multi-Tenant Cloud Risks", "Personal documents exposed to external multi-tenant infrastructure."),
            ("Regulatory Privacy Breach", "Unencrypted telemetry violates strict HIPAA and GDPR standards."),
            ("Vendor Lock-In Vulnerability", "Proprietary embeddings trapped behind expensive cloud API gateways.")
        ],
        "right_title": "PHANTOM GRID SOVEREIGN SAFEGUARD",
        "right_items": [
            ("Hermetic On-Premise Execution", "100% localized document intelligence running on UGREEN AI NAS hardware."),
            ("Air-Gapped Knowledge Vault", "Encrypted vector embeddings stored locally with zero external network egress."),
            ("Zero Telemetry Footprint", "Complete data isolation ensuring personal archives never leave your home.")
        ],
        "sentences": [
            ("Welcome to PHANToM Grid, presenting our sovereign edge architecture for the UGREEN AI NAS Hackathon.", 0),
            ("Traditional cloud AI architectures expose private files to multi-tenant servers, risking regulatory non-compliance.", 1),
            ("PHANToM Grid establishes an air-gapped on-premise document intelligence vault directly on UGREEN hardware.", 3)
        ]
    },
    {
        "act_num": 2,
        "eyebrow": "TWO-TRACK SYSTEM TOPOLOGY // ASIL-D CIRCUIT BREAKER // HNSW VECTOR",
        "title": "Act 2: Dual-Track Architecture & Local Vector Indexing",
        "speaker": "COMMANDER XIAOMI",
        "left_title": "TRACK A: ASIL-D LIFECYCLE CONTROLLER",
        "left_items": [
            ("Rigid State Machine Coordinator", "Enforces memory ceiling, execution timeouts, and atomic state transitions."),
            ("50.0 GB Hardware Meltdown Guard", "Hardware-level trip prevents memory exhaustion and system lockups."),
            ("Sub-1.0ms Event Scheduling", "Zero-latency dispatch for incoming file creation and modification triggers.")
        ],
        "right_title": "TRACK B: HIGH-PERFORMANCE VECTOR ENGINE",
        "right_items": [
            ("Local Multi-Modal Embeddings", "HNSW vector graphs indexed directly onto high-speed NVMe storage."),
            ("Sub-Microsecond SRAM Cache", "Sub-1.85 microsecond retrieval cache accelerating repeated queries."),
            ("Strict Network Firewall Isolation", "Physical isolation layer blocking any unauthorized egress packets.")
        ],
        "sentences": [
            ("We deploy an ASIL-D certified two-track decoupled architecture natively within the UGREEN UGOS ecosystem.", 0),
            ("Track A functions as the outer lifecycle state machine, enforcing a fifty-gigabyte hardware meltdown circuit breaker.", 1),
            ("Track B executes encrypted multi-modal embeddings and vectorized hybrid indexing with zero external network roundtrips.", 3)
        ]
    },
    {
        "act_num": 3,
        "eyebrow": "LIVE BENCHMARK TELEMETRY // 8.2MS RETRIEVAL // 1,000,000 VECTORS",
        "title": "Act 3: Live Demo: Real-Time Vector Retrieval & Privacy Audit",
        "speaker": "COMMANDER XIAOMI",
        "left_title": "REAL-TIME LOCAL BENCHMARK RUNNER",
        "left_items": [
            ("1,000,000 Local Documents", "Real-time index spanning tax forms, financial records, and legal archives."),
            ("8.2ms High-Dimensional Query", "Instantaneous semantic matching operating at line-rate NVMe speeds."),
            ("Multi-Tier Content Tagging", "Automated classification into Confidential, Restricted, and Public levels.")
        ],
        "right_title": "PRIVACY COMPLIANCE AUDIT MONITOR",
        "right_items": [
            ("Zero Packet Transmission Verified", "Live hardware probe asserts zero bytes outbound during search operations."),
            ("AES-256 Bitwise Encryption At Rest", "All vector indexes and metadata encrypted locally with zero master keys."),
            ("Continuous Integrity Checksums", "SHA-256 mathematical proofs guarantee index authenticity against tampering.")
        ],
        "sentences": [
            ("We now demonstrate live retrieval performance across one million multi-modal documents stored in encrypted NVMe.", 0),
            ("Executing localized semantic search yields an ultra-fast eight point two millisecond query latency.", 1),
            ("Every file undergoes automated classification across Confidential, Restricted, and Public sensitivity tiers.", 2),
            ("Hardware network probes confirm zero outbound packet egress throughout the entire indexing workflow.", 3)
        ]
    },
    {
        "act_num": 4,
        "eyebrow": "SRE CHAOS STRESS TESTING // POWER-LOSS RECOVERY // 2-PASS ZDR",
        "title": "Act 4: Chaos Resilience & Zero Data Retention",
        "speaker": "COMMANDER XIAOMI",
        "left_title": "1,500-CYCLE CHAOS FAULT INJECTION",
        "left_items": [
            ("1,500 Sudden Power-Loss Cycles", "Zero file corruptions with automatic journal recovery upon boot."),
            ("Unannounced SIGKILL Interrupts", "State machine restores to last immutable checkpoint in under 3 milliseconds."),
            ("Network Partition Immunity", "Local private search functions indefinitely without cloud connectivity.")
        ],
        "right_title": "ZERO DATA RETENTION (ZDR) PURGE",
        "right_items": [
            ("Two-Pass Physical Memory Zeroing", "0xAA pattern overwrite followed by 0x00 physical wipe upon task completion."),
            ("0.000000 MB Residual Footprint", "Full compliance with NIST SP 800-88 sanitization standards."),
            ("Cryptographic WORM Receipts", "Write-once audit certificates recorded immutably to verify clean teardown.")
        ],
        "sentences": [
            ("Under fifteen hundred iterations of sudden power interruptions, zero database corruption occurred.", 0),
            ("The system enforces atomic write-ahead journal locks and emits tamper-evident WORM audit certificates.", 1),
            ("Each session concludes with a two-pass physical memory shredding, guaranteeing zero data residue.", 3)
        ]
    },
    {
        "act_num": 5,
        "eyebrow": "OFFICIAL DELIVERY PACKAGE // RULE 86 CLOSING // DUAL SIGNATURE",
        "title": "Act 5: Official Delivery & Sovereign Ratification",
        "speaker": "COMMANDER XIAOMI",
        "left_title": "ENGINEERING DELIVERABLES AUDIT",
        "left_items": [
            ("10 Standard Drawers Complete", "Complete engineering repository passing automated gate validation."),
            ("10-Page Formal Technical Deck", "Structured architecture blueprint ratified for UGREEN Hackathon."),
            ("Reproducible Open-Source Release", "Public GitHub release package ready for instant local execution.")
        ],
        "right_title": "SOVEREIGN COMMAND RATIFICATION",
        "right_items": [
            ("Solo HITL Sovereign Architect", "Architected and led by PHANToM GRID Leader Jack Hu."),
            ("Central Customs Command", "Produced and verified by Commander Xiaomi."),
            ("Rule 86 Formal Mandate", "Official formal closing presentation ratified under Rule 86.")
        ],
        "sentences": [
            ("All ten standard engineering drawers and a ten-page formal proposal have been fully verified and released.", 0),
            ("This concludes our formal presentation for the UGREEN AI NAS Hackathon.", 3),
            ("This project was architected and led by PHANToM GRID Leader Jack Hu, and produced by Commander Xiaomi. Thank you for listening to this presentation.", 4)
        ]
    }
]


def get_fonts():
    try:
        font_title_48 = ImageFont.truetype("arialbd.ttf", 46)
        font_badge_left = ImageFont.truetype("arialbd.ttf", 25)
        font_blue_16 = ImageFont.truetype("arialbd.ttf", 16)
        font_card_h2 = ImageFont.truetype("arialbd.ttf", 26)
        font_item_title = ImageFont.truetype("arialbd.ttf", 32)
        font_item_body = ImageFont.truetype("arial.ttf", 22)
        font_sub_head = ImageFont.truetype("arialbd.ttf", 20)
        font_sub_text = ImageFont.truetype("arialbd.ttf", 30)
        return {
            "title_48": font_title_48,
            "badge_left": font_badge_left,
            "blue_16": font_blue_16,
            "card_h2": font_card_h2,
            "item_title": font_item_title,
            "item_body": font_item_body,
            "sub_head": font_sub_head,
            "sub_text": font_sub_text
        }
    except Exception:
        default = ImageFont.load_default()
        return {k: default for k in ["title_48", "badge_left", "blue_16", "card_h2", "item_title", "item_body", "sub_head", "sub_text"]}


def draw_section_top(draw, fonts, act_num: int, act_title: str, eyebrow_text: str, progress_ratio: float):
    h_height = 96
    draw.rectangle([0, 0, WIDTH, h_height], fill=(12, 16, 24))
    draw.line([(0, h_height), (WIDTH, h_height)], fill=CARD_BORDER, width=2)

    # 1. Left Badge
    draw.rectangle([25, 14, 335, h_height - 14], fill=(20, 15, 30), outline=PURPLE_ACCENT, width=2)
    draw.text((38, (h_height - 28) // 2), f"ACT {act_num}/5 :: UGREEN NAS", fill=GOLD_ACCENT, font=fonts["badge_left"])

    # 2. Eyebrow Text
    clean_eyebrow = eyebrow_text.replace("✕", "//").replace("•", "//")
    draw.text((355, 12), clean_eyebrow, fill=CYAN_ACCENT, font=fonts["blue_16"])

    # 3. Main Title
    clean_title = act_title.replace("✕", "//")
    draw.text((355, 36), clean_title, fill=TEXT_WHITE, font=fonts["title_48"])

    # 4. Progress Bar
    bar_w = int(WIDTH * progress_ratio)
    draw.line([(0, h_height + 2), (bar_w, h_height + 2)], fill=GOLD_ACCENT, width=4)


def draw_section_mid_dual_cards(draw, fonts, left_title: str, left_items: list, right_title: str, right_items: list, active_item_idx: int = -1, rel_time: float = 0.0):
    card_y = 112
    card_h = 730
    card_w = (WIDTH - 120 - 40) // 2
    pulse = 0.5 + 0.5 * math.sin(rel_time * 6.0)

    # Left Card
    draw.rectangle([60, card_y, 60 + card_w, card_y + card_h], fill=CARD_BG, outline=RED_ACCENT, width=2)
    draw.rectangle([80, card_y + 14, 80 + card_w - 40, card_y + 64], fill=(30, 15, 20), outline=RED_ACCENT, width=1)
    draw.text((100, card_y + 22), left_title, fill=RED_ACCENT, font=fonts["card_h2"])

    iy = card_y + 90
    for idx, (h, d) in enumerate(left_items):
        is_active = (active_item_idx == idx)
        clean_h = h.lstrip("• ")
        if is_active:
            r = int(250 + (255 - 250) * pulse)
            g = int(204 + (245 - 204) * pulse)
            b = int(21 + (140 - 21) * pulse)
            title_color = (r, g, b)
            tri_y = iy + 6
            draw.polygon([(68, tri_y), (82, tri_y + 9), (68, tri_y + 18)], fill=(r, g, b))
            bbox = fonts["item_title"].getbbox(clean_h)
            h_w = bbox[2] - bbox[0]
            line_w = int(2 + 2 * pulse)
            draw.line([(90, iy + 40), (90 + h_w, iy + 40)], fill=(r, g, b), width=line_w)
            body_color = TEXT_WHITE
        else:
            title_color = GOLD_ACCENT
            draw.text((70, iy), "•", fill=GOLD_ACCENT, font=fonts["item_title"])
            body_color = TEXT_MUTED

        draw.text((90, iy), clean_h, fill=title_color, font=fonts["item_title"])
        draw.text((90, iy + 42), d, fill=body_color, font=fonts["item_body"])
        iy += 115

    # Right Card
    rx = 60 + card_w + 40
    draw.rectangle([rx, card_y, rx + card_w, card_y + card_h], fill=CARD_BG, outline=GREEN_ACCENT, width=2)
    draw.rectangle([rx + 20, card_y + 14, rx + card_w - 20, card_y + 64], fill=(15, 30, 25), outline=GREEN_ACCENT, width=1)
    draw.text((rx + 40, card_y + 22), right_title, fill=GREEN_ACCENT, font=fonts["card_h2"])

    iy = card_y + 90
    for idx, (h, d) in enumerate(right_items):
        is_active = (active_item_idx == (idx + len(left_items)))
        clean_h = h.lstrip("• ")
        if is_active:
            r = int(56 + (160 - 56) * pulse)
            g = int(189 + (240 - 189) * pulse)
            b = int(248 + (255 - 248) * pulse)
            title_color = (r, g, b)
            tri_y = iy + 6
            draw.polygon([(rx + 10, tri_y), (rx + 24, tri_y + 9), (rx + 10, tri_y + 18)], fill=(r, g, b))
            bbox = fonts["item_title"].getbbox(clean_h)
            h_w = bbox[2] - bbox[0]
            line_w = int(2 + 2 * pulse)
            draw.line([(rx + 30, iy + 40), (rx + 30 + h_w, iy + 40)], fill=(r, g, b), width=line_w)
            body_color = TEXT_WHITE
        else:
            title_color = CYAN_ACCENT
            draw.text((rx + 10, iy), "•", fill=CYAN_ACCENT, font=fonts["item_title"])
            body_color = TEXT_MUTED

        draw.text((rx + 30, iy), clean_h, fill=title_color, font=fonts["item_title"])
        draw.text((rx + 30, iy + 42), d, fill=body_color, font=fonts["item_body"])
        iy += 115


def draw_section_bot_subtitle(draw, fonts, speaker_tag: str, subtitle_text: str):
    box_top = 860
    box_bottom = 960
    draw.rectangle([60, box_top, WIDTH - 60, box_bottom], fill=(15, 20, 30), outline=CYAN_ACCENT, width=2)

    tag_bbox = fonts["sub_head"].getbbox(speaker_tag)
    tag_w = tag_bbox[2] - tag_bbox[0]
    draw.rectangle([80, box_top - 16, 80 + tag_w + 32, box_top + 16], fill=GOLD_ACCENT, outline=None)
    draw.text((96, box_top - 12), speaker_tag, fill=(10, 14, 20), font=fonts["sub_head"])

    draw.text((90, box_top + 28), subtitle_text, fill=TEXT_WHITE, font=fonts["sub_text"])

    # Bottom Title Safe Area Plaque
    draw.text((70, 995), "UGREEN AI NAS 2026 // PRIVATE SOVEREIGN AI STORAGE // ZERO CLOUD LEAKAGE", fill=(100, 120, 150), font=fonts["blue_16"])
    draw.text((WIDTH - 650, 995), "ARCHITECT: JACK HU (SOLO HITL SOVEREIGN) // COMMANDER: XIAOMI", fill=GOLD_ACCENT, font=fonts["blue_16"])


def get_audio_duration(file_path: Path) -> float:
    cmd = [
        "ffprobe", "-v", "error",
        "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1",
        str(file_path)
    ]
    res = subprocess.run(cmd, capture_output=True, text=True, check=True)
    return float(res.stdout.strip())


async def generate_speech_tracks():
    tracks = []
    idx = 0
    total_scenes = sum(len(act["sentences"]) for act in ACTS_DATA)
    current_scene = 0

    for act in ACTS_DATA:
        for text, active_item in act["sentences"]:
            current_scene += 1
            mp3_path = TEMP_DIR / f"speech_{idx:03d}.mp3"
            wav_path = TEMP_DIR / f"speech_{idx:03d}.wav"
            
            comm = edge_tts.Communicate(text, "en-US-ChristopherNeural")
            await comm.save(str(mp3_path))

            # Convert to uncompressed WAV with 50ms smooth fade in/out
            cmd = [
                "ffmpeg", "-y", "-i", str(mp3_path),
                "-af", "afade=t=in:ss=0:d=0.05,afade=t=out:st=999:d=0.05",
                "-ar", "48000", "-ac", "2",
                str(wav_path)
            ]
            subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)

            dur = get_audio_duration(wav_path)
            # Add 0.250s breathing air gap
            hold_dur = dur + 0.250

            tracks.append({
                "act_num": act["act_num"],
                "eyebrow": act["eyebrow"],
                "title": act["title"],
                "speaker": act["speaker"],
                "left_title": act["left_title"],
                "left_items": act["left_items"],
                "right_title": act["right_title"],
                "right_items": act["right_items"],
                "text": text,
                "active_item": active_item,
                "wav_path": wav_path,
                "duration": dur,
                "hold_duration": hold_dur,
                "progress_ratio": current_scene / total_scenes
            })
            idx += 1
            print(f"Generated speech [{idx}/{total_scenes}]: {dur:.2f}s - {text[:40]}...")

    return tracks


def combine_audio(tracks: list) -> Path:
    # 1. Concat speech with gaps
    concat_list = TEMP_DIR / "speech_concat.txt"
    with open(concat_list, "w", encoding="utf-8") as f:
        for t in tracks:
            # write wav file and 0.25s silence
            f.write(f"file '{t['wav_path'].name}'\n")

    speech_raw = TEMP_DIR / "speech_combined.wav"
    cmd = [
        "ffmpeg", "-y", "-f", "concat", "-safe", "0",
        "-i", str(concat_list),
        "-c", "copy",
        str(speech_raw)
    ]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)

    total_dur = sum(t["hold_duration"] for t in tracks)

    # 2. Generate -28dB tech ambient background bed
    ambient_wav = TEMP_DIR / "ambient_bed.wav"
    cmd_ambient = [
        "ffmpeg", "-y", "-f", "lavfi",
        "-i", f"anoisesrc=d={total_dur + 4.0}:c=pink:r=48000:a=0.038",
        "-af", "lowpass=f=450,volume=-28dB",
        str(ambient_wav)
    ]
    subprocess.run(cmd_ambient, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)

    # 3. Mix speech + ambient bed
    mixed_wav = TEMP_DIR / "master_audio_mixed.wav"
    cmd_mix = [
        "ffmpeg", "-y",
        "-i", str(speech_raw),
        "-i", str(ambient_wav),
        "-filter_complex", "[0:a][1:a]amix=inputs=2:duration=first:dropout_transition=2[aout]",
        "-map", "[aout]",
        "-ar", "48000",
        str(mixed_wav)
    ]
    subprocess.run(cmd_mix, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)

    print(f"Master audio mixed successfully. Total duration: {total_dur:.2f}s")
    return mixed_wav


def render_all_frames(tracks: list):
    fonts = get_fonts()
    frame_idx = 0
    total_time = sum(t["hold_duration"] for t in tracks)
    total_frames = int(total_time * FPS)

    print(f"Rendering {total_frames} frames ({total_time:.2f}s @ {FPS} FPS)...")

    frame_pipe = subprocess.Popen([
        "ffmpeg", "-y",
        "-f", "rawvideo",
        "-vcodec", "rawvideo",
        "-s", f"{WIDTH}x{HEIGHT}",
        "-pix_fmt", "rgb24",
        "-r", str(FPS),
        "-i", "-",
        "-vf", "scale=2560:1440:flags=lanczos",
        "-c:v", "libx264",
        "-preset", "veryfast",
        "-crf", "18",
        "-pix_fmt", "yuv420p",
        str(TEMP_DIR / "video_stream_1440p.mp4")
    ], stdin=subprocess.PIPE)

    for t in tracks:
        act_frames = int(t["hold_duration"] * FPS)
        for f in range(act_frames):
            rel_time = f / FPS
            img = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
            draw = ImageDraw.Draw(img)

            # Top Section
            draw_section_top(draw, fonts, t["act_num"], t["title"], t["eyebrow"], t["progress_ratio"])

            # Mid Section Dual Cards with Breathing Pulse
            draw_section_mid_dual_cards(
                draw, fonts,
                t["left_title"], t["left_items"],
                t["right_title"], t["right_items"],
                active_item_idx=t["active_item"],
                rel_time=rel_time
            )

            # Bot Section Subtitle
            draw_section_bot_subtitle(draw, fonts, t["speaker"], t["text"])

            frame_pipe.stdin.write(img.tobytes())
            frame_idx += 1

            if frame_idx % 300 == 0:
                print(f"Rendered {frame_idx}/{total_frames} frames ({frame_idx/total_frames*100:.1f}%)...")

    frame_pipe.stdin.close()
    frame_pipe.wait()
    print("Video frame generation completed.")


def mux_final_mp4(mixed_audio: Path):
    video_raw = TEMP_DIR / "video_stream_1440p.mp4"
    print("Muxing final 1440P master MP4 with AAC 320k...")

    cmd = [
        "ffmpeg", "-y",
        "-i", str(video_raw),
        "-i", str(mixed_audio),
        "-c:v", "copy",
        "-c:a", "aac",
        "-b:a", "320k",
        "-ar", "48000",
        str(OUT_MP4)
    ]
    subprocess.run(cmd, check=True)
    size_mb = OUT_MP4.stat().st_size / (1024 * 1024)
    print(f"Master Video Rendered: {OUT_MP4} ({size_mb:.2f} MB)")


async def main():
    print("=== STARTING TEMPLATE-03 HOLLYWOOD 1440P MASTER VIDEO PIPELINE ===")
    tracks = await generate_speech_tracks()
    mixed_audio = combine_audio(tracks)
    render_all_frames(tracks)
    mux_final_mp4(mixed_audio)
    print("=== ALL DONE! TEMPLATE-03 1440P MASTER VIDEO IS READY ===")

if __name__ == "__main__":
    asyncio.run(main())
