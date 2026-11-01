<script setup lang="ts">
defineProps<{ kind: 'p1' | 'p2' | 'p3' }>()

const monthlyCancel = [17.55, 91.53, 8.34, 10.50, 33.32, 8.95, 13.71, 11.41, 22.93, 16.98, 41.61, 24.99, 174.09]
const monthLabels = ['12/10', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12/11*']
</script>

<template>
<svg v-if="kind === 'p1'" class="brief-evidence" viewBox="0 0 920 350" role="img" aria-label="Giá trị hủy theo tháng có hai đỉnh vào tháng 1 và tháng 12 năm 2011; tỷ lệ hủy toàn kỳ là 4.64 phần trăm và điều chỉnh là 2.30 phần trăm.">
  <text x="0" y="22" class="section-label">GIÁ TRỊ HỦY THEO THÁNG · £ NGHÌN</text>
  <g v-for="tick in [0,50,100,150,200]" :key="tick">
    <line x1="45" x2="610" :y1="278-tick*1.12" :y2="278-tick*1.12" class="grid" />
    <text x="36" :y="283-tick*1.12" text-anchor="end" class="axis">{{tick}}</text>
  </g>
  <g v-for="(value,i) in monthlyCancel" :key="i">
    <rect :x="53+i*42" :y="278-value*1.12" width="24" :height="value*1.12" :class="i===1 || i===12 ? 'warn' : 'base'" />
    <text :x="65+i*42" y="298" text-anchor="middle" class="axis">{{monthLabels[i]}}</text>
  </g>
  <path d="M107 164 L152 108" class="leader" />
  <text x="157" y="93" class="annotation">18/01 · đảo ngược £77.2k</text>
  <text x="157" y="112" class="axis">trong 16 phút</text>
  <path d="M569 83 L511 52" class="leader" />
  <text x="506" y="34" text-anchor="end" class="annotation">09/12 · đảo ngược £168.5k</text>
  <text x="506" y="53" text-anchor="end" class="axis">trong 12 phút</text>
  <text x="44" y="332" class="foot">* 12/2011 chỉ đến 09/12</text>

  <line x1="640" x2="640" y1="10" y2="323" class="divider" />
  <text x="670" y="22" class="section-label">TỶ LỆ HỦY / GROSS</text>
  <text x="670" y="70" class="small">Toàn bộ hợp lệ</text>
  <rect x="670" y="84" width="210" height="42" class="warn" />
  <text x="775" y="113" text-anchor="middle" class="white big">4.64%</text>
  <text x="670" y="174" class="small">Loại cả mua và hủy của hai cặp</text>
  <rect x="670" y="188" width="104" height="42" class="accent" />
  <text x="722" y="217" text-anchor="middle" class="white big">2.30%</text>
  <text x="670" y="270" class="annotation">Net không đổi</text>
  <text x="670" y="296" class="metric">£9.77M</text>
  <text x="670" y="320" class="foot">Phân tích độ nhạy, không phải cải thiện vận hành</text>
</svg>

<svg v-else-if="kind === 'p2'" class="brief-evidence" viewBox="0 0 920 350" role="img" aria-label="Top 434 người mua chiếm 10.01 phần trăm số người mua và 60.21 phần trăm net sales có ID; từ tháng 1 đến tháng 11 người mua và hóa đơn mỗi người tăng nhưng gross mỗi người giảm.">
  <text x="0" y="22" class="section-label">TỶ TRỌNG NGƯỜI MUA SO VỚI NET SALES CÓ ID</text>
  <g v-for="tick in [0,25,50,75,100]" :key="tick">
    <line x1="48" x2="530" :y1="280-tick*2.15" :y2="280-tick*2.15" class="grid" />
    <text x="39" :y="285-tick*2.15" text-anchor="end" class="axis">{{tick}}%</text>
  </g>
  <rect x="112" y="258.5" width="58" height="21.5" class="base" />
  <rect x="178" y="150.5" width="58" height="129.5" class="accent" />
  <text x="141" y="249" text-anchor="middle" class="value">10.01%</text>
  <text x="207" y="141" text-anchor="middle" class="value">60.21%</text>
  <rect x="342" y="86.5" width="58" height="193.5" class="base" />
  <rect x="408" y="194.5" width="58" height="85.5" class="accent" />
  <text x="371" y="77" text-anchor="middle" class="value">89.99%</text>
  <text x="437" y="185" text-anchor="middle" class="value">39.79%</text>
  <text x="174" y="310" text-anchor="middle" class="small">434 người dẫn đầu</text>
  <text x="404" y="310" text-anchor="middle" class="small">3,900 người còn lại</text>
  <rect x="115" y="327" width="12" height="12" class="base" /><text x="133" y="338" class="foot">% người mua</text>
  <rect x="245" y="327" width="12" height="12" class="accent" /><text x="263" y="338" class="foot">% net sales</text>

  <line x1="560" x2="560" y1="10" y2="340" class="divider" />
  <text x="590" y="22" class="section-label">01/2011 → 11/2011</text>
  <g transform="translate(590,55)">
    <text x="0" y="0" class="small">Người mua có ID</text><text x="0" y="40" class="metric">739 → 1,660</text><text x="292" y="40" text-anchor="end" class="up">+124.6%</text>
    <line x1="0" x2="292" y1="65" y2="65" class="divider" />
    <text x="0" y="98" class="small">Hóa đơn / người mua</text><text x="0" y="138" class="metric">1.33 → 1.59</text><text x="292" y="138" text-anchor="end" class="up">+19.5%</text>
    <line x1="0" x2="292" y1="163" y2="163" class="divider" />
    <text x="0" y="196" class="small">Gross / người mua hoạt động</text><text x="0" y="236" class="metric">£761 → £685</text><text x="292" y="236" text-anchor="end" class="down">-10.1%</text>
    <text x="0" y="278" class="foot">Tập khách thay đổi theo tháng; chưa phải cohort.</text>
  </g>
</svg>

<svg v-else class="brief-evidence" viewBox="0 0 920 350" role="img" aria-label="Hai cặp mua kèm có lift 6.41 và 14.06; Đức và Pháp có cơ sở người mua rộng hơn các thị trường so sánh dù AOV thấp hơn.">
  <text x="0" y="22" class="section-label">MUA KÈM · QUAN SÁT SO VỚI KỲ VỌNG ĐỘC LẬP</text>
  <g transform="translate(0,48)">
    <text x="0" y="0" class="small">Jumbo Bag · 85099B / 22386</text>
    <rect x="0" y="18" width="64" height="22" class="base" /><text x="72" y="35" class="axis">128.7 kỳ vọng</text>
    <rect x="0" y="50" width="412" height="28" class="accent" /><text x="400" y="71" text-anchor="end" class="white value">825</text>
    <text x="0" y="109" class="metric">Lift 6.41</text><text x="160" y="107" class="foot">Support 4.17% · Confidence 39.49%</text>
  </g>
  <g transform="translate(0,192)">
    <text x="0" y="0" class="small">Regency Teacup · 22699 / 22697</text>
    <rect x="0" y="18" width="27" height="22" class="base" /><text x="35" y="35" class="axis">54.6 kỳ vọng</text>
    <rect x="0" y="50" width="384" height="28" class="accent" /><text x="372" y="71" text-anchor="end" class="white value">767</text>
    <text x="0" y="109" class="metric">Lift 14.06</text><text x="175" y="107" class="foot">Support 3.88% · Confidence 72.02%</text>
  </g>

  <line x1="485" x2="485" y1="10" y2="340" class="divider" />
  <text x="515" y="22" class="section-label">THỊ TRƯỜNG QUỐC TẾ · AOV × NGƯỜI MUA ID</text>
  <line x1="545" x2="885" y1="302" y2="302" class="axis-line" />
  <line x1="545" x2="545" y1="56" y2="302" class="axis-line" />
  <text x="715" y="337" text-anchor="middle" class="foot">Số người mua có ID →</text>
  <text x="518" y="58" class="foot">AOV £</text>
  <rect x="795" y="238" width="80" height="55" rx="7" class="target-zone" />
  <text x="835" y="230" text-anchor="middle" class="foot accent-text">Ứng viên thử nghiệm</text>
  <circle cx="574" cy="71" r="16" class="bubble-muted" /><text x="597" y="69" class="axis">Netherlands · 9</text>
  <circle cx="554" cy="224" r="15" class="bubble-muted" /><text x="568" y="216" class="axis">EIRE · 3</text>
  <circle cx="850" cy="265" r="15" class="bubble" /><path d="M838 254 L785 238" class="label-line" /><text x="780" y="239" text-anchor="end" class="value">Germany · 94</text>
  <circle cx="826" cy="263" r="14" class="bubble" /><path d="M814 272 L785 286" class="label-line" /><text x="780" y="291" text-anchor="end" class="value">France · 87</text>
  <circle cx="574" cy="118" r="12" class="bubble-muted" /><text x="592" y="111" class="axis">Australia · 9</text>
  <text x="548" y="319" class="axis">0</text><text x="882" y="319" text-anchor="end" class="axis">100</text>
</svg>
</template>

<style scoped>
.brief-evidence{display:block;width:100%;height:350px;margin-top:8px;overflow:visible}text{font-family:Roboto,sans-serif;fill:#0f172a}.section-label{font-size:14px;font-weight:700;letter-spacing:.7px;fill:#0b7658}.axis,.foot{font-size:12px;fill:#64748b}.small{font-size:15px;fill:#475569}.annotation,.value{font-size:15px;font-weight:700}.metric{font-size:28px;font-weight:700}.big{font-size:20px;font-weight:700}.white{fill:white}.grid{stroke:#e2e8f0;stroke-width:1}.divider{stroke:#cbd5e1;stroke-width:1}.axis-line{stroke:#94a3b8;stroke-width:1.5}.leader{stroke:#b45309;stroke-width:1.5;fill:none}.label-line{stroke:#168793;stroke-width:1;fill:none}.base{fill:#cbd5e1}.accent{fill:#168793}.warn{fill:#b45309}.up{font-size:17px;font-weight:700;fill:#168793}.down{font-size:17px;font-weight:700;fill:#b45309}.bubble{fill:#168793;opacity:.86}.bubble-muted{fill:#b9c5d1;opacity:.9}.target-zone{fill:#e2f1ee;stroke:#168793;stroke-dasharray:4 4}.accent-text{fill:#0b7658}
</style>
