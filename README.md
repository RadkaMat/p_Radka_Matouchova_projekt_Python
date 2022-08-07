## Autor projektu: Radka M. ##

# python_projekt_edinburkska_kola
Analýza půjčování kol služkou "bike sharing" v městě Edinburk provozovanou firmou Just Eat Cycles
Zdroj dat pro stažení: https://engeto.com/files/db_portal_template.sql 
Pro analýzu bude použit jiný zdroj: Madia DB server data.engeto.com)
Použitý software pro vypracování analýzy: Jupyter Notebook 6.4.8

Zdrojové tabulky:
edinburgh_bikes - obsahuje 438 259 záznamů o výpůjčkách kol ze 168 cyklicktických stanic, za časové období od 2018-09-15 08:52:05 do 2021-07-01 00:20:36.

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
