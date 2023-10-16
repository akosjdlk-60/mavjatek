# mavjatek
- Backstory: Budapesten vagyunk és kapunk egy levelet hogy meghalt az egyik bécsi rokonunk. Csórók vagyunk 0 pénzzel de el akarunk jutni Bécsbe a temetésre ami 3 nap múlva 15:00kor van.
- Cél: Időben eljutni a temetésre, nem meghalni, venni egy virágot a sírra.
- Plot twist: (20%) Komáromban leszállsz a vonatról, de nem figyelsz és elüt egy tehervonat.
- Statok: Energia(75-50), Telítettség(50-100), Pénz(0-250), Idő(08:00), Időjárás(napos)
- Starter inventory: 1 sportszelet

### Inventory
- Fánk
- Sportszelet
- Energiaital

### Energia
- ha 0: meghalsz
- séta: random(15, 20)%, 1 óra
- futás: random(30, 35)%, 20p
- egyéb: random(1, 3)%
- tölteni alvással vagy energiaitallal(max)

### Telítettség
- ha 0: meghalsz
- tölthető: fánk(50%) & sportszelet(35%)
- 1:2 konvertál alvás közben energiává
- óránként csökken(10-15)%

### Pénz
- kaját, jegyet, energiaitalt, quest itemet lehet venni vele
- meglophatnak
- te is lophatsz
- lehet kéregetni
- megbüntetnek, (vonatjegy x 1,5) ha nincs elég vesztettél (börtön)

### Idő
- alvás közben in game idő gyorsabban telik
- bliccelés közben irl idő nagyobb

### Időjárás
- naponta random
- napos
- esős

### Költségek:
- vonatjegy: random(500, 600)
- fánk: 250
- sportszelet: 180
- energiaital: 500
- virág: 1500

## Menük:
- főmenü (storyline explaining) -- menu.fomenu
- Állomásmenü -- menu.allomasmenu
- boltmenü -- menu.boltmenu
- vonatmenü -- menu.vonatmenu

### Állomás menüpontok:
- Séta a boltba
- Futás a boltba
- Vissza a vonatra
- jegy vásárlás
- Kisgyerek meglopása 100-250, 10% hogy lecsuknak
- Öltönyös úriember meglopása 300-600, 40% hogy lecsuknak
- kéregetés max. 100, állomásonként max 1x
- vár x-ig

### Bolt menüpontok:
- Energiaital vásárlás
- Sportszelet vásárlás
- Fánk vásárlás
- Virág vásárlás
- Virág lopás (60% lecsuknak)
- Étel lopás (20% lecsuknak)
- Séta az állomásra
- Futás az állomásra

### Vonat menüpontok:
- Leszáll
- Alvás
- Bliccelés (elbújik a WC ben)
- nagy esély a vonatrandom eventre

### Vonat eventek
- Biztósitóberendezési hiba miatt késés (min. 30p) max 1 / vonat
- Felsővezeték szakadás (2óra vagy pótlóbusz: ha nincs jegy => baj) max 1 / vonat
- Valaki elkezd hozzád beszélni: -20% energia
- Jön az ellenőr (ha nincs jegy akkor bűntetés)

### Város Eventek:
- Kirabolnak: -(15-50)% pénz                    --- 10%, este 20:00 után 25%
- Valaki elkezd hozzád beszélni: -20% energia   --- 30% este 20:00 után 0%
- Találsz egy 500ast a földön                   --- 5%
- Találsz egy 200ast a földön                   --- 10%
- Találsz egy 50est a földön                    --- 10%
- Találsz egy 10est a földön                    --- 10%
