# S204 – Abel, Barclay & Payne (BMJ Open 2016): Adjusted IMD across UK countries

## Summary in my own words

Abel, Barclay and Payne show that the four UK nations each publish their own Index of Multiple Deprivation: on LSOAs in England and Wales, Super Output Areas (SOAs) in Northern Ireland and data zones in Scotland. The indices are built differently and from data of different years, so they cannot be compared directly, and putting people from different nations into country-specific quintiles assumes equal deprivation levels across nations, which is false. They build UK-adjusted scores from the income and employment domains and show that Wales and Northern Ireland are more deprived than England and Scotland. For OULAD, a single `imd_band` across England, Wales, Scotland and Ireland regions is comparable only within a nation unless an adjusted index was used.

## Key facts

- Not comparable – "due to the fact that the four constituent nations of the UK have constructed somewhat different indices, direct comparisons between the countries on the basis of these indices is not possible"
- Geographies – "The IMD are defined for lower layer super output areas (LSOAs) in England and Wales, super output areas (SOAs) in Northern Ireland and data zones in Scotland."
- Counts – "There are 32 844 LSOAs in England and 1909 LSOAs in Wales, with 890 SOAs in Northern Ireland and 6505 data zones in Scotland."
- Different data years – "The source data for different countries relate to different years, which may introduce error to UK-wide indices."
- Naive quintiles mislead – "As average deprivation levels may differ between countries, this may give misleading results."
- Northern Ireland most deprived – "Northern Ireland was the most deprived of all the UK countries."
- National indices cited: Office of the Chief Statistician and Performance (Scottish IMD 2012), DCLG (English indices 2015; S203), Northern Ireland Statistics and Research Agency (NI Multiple Deprivation Measure 2010), Welsh Government (Welsh IMD 2014) – "Northern Ireland multiple deprivation measure 2010"

## Used in

02-03-codes-sensitive.md (`imd_band` comparability across regions), 03-02-missingness-validity.md, 03-04-temporal-representativeness.md (region and IMD representativeness).

## Against reference.md

Extends the outline items "sensitive attributes" (Section 2) and "representativeness" (Section 3). No contradiction.

## Reliability

Primary, peer-reviewed: BMJ Open 6(11), e012750 (2016); authors at University of Exeter and University of Bristol. Read from the PubMed Central full text. Citation traction: 216 citations in OpenAlex ("cited_by_count (OpenAlex): 216"), as of 2026-11-06.

## Open questions

The paper does not discuss OULAD; whether OU mapped Welsh and Scottish students to their own national indices or left `imd_band` empty is not documented. The Republic of Ireland has no UK IMD at all.
