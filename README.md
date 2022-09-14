## Autor projektu: Radka M. ##

# python_projekt_edinburkska_kola Zadání

    V Edinburghu, stejně jako v dalších městech, funguje systém "bike sharing" - ve městě jsou stanice s koly, člověk si může nějaké půjčit
    a potom ho vrátit v nějaké další stanici. Problém je, že v některých stanicích se kola pravidelně hromadí a jinde naopak chybí. 
    Provozovatel kol, firma Just Eat Cycles, zadala projekt, jehož cílem je systém zefektivnit.
    Zdroj dat pro stažení: https://engeto.com/files/db_portal_template.sql 
    Zdroj dat pro tento projekt: Madia DB server data.engeto.com
    Použitý software pro vypracování analýzy: Jupyter Notebook 6.4.8 (anaconda3), Python 3.9.12 (ipykernel)

Zdrojové tabulky:

    edinburgh_bikes - obsahuje 438 259 záznamů o výpůjčkách kol ze 170 cyklicktických stanic za časové období od 2018-09-15 08:52:05 do 2021-07-01 00:20:36.
    edinburgh_weather - obsahuje 6 336 záznamů o naměřených teplotách a dalších údajů o počasí za časové období od 2018-09-01 00:00:00 do 2020-10-31 21:00:00.
    pozn. nebylo možné sehnat novější data od Just Eat Cycles, protože ukončili svou činnost k datu 2021-09-17 (viz. jejich facebook).
    
Na základě dat o všech výpůjčkách zjistěte následující informace:

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
