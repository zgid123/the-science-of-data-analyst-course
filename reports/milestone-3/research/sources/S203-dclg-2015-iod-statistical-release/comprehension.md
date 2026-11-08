# S203 – DCLG (2015). The English Indices of Deprivation 2015: Statistical release

## Summary in my own words

The Department for Communities and Local Government (DCLG) released the English Indices of Deprivation 2015 on 30 September 2015. They measure relative deprivation for 32,844 Lower-layer Super Output Areas (LSOAs) in England, each with about 1,500 residents. The Index of Multiple Deprivation (IMD) 2015 combines 37 indicators in seven weighted domains, mostly from 2012/13 data, and ranks every LSOA; the ranks are split into ten equal groups (deciles). The release stresses that the IMD measures relative deprivation of an area, not of every person living in it, and covers England only. For OULAD, `imd_band` is a band of this kind of area-level, England-based relative ranking (the descriptor S002 cites Smith et al., 2015, the Technical Report of the same indices).

## Key facts

- Scope England – "The English Indices of Deprivation measure relative levels of deprivation in 32,844 small areas or neighbourhoods, called Lower-layer Super Output Areas, in England"
- Data years – "Most of the indicators used for these statistics are from 2012/13"
- Area, not person – "these statistics are a measure of relative deprivation, not affluence, and to recognise that not every person in a highly deprived area will themselves be deprived"
- Construction – "The English Indices of Deprivation 2015 are based on 37 separate indicators, organised across seven distinct domains1 of deprivation"
- Deciles – "The 32,844 neighbourhoods have been divided according to their deprivation rank into 10 equal groups (deciles)."
- No fixed threshold – "the Indices of Deprivation are a continuous scale of deprivation"
- LSOA size – "with an average of approximately 1,500 residents or 650 households"
- Companion documents – "A full Research Report, Technical Report and guidance documents accompany the release"; the Technical Report is Smith T. et al. (DCLG 2015), cited by the OULAD descriptor (S002) as its IMD reference.

## Used in

02-03-codes-sensitive.md (definition of `imd_band`), 03-02-missingness-validity.md (why `imd_band` can be missing or not comparable), 03-04-temporal-representativeness.md (IMD reference years).

## Against reference.md

Extends the outline items "categorical codes, sensitive attributes" (Section 2) and "representativeness" (Section 3): the IMD is England-only and area-based. No contradiction. Note: OULAD covers 2013–2014 while the IMD 2015 was released in September 2015; S002 cites the 2015 Technical Report, so which IMD edition (2010 or 2015) the OU used for each student is not stated.

## Reliability

Primary: UK government official statistics (DCLG, gov.uk publishing service), PDF fetched directly. Citation traction not applicable (official statistics).

## Open questions

Which IMD edition (2010 or 2015) underlies OULAD `imd_band`, and how the OU assigned a band to students in Wales, Scotland and Ireland, is not documented in any source on disk. OULAD bands are 10-percentage-point ranges (e.g. "0-10%"), which match the deciles, but the descriptor does not say so explicitly.
