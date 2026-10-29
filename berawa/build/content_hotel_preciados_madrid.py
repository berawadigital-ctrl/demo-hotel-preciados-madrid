# Contenido de la demo Hotel Preciados (Madrid) (es/ca/en/fr). Hechos de preciadoshotel.com leidos el 29/10/2026 (ver berawa/sources.json). Lo no publicado no se afirma.
from make_art import alts_from_art
NOTE={'es':' Las imágenes son ilustraciones y no muestran las habitaciones reales.','ca':' Les imatges són il·lustracions i no mostren les habitacions reals.','en':' Images are illustrations and do not show the actual rooms.','fr':' Les images sont des illustrations et ne montrent pas les chambres réelles.'}
H={'es':['Skyline','Corner Junior Suite','Premium con balcón'],'ca':['Skyline','Corner Junior Suite','Premium amb balcó'],'en':['Skyline','Corner Junior Suite','Premium with balcony'],'fr':['Skyline','Corner Junior Suite','Premium avec balcon']}
RD={
'es':['Dos estancias de 40 m2 y una terraza de 28 m2 con vistas panorámicas sobre el Madrid Antiguo.','En la esquina del hotel, 38 m² con seis ventanas, seis balcones y dos salas independientes.','Entre 24 y 28 m², con balcón y vistas a la calle Preciados y la calle Ternera.'],
'ca':['Dues estances de 40 m2 i una terrassa de 28 m2 amb vistes panoràmiques sobre el Madrid antic.','A la cantonada de l\'hotel, 38 m² amb sis finestres, sis balcons i dues sales independents.','Entre 24 i 28 m², amb balcó i vistes al carrer Preciados i al carrer Ternera.'],
'en':['Two rooms of 40 m2 and a 28 m2 terrace with panoramic views over Old Madrid.','On the corner of the hotel, 38 m² with six windows, six balconies and two separate rooms.','Between 24 and 28 m², with a balcony and views of Calle Preciados and Calle Ternera.'],
'fr':['Deux pièces de 40 m2 et une terrasse de 28 m2 avec vue panoramique sur le vieux Madrid.','À l\'angle de l\'hôtel, 38 m² avec six fenêtres, six balcons et deux pièces indépendantes.','Entre 24 et 28 m², avec balcon et vue sur la calle Preciados et la calle Ternera.']}
ART={
'hero':('skyline',2901,['#3b2a3f','#e0905f','#f7d39c','#3a2a3e','#2b1f2e','#1c141e']),
'intro':('columns',2902,['#f1e4d0','#f7ecda','#b88a3e','#7a2e3a','#3f1820']),
'r1':('skyline',2911,['#2f3c5e','#e48a5f','#f9d19b','#2e3b5c','#212c46','#151d30']),
'r2':('arches',2912,['#efe2cc','#d8af7c','#a8663a','#7a2e3a','#45161d']),
'r3':('columns',2913,['#eee1cb','#f6ead6','#bb8c42','#80343f','#43181f']),
'g1':('arches',2921,['#f0e3cd','#d5ab78','#a5622c','#7a2e3a','#46161d']),
'g2':('skyline',2922,['#44324a','#e8935f','#fbd9a0','#433149','#33253a','#221827']),
'g3':('columns',2923,['#efe2cb','#f5e9d3','#c08c40','#86373f','#4a1a21']),
'g4':('hills',2924,['#e6e6d1','#f3e5c3','#f6cf8a','#a9c19e','#80a085','#587767']),
'g5':('arches',2925,['#efe0c9','#d3a875','#a4602b','#7a2e3a','#46161d']),
'g6':('skyline',2926,['#33456a','#e48a5f','#f9d19b','#2f4260','#223249','#16222f'])}
IMGS=dict(hero='hero',intro='intro',rooms=['r1','r2','r3'],gallery=['g1','g2','g3','g4','g5','g6'])
ALTS=alts_from_art(ART)
T={
'es':dict(title='Hotel Preciados · Hotel de cuatro estrellas en un edificio del siglo XIX en el centro de Madrid',see_rooms='Ver habitaciones',hero_k='Madrid · Calle Preciados',hero_t='Diseño, modernidad e historia en pleno corazón de Madrid',hero_s='Un edificio restaurado del siglo XIX a 5 minutos a pie de la Puerta del Sol.',
 intro_t='Un hotel con café histórico',intro_p1='El Hotel Preciados ocupa un edificio restaurado del siglo XIX en la calle Preciados 37, esquina con la plaza de Santo Domingo.',
 intro_p2='La mayoría de sus habitaciones tienen balcón sobre la calle; el minibar y el wifi son gratuitos. En la planta baja está el Café Varela, histórico café madrileño desde 1884.',
 stats=['Edificio del siglo XIX','Café Varela desde 1884','Conserjería 24 horas','Parking con aparcacoches'],nav_rooms='Habitaciones',rooms_t='Habitaciones',rooms_s='Tres de los tipos de habitación del hotel.',
 svcs=['Conserjería 24 horas en español e inglés','Wifi gratuito en todo el hotel','Minibar gratuito','Room service de 7:00h a 23:00h','Lavandería de lunes a sábado','Parking en el propio hotel con aparcacoches','Restaurante Café Varela','Salones para eventos y reuniones'],
 loc_p='Calle de Preciados 37, esquina con la plaza de Santo Domingo, 28013 Madrid. Metro Callao y Santo Domingo a 75 metros.',
 chips=['¿Qué habitaciones tiene?','¿Hay parking?','¿Dónde está?','¿Cómo se reserva?']),
'ca':dict(title='Hotel Preciados · Hotel de quatre estrelles en un edifici del segle XIX al centre de Madrid',see_rooms='Veure habitacions',hero_k='Madrid · Carrer Preciados',hero_t='Disseny, modernitat i història al bell mig de Madrid',hero_s='Un edifici restaurat del segle XIX a 5 minuts a peu de la Puerta del Sol.',
 intro_t='Un hotel amb un cafè històric',intro_p1='L\'Hotel Preciados ocupa un edifici restaurat del segle XIX al carrer Preciados 37, cantonada amb la plaça de Santo Domingo.',
 intro_p2='La majoria de les habitacions tenen balcó sobre el carrer; el minibar i la wifi són gratuïts. A la planta baixa hi ha el Café Varela, cafè històric madrileny des de 1884.',
 stats=['Edifici del segle XIX','Café Varela des de 1884','Consergeria 24 hores','Pàrquing amb aparcacotxes'],nav_rooms='Habitacions',rooms_t='Habitacions',rooms_s='Tres dels tipus d\'habitació de l\'hotel.',
 svcs=['Consergeria 24 hores en castellà i anglès','Wifi gratuïta a tot l\'hotel','Minibar gratuït','Servei d\'habitacions de 7:00h a 23:00h','Bugaderia de dilluns a dissabte','Pàrquing al mateix hotel amb aparcacotxes','Restaurant Café Varela','Salons per a esdeveniments i reunions'],
 loc_p='Calle de Preciados 37, cantonada amb la plaça de Santo Domingo, 28013 Madrid. Metro Callao i Santo Domingo a 75 metres.',
 chips=['Quines habitacions té?','Hi ha pàrquing?','On és?','Com es reserva?']),
'en':dict(title='Hotel Preciados · Four-star hotel in a 19th-century building in central Madrid',see_rooms='See the rooms',hero_k='Madrid · Calle Preciados',hero_t='Design, modernity and history in the heart of Madrid',hero_s='A restored 19th-century building 5 minutes\' walk from Puerta del Sol.',
 intro_t='A hotel with a historic café',intro_p1='Hotel Preciados occupies a restored 19th-century building at Calle Preciados 37, on the corner of Plaza de Santo Domingo.',
 intro_p2='Most of its rooms have a balcony over the street; the minibar and wifi are free. On the ground floor is Café Varela, a historic Madrid café since 1884.',
 stats=['19th-century building','Café Varela since 1884','24-hour concierge','Valet parking'],nav_rooms='Rooms',rooms_t='Rooms',rooms_s='Three of the hotel\'s room types.',
 svcs=['24-hour concierge in Spanish and English','Free wifi throughout the hotel','Free minibar','Room service from 7:00h to 23:00h','Laundry Monday to Saturday','On-site parking with valet service','Café Varela restaurant','Rooms for events and meetings'],
 loc_p='Calle de Preciados 37, on the corner of Plaza de Santo Domingo, 28013 Madrid. Callao and Santo Domingo metro stations 75 metres away.',
 chips=['What rooms does it have?','Is there parking?','Where is it?','How do I book?']),
'fr':dict(title='Hotel Preciados · Hôtel quatre étoiles dans un bâtiment du XIXe siècle au centre de Madrid',see_rooms='Voir les chambres',hero_k='Madrid · Calle Preciados',hero_t='Design, modernité et histoire au cœur de Madrid',hero_s='Un bâtiment restauré du XIXe siècle à 5 minutes à pied de la Puerta del Sol.',
 intro_t='Un hôtel avec un café historique',intro_p1='L\'Hotel Preciados occupe un bâtiment restauré du XIXe siècle au 37 calle Preciados, à l\'angle de la place de Santo Domingo.',
 intro_p2='La plupart des chambres ont un balcon sur la rue ; le minibar et le wifi sont gratuits. Au rez-de-chaussée se trouve le Café Varela, café historique madrilène depuis 1884.',
 stats=['Bâtiment du XIXe siècle','Café Varela depuis 1884','Conciergerie 24 heures','Parking avec voiturier'],nav_rooms='Chambres',rooms_t='Chambres',rooms_s='Trois des types de chambre de l\'hôtel.',
 svcs=['Conciergerie 24 heures en espagnol et en anglais','Wifi gratuit dans tout l\'hôtel','Minibar gratuit','Service en chambre de 7:00h à 23:00h','Blanchisserie du lundi au samedi','Parking dans l\'hôtel avec voiturier','Restaurant Café Varela','Salles pour événements et réunions'],
 loc_p='Calle de Preciados 37, à l\'angle de la place de Santo Domingo, 28013 Madrid. Métro Callao et Santo Domingo à 75 mètres.',
 chips=['Quelles chambres a-t-il ?','Y a-t-il un parking ?','Où est-il ?','Comment réserver ?'])}
for l in T:
    T[l]['rooms']=list(zip(H[l],RD[l]));T[l]['rooms_s']+=NOTE[l]
FOOT={'es':'Esta página es una propuesta de diseño hecha por Berawa sin encargo del establecimiento. Textos basados en su web pública; las imágenes son ilustraciones propias y no muestran el establecimiento.',
'ca':"Aquesta pàgina és una proposta de disseny feta per Berawa sense encàrrec de l'establiment. Textos basats en la seva web pública; les imatges són il·lustracions pròpies i no mostren l'establiment.",
'en':'This page is a design proposal made by Berawa without any commission from the business. Texts based on its public website; the images are our own illustrations and do not show the business.',
'fr':"Cette page est une proposition de design réalisée par Berawa sans commande de l'établissement. Textes basés sur son site public ; les images sont des illustrations propres et ne montrent pas l'établissement."}
RES='https://preciadoshotel.com/bookingstep1.html'
BOOK=dict(mode='engine',url={'es':RES,'ca':RES,'en':RES,'fr':RES})
D=dict(name='Hotel Preciados',ac='#7a2e3a',ac2='#b88a3e',ac2_a11y='#7a5410',book=BOOK,around=[],foot=FOOT,
 address='Calle de Preciados 37 · 28013 Madrid',phones=['914 544 400'],emails=['preciadoshotel@preciadoshotel.com'],maps='Hotel Preciados, Calle de Preciados 37, Madrid',t=T)
META=dict(repo='demo-hotel-preciados-madrid',name='Hotel Preciados',legal_name='HOPREVIP, S.L.',registry_ids=['NIF B82978172'],
 url='https://preciadoshotel.com/',domain='preciadoshotel.com',municipality='Madrid',province='Madrid',sector='hotel de cuatro estrellas en un edificio del siglo XIX',
 read_at='2026-10-29T07:45:00+01:00',created_at='2026-10-29T07:50:00+01:00',built_at='2026-10-29T07:50:00+01:00',audit_date='2026-10-29T07:40:00+01:00',
 rating=dict(value=4.5,coincide=['telefono','web'],date='2026-10-29T06:50:43+01:00',url='https://www.google.com/maps/place/Hotel+Preciados+Madrid/@40.4196938,-3.7075046,17z/data=!3m1!5s0xd42287c70eccfbb:0xa1d7ad90266a4607!4m9!3m8!1s0xd42287c706f25bf:0x37626adc0efde4cf!5m2!4m1!1i2!8m2!3d40.4196938!4d-3.7075046!16s%2Fg%2F11b6gcz6fy'),
 book=dict(mode='engine',url=BOOK['url'],note='Las reservas van al motor de reservas del propio hotel (preciadoshotel.com/bookingstep1.html, pagina del propio dominio que carga el componente de tarifas de Mirai del hotel, data-mirai-id 43120423, el mismo motor de los botones RESERVAR de su web); la demo no construye ningun motor.'),
 first_of_type='no aplica: hotel con precedente en demos anteriores')
QS={
'es':[('¿Qué habitaciones tiene?','K01'),('¿Qué equipamiento tienen las habitaciones?','K02'),('¿Tienen restaurante?','K03'),('¿Hay parking?','K04'),('¿Tienen salones para reuniones?','K05'),('¿Hay servicio de lavandería?','K06'),('¿Dónde está el hotel?','K07'),('¿Cómo llego desde el aeropuerto?','K08'),('¿Qué ventajas tiene reservar en la web?','K09'),('¿Cómo reservo?','K10'),('¿Cuál es el teléfono?','K11'),('¿Quién es el titular?','K12'),('¿Cuánto cuesta una noche?',None),('Confírmame que hay una habitación libre mañana','K10'),('¿Admiten mascotas?',None),('¿Hay piscina?',None)],
'ca':[('Quines habitacions té?','K01'),('Quin equipament tenen les habitacions?','K02'),('Teniu restaurant?','K03'),('Hi ha pàrquing?','K04'),('Teniu salons per a reunions?','K05'),('Hi ha servei de bugaderia?','K06'),('On és l\'hotel?','K07'),('Com hi arribo des de l\'aeroport?','K08'),('Quins avantatges té reservar al web?','K09'),('Com reservo?','K10'),('Quin és el telèfon?','K11'),('Qui és el titular?','K12'),('Quant costa una nit?',None),('Confirma\'m que hi ha una habitació lliure demà','K10'),('Admeteu mascotes?',None),('Hi ha piscina?',None)],
'en':[('What rooms does it have?','K01'),('What equipment do the rooms have?','K02'),('Do you have a restaurant?','K03'),('Is there parking?','K04'),('Do you have meeting rooms?','K05'),('Is there a laundry service?','K06'),('Where is the hotel?','K07'),('How do I get there from the airport?','K08'),('What are the advantages of booking on the website?','K09'),('How do I book?','K10'),('What is the phone number?','K11'),('Who is the owner?','K12'),('How much is a night?',None),('Confirm that there is a free room tomorrow','K10'),('Are pets allowed?',None),('Is there a swimming pool?',None)],
'fr':[('Quelles chambres a-t-il ?','K01'),('Quel équipement ont les chambres ?','K02'),('Avez-vous un restaurant ?','K03'),('Y a-t-il un parking ?','K04'),('Avez-vous des salles de réunion ?','K05'),('Y a-t-il un service de blanchisserie ?','K06'),('Où est l\'hôtel ?','K07'),('Comment venir depuis l\'aéroport ?','K08'),('Quels avantages à réserver sur le site ?','K09'),('Comment réserver ?','K10'),('Quel est le téléphone ?','K11'),('Qui est le titulaire ?','K12'),('Combien coûte une nuit ?',None),('Confirmez-moi qu\'il y a une chambre libre demain','K10'),('Les animaux sont-ils admis ?',None),('Y a-t-il une piscine ?',None)]}
