# 8'13

# Brad prvo pokazuje kako se moze referenca na style unijeti u sam p-tag ala <p style="background-color:blue"> . Treba primjetiti standardnost ovog unosa. Svi unosi u tagove idu sa znakom jednakosti i "".

# druga opcija je unosenje u <head> kao novi tag <style></style> pa unutar njega p sa {background-color: yellow}. Ovakav stil odnosi se na sve paragrafe ali samo ovog html-fajla, a za onog koji zelimo da je poseban primjenimo 1. nacin!

# treca opcija i best practices je stiliranje kroz poseban css-fajl i unutar njega isto kao i u 2. rjesenju p {backgrund...} a u head unosimo tag <link href=...>

# dodavanjem style u body/paragraf, head i poseban css fajl izvrsio sam provjeru i potvrdio da ako svi unosi postoje za pojedinu stranicu, prioritet ima /body/tag-style pa /head/style i tek na kraju style css-fajla!
