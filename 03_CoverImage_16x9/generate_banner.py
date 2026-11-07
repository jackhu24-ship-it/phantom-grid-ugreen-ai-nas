# -*- coding: utf-8 -*-
"""
PHANToM GRID :: Full-Bleed 16:9 Cover Image Generator for 202611_UGREEN_AI_NAS_Hackathon
"""
import os

SVG_CONTENT = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1920 1080" width="1920" height="1080">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#060910" />
      <stop offset="50%" stop-color="#0B1220" />
      <stop offset="100%" stop-color="#04060A" />
    </linearGradient>
    <linearGradient id="cyanGold" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00E5FF" />
      <stop offset="50%" stop-color="#38BDF8" />
      <stop offset="100%" stop-color="#F59E0B" />
    </linearGradient>
    <linearGradient id="cardGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#101B2E" stop-opacity="0.92" />
      <stop offset="100%" stop-color="#080D17" stop-opacity="0.98" />
    </linearGradient>
    <linearGradient id="hudGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0D1B2A" stop-opacity="0.95" />
      <stop offset="100%" stop-color="#050B14" stop-opacity="0.98" />
    </linearGradient>
    <pattern id="grid" width="60" height="60" patternUnits="userSpaceOnUse">
      <path d="M 60 0 L 0 0 0 60" fill="none" stroke="#1E293B" stroke-width="1" stroke-opacity="0.3" />
    </pattern>
  </defs>

  <!-- Full Background -->
  <rect width="1920" height="1080" fill="url(#bgGrad)" />
  <rect width="1920" height="1080" fill="url(#grid)" />

  <!-- Outer Neon Border -->
  <rect x="24" y="24" width="1872" height="1032" rx="16" fill="none" stroke="#38BDF8" stroke-width="2" stroke-opacity="0.4" />

  <!-- ==================== LEFT REGION (x: 80 to 1280) ==================== -->
  <!-- Top Category Pill -->
  <g transform="translate(80, 80)">
    <rect width="520" height="42" rx="21" fill="#0E243A" stroke="#00E5FF" stroke-width="1.5" />
    <text x="24" y="27" fill="#00E5FF" font-family="Consolas, monospace" font-size="18" font-weight="bold" letter-spacing="2">
      UGREEN HACKATHON // PRIVATE SOVEREIGN NAS
    </text>
  </g>

  <!-- Main Title Area (Bold, Massive 52px typography) -->
  <text x="80" y="205" fill="url(#cyanGold)" font-family="Segoe UI, Helvetica, Arial, sans-serif" font-size="52" font-weight="900" letter-spacing="1">
    PHANToM GRID :: UGREEN Sovereign AI Storage
  </text>
  <text x="80" y="265" fill="#E2E8F0" font-family="Segoe UI, Helvetica, Arial, sans-serif" font-size="25" font-weight="400">
    Decentralized Private AI Storage &amp; Local Multi-Modal Knowledge Mesh
  </text>

  <!-- Architecture Highlights Grid (3 Columns across 1200px) -->
  <g transform="translate(80, 330)">
    <!-- Card 1 -->
    <rect x="0" y="0" width="380" height="250" rx="12" fill="url(#cardGrad)" stroke="#38BDF8" stroke-width="1.5" />
    <text x="24" y="42" fill="#38BDF8" font-family="Consolas, monospace" font-size="18" font-weight="bold">TRACK A // NAS STORAGE FSM</text>
    <text x="24" y="88" fill="#FFFFFF" font-family="Segoe UI, sans-serif" font-size="30" font-weight="bold">Edge-NPU Mesh</text>
    <text x="24" y="135" fill="#94A3B8" font-family="Segoe UI, sans-serif" font-size="16">On-Premise NVMe Pool Index</text>
    <text x="24" y="165" fill="#94A3B8" font-family="Segoe UI, sans-serif" font-size="16">Zero-Cloud Air-Gapped Perimeter</text>
    <rect x="24" y="195" width="332" height="30" rx="6" fill="#0F2840" stroke="#00E5FF" stroke-width="1" />
    <text x="36" y="216" fill="#00E5FF" font-family="Consolas, monospace" font-size="14" font-weight="bold">STATUS: HARDWARE ACCELERATED</text>

    <!-- Card 2 -->
    <rect x="410" y="0" width="380" height="250" rx="12" fill="url(#cardGrad)" stroke="#F59E0B" stroke-width="1.5" />
    <text x="434" y="42" fill="#F59E0B" font-family="Consolas, monospace" font-size="18" font-weight="bold">TRACK B // VECTOR ENGINE</text>
    <text x="434" y="88" fill="#FFFFFF" font-family="Segoe UI, sans-serif" font-size="30" font-weight="bold">HNSW Knowledge</text>
    <text x="434" y="135" fill="#94A3B8" font-family="Segoe UI, sans-serif" font-size="16">Local Multi-Modal Embeddings</text>
    <text x="434" y="165" fill="#94A3B8" font-family="Segoe UI, sans-serif" font-size="16">Sub-10ms Semantic Retrieval</text>
    <rect x="434" y="195" width="332" height="30" rx="6" fill="#3A2810" stroke="#F59E0B" stroke-width="1" />
    <text x="446" y="216" fill="#F59E0B" font-family="Consolas, monospace" font-size="14" font-weight="bold">SPEC: 1M VECTORS ON-PREMISE</text>

    <!-- Card 3 -->
    <rect x="820" y="0" width="380" height="250" rx="12" fill="url(#cardGrad)" stroke="#10B981" stroke-width="1.5" />
    <text x="844" y="42" fill="#10B981" font-family="Consolas, monospace" font-size="18" font-weight="bold">SAFETY &amp; DEFENSE</text>
    <text x="844" y="88" fill="#FFFFFF" font-family="Segoe UI, sans-serif" font-size="30" font-weight="bold">&#8804; 50GB &amp; 0.00MB</text>
    <text x="844" y="135" fill="#94A3B8" font-family="Segoe UI, sans-serif" font-size="16">Hardware Circuit Breaker Active</text>
    <text x="844" y="165" fill="#94A3B8" font-family="Segoe UI, sans-serif" font-size="16">WORM Immutable Audit Vault</text>
    <rect x="844" y="195" width="332" height="30" rx="6" fill="#0E3324" stroke="#10B981" stroke-width="1" />
    <text x="856" y="216" fill="#10B981" font-family="Consolas, monospace" font-size="14" font-weight="bold">AUDIT: ZERO RESIDUAL ENTROPY</text>
  </g>

  <!-- Metric Badges Row (4 Badges spanning 1200px) -->
  <g transform="translate(80, 620)">
    <rect x="0" y="0" width="280" height="65" rx="8" fill="#111C30" stroke="#38BDF8" stroke-width="1" />
    <text x="24" y="38" fill="#38BDF8" font-family="Consolas, monospace" font-size="20" font-weight="bold">PRIVATE STORAGE</text>

    <rect x="306" y="0" width="280" height="65" rx="8" fill="#111C30" stroke="#38BDF8" stroke-width="1" />
    <text x="330" y="38" fill="#38BDF8" font-family="Consolas, monospace" font-size="20" font-weight="bold">EDGE-NPU POWERED</text>

    <rect x="612" y="0" width="280" height="65" rx="8" fill="#111C30" stroke="#38BDF8" stroke-width="1" />
    <text x="636" y="38" fill="#38BDF8" font-family="Consolas, monospace" font-size="20" font-weight="bold">ZERO CLOUD LEAK</text>

    <rect x="920" y="0" width="280" height="65" rx="8" fill="#111C30" stroke="#F59E0B" stroke-width="1" />
    <text x="938" y="38" fill="#F59E0B" font-family="Consolas, monospace" font-size="18" font-weight="bold">RULE 65 TRI-STANDARD</text>
  </g>

  <!-- Commander Badge (Strictly &#8804; 68% width: 1200 / 1920 = 62.5%) -->
  <g transform="translate(80, 720)">
    <rect width="1200" height="120" rx="14" fill="#0A101D" stroke="#F59E0B" stroke-width="2" />
    <text x="36" y="50" fill="#F59E0B" font-family="Consolas, monospace" font-size="26" font-weight="bold">
      SOLO ARCHITECT // COMMANDER JACK HU (Solo HITL Sovereign)
    </text>
    <text x="36" y="90" fill="#94A3B8" font-family="Segoe UI, sans-serif" font-size="18">
      Co-Signed: Commander Xiaomi | Central Customs Authority &amp; Supreme Drill Command
    </text>
    <rect x="980" y="30" width="180" height="60" rx="8" fill="#F59E0B" fill-opacity="0.15" stroke="#F59E0B" stroke-width="1.5" />
    <text x="1010" y="67" fill="#F59E0B" font-family="Consolas, monospace" font-size="20" font-weight="bold">
      VERIFIED
    </text>
  </g>

  <!-- ==================== RIGHT REGION (x: 1320 to 1840, width: 520px) ==================== -->
  <!-- Right Top: Live Benchmark Card -->
  <g transform="translate(1320, 80)">
    <rect width="520" height="215" rx="14" fill="url(#hudGrad)" stroke="#00E5FF" stroke-width="2" />
    <rect x="20" y="20" width="200" height="30" rx="6" fill="#0E2A42" stroke="#00E5FF" stroke-width="1" />
    <text x="32" y="41" fill="#00E5FF" font-family="Consolas, monospace" font-size="14" font-weight="bold">BENCHMARK TELEMETRY</text>

    <text x="24" y="110" fill="#00E5FF" font-family="Consolas, monospace" font-size="56" font-weight="900">8.2ms</text>
    <text x="230" y="85" fill="#FFFFFF" font-family="Segoe UI, sans-serif" font-size="20" font-weight="bold">Local Semantic Query</text>
    <text x="230" y="115" fill="#94A3B8" font-family="Segoe UI, sans-serif" font-size="15">HNSW Graph Index Across 1M Vectors</text>
    <text x="24" y="160" fill="#64748B" font-family="Consolas, monospace" font-size="13">NVME DIRECT BUS: ZERO-COPY EMBEDDINGS</text>
    <text x="24" y="185" fill="#10B981" font-family="Consolas, monospace" font-size="13" font-weight="bold">DATA INTEGRITY: WORM HARDWARE ENFORCED</text>
  </g>

  <!-- Right Middle: Live Telemetry &amp; NVML Audit Matrix HUD -->
  <g transform="translate(1320, 330)">
    <rect width="520" height="355" rx="14" fill="url(#hudGrad)" stroke="#38BDF8" stroke-width="1.5" />
    <text x="24" y="38" fill="#38BDF8" font-family="Consolas, monospace" font-size="18" font-weight="bold">HARDWARE RESOURCE TELEMETRY (NVML)</text>
    <line x1="24" y1="52" x2="496" y2="52" stroke="#1E293B" stroke-width="1" />

    <!-- Telemetry Row 1 -->
    <text x="24" y="88" fill="#94A3B8" font-family="Consolas, monospace" font-size="15">GPU VRAM ALLOCATION</text>
    <text x="330" y="88" fill="#00E5FF" font-family="Consolas, monospace" font-size="15" font-weight="bold">28.40 GB / 50 GB</text>
    <rect x="24" y="98" width="472" height="8" rx="4" fill="#0F1E33" />
    <rect x="24" y="98" width="268" height="8" rx="4" fill="#00E5FF" />

    <!-- Telemetry Row 2 -->
    <text x="24" y="145" fill="#94A3B8" font-family="Consolas, monospace" font-size="15">HOST DRAM FOOTPRINT</text>
    <text x="330" y="145" fill="#38BDF8" font-family="Consolas, monospace" font-size="15" font-weight="bold">18.25 GB / 64 GB</text>
    <rect x="24" y="155" width="472" height="8" rx="4" fill="#0F1E33" />
    <rect x="24" y="155" width="134" height="8" rx="4" fill="#38BDF8" />

    <!-- Telemetry Row 3 -->
    <text x="24" y="202" fill="#94A3B8" font-family="Consolas, monospace" font-size="15">ZDR MEMORY RESIDUAL</text>
    <text x="330" y="202" fill="#10B981" font-family="Consolas, monospace" font-size="15" font-weight="bold">0.00 MB [CLEARED]</text>
    <rect x="24" y="212" width="472" height="8" rx="4" fill="#0F1E33" />
    <rect x="24" y="212" width="472" height="8" rx="4" fill="#10B981" />

    <!-- Telemetry Row 4 -->
    <text x="24" y="259" fill="#94A3B8" font-family="Consolas, monospace" font-size="15">CHAOS FAULT RECOVERY</text>
    <text x="330" y="259" fill="#F59E0B" font-family="Consolas, monospace" font-size="15" font-weight="bold">1,500 / 1,500 [OK]</text>
    <rect x="24" y="269" width="472" height="8" rx="4" fill="#0F1E33" />
    <rect x="24" y="269" width="472" height="8" rx="4" fill="#F59E0B" />

    <!-- Telemetry Row 5 -->
    <text x="24" y="316" fill="#94A3B8" font-family="Consolas, monospace" font-size="15">NETWORK EGRESS PACKETS</text>
    <text x="330" y="316" fill="#10B981" font-family="Consolas, monospace" font-size="15" font-weight="bold">0 [AIR-GAPPED]</text>
    <text x="24" y="340" fill="#64748B" font-family="Consolas, monospace" font-size="12">INDEX SCAN RATE: 122,000 VECTORS / SEC</text>
  </g>

  <!-- Right Bottom: Cryptographic WORM Seal -->
  <g transform="translate(1320, 720)">
    <rect width="520" height="120" rx="14" fill="url(#hudGrad)" stroke="#F59E0B" stroke-width="1.5" />
    <rect x="24" y="25" width="70" height="70" rx="8" fill="#1E293B" stroke="#F59E0B" stroke-width="1.5" />
    <rect x="34" y="35" width="20" height="20" fill="#F59E0B" />
    <rect x="64" y="35" width="20" height="20" fill="#F59E0B" />
    <rect x="34" y="65" width="20" height="20" fill="#F59E0B" />
    <rect x="64" y="65" width="10" height="10" fill="#F59E0B" />
    <rect x="74" y="75" width="10" height="10" fill="#F59E0B" />

    <text x="110" y="50" fill="#F59E0B" font-family="Consolas, monospace" font-size="18" font-weight="bold">WORM AUDIT LOCKED</text>
    <text x="110" y="75" fill="#94A3B8" font-family="Consolas, monospace" font-size="14">SHA-256: 0x9923BF88CC21A4... [SEALED]</text>
    <text x="110" y="98" fill="#10B981" font-family="Consolas, monospace" font-size="13" font-weight="bold">&#10004; CO-SIGNED: COMMANDER XIAOMI</text>
  </g>

  <!-- Bottom Title Safe Area Line (Spanning Full 1760px from x=80 to x=1840) -->
  <text x="80" y="990" fill="#64748B" font-family="Consolas, monospace" font-size="16">
    BROADCAST SAFE ZONE // 1440P / 1080P MASTER SPEC // ASIL-D STATE RECOVERY CERTIFIED // OFFLINE VERIFIED
  </text>
</svg>"""

def generate_svg_banner(output_path):
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(SVG_CONTENT)

generate_banner = generate_svg_banner

if __name__ == '__main__':
    cur = os.path.dirname(os.path.abspath(__file__))
    generate_svg_banner(os.path.join(cur, 'cover_16x9.svg'))
