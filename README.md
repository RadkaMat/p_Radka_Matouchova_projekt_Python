## Autor projektu: Radka M. ##

# python_projekt_edinburkska_kola
    Analýza půjčování kol služkou "bike sharing" v městě Edinburk (hl. město Skotska) provozovanou firmou Just Eat Cycles od září 2018.
    Zdroj dat pro stažení: https://engeto.com/files/db_portal_template.sql 
    Zdroj dat pro tento projekt: Madia DB server data.engeto.com
    Použitý software pro vypracování analýzy: Jupyter Notebook 6.4.8 (anaconda3), Python 3.9.12 (ipykernel)

Zdrojové tabulky:
    edinburgh_bikes - obsahuje 438 259 záznamů o výpůjčkách kol ze 170 cyklicktických stanic za časové období od 2018-09-15 08:52:05 do 2021-07-01 00:20:36.
    edinburgh_weather - obsahuje 6 336 záznamů o naměřených teplotách a dalších údajů o počasí za časové období o 2018-09-01 00:00:00 do 2020-10-31 21:00:00.
    pozn. nebylo možné sehnat novější data od Just Eat Cycles, protože ukončili činnost k datu 17.9.2021.
    
Na základě dat o všech výpůjčkách zjistěte minimálně následující informace:

    1. identifikujte aktivní a neaktivní stanice
    2. identifikujte nejfrekventovanější stanice
    3. identifikujte stanice, na kterých se kola hromadí a stanice, kde potenciálně chybí
    4. spočítejte vzdálenosti mezi jednotlivými stanicemi
    5. jak dlouho trvá jedna výpůjčka? Najděte odlehlé hodnoty, zobrazte histogram

Analýza poptávky:

    6. zobrazte vývoj poptávky po půjčování kol v čase
    7. identifikujte příčiny výkyvů poptávky
    8. zjistěte vliv počasí na poptávku po kolech (údaje o počasí v Edinburghu jsou v tabulce edinburgh_weather)
    9. půjčují si lidé kola více o víkendu než během pracovního týdne?
