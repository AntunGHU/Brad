# 15'22

# Manje-vise, html i css su isti kao u ArtGalery1. Ovdje ce Brad samo izvrsiti primjenu filter-elementa css-a

# Novi elementi su:
# ? img {
# ?   width:18%;
# ?   filter: grayscale(100%);
# ? }
# ?
# ? img:hover {
# ?   filter: grayscale(0%);
# ? }
# koji staticno primjenjuju filter: grayscale sa 100% a kod hover-anja 0%. Jos jedan element sa hoveranjem! Ovog puta img!!!

# I zaista novo i kao priprema za bootstrap je element vjesnik css-jezika tj bootstrapa:
# ? .paintings:hover .titles {
# ?   display: block;
# ? }
# dakle dva elementa u liniji koda css-a: .paintings:hover  i .titles pa {}. Da bi to bilo moguce, div-titles morao je biti child od diva paintings u okviru html-a!!!
