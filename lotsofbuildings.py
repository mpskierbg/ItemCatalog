from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# you must install the wikipedia module with pip install wikipedia
# it doesnt seem to work with python 2+, so use python 3+
import wikipedia
from database_setup import Building, Base, BuildingInfo

engine = create_engine('sqlite:///buildinginfo1.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

building1 = Building(name="Willis Tower")

session.add(building1)
session.commit()

description = wikipedia.summary(building1.name, sentences=4)

info = BuildingInfo(name=building1.name,
                    description=description,
                    year_completed='1973',
                    architect='Skidmore, Owings and Merrill',
                    continent='North America',
                    country='United States of America',
                    style='International',
                    height='1,729',
                    floors='108',
                    building=building1,
                    )

session.add(info)
session.commit()

building2 = Building(name="Burj Khalifa")

session.add(building2)
session.commit()

info = BuildingInfo(name=building2.name,
                    description=wikipedia.summary(building2.name, sentences=4),
                    year_completed='2009',
                    architect='Adrian Smith at SOM',
                    continent='Asia',
                    country='United Arab Emirates',
                    style='Neo-Futurism',
                    height='2,722',
                    floors='154',
                    building=building2,
                    tallest_world=True,
                    tallest_country=True,
                    tallest_continent=True,
                    )

session.add(info)
session.commit()

building3 = Building(name="Shanghai Tower")

session.add(building3)
session.commit()

info = BuildingInfo(name=building3.name,
                    description=wikipedia.summary(building3.name, sentences=4),
                    year_completed='2015',
                    architect='Jun Xia (Gensler) TJAD',
                    continent='Asia',
                    country='China',
                    style='Futurist',
                    height='2,073',
                    floors='128',
                    building=building3,
                    tallest_country=True,
                    )

session.add(info)
session.commit()

building4 = Building(name="Abraj Al-Bait Clock Tower")

session.add(building4)
session.commit()

info = BuildingInfo(name=building4.name,
                    description=wikipedia.summary(building4.name, sentences=4),
                    year_completed='2012',
                    architect='SL Rasch GmbH and Dar Al-Handasah Architects',
                    continent='Asia',
                    country='Saudia Arabia',
                    style='Postmodern',
                    height='1,972',
                    floors='120',
                    building=building4,
                    tallest_country=True,
                    )

session.add(info)
session.commit()

building5 = Building(name="Ping An Finance Centre")

session.add(building5)
session.commit()

info = BuildingInfo(name=building5.name,
                    description=wikipedia.summary(building5.name, sentences=4),
                    year_completed='2017',
                    architect='Kohn Pedersen Fox Associates',
                    continent='Asia',
                    country='China',
                    style='Neo-Futurism',
                    height='1,966',
                    floors='115',
                    building=building5,
                    )

session.add(info)
session.commit()

building6 = Building(name="Lotte World Tower")

session.add(building6)
session.commit()

info = BuildingInfo(name=building6.name,
                    description=wikipedia.summary(building6.name, sentences=4),
                    year_completed='2016',
                    architect='Kohn Pedersen Fox Associates',
                    continent='Asia',
                    country='South Korea',
                    style='Futurist',
                    height='1,823',
                    floors='123',
                    building=building6,
                    tallest_country=True,
                    )

session.add(info)
session.commit()

building7 = Building(name="One World Trade Center")

session.add(building7)
session.commit()

info = BuildingInfo(name=building7.name,
                    description=wikipedia.summary(building7.name, sentences=4),
                    year_completed='2014',
                    architect='David Childs and Daniel Libeskind',
                    continent='North America',
                    country='United States of America',
                    style='	Contemporary modern',
                    height='1,792',
                    floors='104',
                    building=building7,
                    tallest_continent=True,
                    tallest_country=True,
                    )

session.add(info)
session.commit()

building8 = Building(name="Guangzhou CTF Finance Centre")

session.add(building8)
session.commit()

info = BuildingInfo(name=building8.name,
                    description=wikipedia.summary(building8.name, sentences=4),
                    year_completed='2016',
                    architect='Kohn Pedersen Fox Associates',
                    continent='Asia',
                    country='China',
                    style='Contemporary modern',
                    height='1,739',
                    floors='111',
                    building=building8,
                    )

session.add(info)
session.commit()

building9 = Building(name="Taipei 101")

session.add(building9)
session.commit()

info = BuildingInfo(name=building9.name,
                    description=wikipedia.summary(building9.name, sentences=4),
                    year_completed='2004',
                    architect='C.Y. Lee & Partners',
                    continent='Asia',
                    country='Taiwan',
                    style='Postmodern',
                    height='1,671',
                    floors='101',
                    building=building9,
                    tallest_country=True,
                    )

session.add(info)
session.commit()

building10 = Building(name="Shanghai World Financial Center")

session.add(building10)
session.commit()
info = BuildingInfo(name=building10.name,
                    description=wikipedia.summary(building10.name, sentences=4),
                    year_completed='2008',
                    architect='Kohn Pedersen Fox Associates',
                    continent='Asia',
                    country='China',
                    style='Neo-Futurism',
                    height='1,621',
                    floors='101',
                    building=building10,
                    )

session.add(info)
session.commit()

building11 = Building(name="International Commerce Centre")

session.add(building11)
session.commit()

info = BuildingInfo(name=building11.name,
                    description=wikipedia.summary(building11.name, sentences=4),
                    year_completed='2010',
                    architect='Kohn Pedersen Fox Associates',
                    continent='Asia',
                    country='China',
                    style='	Contemporary modern',
                    height='1,587',
                    floors='108',
                    building=building11,
                    )

session.add(info)
session.commit()

building12 = Building(name="Lakhta Center")

session.add(building12)
session.commit()

info = BuildingInfo(name=building12.name,
                    description=wikipedia.summary(building12.name, sentences=4),
                    year_completed='2018',
                    architect='Kettle Collective',
                    continent='Europ',
                    country='Russia',
                    style='Neo-Futurism',
                    height='1,516',
                    floors='87',
                    building=building12,
                    tallest_continent=True,
                    tallest_country=True,
                    )

session.add(info)
session.commit()

building13 = Building(name="Changsha IFS Tower T1")

session.add(building13)
session.commit()

info = BuildingInfo(name=building13.name,
                    description=wikipedia.summary(building13.name, sentences=4),
                    year_completed='2017',
                    architect='Wong Tung & Partners',
                    continent='Asia',
                    country='China',
                    style='Contemporary modern',
                    height='1,482.9',
                    floors='95',
                    building=building13,
                    )

session.add(info)
session.commit()

building14 = Building(name="Petronas Towers")

session.add(building14)
session.commit()

info = BuildingInfo(name=building14.name,
                    description=wikipedia.summary(building14.name, sentences=4),
                    year_completed='1996',
                    architect='Cesar Pelli & Association Architects',
                    continent='Asia',
                    country='Malaysia',
                    style='Postmodern',
                    height='1,483',
                    floors='88',
                    building=building14,
                    tallest_country=True,
                    )

session.add(info)
session.commit()

building15 = Building(name="Zifeng Tower")

session.add(building15)
session.commit()

info = BuildingInfo(name=building15.name,
                    description=wikipedia.summary(building15.name, sentences=4),
                    year_completed='2010',
                    architect='Adrian Smith at SOM',
                    continent='Asia',
                    country='China',
                    style='Modern',
                    height='1,480',
                    floors='66',
                    building=building15,
                    )

session.add(info)
session.commit()

building16 = Building(name="KK100")

session.add(building16)
session.commit()

info = BuildingInfo(name=building16.name,
                    description=wikipedia.summary(building16.name, sentences=4),
                    year_completed='2011',
                    architect='TFP Farrells',
                    continent='Asia',
                    country='China',
                    style='Contemporary modern',
                    height='1,449',
                    floors='100',
                    building=building16,
                    )

session.add(info)
session.commit()

building17 = Building(name="Guangzhou International Finance Center")

session.add(building17)
session.commit()

info = BuildingInfo(name=building17.name,
                    description=wikipedia.summary(building17.name, sentences=4),
                    year_completed='2010',
                    architect='WilkinsonEyre',
                    continent='Asia',
                    country='China',
                    style='Neo-Futurism',
                    height='1,439',
                    floors='103',
                    building=building17,
                    )

session.add(info)
session.commit()

building18 = Building(name="432 Park Avenue")

session.add(building18)
session.commit()

info = BuildingInfo(name=building18.name,
                    description=wikipedia.summary(building18.name, sentences=4),
                    year_completed='2015',
                    architect='Rafael Vinoly and SLCE Architects, LLP',
                    continent='North America',
                    country='United States of America',
                    style='Postmodern',
                    height='1,396',
                    floors='85',
                    building=building18,
                    )

session.add(info)
session.commit()

building19 = Building(name="Marina 101")

session.add(building19)
session.commit()

info = BuildingInfo(name=building19.name,
                    description=wikipedia.summary(building19.name, sentences=4),
                    year_completed='2017',
                    architect='National Engineering Bureau',
                    continent='Asia',
                    country='United AraB Emirates',
                    style='Contemporary modern',
                    height='1,417',
                    floors='101',
                    building=building19,
                    )

session.add(info)
session.commit()

building20 = Building(name="Trump International Hotel and Tower (Chicago)")

session.add(building20)
session.commit()

info = BuildingInfo(name=building20.name,
                    description=wikipedia.summary(building20.name, sentences=4),
                    year_completed='2009',
                    architect='Adrian Smith at SOM',
                    continent='North America',
                    country='United States of America',
                    style='Modern',
                    height='1,388',
                    floors='98',
                    building=building20,
                    )

session.add(info)
session.commit()

building21 = Building(name="Jin Mao Tower")

session.add(building21)
session.commit()

info = BuildingInfo(name=building21.name,
                    description=wikipedia.summary(building21.name, sentences=4),
                    year_completed='1999',
                    architect='Adrian Smith at SOM',
                    continent='Asia',
                    country='China',
                    style='Neo-Futurism',
                    height='1,380',
                    floors='88',
                    building=building21,
                    )

session.add(info)
session.commit()

building22 = Building(name="Princess Tower")

session.add(building22)
session.commit()

info = BuildingInfo(name=building22.name,
                    description=wikipedia.summary(building22.name, sentences=4),
                    year_completed='2012',
                    architect='Eng. Adnan Saffarini Office',
                    continent='Asia',
                    country='United Arab Emirates',
                    style='Postmodern',
                    height='1,358',
                    floors='101',
                    building=building22,
                    )

session.add(info)
session.commit()

building23 = Building(name="Al Hamra Tower")

session.add(building23)
session.commit()

info = BuildingInfo(name=building23.name,
                    description=wikipedia.summary(building23.name, sentences=4),
                    year_completed='2011',
                    architect='Gary Paul Haney and Callison at SOM',
                    continent='Asia',
                    country='Kuwait',
                    style='Sculpted',
                    height='1,358',
                    floors='80',
                    building=building23,
                    tallest_country=True,
                    )

session.add(info)
session.commit()

building24 = Building(name="International Finance Centre (Hong Kong)")

session.add(building24)
session.commit()

info = BuildingInfo(name=building24.name,
                    description=wikipedia.summary(building24.name, sentences=4),
                    year_completed='2003',
                    architect='Cesar Pelli & Association Architects',
                    continent='Asia',
                    country='China',
                    style='Modern',
                    height='1,362.9',
                    floors='88',
                    building=building24,
                    )

session.add(info)
session.commit()

building25 = Building(name="China Resources Headquarters")

session.add(building25)
session.commit()

info = BuildingInfo(name=building25.name,
                    description=wikipedia.summary(building25.name, sentences=4),
                    year_completed='2017',
                    architect='Kohn Pedersen Fox Associates',
                    continent='Asia',
                    country='China',
                    style='Neo-Futurism',
                    height='1,286',
                    floors='66',
                    building=building25,
                    )

session.add(info)
session.commit()

building26 = Building(name="23 Marina")

session.add(building26)
session.commit()

info = BuildingInfo(name=building26.name,
                    description=wikipedia.summary(building26.name, sentences=4),
                    year_completed='2012',
                    architect='Hafeez Contractor KEO International Consultants',
                    continent='Asia',
                    country='United Arab Emirates',
                    style='Contemporary modern',
                    height='1,289',
                    floors='89',
                    building=building26,
                    )

session.add(info)
session.commit()

building27 = Building(name="CITIC Plaza")

session.add(building27)
session.commit()

info = BuildingInfo(name=building27.name,
                    description=wikipedia.summary(building27.name, sentences=4),
                    year_completed='1996',
                    architect='Dennis Lau & Ng Chun Man Architects & Engineers',
                    continent='Asia',
                    country='China',
                    style='Modern',
                    height='1,280',
                    floors='80',
                    building=building27,
                    )

session.add(info)
session.commit()

building28 = Building(name="Shun Hing Square")

session.add(building28)
session.commit()

info = BuildingInfo(name=building28.name,
                    description=wikipedia.summary(building28.name, sentences=4),
                    year_completed='1996',
                    architect='K.Y. Cheung Design Associates',
                    continent='Asia',
                    country='China',
                    style='Contemporary modern',
                    height='1,260',
                    floors='69',
                    building=building28,
                    )

session.add(info)
session.commit()

building29 = Building(name="Eton Place Dalian")

session.add(building29)
session.commit()

info = BuildingInfo(name=building29.name,
                    description=wikipedia.summary(building29.name, sentences=4),
                    year_completed='2015',
                    architect='NBBJ',
                    continent='Asia',
                    country='China',
                    style='Modern',
                    height='1,273',
                    floors='81',
                    building=building29,
                    )

session.add(info)
session.commit()

building30 = Building(name="Burj Mohammed bin Rashid")

session.add(building30)
session.commit()

info = BuildingInfo(name=building30.name,
                    description=wikipedia.summary(building30.name, sentences=4),
                    year_completed='2014',
                    architect='Foster + Partners',
                    continent='Asia',
                    country='United Arab Emirates',
                    style='Neo-Futurism',
                    height='1,253',
                    floors='92',
                    building=building30,
                    )

session.add(info)
session.commit()

building31 = Building(name="Empire State Building")

session.add(building31)
session.commit()

info = BuildingInfo(name=building31.name,
                    description=wikipedia.summary(building31.name, sentences=4),
                    year_completed='1931',
                    architect='	Shreve, Lamb and Harmon',
                    continent='North America',
                    country='United States of America',
                    style='Art Deco',
                    height='1,454',
                    floors='102',
                    building=building31,
                    )

session.add(info)
session.commit()

building32 = Building(name="Elite Residence")

session.add(building32)
session.commit()

info = BuildingInfo(name=building32.name,
                    description=wikipedia.summary(building32.name, sentences=4),
                    year_completed='2012',
                    architect='Adnan Saffarini',
                    continent='Asia',
                    country='United Arab Emirates',
                    style='Modern',
                    height='1,248',
                    floors='87',
                    building=building32,
                    )

session.add(info)
session.commit()

building33 = Building(name="Central Plaza (Hong Kong)")

session.add(building33)
session.commit()

info = BuildingInfo(name=building33.name,
                    description=wikipedia.summary(building33.name, sentences=4),
                    year_completed='1992',
                    architect='Dennis Lau & Ng Chun Man Architects & Engineers (HK) Ltd.',
                    continent='Asia',
                    country='China',
                    style='Postmodern',
                    height='1,227',
                    floors='78',
                    building=building33,
                    )

session.add(info)
session.commit()

building34 = Building(name="Federation Tower")

session.add(building34)
session.commit()

info = BuildingInfo(name=building34.name,
                    description=wikipedia.summary(building34.name, sentences=4),
                    year_completed='2017',
                    architect='nps+partner, Schweger Associated Architects',
                    continent='Europe',
                    country='Russia',
                    style='Postmodern',
                    height='1,476',
                    floors='97',
                    building=building34,
                    )

session.add(info)
session.commit()

building35 = Building(name="Bank of China Tower (Hong Kong)")

session.add(building35)
session.commit()

info = BuildingInfo(name=building35.name,
                    description=wikipedia.summary(building35.name, sentences=4),
                    year_completed='1990',
                    architect='I. M. Pei & Partners, Sherman Kung & Associates Architects Ltd. Thomas Boada S.L.',
                    continent='Asia',
                    country='China',
                    style='Neo-Futurism',
                    height='1,205.4',
                    floors='72',
                    building=building35,
                    )

session.add(info)
session.commit()

building36 = Building(name="Bank of America Tower (Manhattan)")

session.add(building36)
session.commit()

info = BuildingInfo(name=building36.name,
                    description=wikipedia.summary(building36.name, sentences=4),
                    year_completed='2009',
                    architect='	COOKFOX Architects and Adamson Associates Architects',
                    continent='North America',
                    country='United States of America',
                    style='Neo-Futurism',
                    height='1,200',
                    floors='55',
                    building=building36,
                    )

session.add(info)
session.commit()

building37 = Building(name="Almas Tower")

session.add(building37)
session.commit()

info = BuildingInfo(name=building37.name,
                    description=wikipedia.summary(building37.name, sentences=4),
                    year_completed='2009',
                    architect='Atkins Middle East',
                    continent='Asia',
                    country='United Arab Emirates',
                    style='Modern',
                    height='1,180',
                    floors='68',
                    building=building37,
                    )

session.add(info)
session.commit()

building38 = Building(name="Ahmed Abdul Rahim Al Attar Tower")

session.add(building38)
session.commit()

info = BuildingInfo(name=building38.name,
                    description=wikipedia.summary(building38.name, sentences=4),
                    year_completed='2017',
                    architect='Gulf Engineering & Consultants',
                    continent='Asia',
                    country='United Arab Emirates',
                    style='Neo-Futurism',
                    height='1,174',
                    floors='75',
                    building=building38,
                    )

session.add(info)
session.commit()

building39 = Building(name="JW Marriott Marquis Dubai")

session.add(building39)
session.commit()

info = BuildingInfo(name=building39.name,
                    description=wikipedia.summary(building39.name, sentences=4),
                    year_completed='2013',
                    architect='Arch Group Consultants',
                    continent='Asia',
                    country='United Arab Emirates',
                    style='Postmodern',
                    height='1,166',
                    floors='82',
                    building=building39,
                    )

session.add(info)
session.commit()

building40 = Building(name="Emirates Office Tower")

session.add(building40)
session.commit()

info = BuildingInfo(name=building40.name,
                    description=wikipedia.summary(building40.name, sentences=4),
                    year_completed='1999',
                    architect='Hazel W.S. Wong Norr Group Consultants Int. Ltd.',
                    continent='Asia',
                    country='United Arab Emirates',
                    style='Neo-Futurism',
                    height='1,163',
                    floors='52',
                    building=building40,
                    )

session.add(info)
session.commit()

building41 = Building(name="OKO Tower")

session.add(building41)
session.commit()

info = BuildingInfo(name=building41.name,
                    description=wikipedia.summary(building41.name, sentences=4),
                    year_completed='2015',
                    architect='Skidmore, Owings and Merrill',
                    continent='Europe',
                    country='Russia',
                    style='Neo-Futurism',
                    height='1,160',
                    floors='85',
                    building=building41,
                    )

session.add(info)
session.commit()

building42 = Building(name="The Marina Torch")

session.add(building42)
session.commit()

info = BuildingInfo(name=building42.name,
                    description=wikipedia.summary(building42.name, sentences=4),
                    year_completed='2011',
                    architect='Khatib and Alami',
                    continent='Asia',
                    country='United Arab Emirates',
                    style='Postmodern',
                    height='1,105',
                    floors='82',
                    building=building42,
                    )

session.add(info)
session.commit()

building43 = Building(name="Forum 66")

session.add(building43)
session.commit()

info = BuildingInfo(name=building43.name,
                    description=wikipedia.summary(building43.name, sentences=4),
                    year_completed='2015',
                    architect='Kohn Pedersen Fox Associates',
                    continent='Asia',
                    country='China',
                    style='Modern',
                    height='1,151.6',
                    floors='76',
                    building=building43,
                    )

session.add(info)
session.commit()

building44 = Building(name="The Pinnacle (Guangzhou)")

session.add(building44)
session.commit()

info = BuildingInfo(name=building44.name,
                    description=wikipedia.summary(building44.name, sentences=4),
                    year_completed='2012',
                    architect='Guangzhou Hanhua Architects & Engineers',
                    continent='Asia',
                    country='China',
                    style='Postmodern',
                    height='1,180',
                    floors='60',
                    building=building44,
                    )

session.add(info)
session.commit()

building45 = Building(name="875 North Michigan Avenue")

session.add(building45)
session.commit()

info = BuildingInfo(name=building45.name,
                    description=wikipedia.summary(building45.name, sentences=4),
                    year_completed='1969',
                    architect='Fazlur Rahman Khan Skidmore, Owings and Merrill',
                    continent='North America',
                    country='United States of America',
                    style='Structural Expressionism',
                    height='1,500',
                    floors='100',
                    building=building45,
                    )

session.add(info)
session.commit()

building46 = Building(name="Keangnam Hanoi Landmark Tower")

session.add(building46)
session.commit()

info = BuildingInfo(name=building46.name,
                    description=wikipedia.summary(building46.name, sentences=4),
                    year_completed='2011',
                    architect='Heerim, Samoo, Aum & Lee, HOK',
                    continent='Asia',
                    country='Vietnam',
                    style='Modern',
                    height='1,150',
                    floors='72',
                    building=building46,
                    tallest_country=True,
                    )

session.add(info)
session.commit()

building47 = Building(name="Ryugyong Hotel")

session.add(building47)
session.commit()

info = BuildingInfo(name=building47.name,
                    description=wikipedia.summary(building47.name, sentences=4),
                    year_completed='0000',
                    architect='Baikdoosan Architects & Engineers',
                    continent='Asia',
                    country='North Korea',
                    style='Neo-Futurism',
                    height='1,082.7',
                    floors='105',
                    building=building47,
                    tallest_country=True,
                    )

session.add(info)
session.commit()

building48= Building(name="Q1 (building)")

session.add(building48)
session.commit()

info = BuildingInfo(name=building48.name,
                    description=wikipedia.summary(building48.name, sentences=4),
                    year_completed='2005',
                    architect='Sunland Group',
                    continent='Australia',
                    country='Australia',
                    style='Postmodern',
                    height='1,058',
                    floors='78',
                    building=building48,
                    tallest_country=True,
                    )

session.add(info)
session.commit()

building49 = Building(name="Grand Hyatt Manila")

session.add(building49)
session.commit()

info = BuildingInfo(name=building49.name,
                    description=wikipedia.summary(building49.name, sentences=4),
                    year_completed='2017',
                    architect='	Wong & Ouyang Casas Architects',
                    continent='Asia',
                    country='Philippines',
                    style='	Contemporary and Postmodern',
                    height='1,043.3',
                    floors='66',
                    building=building49,
                    )

session.add(info)
session.commit()

building50 = Building(name="First Canadian Place")

session.add(building50)
session.commit()

info = BuildingInfo(name=building50.name,
                    description=wikipedia.summary(building50.name, sentences=4),
                    year_completed='1975',
                    architect='Bregman + Hamann Architects Edward Durell Stone & Associates',
                    continent='North America',
                    country='Canada',
                    style='Contemporary modern',
                    height='978',
                    floors='72',
                    building=building50,
                    )

session.add(info)
session.commit()


print('All buildings added')
