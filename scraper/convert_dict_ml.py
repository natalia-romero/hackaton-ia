
from categories import CELL, NOTEBOOK, STEREO_SYSTEM, KEYBOARD, \
    MOUSE, WEARABLE, TABLET, REFRIGERATOR, HEADPHONES, \
    KEYBOARD_MOUSE_COMBO, VIDEO_GAME_CONSOLE, MONITOR, \
    MEMORY_CARD, GAMING_CHAIR, STORAGE_DRIVE, POWER_SUPPLY, COMPUTER_CASE, \
    USB_FLASH_DRIVE, RAM, TELEVISION, AIR_CONDITIONER, OVEN, WASHING_MACHINE, \
    UPS, ALL_IN_ONE, VACUUM_CLEANER, PRINTER
categories_code = {
    'MLC1051': 'Celulares y Telefonía',
    'MLC1648': 'Computación',
    'MLC1000': 'Electrónica, Audio y Video',
    'MLC1574': 'Hogar y Muebles',
    'MLC1010': 'Audio',
    'MLC5054': 'Cables',
    'MLC4632': 'Controles Remotos',
    'MLC430918': 'Cables y Hubs USB',
    'MLC430687': 'Notebooks y Accesorios',
    'MLC454379': 'Periféricos de PC',
    'MLC433676': 'Tablets y Accesorios',
    'MLC159241': 'Lápices Touch',
    'MLC159232': 'Teclados',
    'MLC1714': 'Mouses',
    'MLC1713': 'Teclados',
    'MLC373735': 'Trackpads',
    'MLC6593': 'Cables y Adaptadores',
    'MLC11878': 'Candados de Seguridad',
    'MLC3813': 'Accesorios para Celulares',
    'MLC417704': 'Smartwatches y Accesorios',
    'MLC417755': 'Cargadores',
    'MLC434353': 'Mallas',
    'MLC436011': 'Adaptadores',
    'MLC4922': 'Cables de Datos',
    'MLC432437': 'Carcasas, Fundas y Protectores',
    'MLC5546': 'Cargadores',
    'MLC5549': 'Otros',
    'MLC157684': 'Cargadores con Cable',
    'MLC157688': 'Inalambrico',
    'MLC49334': 'Para TV',
    'MLC49342': 'Otros',
    'MLC116538': 'Smartwatches',
    'MLC85756': 'Accesorios',
    'MLC82067': 'Tablets',
    'MLC430637': 'PC de Escritorio',
    'MLC3690': 'Accesorios para Audio y Video',
    'MLC157822': 'Netbooks',
    'MLC1652': 'Notebooks',
    'MLC1055': 'Celulares y Smartphones',
    'MLC5726': 'Electrodomésticos',
    'MLC1430': 'Vestuario y Calzado',
    'MLC1012': 'Audio Portátil y Accesorios',
    'MLC3697': 'Audífonos',
    'MLC440071': 'Artefactos de Cuidado Personal',
    'MLC1581': 'Pequeños Electrodomésticos',
    'MLC1667': 'Cámaras Web',
    'MLC430630': 'Mouses y Teclados',
    'MLC1053': 'Telefonía Fija e Inalámbrica',
    'MLC432435': 'Colgantes y Soportes',
    'MLC439917': 'Apoya Celulares',
    'MLC439919': 'Porta Celulares',
    'MLC157686': 'Portatiles',  # baterias
    'MLC157694': 'Carcasas y Fundas',
    'MLC175454': 'Cases',
    'MLC12953': 'Láminas Protectoras',
    'MLC1144': 'Consolas y Videojuegos',
    'MLC1500': 'Construcción',
    'MLC1132': 'Juegos y Juguetes',
    'MLC1582': 'Iluminación para el Hogar',
    'MLC177170': 'Seguridad para el Hogar',
    'MLC1066': 'Alarmas y Sensores',
    'MLC179831': 'Circuito de Cámaras',
    'MLC5713': 'Cámaras de Vigilancia',
    'MLC438578': 'Accesorios para Consolas',
    'MLC439527': 'Accesorios para PC Gaming',
    'MLC455245': 'Xbox Series X/S',
    'MLC161962': 'Otros Xboxs',
    'MLC447778': 'Accesorios para PC Gaming',
    'MLC1655': 'Monitores y Accesorios',
    'MLC6263': 'Kits de Mouse y Teclado',
    'MLC1747': 'Accesorios para Vehículos',
    'MLC1071': 'Animales y Mascotas',
    'MLC1368': 'Arte, Librería y Cordonería',
    'MLC1384': 'Bebés',
    'MLC1246': 'Belleza y Cuidado Personal',
    'MLC1039': 'Cámaras y Accesorios',
    'MLC1276': 'Deportes y Fitness',
    'MLC3025': 'Libros, Revistas y Comics',
    'MLC3937': 'Relojes y Joyas',
    'MLC409431': 'Salud y Equipamiento Médico',
    'MLC174421': 'Pesas de Baño',
    'MLC66176': 'Termómetros',
    'MLC435370': 'Otros',
    'MLC3948': 'Relojes Murales',
    'MLC399230': 'Smartwatches',
    'MLC1631': 'Adornos y Decoración del Hogar',
    'MLC1592': 'Cocina y Menaje',
    'MLC436380': 'Muebles para el Hogar',
    'MLC436246': 'Textiles de Hogar y Decoración',
    'MLC177171': 'Porteros Eléctricos',
    'MLC163740': 'Ampolletas',
    'MLC163822': 'Cintas LED',
    'MLC431414': 'Accesorios para TV',
    'MLC11830': 'Componentes Electrónicos',
    'MLC174349': 'Media Streaming',
    'MLC9239': 'Proyectores y Telones',
    'MLC409415': 'Asistentes Virtuales',
    'MLC1024': 'Equipos de DJ y Accesorios',
    'MLC440366': 'Micrófonos y Preamplificadores',
    'MLC1362': 'Camping, Caza y Pesca',
    'MLC410723': 'Monopatines y Scooters',
    'MLC1049': 'Accesorios para Cámaras',
    'MLC4660': 'Filmadoras y Cámaras de Acción',
    'MLC420011': 'Estudio e Iluminación',
    'MLC174272': 'Para Cámaras de Acción',
    'MLC430367': 'Tarjetas de Memoria y Lectores',
    'MLC439596': 'Audífonos',
    'MLC448169': 'Controles para Gamers',
    'MLC187264': 'Sillas Gamer',
    'MLC439597': 'Otros',
    'MLC159228': 'Para PlayStation',
    'MLC159227': 'Para Xbox',
    'MLC116370': 'PS4 - PlayStation 4',
    'MLC455263': 'PS5 - PlayStation 5',
    'MLC440985': 'Cables y Adaptadores',
    'MLC116375': 'Otros',
    'MLC430598': 'Almacenamiento',
    'MLC1691': 'Componentes de PC',
    'MLC1700': 'Conectividad y Redes',
    'MLC1657': 'Proyectores y Telones',
    'MLC1723': 'Software',
    'MLC159231': 'Estuches y Fundas',
    'MLC159245': 'Láminas Protectoras',
    'MLC3378': 'Parlantes para PC',
    'MLC1716': 'Mouse Pads',
    'MLC440873': 'Tabletas Digitalizadoras',
    'MLC3377': 'Accesorios para Notebooks',
    'MLC54182': 'Bases Enfriadoras',
    'MLC9240': 'Cargadores y Fuentes',
    'MLC40749': 'Fundas',
    'MLC440858': 'Hubs USB',
    'MLC7223': 'Mochilas, Maletines y Fundas',
    'MLC3584': 'Otros',
    'MLC418042': 'Bases',
    'MLC21069': 'Monitores',
    'MLC440656': 'Adaptadores USB',
    'MLC430794': 'Cables de Red y Accesorios',
    'MLC430901': 'Routers',
    'MLC430788': 'Coolers y Ventiladores',
    'MLC430796': 'Discos y Accesorios',
    'MLC430916': 'Fuentes de Alimentación',
    'MLC1696': 'Gabinetes y Soportes de PC',
    'MLC1715': 'Cables',
    'MLC9729': 'Hubs USB',
    'MLC5895': 'Cables de Audio y Video',
    'MLC5877': 'Cables de Datos',
    'MLC1669': 'Discos y Accesorios',
    'MLC1673': 'Pen Drives',
    'MLC6777': 'Audífonos',
    'MLC440657': 'Controles para Gamers',
    'MLC447782': 'Sillas Gamer',
    'MLC447784': 'Otros',
    'MLC417705': 'Otros',
    'MLC5107': 'Cables de Audio y Video',
    'MLC175456': 'Joysticks',
    'MLC7908': 'Memorias',
    'MLC58500': 'Soportes para Vehiculos',
    'MLC432439': 'Otros',
    'MLC420040': 'Fundas Cargadoras',
    'MLC157689': 'Otros',
    'MLC5702': 'Artículos de Bebé para Baños',
    'MLC1392': 'Juegos y Juguetes para Bebés',
    'MLC22867': 'Accesorios de Auto y Camioneta',
    'MLC3381': 'Audio para Vehículos',
    'MLC1058': 'Handies y Radiofrecuencia',
    'MLC5542': 'Manos Libres',
    'MLC1002': 'Televisores',
    'MLC10177': 'Home Theater',
    'MLC1022': 'Parlantes y Subwoofers',
    'MLC2531': 'Climatización',
    'MLC1580': 'Hornos y Cocinas',
    'MLC1578': 'Lavado',
    'MLC1576': 'Refrigeración',
    'MLC9456': 'Refrigeradores',
    'MLC179816': 'Repuestos y Accesorios',
    'MLC4337': 'Aspiradoras',
    'MLC180993': 'Aspiradoras Robot',
    'MLC455108': 'Repuestos y Accesorios',
    'MLC178593': 'Lavadora-Secadoras',
    'MLC174300': 'Lavavajillas',
    'MLC27590': 'Secadoras',
    'MLC29800': 'Aires Acondicionados',
    'MLC176937': 'Repuestos y Accesorios',
    'MLC39109': 'Lápices y Uñetas',
    'MLC178483': 'Herramientas',
    'MLC1499': 'Industrias y Oficinas',
    'MLC1953': 'Otras Categorías',
    'MLC431994': 'Equipaje y Accesorios de Viaje',
    'MLC31406': 'Mochilas',
    'MLC435064': 'Tratamientos Respiratorios',
    'MLC179796': 'Humidificadores',
    'MLC179017': 'Purificadores de Aire',
    'MLC163741': 'Lámparas',
    'MLC1070': 'Otros',
    'MLC438287': 'Para Cocina',
    'MLC438286': 'Para Hogar',
    'MLC439831': 'Otros',
    'MLC440073': 'Artefactos para el Cabello',
    'MLC440072': 'Balanzas de Baño',
    'MLC1292': 'Ciclismo',
    'MLC440627': 'Pulsómetros y Cronómetros',
    'MLC179479': 'Monociclos Eléctricos',
    'MLC455434': 'Monopatines',
    'MLC178749': 'De Pie',
    'MLC455437': 'Eléctricos',
    'MLC163738': 'Cámaras',
    'MLC436831': 'Revelado y Laboratorio',
    'MLC17800': 'Antenas Wireless',
    'MLC11860': 'Parlantes',
    'MLC455192': 'Artefactos para el Cabello',
    'MLC417575': 'Barbería',
    'MLC1253': 'Cuidado de la Piel',
    'MLC393366': 'Higiene Personal',
    'MLC174815': 'Cepillos',
    'MLC447211': 'Cepillos Eléctricos',
    'MLC1720': 'UPS',
    'MLC1722': 'Otros',
    'MLC157821': 'Ultrabooks',
    'MLC440652': 'Switches',
    'MLC1694': 'Memorias RAM',
    'MLC1706': 'Tarjetas de Red',
    'MLC177923': 'Impresión',
    'MLC1676': 'Impresoras',
    'MLC2141': 'Insumos de Impresión',
    'MLC7415': 'Cartuchos de Tinta',
    'MLC10871': 'Tintas',
    'MLC3560': 'Toners',
    'MLC159250': 'Repuestos',
    'MLC191054': 'Micrófonos',
    'MLC159229': 'Para Nintendo',
    'MLC180910': 'Fuentes de Alimentación',
    'MLC180896': 'Headsets',
    'MLC440885': 'Micrófonos',
    'MLC40780': 'Controles Remotos',
    'MLC3581': 'Docking Stations',
    'MLC26532': 'Maletines y Bolsos',
    'MLC26538': 'Mochilas',
    'MLC431333': 'Filtros de Privacidad',
    'MLC418043': 'Soportes',
    'MLC3553': 'Memorias Digitales',
    'MLC430373': 'Otros',
    'MLC181025': 'All In One',
    'MLC1649': 'Computadores',
    'MLC178644': 'Mini PCs',
    'MLC175552': 'Soportes',
    'MLC440682': 'Repuestos para Notebooks',
    'MLC1014': 'Micro y Minicomponentes',
    'MLC438566': 'Consolas',
    'MLC455247': 'Fundas y Estuches',
    'MLC455248': 'Otros',
    'MLC439072': 'Audio y Video para Gaming',
    'MLC180981': 'Cargadores',
    'MLC413744': 'Fundas para Controles',
    'MLC430797': 'Accesorios',
    'MLC1672': 'Discos Duros y SSDs',
    'MLC10190': 'Repuestos',
    'MLC9183': 'Sillas',
    'MLC412717': 'Sillas Tándem',
    'MLC58760': 'Cables de Audio y Video',
    'MLC36587': 'Otros Cables',
    'MLC108729': 'Soportes para Parlantes',
    'MLC5068': 'Baterías',
    'MLC159270': 'Videojuegos',
    'MLC1367': 'Antigüedades y Colecciones',
    'MLC1456': 'Lentes y Accesorios',
    'MLC174662': 'Llaveros',
    'MLC412056': 'Paraguas',
    'MLC66190': 'Lentes de Sol',
    'MLC66191': 'Ópticos',
    'MLC66170': 'Otros',
    'MLC433069': 'Juegos de Agua y Playa',
    'MLC455425': 'Juegos de Construcción',
    'MLC432988': 'Juegos de Mesa y Cartas',
    'MLC436967': 'Juegos de Salón',
    'MLC12037': 'Juguetes Antiestrés e Ingenio',
    'MLC432818': 'Juguetes de Oficios',
    'MLC432888': 'Muñecos y Muñecas',
    'MLC1166': 'Peluches',
    'MLC3422': 'Figuras de Acción',
    'MLC2968': 'Muñecas y Bebés',
    'MLC455651': 'Puzzles',
    'MLC455518': 'Trompos',
    'MLC437053': 'Cartas Coleccionables R.P.G.',
    'MLC1161': 'Juegos de Mesa',
    'MLC175991': 'Puzzles',
    'MLC432989': 'Otros',
    'MLC5541': 'Pilas y Cargadores',
    'MLC440349': 'Video',
    'MLC40673': 'Cargadores de Pilas',
    'MLC9828': 'Pilas',
    'MLC431488': 'Amplificadores y Receivers',
    'MLC172273': 'Pinballs y Arcade',
    'MLC2930': 'PS2 - PlayStation 2',
    'MLC11623': 'PS3 - PlayStation 3',
    'MLC455274': 'Cargadores para Controles',
    'MLC455268': 'Fundas para Controles',
    'MLC455266': 'Gamepads y Joysticks',
    'MLC180980': 'Controles',
    'MLC420068': 'Fuentes de Alimentación',
    'MLC180986': 'Skins',
    'MLC439615': 'Controles y Joysticks',
    'MLC11625': 'Otros',
    'MLC4396': 'Game Boy Advance - GBA',
    'MLC2921': 'Game Cube',
    'MLC178658': 'Nintendo Switch',
    'MLC11223': 'Nintendo Wii',
    'MLC116432': 'Nintendo Wii U',
    'MLC161960': 'Otros Nintendos',
    'MLC190762': 'Fuentes de Alimentación',
    'MLC413678': 'Fundas y Estuches',
    'MLC416556': 'Gamepads y Joysticks',
    'MLC413679': 'Protectores de Pantalla',
    'MLC178843': 'Otros',
    'MLC431792': 'Cables de Red',
    'MLC180937': 'Cuadernos',
    'MLC440143': 'Estuches de Lápices',
    'MLC177774': 'Enfriadores de Aire',
    'MLC183159': 'Estufas y Calefactores',
    'MLC161360': 'Ventiladores',
    'MLC162501': 'Planchas',
    'MLC162504': 'Hervidores',
    'MLC439832': 'Preparación de Alimentos',
    'MLC438297': 'Preparación de Bebidas',
    'MLC162503': 'Arroceras',
    'MLC440064': 'Batidoras',
    'MLC411071': 'Sartenes y Ollas Eléctricas',
    'MLC162507': 'Tostadoras',
    'MLC30852': 'Cocinas',
    'MLC174295': 'Extractores y Purificadores',
    'MLC30854': 'Hornos',
    'MLC436300': 'Artículos de Vino y Coctelería',
    'MLC436280': 'Cocción y Horneado',
    'MLC159273': 'Utensilios de Preparación',
    'MLC436289': 'Vajilla y Artículos de Servir',
    'MLC159287': 'Bandejas',
    'MLC1604': 'Cuchillería',
    'MLC159295': 'Cuchillos de Cocina',
    'MLC159294': 'Juegos de Cuchillería',
    'MLC455317': 'Coladores y Tendederos',
    'MLC455321': 'Medidores de Cocina',
    'MLC180827': 'Otros',
    'MLC159285': 'Baterías de Cocina',
    'MLC159283': 'Ollas',
    'MLC159284': 'Sartenes',
    'MLC440063': 'Balanzas de Cocina',
    'MLC438291': 'Máquinas para Postres',
    'MLC180819': 'Licuadoras',
    'MLC438298': 'Otros',
    'MLC4340': 'Cafeteras',
    'MLC30109': 'Otros',
    'MLC171531': 'Encimeras',
    'MLC385176': 'Calefonts y Termos',
    'MLC440149': 'Sistemas de Monitoreo',
    'MLC174413': 'Timbres',
    'MLC177173': 'Otros',
    'MLC439844': 'Dispensadores y Purificadores',
    'MLC455131': 'Cepillos',
    'MLC455118': 'Filtros',
    'MLC455113': 'Otros',
    'MLC1621': 'Jardín y Aire Libre',
    'MLC162500': 'Freidoras',
    'MLC174302': 'Hornos de Pan',
    'MLC30848': 'Microondas',
    'MLC158419': 'Cavas de Vino',
    'MLC158426': 'Freezers',
    'MLC436298': 'Almacenamiento y Organización',
    'MLC1593': 'Vajilla',
    'MLC440224': 'Fuentes',
    'MLC179055': 'Jarras',
    'MLC30082': 'Juegos de Vajilla',
    'MLC436277': 'Afiladores',
    'MLC180832': 'Moldes',
    'MLC159275': 'Tablas para Picar',
    'MLC440222': 'Bandejas, Asaderas y Fuentes',
    'MLC440124': 'Baterías, Ollas y Sartenes',
    'MLC436281': 'Otros',
    'MLC440219': 'Vaporieras',
    'MLC1899': 'Otros',
    'MLC455059': 'Repuestos y Accesorios',
    'MLC30849': 'Otros',
    'MLC392350': 'Para Cocinas y Hornos',
    'MLC455060': 'Otros',
    'MLC392406': 'Calderas',
    'MLC29793': 'Chimeneas y Salamandras',
    'MLC431237': 'Calefonts',
    'MLC431238': 'Termos',
    'MLC1613': 'Baños',
    'MLC2521': 'Piscinas y Accesorios',
    'MLC455386': 'Spa Exterior',
    'MLC433511': 'Calentadores',
    'MLC440092': 'Limpieza y Mantenimiento',
    'MLC177072': 'Piscinas',
    'MLC30988': 'Otros',
    'MLC1590': 'Otros',
    'MLC1616': 'Accesorios para Baño',
    'MLC443824': 'Tinas',
    'MLC439847': 'Electricidad',
    'MLC180881': 'Mobiliario para Baños',
    'MLC440069': 'Jugueras',
    'MLC429556': 'Minipimers',
    'MLC174293': 'Parrillas Eléctricas',
    'MLC401945': 'Otros',
    'MLC162502': 'Sandwicheras',
    'MLC440067': 'Procesadores',
    'MLC179543': 'Waffleras',
    'MLC162505': 'Yogurteras',
    'MLC436275': 'Utensilios de Repostería',
    'MLC159296': 'Tenedores',
    'MLC455100': 'Para Aires Acondicionados',
    'MLC176940': 'Para Calefont y Termos',
    'MLC435273': 'Gasfitería',
    'MLC411938': 'Mobiliario para Cocinas',
    'MLC438290': 'Otros',
    'MLC440070': 'Exprimidores Eléctricos',
    'MLC175499': 'Mopas a Vapor',
    'MLC4222': 'Teclados',
    'MLC3709': 'Pantallas',
    'MLC159233': 'Pantallas',
    'MLC440859': 'Memorias RAM para Laptops',
    'MLC40779': 'Carcasas',
    'MLC26535': 'Otros',
    'MLC439836': 'Eléctricos',  # estufa
    'MLC159342': 'Reproductor Blu-Ray',
    'MLC1588': 'Lámparas de Techo',
    'MLC418448': 'Teclados Físicos',
    'MLC455085': 'Otros',
    'MLC161249': 'Otros',
    'MLC385693': 'Filtros para Aires Ac.',
    'MLC392407': 'A Gas',
    'MLC161241': 'Eléctricas',
    'MLC159246': 'Carcasas',
    'MLC159234': 'Otros Accesorios',
    'MLC159251': 'Soportes',
    'MLC1695': 'Fuentes de Poder',
    'MLC438144': 'A Combustión',
    'MLC440821': 'Gabinetes',
    'MLC163820': 'Lámparas de Mesa',
    'MLC163742': 'Otras Lámparas',
    'MLC1586': 'Apliques de Pared',
    'MLC1585': 'Lámparas de Pie',
    'MLC183366': 'USB',
    'MLC39209': 'Para Auriculares',
    'MLC436012': 'Otros',
    'MLC6576': 'Chips',
    'MLC432444': 'Otros',
    'MLC429461': 'Docking Stations',
    'MLC3707': 'Discos Duros y SSDs',
    'MLC30850': 'Máquinas de Coser',
    'MLC1606': 'Balanzas de Cocina',
    'MLC174449': 'Parrillas Eléctricas',
    'MLC455114': 'Bolsas',
    'MLC174024': 'Máquinas para Helados',
    'MLC159269': 'Máquina para Pastas',
    'MLC162506': 'Vaporeras',
    'MLC375459': 'Woks',
    'MLC429383': 'Papel Mantequilla',
    'MLC436294': 'Pinzas',
    'MLC440220': 'Biferas',
    'MLC163539': 'Marcos para Fotos',
    'MLC1042': 'Cámaras Digitales',
    'MLC175537': 'Cámaras Análogas',
    'MLC175541': 'Estabilizadores para Cámaras',
    'MLC430419': 'Drones',
    'MLC179485': 'Drones',
    'MLC430383': 'Impresoras',
    'MLC437061': 'Trípodes para Cámaras',
    'MLC9776': 'Cargadores de Baterías',
    'MLC3542': 'Binoculares',
    'MLC174250': 'Micrófonos',
    'MLC70324': 'Para Cámaras Instantáneas',
    'MLC183303': 'Baterías',
    'MLC174273': 'Otros',
    'MLC436880': 'Álbumes de Fotos',
    'MLC440100': 'Bolsos',
    'MLC1045': 'Lentes',
    'MLC413541': 'Oculares',
    'MLC413487': 'Kits para Cámaras de Acción',
    'MLC440107': 'Otros',
    'MLC174279': 'Soportes y Bastones',
    'MLC174248': 'Carcasas',
    'MLC183305': 'Cargadores',
    'MLC3541': 'Telescopios',
    'MLC417788': 'Otros',
    'MLC183307': 'Otros',
    'MLC183313': 'Protectores de Hélices',
    'MLC431308': 'Convertidores de Zapatas',
    'MLC440101': 'Mochilas',
    'MLC70289': 'Fundas y Estuches',
    'MLC436887': 'Otros',
    'MLC3544': 'Otros',
    'MLC70326': 'Controles Remotos',
    'MLC9780': 'Baterías',
    'MLC440099': 'Para Cámaras de Video',
    'MLC430406': 'Baterías',
    'MLC3357': 'Otros',
    'MLC174249': 'Correas',
    'MLC9829': 'Otros',
    'MLC179487': 'Otros',
    'MLC440106': 'USB',
    'MLC183308': 'Cámaras',
    'MLC70325': 'Otros',
    'MLC179048': 'Iluminadores',
    'MLC1046': 'Filtros',
    'MLC414249': 'Kits para Estudio Fotográfico',
    'MLC183306': 'Controles',
    'MLC183309': 'Hélices',
    'MLC174247': 'Monitores',
    'MLC1914': 'Otros',
    'MLC179047': 'Flashes',
    'MLC70299': 'Grips',
    'MLC430411': 'Controles',
    'MLC436885': 'Tubos de Extensión',
    'MLC183302': 'Antenas',
    'MLC183310': 'Mochilas y Estuches',
    'MLC40697': 'Proyectores',
    'MLC18222': 'Soportes',
    'MLC440710': 'Cables Power',
    'MLC4075': 'Micrófonos',
    'MLC172568': 'Parlantes Portátiles',
    'MLC2876': 'Tornamesas',
    'MLC49668': 'Soportes',
    'MLC3698': 'Otros',
    'MLC455701': 'Reproductores Portátiles',
    'MLC174336': 'Conectores',
    'MLC60306': 'Digital',
    'MLC2854': 'Radios',
    'MLC40698': 'Telones',
    'MLC44388': 'Adaptadores',
    'MLC179474': 'Otros',
    'MLC175495': 'Interfaces de Audio',
    'MLC455686': 'Torres de Sonido',
    'MLC174313': 'Otros',
    'MLC174330': 'Sensores Inductivos',
    'MLC417360': 'Luces Led Profesionales',
    'MLC36529': 'Cables de Datos',
    'MLC1021': 'Sinto Amplificadores',
    'MLC174403': 'Monitores de Estudio',
    'MLC2675': 'Amplificadores',
    'MLC439802': 'Espumas Acústicas',
    'MLC430186': 'Para Media Streaming',
    'MLC44895': 'Lásers Profesionales',
    'MLC174561': 'Atriles',
    'MLC178457': 'Alisadores de Pelo',
    'MLC4597': 'Secadores de Pelo',
    'MLC5411': 'Máquinas para Cortar el Pelo',
    'MLC181012': 'Purificadores de Agua',
    'MLC178456': 'Alisadores',
    'MLC43660': 'Rizadores y Onduladores',
    'MLC433579': 'Filtros de Agua',
    'MLC11094': 'Micrófonos',
    'MLC440729': 'Reproductores de CD',
    'MLC429275': 'Correas',
    'MLC2907': 'Equipos Móviles',
    'MLC158420': 'Frigobares',
    'MLC2048': 'Joysticks',
    'MLC455246': 'Joysticks',
    'MLC448171': 'Joysticks',
    'MLC180982': 'Headsets',
    'MLC440875': 'Gamepads',
    'MLC440348': 'Para Otras Consolas',
    'MLC455264': 'Fuentes de Alimentación',
    'MLC455415': 'Cámaras',
    'MLC46509': 'Volantes',
    'MLC58405': 'Gamepads y Joysticks',
    'MLC439660': 'Cables y Adaptadores',
    'MLC416554': 'Gamepads y Joysticks',
    'MLC11964': 'Otros',
    'MLC116433': 'Otros',
    'MLC440647': 'Otros',
    'MLC174376': 'Walkman',

}
categories_name = {
    'Celulares y Telefonía': None,
    'Computación': None,
    'Electrónica, Audio y Video': None,
    'Hogar y Muebles': None,
    'Audio': None,
    'Cables': None,
    'Controles Remotos': None,
    'Cables y Hubs USB': None,
    'Notebooks y Accesorios': NOTEBOOK,
    'Periféricos de PC': None,
    'Tablets y Accesorios': TABLET,
    'Lápices Touch': None,
    'Teclados': KEYBOARD,
    'Mouses': MOUSE,
    'Trackpads': None,
    'Cables y Adaptadores': None,
    'Candados de Seguridad': None,
    'Accesorios para Celulares': None,
    'Smartwatches y Accesorios': WEARABLE,
    'Cargadores': None,
    'Mallas': None,
    'Adaptadores': None,
    'Cables de Datos': None,
    'Carcasas, Fundas y Protectores': None,
    'Otros': None,
    'Cargadores con Cable': None,
    'Inalambrico': None,
    'Para TV': None,
    'Smartwatches': WEARABLE,
    'Accesorios': None,
    'Tablets': TABLET,
    'PC de Escritorio': None,
    'Accesorios para Audio y Video': None,
    'Netbooks': NOTEBOOK,
    'Notebooks': NOTEBOOK,
    'Celulares y Smartphones': CELL,
    'Electrodomésticos': None,
    'Vestuario y Calzado': None,
    'Audio Portátil y Accesorios': STEREO_SYSTEM,
    'Audífonos': HEADPHONES,
    'Artefactos de Cuidado Personal': None,
    'Pequeños Electrodomésticos': OVEN,
    'Cámaras Web': None,
    'Mouses y Teclados': None,
    'Telefonía Fija e Inalámbrica': None,
    'Colgantes y Soportes': None,
    'Apoya Celulares': None,
    'Porta Celulares': None,
    'Portatiles': None,
    'Carcasas y Fundas': None,
    'Cases': None,
    'Láminas Protectoras': None,
    'Consolas y Videojuegos': None,
    'Construcción': None,
    'Juegos y Juguetes': None,
    'Iluminación para el Hogar': None,
    'Seguridad para el Hogar': None,
    'Alarmas y Sensores': None,
    'Circuito de Cámaras': None,
    'Cámaras de Vigilancia': None,
    'Accesorios para Consolas': None,
    'Accesorios para PC Gaming': None,
    'Xbox Series X/S': VIDEO_GAME_CONSOLE,
    'Otros Xboxs': None,
    'Monitores y Accesorios': MONITOR,
    'Kits de Mouse y Teclado': KEYBOARD_MOUSE_COMBO,
    'Accesorios para Vehículos': None,
    'Animales y Mascotas': None,
    'Arte, Librería y Cordonería': None,
    'Bebés': None,
    'Belleza y Cuidado Personal': None,
    'Cámaras y Accesorios': None,
    'Deportes y Fitness': None,
    'Libros, Revistas y Comics': None,
    'Relojes y Joyas': None,
    'Salud y Equipamiento Médico': None,
    'Pesas de Baño': None,
    'Termómetros': None,
    'Relojes Murales': None,
    'Adornos y Decoración del Hogar': None,
    'Cocina y Menaje': None,
    'Muebles para el Hogar': None,
    'Textiles de Hogar y Decoración': None,
    'Porteros Eléctricos': None,
    'Ampolletas': None,
    'Cintas LED': None,
    'Accesorios para TV': None,
    'Componentes Electrónicos': None,
    'Media Streaming': None,
    'Proyectores y Telones': None,
    'Asistentes Virtuales': None,
    'Equipos de DJ y Accesorios': None,
    'Micrófonos y Preamplificadores': None,
    'Camping, Caza y Pesca': None,
    'Monopatines y Scooters': None,
    'Accesorios para Cámaras': None,
    'Filmadoras y Cámaras de Acción': None,
    'Estudio e Iluminación': None,
    'Para Cámaras de Acción': None,
    'Tarjetas de Memoria y Lectores': MEMORY_CARD,
    'Controles para Gamers': None,
    'Sillas Gamer': GAMING_CHAIR,
    'Para PlayStation': None,
    'Para Xbox': None,
    'PS4 - PlayStation 4': VIDEO_GAME_CONSOLE,
    'PS5 - PlayStation 5': VIDEO_GAME_CONSOLE,
    'Almacenamiento': STORAGE_DRIVE,
    'Componentes de PC': None,
    'Conectividad y Redes': None,
    'Software': None,
    'Estuches y Fundas': None,
    'Parlantes para PC': STEREO_SYSTEM,
    'Mouse Pads': None,
    'Tabletas Digitalizadoras': TABLET,
    'Accesorios para Notebooks': None,
    'Bases Enfriadoras': None,
    'Cargadores y Fuentes': None,
    'Fundas': None,
    'Hubs USB': None,
    'Mochilas, Maletines y Fundas': None,
    'Bases': None,
    'Monitores': MONITOR,
    'Adaptadores USB': None,
    'Cables de Red y Accesorios': None,
    'Routers': None,
    'Coolers y Ventiladores': None,
    'Discos y Accesorios': None,
    'Fuentes de Alimentación': POWER_SUPPLY,
    'Gabinetes y Soportes de PC': COMPUTER_CASE,
    'Cables de Audio y Video': None,
    'Pen Drives': USB_FLASH_DRIVE,
    'Joysticks': None,
    'Memorias': MEMORY_CARD,
    'Soportes para Vehiculos': None,
    'Fundas Cargadoras': None,
    'Artículos de Bebé para Baños': None,
    'Juegos y Juguetes para Bebés': None,
    'Accesorios de Auto y Camioneta': None,
    'Audio para Vehículos': None,
    'Handies y Radiofrecuencia': None,
    'Manos Libres': None,
    'Televisores': TELEVISION,
    'Home Theater': STEREO_SYSTEM,
    'Parlantes y Subwoofers': STEREO_SYSTEM,
    'Climatización': AIR_CONDITIONER,
    'Hornos y Cocinas': OVEN,
    'Lavado': WASHING_MACHINE,
    'Refrigeración': REFRIGERATOR,
    'Refrigeradores': REFRIGERATOR,
    'Repuestos y Accesorios': None,
    'Aspiradoras': VACUUM_CLEANER,
    'Aspiradoras Robot': VACUUM_CLEANER,
    'Lavadora-Secadoras': WASHING_MACHINE,
    'Lavavajillas': None,
    'Secadoras': WASHING_MACHINE,
    'Aires Acondicionados': AIR_CONDITIONER,
    'Lápices y Uñetas': None,
    'Herramientas': None,
    'Industrias y Oficinas': None,
    'Otras Categorías': None,
    'Equipaje y Accesorios de Viaje': None,
    'Mochilas': None,
    'Tratamientos Respiratorios': None,
    'Humidificadores': None,
    'Purificadores de Aire': None,
    'Lámparas': None,
    'Para Cocina': None,
    'Para Hogar': None,
    'Artefactos para el Cabello': None,
    'Balanzas de Baño': None,
    'Ciclismo': None,
    'Pulsómetros y Cronómetros': None,
    'Monociclos Eléctricos': None,
    'Monopatines': None,
    'De Pie': None,
    'Cámaras': None,
    'Revelado y Laboratorio': None,
    'Antenas Wireless': None,
    'Parlantes': STEREO_SYSTEM,
    'Barbería': None,
    'Cuidado de la Piel': None,
    'Higiene Personal': None,
    'Cepillos': None,
    'Cepillos Eléctricos': None,
    'UPS': UPS,
    'Ultrabooks': NOTEBOOK,
    'Switches': None,
    'Memorias RAM': RAM,
    'Tarjetas de Red': None,
    'Impresión': None,
    'Impresoras': PRINTER,
    'Insumos de Impresión': None,
    'Cartuchos de Tinta': None,
    'Tintas': None,
    'Toners': None,
    'Repuestos': None,
    'Micrófonos': None,
    'Para Nintendo': None,
    'Headsets': HEADPHONES,
    'Docking Stations': None,
    'Maletines y Bolsos': None,
    'Filtros de Privacidad': None,
    'Soportes': None,
    'Memorias Digitales': None,
    'All In One': ALL_IN_ONE,
    'Computadores': None,
    'Mini PCs': None,
    'Repuestos para Notebooks': None,
    'Micro y Minicomponentes': STEREO_SYSTEM,
    'Consolas': VIDEO_GAME_CONSOLE,
    'Fundas y Estuches': None,
    'Audio y Video para Gaming': None,
    'Fundas para Controles': None,
    'Discos Duros y SSDs': STORAGE_DRIVE,
    'Sillas': None,
    'Sillas Tándem': None,
    'Otros Cables': None,
    'Soportes para Parlantes': None,
    'Baterías': None,
    'Videojuegos': None,
    'Antigüedades y Colecciones': None,
    'Lentes y Accesorios': None,
    'Llaveros': None,
    'Paraguas': None,
    'Lentes de Sol': None,
    'Ópticos': None,
    'Juegos de Agua y Playa': None,
    'Juegos de Construcción': None,
    'Juegos de Mesa y Cartas': None,
    'Juegos de Salón': None,
    'Juguetes Antiestrés e Ingenio': None,
    'Juguetes de Oficios': None,
    'Muñecos y Muñecas': None,
    'Peluches': None,
    'Figuras de Acción': None,
    'Muñecas y Bebés': None,
    'Puzzles': None,
    'Trompos': None,
    'Cartas Coleccionables R.P.G.': None,
    'Juegos de Mesa': None,
    'Pilas y Cargadores': None,
    'Video': None,
    'Cargadores de Pilas': None,
    'Pilas': None,
    'Amplificadores y Receivers': None,
    'Pinballs y Arcade': None,
    'PS2 - PlayStation 2': VIDEO_GAME_CONSOLE,
    'PS3 - PlayStation 3': VIDEO_GAME_CONSOLE,
    'Cargadores para Controles': None,
    'Gamepads y Joysticks': None,
    'Controles': None,
    'Skins': None,
    'Controles y Joysticks': None,
    'Game Boy Advance - GBA': VIDEO_GAME_CONSOLE,
    'Game Cube': VIDEO_GAME_CONSOLE,
    'Nintendo Switch': VIDEO_GAME_CONSOLE,
    'Nintendo Wii': VIDEO_GAME_CONSOLE,
    'Nintendo Wii U': VIDEO_GAME_CONSOLE,
    'Protectores de Pantalla': None,
    'Cables de Red': None,
    'Cuadernos': None,
    'Estuches de Lápices': None,
    'Enfriadores de Aire': None,
    'Estufas y Calefactores': None,
    'Ventiladores': None,
    'Planchas': None,
    'Hervidores': None,
    'Preparación de Alimentos': None,
    'Preparación de Bebidas': None,
    'Arroceras': None,
    'Batidoras': None,
    'Sartenes y Ollas Eléctricas': None,
    'Tostadoras': None,
    'Cocinas': None,
    'Extractores y Purificadores': None,
    'Hornos': OVEN,
    'Artículos de Vino y Coctelería': None,
    'Cocción y Horneado': OVEN,
    'Utensilios de Preparación': None,
    'Vajilla y Artículos de Servir': None,
    'Bandejas': None,
    'Cuchillería': None,
    'Cuchillos de Cocina': None,
    'Juegos de Cuchillería': None,
    'Coladores y Tendederos': None,
    'Medidores de Cocina': None,
    'Baterías de Cocina': None,
    'Ollas': None,
    'Sartenes': None,
    'Balanzas de Cocina': None,
    'Máquinas para Postres': None,
    'Licuadoras': None,
    'Cafeteras': None,
    'Encimeras': None,
    'Calefonts y Termos': None,
    'Sistemas de Monitoreo': None,
    'Timbres': None,
    'Dispensadores y Purificadores': None,
    'Filtros': None,
    'Jardín y Aire Libre': None,
    'Freidoras': None,
    'Hornos de Pan': None,
    'Microondas': OVEN,
    'Cavas de Vino': None,
    'Freezers': REFRIGERATOR,
    'Almacenamiento y Organización': None,
    'Vajilla': None,
    'Fuentes': None,
    'Jarras': None,
    'Juegos de Vajilla': None,
    'Afiladores': None,
    'Moldes': None,
    'Tablas para Picar': None,
    'Bandejas, Asaderas y Fuentes': None,
    'Baterías, Ollas y Sartenes': None,
    'Vaporieras': None,
    'Para Cocinas y Hornos': None,
    'Calderas': None,
    'Chimeneas y Salamandras': None,
    'Calefonts': None,
    'Termos': None,
    'Baños': None,
    'Piscinas y Accesorios': None,
    'Spa Exterior': None,
    'Calentadores': None,
    'Limpieza y Mantenimiento': None,
    'Piscinas': None,
    'Accesorios para Baño': None,
    'Tinas': None,
    'Electricidad': None,
    'Mobiliario para Baños': None,
    'Jugueras': None,
    'Minipimers': None,
    'Parrillas Eléctricas': None,
    'Sandwicheras': None,
    'Procesadores': None,  # procesadores de comida
    'Waffleras': None,
    'Yogurteras': None,
    'Utensilios de Repostería': None,
    'Tenedores': None,
    'Para Aires Acondicionados': None,
    'Para Calefont y Termos': None,
    'Gasfitería': None,
    'Mobiliario para Cocinas': None,
    'Exprimidores Eléctricos': None,
    'Mopas a Vapor': None,
    'Pantallas': None,
    'Memorias RAM para Laptops': RAM,
    'Carcasas': None,
    'Eléctricos': None,
    'Reproductor Blu-Ray': None,
    'Lámparas de Techo': None,
    'Teclados Físicos': KEYBOARD,
    'A Combustión': None,
    'Filtros para Aires Ac.': None,
    'A Gas': None,
    'Eléctricas': None,
    'Otros Accesorios': None,
    'Fuentes de Poder': POWER_SUPPLY,
    'Gabinetes': COMPUTER_CASE,
    'Lámparas de Mesa': None,
    'Otras Lámparas': None,
    'Apliques de Pared': None,
    'Lámparas de Pie': None,
    'USB': None,
    'Para Auriculares': None,
    'Chips': None,
    'Máquinas de Coser': None,
    'Bolsas': None,
    'Máquinas para Helados': None,
    'Máquina para Pastas': None,
    'Vaporeras': None,
    'Woks': None,
    'Papel Mantequilla': None,
    'Pinzas': None,
    'Biferas': None,
    'Marcos para Fotos': None,
    'Cámaras Digitales': None,
    'Cámaras Análogas': None,
    'Estabilizadores para Cámaras': None,
    'Drones': None,
    'Trípodes para Cámaras': None,
    'Cargadores de Baterías': None,
    'Binoculares': None,
    'Para Cámaras Instantáneas': None,
    'Álbumes de Fotos': None,
    'Bolsos': None,
    'Lentes': None,
    'Oculares': None,
    'Kits para Cámaras de Acción': None,
    'Soportes y Bastones': None,
    'Telescopios': None,
    'Protectores de Hélices': None,
    'Convertidores de Zapatas': None,
    'Para Cámaras de Video': None,
    'Correas': None,
    'Iluminadores': None,
    'Kits para Estudio Fotográfico': None,
    'Hélices': None,
    'Flashes': None,
    'Grips': None,
    'Tubos de Extensión': None,
    'Antenas': None,
    'Mochilas y Estuches': None,
    'Proyectores': None,
    'Cables Power': None,
    'Parlantes Portátiles': STEREO_SYSTEM,
    'Tornamesas': None,
    'Reproductores Portátiles': None,
    'Conectores': None,
    'Digital': None,
    'Radios': None,
    'Telones': None,
    'Interfaces de Audio': None,
    'Torres de Sonido': STEREO_SYSTEM,
    'Sensores Inductivos': None,
    'Luces Led Profesionales': None,
    'Sinto Amplificadores': None,
    'Monitores de Estudio': MONITOR,
    'Amplificadores': STEREO_SYSTEM,
    'Espumas Acústicas': None,
    'Para Media Streaming': None,
    'Lásers Profesionales': None,
    'Atriles': None,
    'Otros Nintendos': None,
    'Alisadores de Pelo': None,
    'Secadores de Pelo': None,
    'Máquinas para Cortar el Pelo': None,
    'Purificadores de Agua': None,
    'Alisadores': None,
    'Rizadores y Onduladores': None,
    'Filtros de Agua': None,
    'Reproductores de CD': None,
    'Equipos Móviles': CELL,
    'Frigobares': REFRIGERATOR,
    'Gamepads': None,
    'Para Otras Consolas': None,
    'Volantes': None,
    'Walkman': None
}

all_categories = []
for code, ml_category in categories_code.items():
    all_categories.append((code, ml_category, categories_name[ml_category]))

print(all_categories)