"""Content for /colorado-radon-map/ — Colorado Radon Map landing page.

One new page:
  /colorado-radon-map/   — what the EPA Map of Radon Zones means for Colorado,
                          how to read it, what it does not tell you, and where
                          to go next. Pairs the EPA zone map with CDPHE
                          county-level test data (COEPHT 2005-2017).
"""
import json
from pages_main import s, SOURCES

# Register the new source URLs used on this page (idempotent).
SOURCES.setdefault("epa_map_radon_zones", "https://www.epa.gov/radon/epa-map-radon-zones")
SOURCES.setdefault("epa_action_level_def", "https://www.epa.gov/radon/what-epas-action-level-radon-and-what-does-it-mean")
SOURCES.setdefault("cdphe_testing", "https://cdphe.colorado.gov/hm/testing-your-home-radon")
SOURCES.setdefault("coepht_radon_data", "https://coepht.colorado.gov/radon-data")
SOURCES.setdefault("coepht_radon_viz", "https://cohealthviz.dphe.state.co.us/t/EnvironmentalEpidemiologyPublic/views/Radon/RadonMeasures")
SOURCES.setdefault("epa_health_risk_radon", "https://www.epa.gov/radon/health-risk-radon")


# =========================================================================
# The Colorado map — inline SVG visualization.
#
# Geographic facts:
#   Colorado bounded by 37N-41N latitude, 102.03W-109.03W longitude.
#   Projects to a near-perfect rectangle. 64 counties total.
#   EPA Map of Radon Zones (1993) classifies:
#     - 53 counties as Zone 1 (highest predicted indoor radon >4 pCi/L avg)
#     - 11 counties as Zone 2 (moderate, 2-4 pCi/L avg)
#     - 0  counties as Zone 3 (low, <2 pCi/L avg)
#
# The 11 Zone 2 counties cluster into four geographic regions:
#   - NW corner:           Routt
#   - Central Mountains:   Eagle
#   - SW San Juan Mtns:    Hinsdale, Mineral, San Juan
#   - San Luis Valley:     Alamosa, Conejos, Costilla, Rio Grande, Saguache,
#                          Archuleta (Pagosa Springs)
#
# The SVG below is generated from US Census Cartographic Boundary 20m
# resolution GeoJSON via Ramer-Douglas-Peucker simplification (epsilon
# 0.005 degrees) and an equirectangular projection with cos(mean_lat)
# correction. Source: https://www.epa.gov/radon/epa-map-radon-zones
# Each county <path> carries a <title> for accessibility/screen-reader
# labeling. Regenerate via /agent/workspace/build_co_map_svg.py.
# =========================================================================
COLORADO_MAP_SVG = """
<svg viewBox="0 0 703 590" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="co-map-title co-map-desc" class="co-map">
<title id="co-map-title">Colorado radon zones map by county</title>
<desc id="co-map-desc">A map of Colorado showing all 64 counties shaded by EPA radon zone classification. Fifty-three counties are Zone 1 (highest predicted indoor radon, shown in darker terracotta). Eleven counties are Zone 2 (moderate, shown in lighter wheat color): Alamosa, Archuleta, Conejos, Costilla, Eagle, Hinsdale, Mineral, Rio Grande, Routt, Saguache, and San Juan. No counties are Zone 3. The Zone 2 counties cluster in the northwest (Routt), the central mountains (Eagle), the southwest San Juan Mountains (Hinsdale, Mineral, San Juan), and the San Luis Valley plus Archuleta County in the south.</desc>
<text x="351.5" y="28" text-anchor="middle" font-family="Fraunces, serif" font-size="20" font-weight="600" fill="#14181c">EPA Radon Zones in Colorado</text>
<g stroke="#ffffff" stroke-width="0.6" stroke-linejoin="round">
<path d="M515.2,185.3L410.4,185.3L412.9,182.0L423.8,182.0L421.3,175.8L434.0,175.4L435.7,167.1L427.5,165.4L418.7,178.7L395.4,179.5L395.4,171.6L395.5,165.4L403.6,155.5L515.2,155.6Z" fill="#c97a52" fill-opacity="0.62"><title>Adams County (Zone 1)</title></path>
<path d="M357.0,432.7L334.1,458.0L307.8,458.0L307.8,413.2L359.5,412.9Z" fill="#e5b86f" fill-opacity="0.95"><title>Alamosa County (Zone 2)</title></path>
<path d="M410.4,185.3L515.2,185.3L515.1,205.2L395.3,205.2L395.4,197.7L397.1,198.2L397.3,194.8L398.8,192.3L406.2,195.3L407.9,198.6L410.4,198.6L410.8,195.3L411.2,196.3L413.6,194.6Z" fill="#c97a52" fill-opacity="0.62"><title>Arapahoe County (Zone 1)</title></path>
<path d="M268.9,499.6L179.5,498.9L179.4,450.5L210.9,450.5L210.9,454.0L250.9,452.7L250.9,472.7Z" fill="#e5b86f" fill-opacity="0.95"><title>Archuleta County (Zone 2)</title></path>
<path d="M663.2,499.6L570.4,498.9L571.3,425.2L663.2,425.1L663.2,496.0Z" fill="#c97a52" fill-opacity="0.62"><title>Baca County (Zone 1)</title></path>
<path d="M542.1,408.2L542.4,354.1L600.9,353.9L600.5,425.2L542.1,425.2Z" fill="#c97a52" fill-opacity="0.62"><title>Bent County (Zone 1)</title></path>
<path d="M395.3,125.6L395.5,158.1L392.4,160.2L393.8,160.4L393.4,162.1L390.5,162.8L390.4,164.2L389.6,163.1L390.4,161.2L389.4,161.1L390.4,160.5L388.8,160.8L388.8,162.5L387.1,163.7L387.1,165.4L364.8,165.5L364.8,163.0L340.1,163.3L343.3,151.1L342.1,125.8L382.7,125.7Z" fill="#c97a52" fill-opacity="0.62"><title>Boulder County (Zone 1)</title></path>
<path d="M387.1,165.4L387.1,163.7L388.8,162.5L388.8,160.8L390.4,160.5L389.4,161.1L390.4,161.2L389.6,163.1L390.4,164.2L390.5,162.8L393.4,162.1L393.8,160.4L392.3,160.4L395.5,158.1L395.5,155.5L399.4,155.5L399.4,154.7L399.5,155.5L399.4,154.7L401.1,154.7L401.1,153.9L400.2,153.9L400.2,152.6L401.9,152.2L402.0,150.5L403.6,150.5L403.6,155.5L395.5,165.4Z" fill="#c97a52" fill-opacity="0.62"><title>Broomfield County (Zone 1)</title></path>
<path d="M259.8,263.4L294.2,263.6L301.4,276.9L308.7,276.5L317.9,284.6L319.5,292.1L313.9,305.1L322.0,314.9L319.3,326.6L310.3,333.3L289.3,336.1L271.0,304.5L282.2,280.2L269.9,280.3L257.9,270.2L258.6,267.1L258.1,264.9L259.6,264.4Z" fill="#c97a52" fill-opacity="0.62"><title>Chaffee County (Zone 1)</title></path>
<path d="M662.8,264.6L662.9,314.0L562.6,314.3L563.5,265.7Z" fill="#c97a52" fill-opacity="0.62"><title>Cheyenne County (Zone 1)</title></path>
<path d="M364.7,205.2L326.4,205.4L329.6,197.2L317.9,190.0L321.2,178.8L334.7,177.9L338.8,172.5L351.7,181.5L364.8,184.5Z" fill="#c97a52" fill-opacity="0.62"><title>Clear Creek County (Zone 1)</title></path>
<path d="M336.3,499.3L268.9,499.6L250.9,472.7L250.9,452.7L307.7,453.0L307.8,458.0L334.1,458.0L335.3,478.2L331.7,491.9Z" fill="#e5b86f" fill-opacity="0.95"><title>Conejos County (Zone 2)</title></path>
<path d="M386.4,499.4L336.3,499.3L331.7,491.9L335.3,478.2L334.1,458.0L357.0,432.7L373.9,424.0L383.5,427.9L386.4,465.3Z" fill="#e5b86f" fill-opacity="0.95"><title>Costilla County (Zone 2)</title></path>
<path d="M533.4,354.1L532.7,364.7L522.9,364.8L522.9,371.5L503.7,371.5L483.9,367.7L484.3,324.7L533.1,325.3Z" fill="#c97a52" fill-opacity="0.62"><title>Crowley County (Zone 1)</title></path>
<path d="M395.8,354.9L395.7,394.1L382.9,383.6L374.8,395.9L372.0,391.4L358.1,396.3L346.4,383.4L340.0,367.7L329.3,354.1Z" fill="#c97a52" fill-opacity="0.62"><title>Custer County (Zone 1)</title></path>
<path d="M177.8,307.9L99.7,308.0L99.7,289.6L146.0,260.9L154.2,265.0L177.8,245.1Z" fill="#c97a52" fill-opacity="0.62"><title>Delta County (Zone 1)</title></path>
<path d="M395.4,198.9L394.9,199.7L391.5,199.7L394.4,199.0L392.9,197.7L392.0,198.6L390.4,198.3L390.4,197.3L393.6,197.1L393.7,196.1L395.3,195.4L393.8,195.7L394.2,194.9L392.9,194.2L392.9,193.3L395.4,193.6L394.5,192.2L395.4,191.9L395.4,180.3L394.6,180.3L394.4,179.5L418.7,178.7L427.5,165.4L435.7,167.1L434.0,175.4L421.3,175.8L423.8,182.0L412.9,182.0L410.4,185.3L413.8,194.8L411.2,196.3L410.8,195.3L410.4,198.6L407.9,198.6L406.2,195.3L398.8,192.3L397.3,194.8L397.1,198.2L395.4,197.7ZM392.9,197.4L392.9,197.3Z" fill="#c97a52" fill-opacity="0.62"><title>Denver County (Zone 1)</title></path>
<path d="M40.7,438.1L40.7,398.0L110.6,396.5L114.8,404.9L134.3,400.8L145.7,410.1L136.1,419.2L136.0,425.7L51.8,426.5L40.6,443.3Z" fill="#c97a52" fill-opacity="0.62"><title>Dolores County (Zone 1)</title></path>
<path d="M395.8,205.2L430.3,205.2L430.1,255.2L370.9,255.2L377.0,245.9Z" fill="#c97a52" fill-opacity="0.62"><title>Douglas County (Zone 1)</title></path>
<path d="M292.8,226.6L273.3,228.6L212.2,228.1L212.2,164.8L272.6,164.2L276.9,182.2L295.4,200.3L288.9,216.8Z" fill="#e5b86f" fill-opacity="0.95"><title>Eagle County (Zone 2)</title></path>
<path d="M484.3,324.7L405.4,325.0L405.6,293.2L393.7,293.0L397.6,285.0L397.2,255.1L484.5,255.3L484.1,285.0Z" fill="#c97a52" fill-opacity="0.62"><title>El Paso County (Zone 1)</title></path>
<path d="M430.1,255.2L430.3,205.2L514.5,205.2L514.0,285.2L484.1,285.0L484.5,255.3Z" fill="#c97a52" fill-opacity="0.62"><title>Elbert County (Zone 1)</title></path>
<path d="M405.4,325.0L405.5,354.9L329.3,354.1L310.3,333.3L319.3,326.6L322.0,314.9L313.9,305.1L379.0,304.7L378.8,310.3L405.3,310.1Z" fill="#c97a52" fill-opacity="0.62"><title>Fremont County (Zone 1)</title></path>
<path d="M39.9,228.0L39.9,194.4L138.8,190.5L138.8,175.6L183.9,175.2L183.9,165.0L194.0,165.3L194.1,145.2L219.0,145.1L219.3,164.9L212.2,164.8L212.2,228.1L55.5,228.1Z" fill="#c97a52" fill-opacity="0.62"><title>Garfield County (Zone 1)</title></path>
<path d="M364.8,165.5L364.8,184.5L351.7,181.5L338.8,172.5L340.1,163.3L364.8,163.0Z" fill="#c97a52" fill-opacity="0.62"><title>Gilpin County (Zone 1)</title></path>
<path d="M253.2,104.6L256.8,112.2L267.7,108.5L271.8,115.9L279.8,114.7L290.8,118.6L309.6,112.9L314.8,115.7L320.9,101.0L324.1,99.9L342.1,125.8L343.3,151.1L340.1,163.3L338.8,172.5L334.7,177.9L321.2,178.8L317.9,190.0L309.1,191.2L303.8,177.8L288.8,165.3L272.6,164.2L255.5,164.2L255.0,116.5Z" fill="#c97a52" fill-opacity="0.62"><title>Grand County (Zone 1)</title></path>
<path d="M177.8,245.1L187.2,240.7L188.9,247.4L197.2,256.4L216.4,256.4L222.2,265.2L230.6,270.9L239.9,272.5L249.4,263.6L269.9,280.3L282.2,280.2L271.0,304.5L289.3,336.1L222.2,335.7L222.2,367.6L171.7,367.6L165.8,349.9L177.8,349.9L177.8,307.9Z" fill="#c97a52" fill-opacity="0.62"><title>Gunnison County (Zone 1)</title></path>
<path d="M179.4,450.5L179.4,425.7L180.6,406.2L176.4,404.3L171.7,388.4L176.9,377.5L171.7,367.6L222.2,367.6L222.2,389.5L210.0,391.4L209.4,421.6L211.3,421.6L210.9,450.5Z" fill="#e5b86f" fill-opacity="0.95"><title>Hinsdale County (Zone 2)</title></path>
<path d="M358.1,396.3L372.0,391.4L374.8,395.9L382.9,383.6L395.7,394.1L398.9,398.0L431.6,395.8L457.9,405.3L448.6,414.1L440.3,429.1L440.3,433.1L431.3,442.2L427.2,443.3L427.3,448.5L422.5,452.3L400.6,455.9L386.4,465.3L383.5,427.9L373.9,424.0L357.0,432.7L359.5,412.9L362.0,401.4Z" fill="#c97a52" fill-opacity="0.62"><title>Huerfano County (Zone 1)</title></path>
<path d="M282.7,41.2L294.3,41.4L294.7,48.7L306.1,62.1L324.1,99.9L320.9,101.0L314.8,115.7L309.6,112.9L290.8,118.6L279.8,114.7L271.8,115.9L267.7,108.5L256.8,112.2L253.2,104.6L248.4,85.0L254.6,65.2L253.0,58.4L237.9,48.9L235.4,49.7L234.9,40.8L276.9,41.0Z" fill="#c97a52" fill-opacity="0.62"><title>Jackson County (Zone 1)</title></path>
<path d="M392.9,197.4L393.0,197.4ZM391.9,199.2L394.9,199.7L395.4,198.9L395.3,205.2L395.8,205.2L377.0,245.9L370.9,255.2L364.8,255.2L364.8,165.5L395.5,165.4L395.4,179.5L394.4,179.7L395.4,180.3L395.4,191.9L394.5,192.2L395.4,193.6L392.9,193.5L393.3,194.6L394.2,194.9L393.8,195.7L395.3,195.4L393.7,196.1L393.6,197.1L390.4,197.3L390.5,198.6L392.9,197.7L394.4,199.0L391.9,199.2Z" fill="#c97a52" fill-opacity="0.62"><title>Jefferson County (Zone 1)</title></path>
<path d="M662.9,317.9L663.0,353.7L533.4,354.1L533.1,325.3L562.6,324.3L562.6,314.3L662.9,314.0Z" fill="#c97a52" fill-opacity="0.62"><title>Kiowa County (Zone 1)</title></path>
<path d="M662.5,204.3L662.8,264.6L563.5,265.7L564.3,205.3L595.5,205.0Z" fill="#c97a52" fill-opacity="0.62"><title>Kit Carson County (Zone 1)</title></path>
<path d="M179.5,498.9L99.7,498.9L115.8,458.2L130.0,447.1L131.3,431.2L136.0,425.7L179.4,425.7L179.4,450.5Z" fill="#c97a52" fill-opacity="0.62"><title>La Plata County (Zone 1)</title></path>
<path d="M273.3,228.6L299.2,226.6L294.9,234.6L294.2,263.6L259.8,263.4L266.0,250.9L268.1,234.2Z" fill="#c97a52" fill-opacity="0.62"><title>Lake County (Zone 1)</title></path>
<path d="M375.5,41.4L405.2,41.4L405.0,115.6L395.1,115.6L395.3,125.6L342.1,125.8L324.1,99.9L306.1,62.1L294.7,48.7L294.3,41.4L375.5,41.4Z" fill="#c97a52" fill-opacity="0.62"><title>Larimer County (Zone 1)</title></path>
<path d="M488.4,499.3L386.4,499.4L386.4,465.3L400.6,455.9L422.5,452.3L427.3,448.5L427.2,443.3L431.3,442.2L440.3,433.1L440.3,429.1L448.6,414.1L457.9,405.3L483.6,414.8L483.9,425.2L571.3,425.2L570.4,498.9L512.7,499.1Z" fill="#c97a52" fill-opacity="0.62"><title>Las Animas County (Zone 1)</title></path>
<path d="M533.1,325.3L484.3,324.7L484.1,285.0L514.0,285.2L514.5,205.2L564.3,205.3L562.6,324.3Z" fill="#c97a52" fill-opacity="0.62"><title>Lincoln County (Zone 1)</title></path>
<path d="M526.9,40.9L608.8,40.9L609.0,69.8L607.8,105.4L536.6,105.6L536.5,95.7L526.3,95.7Z" fill="#c97a52" fill-opacity="0.62"><title>Logan County (Zone 1)</title></path>
<path d="M39.1,327.2L39.9,228.0L184.0,228.1L180.9,233.1L187.2,240.7L177.8,245.1L154.2,265.0L146.0,260.9L99.7,289.6L99.7,327.2Z" fill="#c97a52" fill-opacity="0.62"><title>Mesa County (Zone 1)</title></path>
<path d="M249.5,403.3L247.9,422.8L248.0,452.6L210.9,454.0L211.3,421.6L209.4,421.6L210.0,391.4L222.2,389.5L233.0,388.9L249.6,398.9Z" fill="#e5b86f" fill-opacity="0.95"><title>Mineral County (Zone 2)</title></path>
<path d="M40.0,41.1L194.0,40.8L194.4,86.9L184.2,93.5L183.2,130.3L39.9,130.1L40.2,79.8Z" fill="#c97a52" fill-opacity="0.62"><title>Moffat County (Zone 1)</title></path>
<path d="M40.4,455.9L40.6,443.3L51.8,426.5L136.0,425.7L131.3,431.2L130.0,447.1L115.8,458.2L99.7,498.9L40.4,499.0L40.4,486.0Z" fill="#c97a52" fill-opacity="0.62"><title>Montezuma County (Zone 1)</title></path>
<path d="M40.7,366.6L39.1,352.9L39.1,327.2L99.7,327.2L99.7,308.0L177.8,307.9L177.8,349.9L165.8,349.9L165.8,346.4L121.6,346.5L125.7,355.2L138.9,359.4L136.4,367.0L40.7,366.9Z" fill="#c97a52" fill-opacity="0.62"><title>Montrose County (Zone 1)</title></path>
<path d="M475.7,155.5L475.9,95.6L536.5,95.7L536.0,155.4L515.3,155.4Z" fill="#c97a52" fill-opacity="0.62"><title>Morgan County (Zone 1)</title></path>
<path d="M522.9,371.5L522.9,364.8L532.7,364.7L533.4,354.1L542.4,354.1L542.1,425.2L483.9,425.2L483.9,367.7L503.7,371.5Z" fill="#c97a52" fill-opacity="0.62"><title>Otero County (Zone 1)</title></path>
<path d="M156.6,395.2L151.6,385.7L142.2,381.4L143.0,371.2L136.4,367.0L138.9,359.4L125.7,355.2L121.6,346.5L165.8,346.4L165.8,349.9L171.7,367.6L176.9,377.5L171.7,388.4Z" fill="#c97a52" fill-opacity="0.62"><title>Ouray County (Zone 1)</title></path>
<path d="M364.7,205.2L364.8,255.2L370.8,255.2L370.9,304.6L313.9,305.1L319.5,292.1L317.9,284.6L308.7,276.5L301.4,276.9L294.2,263.6L294.9,234.6L299.2,226.6L309.7,228.2L314.2,219.9L327.4,208.4L326.4,205.4L347.9,205.0Z" fill="#c97a52" fill-opacity="0.62"><title>Park County (Zone 1)</title></path>
<path d="M662.4,75.8L662.4,105.2L607.8,105.4L609.0,69.8L662.4,69.8Z" fill="#c97a52" fill-opacity="0.62"><title>Phillips County (Zone 1)</title></path>
<path d="M187.2,240.7L180.9,233.1L184.0,228.1L273.3,228.6L268.1,234.2L266.0,250.9L259.6,264.4L258.1,264.9L258.6,267.1L257.9,270.2L249.4,263.6L239.9,272.5L230.6,270.9L222.2,265.2L216.4,256.4L197.2,256.4L188.9,247.4Z" fill="#c97a52" fill-opacity="0.62"><title>Pitkin County (Zone 1)</title></path>
<path d="M663.0,354.4L663.2,425.1L600.5,425.2L600.9,353.9L663.0,353.7Z" fill="#c97a52" fill-opacity="0.62"><title>Prowers County (Zone 1)</title></path>
<path d="M484.3,324.7L483.6,414.8L431.6,395.8L398.9,398.0L395.7,394.1L395.8,354.9L405.5,354.9L405.4,325.0Z" fill="#c97a52" fill-opacity="0.62"><title>Pueblo County (Zone 1)</title></path>
<path d="M39.9,148.8L39.9,130.1L218.9,129.8L219.0,145.1L194.1,145.2L194.0,165.3L183.9,165.0L183.9,175.2L138.8,175.6L138.8,190.5L39.9,194.4Z" fill="#c97a52" fill-opacity="0.62"><title>Rio Blanco County (Zone 1)</title></path>
<path d="M248.0,452.6L247.9,422.8L249.5,403.3L259.0,403.4L259.1,413.3L307.8,413.2L307.7,453.0L250.9,452.7Z" fill="#e5b86f" fill-opacity="0.95"><title>Rio Grande County (Zone 2)</title></path>
<path d="M222.2,40.8L234.9,40.8L235.4,49.7L237.9,48.9L253.0,58.4L254.6,65.2L248.4,85.0L253.2,104.6L255.0,116.5L255.5,164.9L219.3,164.9L218.9,129.8L183.2,130.0L184.2,93.5L194.4,86.9L194.0,40.8Z" fill="#e5b86f" fill-opacity="0.95"><title>Routt County (Zone 2)</title></path>
<path d="M289.3,336.1L310.3,333.3L329.3,354.1L340.0,367.7L346.4,383.4L362.0,401.4L359.5,412.9L259.1,413.3L259.0,403.4L249.5,403.3L249.6,398.9L233.0,388.9L222.2,389.5L222.2,335.7Z" fill="#e5b86f" fill-opacity="0.95"><title>Saguache County (Zone 2)</title></path>
<path d="M156.6,395.2L171.7,388.4L176.4,404.3L180.6,406.2L179.4,425.7L136.0,425.7L136.1,419.2L145.7,410.1Z" fill="#e5b86f" fill-opacity="0.95"><title>San Juan County (Zone 2)</title></path>
<path d="M40.7,398.0L40.7,366.9L136.4,367.0L143.0,371.2L142.2,381.4L151.6,385.7L156.6,395.2L145.7,410.1L134.3,400.8L114.8,404.9L110.6,396.5Z" fill="#c97a52" fill-opacity="0.62"><title>San Miguel County (Zone 1)</title></path>
<path d="M608.8,40.9L662.3,40.9L662.4,69.8L609.0,69.8Z" fill="#c97a52" fill-opacity="0.62"><title>Sedgwick County (Zone 1)</title></path>
<path d="M272.6,164.2L288.8,165.3L303.8,177.8L309.1,191.2L317.9,190.0L329.6,197.2L326.4,205.4L327.4,208.4L314.2,219.9L309.7,228.2L299.1,226.6L292.8,226.6L288.9,216.8L295.4,200.3L276.9,182.2Z" fill="#c97a52" fill-opacity="0.62"><title>Summit County (Zone 1)</title></path>
<path d="M370.8,255.2L397.2,255.1L397.6,285.0L393.7,293.0L405.6,293.2L405.3,310.1L378.8,310.3L379.0,304.7L370.9,304.6Z" fill="#c97a52" fill-opacity="0.62"><title>Teller County (Zone 1)</title></path>
<path d="M515.3,155.4L536.0,155.4L536.6,105.6L597.6,105.4L595.5,155.3L595.5,205.0L515.1,205.2L515.2,155.6Z" fill="#c97a52" fill-opacity="0.62"><title>Washington County (Zone 1)</title></path>
<path d="M410.6,41.4L526.9,40.9L526.3,95.7L475.9,95.6L475.7,155.5L403.6,155.5L403.6,150.5L402.0,150.5L401.9,152.2L400.2,152.6L400.2,153.9L401.1,153.9L401.1,154.7L399.4,154.7L399.5,155.5L399.4,154.7L399.4,155.5L395.2,155.5L395.1,115.6L405.0,115.6L405.2,41.4Z" fill="#c97a52" fill-opacity="0.62"><title>Weld County (Zone 1)</title></path>
<path d="M662.4,105.2L662.5,204.3L595.5,205.0L595.5,155.3L597.6,105.4L607.8,105.4Z" fill="#c97a52" fill-opacity="0.62"><title>Yuma County (Zone 1)</title></path>
</g>
<rect x="40" y="40" width="623" height="460" fill="none" stroke="#14181c" stroke-width="1.2" stroke-opacity="0.18"/>
<g font-family="Inter, sans-serif" fill="#14181c">
<circle cx="401.0" cy="185.3" r="5" fill="#14385a" stroke="#ffffff" stroke-width="1.5"/>
<text x="409.0" y="189.3" text-anchor="start" font-size="12" font-weight="600">Denver</text>
<circle cx="416.2" cy="289.5" r="5" fill="#14385a" stroke="#ffffff" stroke-width="1.5"/>
<text x="424.2" y="293.5" text-anchor="start" font-size="12" font-weight="600">Colorado Springs</text>
<circle cx="434.8" cy="355.8" r="4" fill="#14385a" stroke="#ffffff" stroke-width="1.5"/>
<text x="442.8" y="359.8" text-anchor="start" font-size="11" font-weight="400">Pueblo</text>
<circle cx="393.0" cy="88.1" r="4" fill="#14385a" stroke="#ffffff" stroke-width="1.5"/>
<text x="401.0" y="92.1" text-anchor="start" font-size="11" font-weight="400">Fort Collins</text>
<circle cx="84.5" cy="263.1" r="4" fill="#14385a" stroke="#ffffff" stroke-width="1.5"/>
<text x="92.5" y="267.1" text-anchor="start" font-size="11" font-weight="400">Grand Junction</text>
<circle cx="144.0" cy="468.0" r="4" fill="#14385a" stroke="#ffffff" stroke-width="1.5"/>
<text x="152.0" y="472.0" text-anchor="start" font-size="11" font-weight="400">Durango</text>
</g>
<g transform="translate(58.0, 56.0)">
<path d="M 0 0 L 5 12 L 0 9 L -5 12 Z" fill="#14181c"/>
<text x="0" y="26" text-anchor="middle" font-family="Inter, sans-serif" font-size="10" font-weight="600" fill="#14181c">N</text>
</g>
<g transform="translate(40, 560)" font-family="Inter, sans-serif" fill="#14181c">
<rect x="0" y="0" width="22" height="14" fill="#c97a52" fill-opacity="0.62" stroke="#8e3d22" stroke-width="0.6"/>
<text x="30" y="11" font-size="12">Zone 1 — highest predicted radon (53 counties)</text>
<rect x="370" y="0" width="22" height="14" fill="#e5b86f" fill-opacity="0.95" stroke="#8a6d1a" stroke-width="0.6"/>
<text x="400" y="11" font-size="12">Zone 2 — moderate (11 counties)</text>
</g>
</svg>

"""


# =========================================================================
# /colorado-radon-map/  -- main body
# =========================================================================
COLORADO_MAP_BODY = f"""
<section>
  <div class="prose-wide">
    <p>If you searched for a Colorado radon map, you probably want a quick visual answer to one of two questions: <em>is my area high risk?</em> or <em>how worried should I be about radon in Colorado?</em> The honest answer to both is the same: <strong>almost all of Colorado is classified as the EPA's highest indoor-radon zone</strong> — and even in the eleven counties that aren't, CDPHE still says about <strong>one in two Colorado homes</strong> tests above the EPA action level.<sup><a href="#src-1">[1]</a></sup><sup><a href="#src-2">[2]</a></sup></p>
    <p>This page walks through what the EPA Map of Radon Zones actually shows, where to read Colorado-specific county data, and — most importantly — what the map <em>does not</em> tell you about your specific home.</p>
  </div>
</section>

<section>
  <h2>The Colorado radon zones map</h2>
  <figure class="figure co-map-figure">
    {COLORADO_MAP_SVG}
    <figcaption>
      <strong>Colorado counties by EPA radon zone.</strong> Out of Colorado's 64 counties, 53 are classified as Zone 1 (highest predicted indoor radon, shown in darker terracotta) and 11 are Zone 2 (moderate, shown in lighter wheat). Zero counties are Zone 3. The 11 Zone 2 counties cluster in four geographic regions: Routt in the northwest, Eagle in the central mountains, the southwest San Juan Mountains (Hinsdale, Mineral, San Juan), and the San Luis Valley plus Archuleta County in the south. County boundaries from U.S. Census Cartographic Boundary Files; classification from <a href="{s('epa_map_radon_zones')}" rel="noopener" target="_blank">EPA Map of Radon Zones</a>. Hover over any county for its zone classification. <strong>This map is not a substitute for testing your specific home — EPA recommends every home be tested regardless of zone.</strong><sup><a href="#src-3">[3]</a></sup>
    </figcaption>
  </figure>
  <div class="prose-wide">
    <p>The Map of Radon Zones was developed by the U.S. Environmental Protection Agency in 1993 using indoor radon measurements, geology, aerial radioactivity, soil parameters, and foundation types. EPA's own description is unambiguous: the map "is intended to help governments and other organizations target risk-reduction activities and resources" and "should not be used to determine if individual homes need to be tested."<sup><a href="#src-3">[3]</a></sup> EPA recommends every home be tested for radon, no matter where it is.</p>
  </div>
</section>

<section>
  <h2>How to read EPA radon zones</h2>
  <div class="prose-wide">
    <p>EPA divides U.S. counties into three zones based on predicted average indoor radon levels:</p>
    <table class="compact">
      <thead>
        <tr><th>Zone</th><th>Predicted average indoor radon</th><th>What it means</th></tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Zone 1</strong></td>
          <td>Greater than 4.0 pCi/L</td>
          <td>Highest predicted potential. Building codes in Zone 1 counties commonly require new construction radon-resistant features.</td>
        </tr>
        <tr>
          <td><strong>Zone 2</strong></td>
          <td>Between 2.0 and 4.0 pCi/L</td>
          <td>Moderate predicted potential. Still requires testing — many homes here come back above 4.0 pCi/L.</td>
        </tr>
        <tr>
          <td><strong>Zone 3</strong></td>
          <td>Less than 2.0 pCi/L</td>
          <td>Lowest predicted potential. EPA still recommends testing every home.</td>
        </tr>
      </tbody>
    </table>
    <p>Two things to keep in mind when reading the map:</p>
    <ul>
      <li><strong>The zone is an average across an entire county</strong> — not a verdict on any one home. Homes within a single county can vary from below 1 pCi/L to above 40 pCi/L depending on geology under the lot, foundation type, and construction.</li>
      <li><strong>The map is from 1993</strong> and has not been updated. EPA itself recommends pairing it with local data. For Colorado, that local data comes from the Colorado Department of Public Health and Environment (CDPHE) and from county-level testing results published by the Colorado Environmental Public Health Tracking program (COEPHT).<sup><a href="#src-2">[2]</a></sup><sup><a href="#src-4">[4]</a></sup></li>
    </ul>
  </div>
</section>

<section>
  <h2>Why most of Colorado is Zone 1</h2>
  <div class="prose-wide">
    <p>Colorado's geology is the short answer. The Rocky Mountain uplift produced uranium-bearing granites — particularly the Pikes Peak granite that underlies much of the Front Range — and Cretaceous-era sediments like the Pierre Shale that contain trace uranium. Uranium decays slowly through a chain of radioactive elements, eventually producing radon-222, the gas we test for. Where uranium is concentrated in bedrock, radon is concentrated in soil gas above it.</p>
    <p>That's why 53 of Colorado's 64 counties — the Front Range corridor, the eastern plains, and most of the western slope — sit in EPA Zone 1. It's not just elevation; it's the specific rock chemistry under those counties. The deeper geological story is on our <a href="/radon-basics/why-common-in-colorado/">Why radon is common in Colorado</a> page.</p>
  </div>
</section>

<section>
  <h2>The 11 Colorado counties classified as Zone 2</h2>
  <div class="prose-wide">
    <p>The eleven Zone 2 counties are not "safer" — they're just <em>less consistently elevated on average</em>. CDPHE's statement that <strong>radon is found at elevated levels in one out of every two Colorado homes</strong> applies statewide, including Zone 2 counties.<sup><a href="#src-2">[2]</a></sup></p>
    <p>The 11 Zone 2 counties cluster geographically in four regions:</p>
    <table class="compact">
      <thead>
        <tr><th>Region</th><th>Counties</th><th>What's there</th></tr>
      </thead>
      <tbody>
        <tr>
          <td>Northwest Colorado</td>
          <td>Routt</td>
          <td>Steamboat Springs and the Yampa Valley.</td>
        </tr>
        <tr>
          <td>Central Mountains</td>
          <td>Eagle</td>
          <td>Vail, Eagle, the upper Eagle River valley.</td>
        </tr>
        <tr>
          <td>Southwest San Juan Mountains</td>
          <td>Hinsdale, Mineral, San Juan</td>
          <td>Silverton, Lake City, Creede — high-elevation mountain counties.</td>
        </tr>
        <tr>
          <td>San Luis Valley + Archuleta</td>
          <td>Alamosa, Conejos, Costilla, Rio Grande, Saguache, Archuleta</td>
          <td>The San Luis Valley basin and Pagosa Springs area along the southern border.</td>
        </tr>
      </tbody>
    </table>
    <p>Why are these counties lower-average on the EPA's classification? The underlying geology differs from the Front Range uranium-bearing granites. The San Luis Valley sits on layered sediments deposited by the Rio Grande Rift; the high-elevation mountain counties have different bedrock chemistry; some of these counties also have very low population density and small testing-volume samples, which can influence the classification. Important: even with that, individual homes in Zone 2 counties absolutely can — and routinely do — test above 4.0 pCi/L. The map is a planning tool, not a per-home result.</p>
  </div>
</section>

<section>
  <h2>Beyond EPA zones: Colorado county-level test results</h2>
  <div class="prose-wide">
    <p>EPA zones are a 30-year-old planning classification. If you want a sharper signal about actual radon levels in a specific Colorado county, the Colorado Environmental Public Health Tracking program (COEPHT) publishes county-level summaries of <strong>real radon test results</strong> submitted to the state. The COEPHT dataset covers tests from 2005-2017 and includes two measures by county: average indoor radon value and percent of measurements over 4 pCi/L.<sup><a href="#src-4">[4]</a></sup></p>
    <p>Two caveats to read alongside the COEPHT data:</p>
    <ul>
      <li><strong>Sample sizes vary widely.</strong> Front Range counties with high population (El Paso, Denver, Jefferson, Larimer, Weld, Arapahoe, Boulder) have thousands of test results. Some rural counties have only dozens, which makes the percentages less reliable for those counties.</li>
      <li><strong>The data is self-selected.</strong> Test results were submitted voluntarily by homeowners, contractors, and labs. Homes that tested low and never followed up are still counted; homes that were never tested are not represented at all. The actual statewide rate is likely close to CDPHE's "one in two" headline, but per-county percentages should be read as one data point, not gospel.</li>
    </ul>
    <p>You can browse the COEPHT data two ways:</p>
    <ul>
      <li><a href="{s('coepht_radon_data')}" rel="noopener" target="_blank">COEPHT radon data hub</a> — methodology page with downloadable county-level dataset.</li>
      <li><a href="{s('coepht_radon_viz')}" rel="noopener" target="_blank">COEPHT interactive radon map (Tableau)</a> — the official Colorado map visualization with county-level average and percent-elevated overlays.</li>
    </ul>
    <p>For El Paso County specifically — the Colorado Springs region — El Paso County Public Health reports that <strong>over 40 percent of all homes tested between 2005 and 2023 in El Paso County had high levels of radon</strong>.<sup><a href="#src-5">[5]</a></sup> That's more recent than the 2005-2017 COEPHT cutoff, and it's tracked at the county level rather than the EPA zone level. If you live in El Paso County, that 40%+ number is the more accurate signal than the EPA Zone 1 classification.</p>
  </div>
</section>

<section>
  <h2>What the map does not tell you</h2>
  <div class="callout">
    <strong>Important.</strong> The EPA Radon Zone map is a <em>planning tool</em>. It tells governments and code officials where to focus radon programs. It does not tell you whether your individual home has elevated radon. That requires a test.<sup><a href="#src-3">[3]</a></sup>
  </div>
  <div class="prose-wide">
    <p>Specifically, the map cannot tell you:</p>
    <ul>
      <li><strong>Your specific home's radon level.</strong> Homes a block apart routinely test differently. Two adjacent lots can have different bedrock chemistry, different foundation construction, and different stack-effect pressure profiles.</li>
      <li><strong>Whether your neighborhood differs from the county average.</strong> Some neighborhoods built on different sediments have systematically different averages. Some new-construction subdivisions have passive radon-resistant systems built in (IRC Appendix BE) that can be activated cheaply if needed. <a href="/radon-mitigation-systems/passive-vs-active/">Passive vs active systems &rarr;</a></li>
      <li><strong>How your home's foundation type affects entry.</strong> A walk-out basement on a slope behaves differently from a fully buried basement; a crawlspace behaves differently again. <a href="/radon-basics/by-foundation-type/">Radon by foundation type &rarr;</a></li>
      <li><strong>Whether seasonal patterns matter.</strong> Colorado's winter heating season concentrates radon indoors via the stack effect — a long-term test (90+ days) catches that variability that a short-term snapshot will miss. <a href="/radon-testing/short-term-vs-long-term/">Short-term vs long-term tests &rarr;</a></li>
    </ul>
    <p>EPA's recommendation has not changed in 30 years: <strong>test every home, regardless of zone</strong>. CDPHE's recommendation matches it. The map is useful for understanding why Colorado has a radon problem in the first place. It's not useful as a substitute for testing your specific house.</p>
  </div>
</section>

<section>
  <h2>What to do next</h2>
  <div class="prose-wide">
    <p>Use the table below to pick the right starting point for your situation:</p>
    <table>
      <thead>
        <tr><th>Your situation</th><th>Start here</th></tr>
      </thead>
      <tbody>
        <tr>
          <td>I haven't tested my home yet</td>
          <td><a href="/radon-testing/">How to test for radon in Colorado</a></td>
        </tr>
        <tr>
          <td>I want to understand what a high result means before testing</td>
          <td><a href="/radon-basics/levels-explained/">Radon levels explained (2, 4, 10, 20 pCi/L)</a></td>
        </tr>
        <tr>
          <td>I got a high test result</td>
          <td><a href="/colorado-springs/failed-radon-test/">Failed radon test next steps (Colorado Springs)</a></td>
        </tr>
        <tr>
          <td>I have a mitigation quote and want to evaluate it</td>
          <td><a href="/radon-mitigation-cost/quote-too-high/">Is my radon mitigation quote too high?</a></td>
        </tr>
        <tr>
          <td>I'm buying or selling a home in Colorado</td>
          <td><a href="/radon-testing/during-real-estate-transactions/">Radon testing during a real estate transaction (SB23-206)</a></td>
        </tr>
        <tr>
          <td>I want a quote from a licensed Colorado contractor</td>
          <td><a href="/request-quote/">Request a quote</a></td>
        </tr>
      </tbody>
    </table>
  </div>
</section>

<section>
  <h2>Colorado Springs and El Paso County</h2>
  <div class="prose-wide">
    <p>If you're in or around Colorado Springs, El Paso County is in <strong>EPA Zone 1</strong> and has the most pointed county-level data in Colorado: over 40 percent of homes tested between 2005 and 2023 had elevated radon, per El Paso County Public Health.<sup><a href="#src-5">[5]</a></sup> Our local pages cover testing kits, mitigation cost ranges by foundation scenario, and what to do after a failed test:</p>
    <ul>
      <li><a href="/colorado-springs/"><strong>Colorado Springs radon hub</strong></a> — local prevalence, EPCPH lab kits, contractor verification, SB23-206 real estate context.</li>
      <li><a href="/colorado-springs/radon-testing/"><strong>Radon testing in Colorado Springs</strong></a> — where to get a kit, where to place it, what to do with the result.</li>
      <li><a href="/colorado-springs/radon-mitigation-cost/"><strong>Mitigation cost in Colorado Springs</strong></a> — local quote ranges by scenario ($900-$4,800 depending on foundation).</li>
      <li><a href="/colorado-springs/failed-radon-test/"><strong>Failed radon test next steps</strong></a> — step-by-step playbook for elevated results.</li>
    </ul>
    <p>The Front Range north and west of Colorado Springs — Denver, Jefferson, Boulder, Larimer, Weld counties — all sit in EPA Zone 1 as well. We'll add city-specific hubs for these regions as the site expands.</p>
  </div>
</section>

<section>
  <h2>Frequently asked questions</h2>

  <details>
    <summary>Is my Colorado county high-risk for radon according to the EPA map?</summary>
    <p>Probably. The EPA Map of Radon Zones classifies 53 of Colorado's 64 counties as Zone 1 (highest predicted indoor radon). The 11 Zone 2 counties are Alamosa, Archuleta, Conejos, Costilla, Eagle, Hinsdale, Mineral, Rio Grande, Routt, Saguache, and San Juan. There are no Zone 3 counties in Colorado. Even if your county is Zone 2, CDPHE still recommends testing because about one in two Colorado homes statewide test above the EPA action level.</p>
  </details>

  <details>
    <summary>If my county is EPA Zone 2, is my home safe from radon?</summary>
    <p>No. Zone 2 means the predicted county average is between 2.0 and 4.0 pCi/L, not that homes there are safe. Individual homes in Zone 2 counties routinely test above 4.0 pCi/L — sometimes well above. EPA's own guidance is that the zone map should not be used to decide whether to test an individual home. Every home should be tested.</p>
  </details>

  <details>
    <summary>Why hasn't EPA updated the Colorado radon map since 1993?</summary>
    <p>The Map of Radon Zones was published in 1993 to help governments and code officials target radon programs. EPA's position is that the map served its purpose as a planning tool and that updated, finer-grained data is now better captured at the state and county level. For Colorado-specific results, the COEPHT dataset (county-level test results 2005-2017) and CDPHE's current statewide guidance are more accurate than re-running the EPA zone classification would be.</p>
  </details>

  <details>
    <summary>Can I see Colorado radon test results by county?</summary>
    <p>Yes. The Colorado Environmental Public Health Tracking (COEPHT) program publishes county-level radon test summaries based on actual test results submitted from 2005-2017. Two measures are available: average indoor radon and percent of measurements over 4 pCi/L. The data is available as a downloadable file and as an interactive Tableau map visualization. Note that some rural counties have small sample sizes; the data is most reliable for Front Range counties with high test volume.</p>
  </details>

  <details>
    <summary>What's the difference between the EPA radon zones and CDPHE data?</summary>
    <p>The EPA Map of Radon Zones is a 1993 planning classification — it grouped U.S. counties into three zones based on geology, soil parameters, foundation types, and indoor measurements available at the time. CDPHE data (and the COEPHT dataset) is based on actual indoor radon test results submitted by Colorado homeowners, contractors, and labs from 2005 onward. The CDPHE data is more current and more granular but is also self-selected (only includes homes that were tested). Both data sources point in the same direction: roughly half of Colorado homes test above the EPA action level of 4.0 pCi/L.</p>
  </details>

  <details>
    <summary>If Colorado has so much radon, should I be alarmed?</summary>
    <p>Concerned, not alarmed. Radon is real — it's the second leading cause of lung cancer in the U.S. and the leading cause among non-smokers. But it's also one of the most testable and most fixable indoor air-quality problems. A short-term test kit costs $15-$30 from the El Paso County Public Health lab or CDPHE. If your result comes back above 4.0 pCi/L, a typical Colorado mitigation system runs roughly $1,000-$2,000 per CDPHE, and a properly designed system reduces indoor radon by 80-99 percent. The right framing is: test, find out where you are, and then make a decision with real data instead of a 30-year-old zone classification.</p>
  </details>

  <details>
    <summary>Where does the EPA radon zone map come from?</summary>
    <p>The map was developed by the EPA in 1993 using a combination of indoor radon measurements available at the time, regional geology surveys, aerial radioactivity data (radiation surveys flown by aircraft for the U.S. Department of Energy), soil parameter data, and foundation-type distribution by region. It's intended as a planning tool for governments and code officials targeting radon resources. The full methodology and the underlying state-level supporting documents are available on the <a href="{s('epa_map_radon_zones')}" rel="noopener" target="_blank">EPA Map of Radon Zones page</a>.</p>
  </details>
</section>

<section>
  <div class="callout">
    <strong>One more time, because it matters.</strong> The Colorado Radon Map on this page is a stylized visualization of the EPA's 1993 Map of Radon Zones. <strong>It is not a substitute for testing your specific home.</strong> EPA, CDPHE, and El Paso County Public Health all recommend the same thing: test your home for radon, no matter what your county's zone is. A short-term test kit costs about $15 from the El Paso County Public Health lab. <a href="/radon-testing/">How to test for radon in Colorado &rarr;</a>
  </div>
</section>

<aside class="sources" aria-label="Sources">
  <h2>Sources</h2>
  <ol>
    <li id="src-1">U.S. EPA. <em>EPA Map of Radon Zones</em>. <a href="{s('epa_map_radon_zones')}" rel="noopener" target="_blank">epa.gov/radon/epa-map-radon-zones</a></li>
    <li id="src-2">Colorado Department of Public Health and Environment. <em>Testing your home for radon</em>. <a href="{s('cdphe_testing')}" rel="noopener" target="_blank">cdphe.colorado.gov/hm/testing-your-home-radon</a></li>
    <li id="src-3">U.S. EPA. <em>What is EPA's action level for radon and what does it mean?</em> <a href="{s('epa_action_level_def')}" rel="noopener" target="_blank">epa.gov/radon/what-epas-action-level-radon-and-what-does-it-mean</a></li>
    <li id="src-4">Colorado Environmental Public Health Tracking. <em>Radon data: county-level test results 2005-2017</em>. <a href="{s('coepht_radon_data')}" rel="noopener" target="_blank">coepht.colorado.gov/radon-data</a></li>
    <li id="src-5">El Paso County Public Health. <em>Radon</em>. <a href="{s('elpaso_radon')}" rel="noopener" target="_blank">elpasocountyhealth.org/radon</a></li>
    <li id="src-6">U.S. EPA. <em>Health risk of radon</em>. <a href="{s('epa_health_risk_radon')}" rel="noopener" target="_blank">epa.gov/radon/health-risk-radon</a></li>
  </ol>
</aside>
"""


def colorado_map_faq_jsonld():
    obj = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": "Is my Colorado county high-risk for radon according to the EPA map?",
             "acceptedAnswer": {"@type": "Answer", "text": "Probably. The EPA Map of Radon Zones classifies 53 of Colorado's 64 counties as Zone 1 (highest predicted indoor radon). The 11 Zone 2 counties are Alamosa, Archuleta, Conejos, Costilla, Eagle, Hinsdale, Mineral, Rio Grande, Routt, Saguache, and San Juan. There are no Zone 3 counties in Colorado. Even if your county is Zone 2, CDPHE still recommends testing because about one in two Colorado homes statewide test above the EPA action level."}},
            {"@type": "Question", "name": "If my county is EPA Zone 2, is my home safe from radon?",
             "acceptedAnswer": {"@type": "Answer", "text": "No. Zone 2 means the predicted county average is between 2.0 and 4.0 pCi/L, not that homes there are safe. Individual homes in Zone 2 counties routinely test above 4.0 pCi/L. EPA's own guidance is that the zone map should not be used to decide whether to test an individual home. Every home should be tested."}},
            {"@type": "Question", "name": "Why hasn't EPA updated the Colorado radon map since 1993?",
             "acceptedAnswer": {"@type": "Answer", "text": "The Map of Radon Zones was published in 1993 to help governments and code officials target radon programs. EPA's position is that the map served its purpose as a planning tool and that updated, finer-grained data is now better captured at the state and county level. For Colorado-specific results, the COEPHT dataset (county-level test results 2005-2017) and CDPHE's current statewide guidance are more accurate than re-running the EPA zone classification would be."}},
            {"@type": "Question", "name": "Can I see Colorado radon test results by county?",
             "acceptedAnswer": {"@type": "Answer", "text": "Yes. The Colorado Environmental Public Health Tracking (COEPHT) program publishes county-level radon test summaries based on actual test results submitted from 2005-2017. Two measures are available: average indoor radon and percent of measurements over 4 pCi/L. The data is available as a downloadable file and as an interactive Tableau map visualization."}},
            {"@type": "Question", "name": "What's the difference between EPA radon zones and CDPHE data?",
             "acceptedAnswer": {"@type": "Answer", "text": "The EPA Map of Radon Zones is a 1993 planning classification grouping U.S. counties into three zones based on geology, soil parameters, foundation types, and indoor measurements available at the time. CDPHE data and the COEPHT dataset are based on actual indoor radon test results submitted by Colorado homeowners, contractors, and labs from 2005 onward. The CDPHE data is more current and more granular but is also self-selected. Both point in the same direction: roughly half of Colorado homes test above the EPA action level."}},
            {"@type": "Question", "name": "If Colorado has so much radon, should I be alarmed?",
             "acceptedAnswer": {"@type": "Answer", "text": "Concerned, not alarmed. Radon is real and is the second leading cause of lung cancer in the U.S. But it is also one of the most testable and most fixable indoor air-quality problems. A short-term test kit costs $15-$30, a typical Colorado mitigation system runs roughly $1,000-$2,000 per CDPHE, and a properly designed system reduces indoor radon by 80-99 percent."}}
        ]
    }
    return f'<script type="application/ld+json">{json.dumps(obj)}</script>'
