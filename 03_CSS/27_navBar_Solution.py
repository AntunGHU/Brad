# 9'35

# Prvo Ath trazi kako dobiti <ul> bez tocki i nalazi da stavivsi u css "ul {list-style-type: none;}"!
# Potom trazi rjesenje preustroja iz jednog ispod drugog u jedan kraj drugog. To dobija sa "li {float: left;}"
# Ukidanje text-decoration na svakom linku, + padding + color + disply sa
# ? a {
# ?   text-decoration: none;
# ?   padding: 13px;
# ?   color: white;
# ?   display: block;
# ? }
# Sve skupa css:
# ? ul {
# ?   list-style-type: none;
# ?   background-color: blue;
# ?   overflow: hidden;
# ? }
# ?
# ? li {
# ?   float: left;
# ? }
# ?
# ? a {
# ?   text-decoration: none;
# ?   padding: 13px;
# ?   color: white;
# ?   display: block;       # bez kojeg nema padding-a ispod!
# ? }
# ?
# ? a:hover{
# ?   background-color: black;
# ? }
# overflow ostaje malo nejasno objasnjen kao uvjet
