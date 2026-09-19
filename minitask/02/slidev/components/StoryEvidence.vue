<script setup lang="ts">
defineProps<{ kind: 'cancellations' | 'adjustment' | 'activity' | 'peaks' | 'countries' | 'bundles' }>()
const activity = [
 { label: 'Người mua có ID', a: 739, b: 1660, max: 1800, av: '739', bv: '1,660', change: '+124.6%', color: '#168793' },
 { label: 'Hóa đơn / người mua', a: 1.33, b: 1.59, max: 1.8, av: '1.33', bv: '1.59', change: '+19.5%', color: '#168793' },
 { label: 'Gross / người mua', a: 761.41, b: 684.66, max: 850, av: '£761.41', bv: '£684.66', change: '−10.1%', color: '#b45309' },
]
const peaks = [
 { label: 'Regency Cakestand', month: 0 },
 { label: 'White Hanging Heart', month: 1 },
 { label: 'Party Bunting', month: 5 },
 { label: 'Jumbo Bag / Rabbit Night Light', month: 11 },
 { label: 'Paper Chain / Chilli Lights', month: 11 },
]
const countries = [
 { name: 'Germany', sku: 'Regency Cakestand · 22423', value: 4.12, color: '#0b7658' },
 { name: 'France', sku: 'Rabbit Night Light · 23084', value: 4.00, color: '#168793' },
 { name: 'Australia', sku: 'Rabbit Night Light · 23084', value: 2.47, color: '#168793' },
 { name: 'Japan', sku: 'Rabbit Night Light · 23084', value: 17.19, color: '#168793' },
]
const pairs = [
 { name: 'Jumbo Bag · Red / Pink Polkadot', sku: '85099B / 22386', observed: 825, expected: 2089*1218/19773, lift: '6.41' },
 { name: 'Regency Teacup · Roses / Green', sku: '22699 / 22697', observed: 767, expected: 1065*1013/19773, lift: '14.06' },
]
</script>
<template>
<svg v-if="kind === 'cancellations'" viewBox="0 0 880 310" role="img" aria-label="Hai cặp đảo ngược chiếm 51.62% giá trị hủy; giao dịch mua và hủy cách nhau 16 và 12 phút.">
 <text x="0" y="24" class="caption">Tổng giá trị hủy £475,901.16</text>
 <rect x="0" y="42" width="139.48" height="52" fill="#b45309"/><rect x="139.48" y="42" width="304.47" height="52" fill="#dc7c24"/><rect x="443.95" y="42" width="416.05" height="52" fill="#cbd5e1"/>
 <text x="222" y="75" text-anchor="middle" class="white bold">Hai cặp: 51.62%</text><text x="651" y="75" text-anchor="middle">Các hủy còn lại: 48.38%</text>
 <text x="0" y="147" class="bold">18/01/2011 · £77,183.60</text><text x="0" y="174" class="small">Khách 12346 · SKU 23166</text>
 <line x1="420" y1="155" x2="790" y2="155" stroke="#b45309" stroke-width="3"/><circle cx="420" cy="155" r="7" fill="#168793"/><circle cx="790" cy="155" r="7" fill="#b45309"/>
 <text x="420" y="135" text-anchor="middle">Mua 10:01</text><text x="790" y="135" text-anchor="middle">Hủy 10:17</text><text x="605" y="183" text-anchor="middle" class="bold">16 phút</text>
 <text x="0" y="241" class="bold">09/12/2011 · £168,469.60</text><text x="0" y="268" class="small">Khách 16446 · SKU 23843</text>
 <line x1="420" y1="249" x2="697.5" y2="249" stroke="#dc7c24" stroke-width="3"/><circle cx="420" cy="249" r="7" fill="#168793"/><circle cx="697.5" cy="249" r="7" fill="#dc7c24"/>
 <text x="420" y="229" text-anchor="middle">Mua 09:15</text><text x="697.5" y="229" text-anchor="middle">Hủy 09:27</text><text x="559" y="278" text-anchor="middle" class="bold">12 phút</text>
</svg>
<svg v-else-if="kind === 'adjustment'" viewBox="0 0 880 310" role="img" aria-label="Tỷ lệ hủy thô 4.64%, điều chỉnh 2.30%. Net không đổi, đây là phân tích độ nhạy.">
 <text x="0" y="24" class="caption">Hủy / gross sales · cùng thang đo, bắt đầu từ 0%</text>
 <g v-for="tick in [0,1,2,3,4,5]" :key="tick"><line :x1="220+tick*105" :x2="220+tick*105" y1="48" y2="196" stroke="#e2e8f0"/><text :x="220+tick*105" y="220" text-anchor="middle" class="small">{{tick}}%</text></g>
 <text x="0" y="88">Toàn bộ hợp lệ</text><rect x="220" y="59" :width="4.64*105" height="42" fill="#b45309"/><text x="727" y="88" class="bold">4.64%</text>
 <text x="0" y="166">Bỏ cả mua và hủy</text><rect x="220" y="137" :width="2.30*105" height="42" fill="#168793"/><text x="481" y="166" class="bold">2.30%</text>
 <rect x="0" y="251" width="860" height="49" rx="4" fill="#e2f1ee"/><text x="430" y="282" text-anchor="middle" class="bold">Net sales vẫn là £9,771,318.16 ở cả hai phạm vi</text>
</svg>
<svg v-else-if="kind === 'activity'" viewBox="0 0 880 310" role="img" aria-label="Tháng 1 đến tháng 11: người mua tăng 124.6%, hóa đơn mỗi người tăng 19.5%, gross mỗi người giảm 10.1%.">
 <rect x="0" y="5" width="14" height="14" fill="#cbd5e1"/><text x="23" y="18" class="small">01/2011</text><rect x="135" y="5" width="14" height="14" fill="#168793"/><text x="158" y="18" class="small">11/2011 · ba thang đo riêng, đều bắt đầu từ 0</text>
 <g v-for="(row,i) in activity" :key="row.label" :transform="`translate(${i*295},0)`">
 <text x="0" y="63" class="bold">{{row.label}}</text><text x="0" y="105" class="big" :fill="row.color">{{row.change}}</text>
 <line x1="0" x2="0" y1="132" y2="238" stroke="#94a3b8"/>
 <rect x="0" y="140" :width="row.a/row.max*205" height="31" fill="#cbd5e1"/><text x="0" y="133" class="small">{{row.av}}</text>
 <rect x="0" y="198" :width="row.b/row.max*205" height="31" :fill="row.color"/><text x="0" y="192" class="small">{{row.bv}}</text>
 <text x="0" y="257" class="small">0</text>
 </g>
 <text x="0" y="295" class="caption">Tăng quy mô người mua không đồng nghĩa mỗi người chi tiêu nhiều hơn.</text>
</svg>
<svg v-else-if="kind === 'peaks'" viewBox="0 0 880 310" role="img" aria-label="Tháng gross sales cao nhất khác nhau theo sản phẩm: tháng 12 năm 2010, tháng 1, tháng 5 và tháng 11 năm 2011.">
 <text x="0" y="19" class="caption">Chấm = tháng có gross sales cao nhất của SKU trong kỳ</text>
 <g v-for="i in [0,1,5,11]" :key="i"><line :x1="350+i*42" :x2="350+i*42" y1="65" y2="282" stroke="#cbd5e1"/><text :x="350+i*42" y="49" :text-anchor="i===0 ? 'end' : i===1 ? 'start' : 'middle'" class="small">{{i===0?'12/2010':`${String(i).padStart(2,'0')}/2011`}}</text></g>
 <g v-for="(row,i) in peaks" :key="row.label"><text x="0" :y="90+i*43">{{row.label}}</text><line x1="350" x2="812" :y1="84+i*43" :y2="84+i*43" stroke="#e2e8f0"/><circle :cx="350+row.month*42" :cy="84+i*43" r="9" :fill="row.month===11?'#168793':'#64748b'"/></g>
</svg>
<svg v-else-if="kind === 'countries'" viewBox="0 0 880 310" role="img" aria-label="Tỷ trọng SKU dẫn đầu trong net sales từng nước: Đức 4.12%, Pháp 4%, Australia 2.47%, Nhật 17.19%.">
 <text x="0" y="21" class="caption">Net của SKU / tổng net hàng hóa trong nước (%)</text>
 <g v-for="tick in [0,5,10,15,20]" :key="tick"><line :x1="370+tick*21" :x2="370+tick*21" y1="43" y2="274" stroke="#e2e8f0"/><text :x="370+tick*21" y="296" text-anchor="middle" class="small">{{tick}}%</text></g>
 <g v-for="(row,i) in countries" :key="row.name"><text x="0" :y="64+i*59" class="bold">{{row.name}}</text><text x="0" :y="85+i*59" class="small">{{row.sku}}</text><rect x="370" :y="50+i*59" :width="row.value*21" height="28" :fill="row.color"/><text :x="380+row.value*21" :y="71+i*59" class="bold">{{row.value.toFixed(2)}}%</text></g>
</svg>
<svg v-else viewBox="0 0 880 310" role="img" aria-label="Mua kèm quan sát so với kỳ vọng độc lập: 825 so với 128.7 hóa đơn và 767 so với 54.6 hóa đơn. Không phải hiệu quả thử nghiệm.">
 <rect x="0" y="4" width="14" height="14" fill="#cbd5e1"/><text x="23" y="17" class="small">Kỳ vọng nếu độc lập</text><rect x="280" y="4" width="14" height="14" fill="#168793"/><text x="303" y="17" class="small">Quan sát · số hóa đơn mua kèm</text>
 <g v-for="(row,i) in pairs" :key="row.sku" :transform="`translate(${i*445},0)`">
 <text x="0" y="61" class="bold">{{row.name}}</text><text x="0" y="85" class="small">{{row.sku}}</text>
 <rect x="0" y="112" :width="row.expected/900*325" height="35" fill="#cbd5e1"/><text :x="row.expected/900*325+12" y="137">{{row.expected.toFixed(1)}}</text>
 <rect x="0" y="166" :width="row.observed/900*325" height="35" fill="#168793"/><text :x="row.observed/900*325+12" y="191" class="bold">{{row.observed}}</text>
 <line x1="0" x2="325" y1="212" y2="212" stroke="#94a3b8"/><text x="0" y="233" class="small">0</text><text x="325" y="233" text-anchor="end" class="small">900 hóa đơn</text>
 <text x="0" y="286" class="big">Lift {{row.lift}}</text>
 </g>
</svg>
</template>
<style scoped>
svg{display:block;width:100%;height:300px;margin-top:20px;overflow:visible}text{font-family:Roboto,sans-serif;font-size:18px;fill:#0f172a}.small{font-size:14px;fill:#64748b}.caption{font-size:16px;fill:#475569}.bold{font-weight:700}.white{fill:white}.big{font-size:32px;font-weight:700}
</style>
