--
-- PostgreSQL database dump
--

-- Dumped from database version 9.0.2
-- Dumped by pg_dump version 9.0.2
-- Started on 2011-03-01 20:23:19 CET

SET statement_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = off;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET escape_string_warning = off;

SET search_path = public, pg_catalog;

--
-- TOC entry 1866 (class 0 OID 0)
-- Dependencies: 1565
-- Name: frontend_incident_id_seq; Type: SEQUENCE SET; Schema: public; Owner: incidents-ratp
--

SELECT pg_catalog.setval('frontend_incident_id_seq', 196, true);


--
-- TOC entry 1867 (class 0 OID 0)
-- Dependencies: 1561
-- Name: frontend_line_id_seq; Type: SEQUENCE SET; Schema: public; Owner: incidents-ratp
--

SELECT pg_catalog.setval('frontend_line_id_seq', 28, true);


--
-- TOC entry 1868 (class 0 OID 0)
-- Dependencies: 1563
-- Name: frontend_station_id_seq; Type: SEQUENCE SET; Schema: public; Owner: incidents-ratp
--

SELECT pg_catalog.setval('frontend_station_id_seq', 1, false);


--
-- TOC entry 1861 (class 0 OID 722021)
-- Dependencies: 1562
-- Data for Name: frontend_line; Type: TABLE DATA; Schema: public; Owner: incidents-ratp
--

COPY frontend_line (id, name) FROM stdin;
1	Metro 1
2	Metro 3
3	Metro 2
4	Metro 4
5	Metro 5
6	Metro 6
7	Metro 7
8	Metro 8
9	Metro 9
10	Metro 10
11	Metro 11
12	Metro 12
13	Metro 13
14	Metro 14
15	RER A
16	RER B
17	RER C
18	RER D
19	RER E
28	Transilien J
\.


--
-- TOC entry 1862 (class 0 OID 722029)
-- Dependencies: 1564 1861
-- Data for Name: frontend_station; Type: TABLE DATA; Schema: public; Owner: incidents-ratp
--

COPY frontend_station (id, name, line_id) FROM stdin;
\.


--
-- TOC entry 1863 (class 0 OID 722042)
-- Dependencies: 1566 1861 1862
-- Data for Name: frontend_incident; Type: TABLE DATA; Schema: public; Owner: incidents-ratp
--

COPY frontend_incident (id, line_id, station_id, "time", plus, minus, ended, reason, contributors, validated) FROM stdin;
60	2	\N	2011-02-25 07:39:58.268825+01	0	4	0	Incident technique trafic perturbé sur l'ensemble de à jme.	b_zak3@hotmail.com	f
45	15	\N	2011-02-24 07:38:49.578789+01	0	4	0	Le site http://www.ratp.fr/horaires/fr/ratp/rer/prochains_passages/RA/Charles+de+Gaulle-Etoile/A est supposé fournir les horaires des prochaines rames, mais aussi signaler par un bandeau, les incidents, les modifications ou interruptions de trafic, leur cause, leur durée prévue.\r\nOr bien que le RERA ne desserve plus Poissy ni Cergy à partir de 22h00, aucun bandeau ne l'indiquait hier soir sur le site.. ! aucune information sur le fait que le trafic était interrompu.\r\nIl fallait donc se rendre en station pour apprendre qu'il n'y avait plus à attendre de RER vers Poissy, et qu'il fallait donc rejoindre donc le réseau SNCF via la gare st Lazare.	gpecheu@orange.fr	f
16	16	\N	2010-12-14 00:36:50+01	3	0	9	Mesure de sécurité	(14440997303877633, ogirardot),(14440997303877633, ogirardot),(14440997303877633, ogirardot),(14440997303877633, ogirardot)	f
17	16	\N	2010-12-14 00:36:45+01	0	6	0	test	(14462009990975488, ogirardot)	f
1	\N	\N	2010-12-13 08:37:34+01	0	6	0	Hop	P@2603.fr	f
2	2	\N	2010-12-14 00:37:32+01	5	11	0	test Père Noël sur la voie	me	f
18	16	\N	2010-12-14 00:37:38+01	0	5	0	test 2	(14463728363773952, ogirardot)	f
12	15	\N	2010-12-14 00:02:18+01	8	7	0	colis suspect	(14251438389592064, un_Jon),(14251438389592064, un_Jon),(14251438389592064, un_Jon),(14251438389592064, un_Jon),(14251438389592064, un_Jon),(14251438389592064, un_Jon),(14251438389592064, un_Jon),(14251438389592064, un_Jon),(14251438389592064, un_Jon)	f
13	2	\N	2010-12-14 00:02:18+01	8	0	8	test Pere Noël sur la voie	(14217654910849024, pdubost),(14217654910849024, pdubost),(14217654910849024, pdubost),(14217654910849024, pdubost),(14217654910849024, pdubost),(14217654910849024, pdubost),(14217654910849024, pdubost),(14217654910849024, pdubost),(14217654910849024, pdubost)	f
59	16	\N	2011-02-25 08:05:01.745094+01	24	22	16	Ligne B en direction de l'aéroport CDG, un matin pluvieux. Il aurait du s'arrêter à La Plaine stade de France. Après la sortie du tunnel de gare de nord, les gens commencent à se lever et là.... surprise : le chauffeur ne s'arrête pas, juste un simple message "j'ai oublié de m'arrêter"....\r\nstation suivante: pas de RER qui nous attend! obligé d'attendre 15mn supplémentaires pour avoir un train dans le sens inverse!\r\ninadmissible!	domynosol@hotmail.com	t
8	17	\N	2010-12-14 00:37:19+01	3	5	6	Accident grave de voyageur	ssaboum@gmail.com	f
20	5	\N	2010-12-14 08:52:05+01	1	0	0	panne de signalisation	(14585369353781248, ogirardot)	t
7	10	\N	2010-12-14 00:37:23+01	1	0	5	Accident grave de voyageur	ssaboum@gmail.com	f
3	2	\N	2010-12-14 00:37:09+01	0	6	1	test Pere Noël sur la voie	twitter	f
19	15	\N	2010-12-14 09:52:50+01	2	0	0	mesure de sécurité	(14585464564482049, ogirardot)	t
21	6	\N	2010-12-14 10:50:51+01	2	0	0	panne de signalisation	(14585307475222528, ogirardot)	t
11	16	\N	2010-12-13 22:18:21+01	0	0	18	mesure de sécurité	ssaboum@gmail.com	f
22	15	\N	2010-12-14 17:47:50+01	1	0	0	Un accident grave de voyageur à Bécon les Bruyères perturbe le trafic sur la ligne.\r\nLes trains circulent avec des retards de 10 à 20 minutes et des suppressions et modifications de desserte sont possibles sur les axes : Cergy Le Haut et Poissy. 	ssaboum@gmail.com	t
6	18	\N	2010-12-14 00:37:25+01	2	0	7	Incident technique	ssaboum@gmail.com	f
4	15	\N	2010-12-14 00:37:28+01	7	9	20	colis suspect	ssaboum@gmail.com	f
5	13	\N	2010-12-14 00:37:30+01	0	7	3	c'est la 13	xlinh.labbe@gmail.com	f
10	2	\N	2010-12-13 22:19:41+01	1	0	19	panne électrique	ssaboum@gmail.com	f
62	17	\N	2011-02-25 10:27:19.695421+01	4	7	0	Ralentissement entre juvisy et bfm	marsu15@gmail.com	f
47	16	\N	2011-02-24 10:54:05.096288+01	15	20	8	pas de signalisation TV à Cité U	(40674790947688448, TDLKB)	f
41	9	\N	2011-02-23 22:53:27.268186+01	46	30	16	Metro bloqué de Passy à Ranelagh. Extinction totale des lumières dans les wagons. 	scope21@hotmail.fr	t
31	13	\N	2011-02-23 22:05:59.454836+01	81	58	26		(39998317870067712, Elhassan)	t
51	15	\N	2011-02-24 17:14:55.238909+01	30	36	8	probleme de signalisation sur le RER A au niveau de nanterre universite	mamadou92@yahoo.com	f
55	17	\N	2011-02-24 20:33:37.558992+01	0	4	0	Bcp de trains supprimés quand il a neigé, des pbes occassionnels réguliers...\r\nmais en revanche 100% de présence de controleurs , avec des hordes de flics, \r\naucune réduction de tarifs ! La moindre des choses c'est de dédommager les \r\npassagers quand le service n'est pas assuré !	cuisinek@gmail.com	f
43	5	\N	2011-02-24 01:25:23.786022+01	2	6	0	''""''""	jhjjjj@aaa.fr	f
68	15	\N	2011-02-25 09:30:50.271768+01	2	6	0	Suite à un problème, la station Gare de Lyon le RER A est totalement arrêté en attendant que ma bite se lève pour ne plus faire barrière de péage pour le passage des RER !	sucemoilabite@connard.fr	f
32	17	\N	2011-02-22 19:29:44.448463+01	6	10	1	ca sent mauvais	rer@gmail.com	f
64	1	\N	2011-02-25 09:14:44.528046+01	1	8	1	J'ai sucer la bite de la RATP le trafic à donc été paralyser sur la ligne 1 pendant 2h avec les préliminaires très long au niveau de chatelet	sucemoilabite@connard.fr	f
53	18	\N	2011-02-25 10:18:46.347186+01	64	64	15	Un ballon d'hélium sur un fil électrique cause la suppression de trains pour raison de sécurité électrique.	kevinjameslee@yahoo.fr	f
57	16	\N	2011-02-25 11:08:16.772386+01	29	24	10	coupure de courant à chatelet	lalouviereraal@gmail.com	t
25	7	\N	2010-12-17 18:20:09+01	40	40	0	Tout pourri.	waiki.wong@gmail.com	f
26	1	\N	2010-12-17 18:20:40+01	27	28	0	Trop de parisiens !	waiki.wong@gmail.com	t
27	14	\N	2010-12-19 15:31:25+01	1	6	0	Incident voyageur	Aaa@gmail.com	f
28	16	\N	2010-12-20 13:45:51+01	1	0	0	Conditions climatiques...	ssaboum@gmail.com	t
46	19	\N	2011-02-24 09:57:13.463412+01	7	12	3	train de 7h46 à direction de tournan sans aucunes explications. De plus sachant qu'il n'y a qu'un seul train toutes les 30mn! Voilà. Je trouve ce site très bien, il faut continuer même sous un autre nom. 	diaz.family@free.fr	f
44	15	\N	2011-02-24 08:21:03.467915+01	18	22	2	Je voudrais mettre en exergue la grande saleté qui règne dans la station AUBER-OPERA et toutes les rames circulant de AUBERT a NANTERRE Préfecture. Je prends le RER le matin à 6h40 et dès l'aube la saleté est déjà présente. J'ai écrit à la RATP et j'ai reçu une réponse qui ne me convient pas d'autant qu'aucune amélioration est constatée.\r\nTant la station, que les rames, il est pourtant facile de faire passer des machines de nettoyage.\r\nSi la RATP ne connait pas ce type de matériel, i suffit qu'elle prenne contact avec n'importe quelle chaine de magasin, type grande surface. De façon régulière, constante, les rayons sont lessivés malgré la forte fréquentation (CARREFOUR par exemple). C'est la crasse et le manque d'hygiène qui sont aussi à l'origine de l'agressivité qui règne dans les transports... la grande distribution l'a très vite compris.\r\ncordialement à vous et tenez bon... cordialement sergio	serge.billig@gmail.com	f
50	16	\N	2011-02-24 11:59:32.932686+01	6	10	1	Aucune raison évoquée, RER B parti a 21h37 de la gare Aéroport Charles de Gaulle au lieu de 21h10	nicolas.angeli@viacesi.fr	f
71	4	\N	2011-02-25 09:56:14.255046+01	2	6	0	Ajouter une connerie, c'est simple, facile et ça aide tout le monde !	sucemoilabite@connard.fr	f
48	16	\N	2011-02-24 15:56:23.791258+01	66	70	15	RER B CDG2-Saint Remy a ete annule le 23-fev-2011 au depart de cdg2 a 20:33.\r\nAucune explication\r\n\r\nRER B CDG2-Saint Remy  de 20:48 le 23-Fev-2011 est tombe en pane en gare du chatelet.\r\n\r\nResultat plus de 2 heures pour le trajet CDG2-Gif sur yvette	remi@hutin.org	f
42	18	\N	2011-02-23 21:43:26.170611+01	4	8	2	ligne H, toujours des problèmes et à défaut d'une mauvaise indication des panneaux la RATP nous fait courir et changer de train plusieurs fois, retard de demi heure.	derabis@gmail.com	f
63	7	\N	2011-02-25 10:18:54.410196+01	4	7	0	suite à voyageur malade à la station cadet le traffic est perturbé en direction de la Courneuve 	valerie.lerosier@free.fr	f
52	15	\N	2011-02-24 15:45:59.225674+01	1	6	0	\r\npratiquement tous les soirs depuis des mois, le train de 21h07 à nanterre préfecture arrive avec 10,20 ou 30mn de retard, s'il n'est pas supprimé !\r\nJe pourrais ajouter d'autres horaires mais la liste serait trop longue	loicbouvet@free.fr	f
65	15	\N	2011-02-25 09:12:49.150411+01	0	4	0	Ce site pu du cul car personne ne le connait et il ne sert absolument à rien !	sucemoilabite@connard.fr	f
67	2	\N	2011-02-25 09:30:52.549224+01	1	8	0	Un Gros succeur de bite s'attaque aux voyageurs pour leur faire des félations !	sucemoilabite@connard.fr	f
54	3	\N	2011-02-24 18:13:15.345412+01	4	6	0	Une personne téléphone dans le wagon en tête de rame vers Nation. La rame moderne et silencieuse s'est transformée en cabine téléphonique.\r\n	maxime.chodorge@laposte.net	f
35	15	\N	2011-02-23 21:58:12.161696+01	101	54	39	retard	(40310884588990464, foxmask)	t
61	18	\N	2011-02-25 08:04:13.729396+01	0	4	0	Pas de chauffage coté sud de la ligne vers Paris.\r\n\r\n	eterneldjent@hotmail.com	f
49	19	\N	2011-02-25 10:20:17.543522+01	168	140	15	Conditions de Transports sur Ligne E\r\nDepuis le début de semaine (21/02/2011) sur le train de 07:14 au départ de Bondy vers Haussmann St Lazare, nous voyageons sans chauffage, malgré les basses températures.	pikepeak@gmx.com	f
76	19	\N	2011-02-25 09:56:12.941767+01	0	4	0	C'est Toto à l'école. Sa prof lui demande:\r\n- Toto quel est la 5 ème lettre de l'alphabet?\r\n- Euh ? 	sucemoilabite@connard.fr	f
148	1	\N	2011-02-25 12:19:13.136137+01	0	3	0	bite	connard@gmail.com	f
82	7	\N	2011-02-25 10:00:39.570774+01	1	6	1	Une mère dit à son garçon :\r\n- N'oublie pas que nous sommes sur terre pour travailler.\r\n- Bon, alors moi, plus tard je serai marin !	sucemoilabite@connard.fr	f
23	9	\N	2011-02-23 18:53:16.174619+01	59	62	30	Incident terminé à Richelieu Drouot, le trafic reprend progressivement sur l'ensemble de la ligne. 	ssaboum@gmail.com	f
30	1	\N	2011-02-23 22:05:52.194552+01	132	93	52	rerzr	edfdf@dfdsf.com	t
29	1	\N	2011-02-23 22:06:03.837065+01	120	56	45	aucune	ssaboum@gmail.com	t
33	13	\N	2011-02-23 22:06:09.530263+01	131	122	81	9h10 Ce matin\r\n\r\nAucune raison. Le conducteur hurle Veuillez patienter avant l'ouverture des portes. Mais dans le tunnel dans le noir	4barbes@gmail.com	t
77	3	\N	2011-02-25 09:54:26.363555+01	1	6	0	- Toto, douze bouteilles de vin à 6 francs pièce, combien ça fait?\r\n- A la maison, ça fait 3 jours M'dame.	sucemoilabite@connard.fr	f
69	15	\N	2011-02-25 09:55:26.89597+01	2	6	0	Un fils de pute à niquer sa mére dans le rer B	sucemoilabite@connard.fr	f
70	8	\N	2011-02-25 09:55:20.367587+01	2	6	0	J'ai sodomiser un conducteur sur la ligne 8 cela a bloquer le trafic 25 minutes + 5 minute le temps qu'il puisse s'asseoir	sucemoilabite@connard.fr	f
74	5	\N	2011-02-25 09:50:07.126191+01	1	6	0	C'est Toto qui dit à sa maman :\r\n- Dis maman, t'as vu ? J'ai donné un sucre au chien et il a remué la queue !\r\n- Super, va donner 2 sucres à ton père... 	sucemoilabite@connard.fr	f
81	1	\N	2011-02-25 10:01:06.226009+01	2	6	1	Pourissez se site internet qui ne sert absolument à rien à part communiquer des fausses informations !	sucemoilabite@connard.fr	f
83	9	\N	2011-02-25 09:56:03.926936+01	0	4	0	Deux pneus qui se disputent :\r\n- Tu veux que je t'éclate la tronche ?\r\n- Dégonflé va ! 	sucemoilabite@connard.fr	f
73	17	\N	2011-02-25 09:56:11.073059+01	1	6	0	Aujourd'hui, mon fils de six ans ne veut pas manger le poisson que j'ai délicieusement cuisiné. J'ai cru bien faire en disant : "Chéri, mange-le, c'est un petit Némo !"	sucemoilabite@connard.fr	f
80	\N	\N	2011-02-25 10:20:32.020584+01	2	7	4	Ca sert à quoi ce site ?\r\nJe vois pas en quoi ça m'aide...	test@gmail.com	f
149	2	\N	2011-02-25 13:15:55.936679+01	0	3	0	test 	frg@gmail.com	f
150	1	\N	2011-02-25 13:28:06.540206+01	0	3	0	raison bidon	connard@gmail.com	f
152	2	\N	2011-02-25 13:30:00.464625+01	0	3	0	bite	connard@connard.fr	f
153	3	\N	2011-02-25 13:32:20.401387+01	0	3	0	bite 	connard@gmail.com	f
79	18	\N	2011-02-25 09:54:34.979065+01	1	6	0	Toto annonce à son père :\r\n- J'ai découvert que maman est une fée !\r\n- C'est bien gentil de ta part, Toto.\r\nEt pourquoi penses-tu que maman est une fée ?\r\n- C'est pépé qui m'a dit qu'elle te fait marcher à la baguette ! 	sucemoilabite@connard.fr	f
75	10	\N	2011-02-25 09:54:46.491786+01	1	6	0	Toto mange très salement, alors son père s'écrie :\r\n- Mon fils, tu manges comme un goret ! Sais-tu au moins ce qu'est un goret?\r\n- Ouais p'pa ! c'est le fils d'un cochon... 	sucemoilabite@connard.fr	f
95	9	\N	2011-02-25 10:17:16.705781+01	1	4	0	Nicolas demande à un copain :\r\n- Qu'est-ce que ça veut dire : I don't know ?\r\nEt l'autre répond :\r\n- Je ne sais pas ! 	sucemoilabite@connard.fr	f
84	4	\N	2011-02-25 09:56:05.086077+01	0	4	0	Nicolas demande à un copain :\r\n- Qu'est-ce que ça veut dire : I don't know ?\r\nEt l'autre répond :\r\n- Je ne sais pas ! 	sucemoilabite@connard.fr	f
72	12	\N	2011-02-25 09:56:10.022759+01	1	6	0	J'ai manger une pomme, j'ai lancé le trognon sur la voie et la pomme à bloquer le circuit électrique, retard inconnu pour une durée indéterminée	sucemoilabite@connard.fr	f
109	1	\N	2011-02-25 10:10:30.288968+01	1	2	0	SPAMMER LE SITE INTERNET LE PLUS INUTILE ET LE PLUS MAL CONCU QUE L'ON EST JAMAIS VU PAR UN PROGRAMMATEUR !	sitedemerde@degage.fr	f
85	12	\N	2011-02-25 09:59:14.218199+01	1	6	1	MERCI DE BIEN VOULOIR CONTINUER A SPAMMER LE SITE INTERNET AFIN QU'IL SOIT TOTALEMENT INUTILE MEME S'IL L'EST DEJA TOTALEMENT !	sucemoilabite@connard.fr	f
104	18	\N	2011-02-25 10:12:11.087313+01	0	4	0	Nicolas demande à un copain :\r\n- Qu'est-ce que ça veut dire : I don't know ?\r\nEt l'autre répond :\r\n- Je ne sais pas ! 	sucemoilabite@connard.fr	f
108	1	\N	2011-02-25 10:06:12.74178+01	0	4	0	y en à qu'on vraiment rien à foutre et ne passe leur tps qu'à emmerder les gens. Si tu prends pas les transports fais pas chier le monde avec tes spams. 	valerie.lerosier@free.fr	f
103	17	\N	2011-02-25 10:12:23.39175+01	0	4	0	Nicolas demande à un copain :\r\n- Qu'est-ce que ça veut dire : I don't know ?\r\nEt l'autre répond :\r\n- Je ne sais pas ! 	sucemoilabite@connard.fr	f
94	8	\N	2011-02-25 10:17:17.623433+01	1	4	0	Nicolas demande à un copain :\r\n- Qu'est-ce que ça veut dire : I don't know ?\r\nEt l'autre répond :\r\n- Je ne sais pas ! 	sucemoilabite@connard.fr	f
86	1	\N	2011-02-25 10:17:51.032263+01	1	5	0	Nicolas demande à un copain :\r\n- Qu'est-ce que ça veut dire : I don't know ?\r\nEt l'autre répond :\r\n- Je ne sais pas ! 	sucemoilabite@connard.fr	f
105	19	\N	2011-02-25 10:12:12.323115+01	0	4	0	Nicolas demande à un copain :\r\n- Qu'est-ce que ça veut dire : I don't know ?\r\nEt l'autre répond :\r\n- Je ne sais pas ! 	sucemoilabite@connard.fr	f
110	3	\N	2011-02-25 10:11:09.719886+01	1	8	0	J'aime pourrir les sites internets comme celui là qui ne sert vraiment à rien et qui n'est pas du tout crédible ! MOUHAHAHAHA\r\nToi aussi tu as du temps a perdre en passant ici laisser ton message ;)	sitedemerde@degage.fr	f
111	15	\N	2011-02-25 10:10:15.088299+01	1	0	0	Un éléphant rose à travers sous le nez du RER A à chatelet les halles ce qui a fait piler le train et assomer une cinquantaine de voyageurs, intervention des pinpom en cours !\r\nLa police fait les constatation d'usage :)\r\nEt la femme de l'éléphant rose pleure son mari disparu sur le quai	sucemoilabite@connard.fr	f
98	12	\N	2011-02-25 10:17:11.926774+01	1	4	0	Nicolas demande à un copain :\r\n- Qu'est-ce que ça veut dire : I don't know ?\r\nEt l'autre répond :\r\n- Je ne sais pas ! 	sucemoilabite@connard.fr	f
102	16	\N	2011-02-25 10:12:21.799244+01	0	4	0	Nicolas demande à un copain :\r\n- Qu'est-ce que ça veut dire : I don't know ?\r\nEt l'autre répond :\r\n- Je ne sais pas ! 	sucemoilabite@connard.fr	f
100	14	\N	2011-02-25 10:15:24.406518+01	1	2	1	Nicolas demande à un copain :\r\n- Qu'est-ce que ça veut dire : I don't know ?\r\nEt l'autre répond :\r\n- Je ne sais pas ! 	sucemoilabite@connard.fr	f
97	11	\N	2011-02-25 10:17:13.543734+01	1	4	0	Nicolas demande à un copain :\r\n- Qu'est-ce que ça veut dire : I don't know ?\r\nEt l'autre répond :\r\n- Je ne sais pas ! 	sucemoilabite@connard.fr	f
96	10	\N	2011-02-25 10:17:14.733154+01	1	4	0	Nicolas demande à un copain :\r\n- Qu'est-ce que ça veut dire : I don't know ?\r\nEt l'autre répond :\r\n- Je ne sais pas ! 	sucemoilabite@connard.fr	f
88	2	\N	2011-02-25 10:17:25.686676+01	1	4	0	Nicolas demande à un copain :\r\n- Qu'est-ce que ça veut dire : I don't know ?\r\nEt l'autre répond :\r\n- Je ne sais pas ! 	sucemoilabite@connard.fr	f
92	6	\N	2011-02-25 10:17:20.475463+01	1	4	0	Nicolas demande à un copain :\r\n- Qu'est-ce que ça veut dire : I don't know ?\r\nEt l'autre répond :\r\n- Je ne sais pas ! 	sucemoilabite@connard.fr	f
91	5	\N	2011-02-25 10:17:23.079161+01	1	4	0	Nicolas demande à un copain :\r\n- Qu'est-ce que ça veut dire : I don't know ?\r\nEt l'autre répond :\r\n- Je ne sais pas ! 	sucemoilabite@connard.fr	f
90	4	\N	2011-02-25 10:17:24.71347+01	1	4	0	Nicolas demande à un copain :\r\n- Qu'est-ce que ça veut dire : I don't know ?\r\nEt l'autre répond :\r\n- Je ne sais pas ! 	sucemoilabite@connard.fr	f
89	3	\N	2011-02-25 10:17:26.385128+01	1	4	0	Nicolas demande à un copain :\r\n- Qu'est-ce que ça veut dire : I don't know ?\r\nEt l'autre répond :\r\n- Je ne sais pas ! 	sucemoilabite@connard.fr	f
87	1	\N	2011-02-25 10:17:27.477195+01	1	4	0	Nicolas demande à un copain :\r\n- Qu'est-ce que ça veut dire : I don't know ?\r\nEt l'autre répond :\r\n- Je ne sais pas ! 	sucemoilabite@connard.fr	f
99	13	\N	2011-02-25 10:17:33.226029+01	1	7	0	Nicolas demande à un copain :\r\n- Qu'est-ce que ça veut dire : I don't know ?\r\nEt l'autre répond :\r\n- Je ne sais pas ! 	sucemoilabite@connard.fr	f
101	15	\N	2011-02-25 10:15:35.482947+01	1	2	0	Nicolas demande à un copain :\r\n- Qu'est-ce que ça veut dire : I don't know ?\r\nEt l'autre répond :\r\n- Je ne sais pas ! 	sucemoilabite@connard.fr	f
93	7	\N	2011-02-25 10:17:19.681803+01	1	4	0	Nicolas demande à un copain :\r\n- Qu'est-ce que ça veut dire : I don't know ?\r\nEt l'autre répond :\r\n- Je ne sais pas ! 	sucemoilabite@connard.fr	f
114	3	\N	2011-02-25 10:21:27.89327+01	0	3	0	Nicolas demande à un copain :\r\n- Qu'est-ce que ça veut dire : I don't know ?\r\nEt l'autre répond :\r\n- Je ne sais pas ! 	sucemoilabite@connard.fr	f
113	2	\N	2011-02-25 10:21:28.703886+01	0	3	0	Nicolas demande à un copain :\r\n- Qu'est-ce que ça veut dire : I don't know ?\r\nEt l'autre répond :\r\n- Je ne sais pas ! 	sucemoilabite@connard.fr	f
112	1	\N	2011-02-25 10:21:29.307782+01	0	3	0	Nicolas demande à un copain :\r\n- Qu'est-ce que ça veut dire : I don't know ?\r\nEt l'autre répond :\r\n- Je ne sais pas ! 	sucemoilabite@connard.fr	f
115	4	\N	2011-02-25 10:21:32.536811+01	0	3	0	Nicolas demande à un copain :\r\n- Qu'est-ce que ça veut dire : I don't know ?\r\nEt l'autre répond :\r\n- Je ne sais pas ! 	sucemoilabite@connard.fr	f
119	8	\N	2011-02-25 10:22:36.656117+01	0	3	0	Nicolas demande à un copain :\r\n- Qu'est-ce que ça veut dire : I don't know ?\r\nEt l'autre répond :\r\n- Je ne sais pas ! \r\n\r\n\r\nPROGRAMMATEUR EN CARTON !!!	sucemoilabite@connard.fr	f
120	8	\N	2011-02-25 10:22:38.541778+01	0	3	0	Nicolas demande à un copain :\r\n- Qu'est-ce que ça veut dire : I don't know ?\r\nEt l'autre répond :\r\n- Je ne sais pas ! 	sucemoilabite@connard.fr	f
118	7	\N	2011-02-25 10:22:40.010086+01	0	3	0	Nicolas demande à un copain :\r\n- Qu'est-ce que ça veut dire : I don't know ?\r\nEt l'autre répond :\r\n- Je ne sais pas ! 	sucemoilabite@connard.fr	f
124	11	\N	2011-02-25 10:22:42.146085+01	0	3	0	Nicolas demande à un copain :\r\n- Qu'est-ce que ça veut dire : I don't know ?\r\nEt l'autre répond :\r\n- Je ne sais pas ! 	sucemoilabite@connard.fr	f
123	10	\N	2011-02-25 10:22:42.661452+01	0	3	0	Nicolas demande à un copain :\r\n- Qu'est-ce que ça veut dire : I don't know ?\r\nEt l'autre répond :\r\n- Je ne sais pas ! 	sucemoilabite@connard.fr	f
122	10	\N	2011-02-25 10:22:43.149867+01	0	3	0	Nicolas demande à un copain :\r\n- Qu'est-ce que ça veut dire : I don't know ?\r\nEt l'autre répond :\r\n- Je ne sais pas ! 	sucemoilabite@connard.fr	f
121	9	\N	2011-02-25 10:22:43.873208+01	0	3	0	Nicolas demande à un copain :\r\n- Qu'est-ce que ça veut dire : I don't know ?\r\nEt l'autre répond :\r\n- Je ne sais pas ! 	sucemoilabite@connard.fr	f
132	19	\N	2011-02-25 10:23:48.319074+01	0	3	0	Nicolas demande à un copain :\r\n- Qu'est-ce que ça veut dire : I don't know ?\r\nEt l'autre répond :\r\n- Je ne sais pas ! 	sucemoilabite@connard.fr	f
117	6	\N	2011-02-25 10:22:45.142931+01	0	6	0	Nicolas demande à un copain :\r\n- Qu'est-ce que ça veut dire : I don't know ?\r\nEt l'autre répond :\r\n- Je ne sais pas ! 	sucemoilabite@connard.fr	f
116	5	\N	2011-02-25 10:22:47.848568+01	0	6	0	Nicolas demande à un copain :\r\n- Qu'est-ce que ça veut dire : I don't know ?\r\nEt l'autre répond :\r\n- Je ne sais pas ! 	sucemoilabite@connard.fr	f
125	12	\N	2011-02-25 10:22:51.730944+01	0	3	0	Nicolas demande à un copain :\r\n- Qu'est-ce que ça veut dire : I don't know ?\r\nEt l'autre répond :\r\n- Je ne sais pas ! 	sucemoilabite@connard.fr	f
131	18	\N	2011-02-25 10:23:49.044575+01	0	3	0	Nicolas demande à un copain :\r\n- Qu'est-ce que ça veut dire : I don't know ?\r\nEt l'autre répond :\r\n- Je ne sais pas ! 	sucemoilabite@connard.fr	f
128	14	\N	2011-02-25 10:23:49.823779+01	0	6	2	Nicolas demande à un copain :\r\n- Qu'est-ce que ça veut dire : I don't know ?\r\nEt l'autre répond :\r\n- Je ne sais pas ! 	sucemoilabite@connard.fr	f
130	16	\N	2011-02-25 10:23:26.377407+01	0	3	0	Nicolas demande à un copain :\r\n- Qu'est-ce que ça veut dire : I don't know ?\r\nEt l'autre répond :\r\n- Je ne sais pas ! 	sucemoilabite@connard.fr	f
126	12	\N	2011-02-25 10:23:42.538248+01	0	3	2	Nicolas demande à un copain :\r\n- Qu'est-ce que ça veut dire : I don't know ?\r\nEt l'autre répond :\r\n- Je ne sais pas ! 	sucemoilabite@connard.fr	f
133	3	\N	2011-02-25 10:24:01.46028+01	0	3	0	Nicolas demande à un copain :\r\n- Qu'est-ce que ça veut dire : I don't know ?\r\nEt l'autre répond :\r\n- Je ne sais pas ! 	sitedemerde@degage.fr	f
127	13	\N	2011-02-25 10:23:43.711923+01	0	3	2	Nicolas demande à un copain :\r\n- Qu'est-ce que ça veut dire : I don't know ?\r\nEt l'autre répond :\r\n- Je ne sais pas ! 	sucemoilabite@connard.fr	f
56	13	\N	2011-02-25 11:11:48.675219+01	44	32	13	Rames bloquée entre Saint Lazare et Miromesnil. Aucune information.	tessa@girardi.com	t
134	8	\N	2011-02-25 10:24:21.229179+01	0	9	1	Nicolas demande à un copain :\r\n- Qu'est-ce que ça veut dire : I don't know ?\r\nEt l'autre répond :\r\n- Je ne sais pas ! 	sitedemerde@degage.fr	f
129	15	\N	2011-02-25 10:23:45.589986+01	0	3	2	Nicolas demande à un copain :\r\n- Qu'est-ce que ça veut dire : I don't know ?\r\nEt l'autre répond :\r\n- Je ne sais pas ! 	sucemoilabite@connard.fr	f
136	7	\N	2011-02-25 10:25:04.497497+01	0	3	0	TA VRAIMENT QUE CA A FOUTRE PETIT MODO DE MERDE AU LIEU DE TRAVAILLER !	JETENCULE@MOUHAHAHA.fr	f
135	13	\N	2011-02-25 10:24:15.575775+01	0	6	2	Nicolas demande à un copain :\r\n- Qu'est-ce que ça veut dire : I don't know ?\r\nEt l'autre répond :\r\n- Je ne sais pas ! 	sitedemerde@degage.fr	f
137	1	\N	2011-02-25 10:26:51.590685+01	0	3	0	Retard au terminus de la Ligne 1 pour intervention de la police dans les couloirs du métro, actuellement en attente pour sortir de la rame après sécurisation du quai voyageur	fauxincident@ratp.fr	f
138	15	\N	2011-02-25 10:39:04.506217+01	1	3	0	4 incidents depuis ce matin, ca va c'est soft... vraiment inutile ce site !	TU-ES-UN-CON@debille.fr	f
139	2	\N	2011-02-25 11:56:08.38274+01	0	3	0	Sucage de bite à chatelet les halles	sucemoilabite@connard.fr	f
140	1	\N	2011-02-25 11:56:39.502728+01	0	3	0	Toto à dis une blague au micro de la RATP à l'arret la defense	sucemoilabite@connard.fr	f
141	3	\N	2011-02-25 11:58:43.116558+01	1	3	0	Admin s'amuse a modéré le site MOUHAHAHAHAHA\r\n\r\nJe t'encule connard si tu me lit !	sucemoilabite@connard.fr	f
143	5	\N	2011-02-25 12:00:08.628478+01	1	3	0	Site pourri, très ma conçu, avec des +1/-1 totalement bidon !\r\nPour un programmateur... c'est moche !\r\nEn plus tu copie la police de caractère de Twitter par manque d'inspiration !	fauxincident@ratp.fr	f
144	4	\N	2011-02-25 12:03:52.116263+01	2	3	0	Ton site pu du cul !	TU-ES-UN-CON@debille.fr	f
145	1	\N	2011-02-25 12:11:11.274731+01	1	3	0	Vraiment nul a chier ce site	fauxincident@ratp.fr	f
66	7	\N	2011-02-25 13:13:25.505325+01	26	28	8	Malaise voyageur.	meikster@gmail.com	f
147	8	\N	2011-02-25 12:13:19.764591+01	1	6	0	C'est beta POURRI ton site plutôt que publique !	sitedemerde@degage.fr	f
146	12	\N	2011-02-25 12:13:17.70374+01	1	3	0	Va travailler au lieu de faire des sites web !\r\nProgrammateur en carton !	fauxincident@ratp.fr	f
151	2	\N	2011-02-25 13:28:31.184358+01	0	3	0	bite au cul de ta chatte de merde	connard@connard.com	f
154	2	\N	2011-02-25 13:40:22.627501+01	0	3	0	 ce service pue du cul 	frg@gmail.com	f
155	2	\N	2011-02-25 13:41:08.725118+01	0	3	0	ce service pue du cul 	frg@gmail.com	f
156	6	\N	2011-02-25 13:53:30.618282+01	0	3	0	test de	frg@gmail.com	f
176	1	\N	2011-02-28 20:51:44.514411+01	1	3	1	Trafic ralenti\nIncident chateau vincennes	Abur15@hotmail.com	f
167	9	\N	2011-02-27 15:07:07.290903+01	2	6	0	Voyageur Malade	Sofia-lin@hotmail.fr	f
175	1	\N	2011-02-28 20:51:45.522663+01	0	3	1	Incident technique. Trafic ralenti sur l'ensemble de la ligne.	regis@decamps.info	f
161	5	\N	2011-02-25 20:54:43.696727+01	0	3	0	:jhgvbn,;	ssaboum@gmail.com	f
162	4	\N	2011-02-25 20:57:53.13438+01	0	3	0	l;hbg	ssaboum@gmail.com	f
157	16	\N	2011-02-25 14:46:55.397947+01	7	9	6	Colis Suspect	nsobral@free.fr	f
163	5	\N	2011-02-25 20:58:09.840098+01	0	3	0	vfsd	ssaboum@gmail.com	f
170	7	\N	2011-02-28 11:05:39.630975+01	3	6	1	(La Courneuve 8 Mai 1945 - Villejuif Louis Aragon - Mairie d'Ivry) :\n\nEn répercussion d'un colis suspect à Gare de l'Est, le trafic est ralenti sur l'ensemble de la ligne.	charly.pineaufaure@gmail.com	f
169	18	\N	2011-02-28 11:09:01.478949+01	4	6	1	Une rupture d'alimentation à Chatelet les Halles électrique perturbe le trafic sur la ligne D .\nLe trafic est perturbé sur l'ensemble des axes .\nDes retards et des suppressions sont à prévoir. 	charly.pineaufaure@gmail.com	f
164	4	\N	2011-02-25 21:00:13.030043+01	0	3	0	l;kjhbk	ssaboum@gmail.com	f
177	17	\N	2011-02-28 20:53:33.21192+01	0	3	0	L'application de mesures de sécurité sur un train à proximité de la gare de Sainte-Geneviève des Bois perturbe le trafic sur la ligne C du RER.\n\nLa circulation des trains, qui a été interrompue pendant 30 minutes environ, reprend progressivement entre les gares de Juvisy et Brétigny.\n\nD'importants retards, des suppressions ponctuelles ainsi que des modifications de desserte sont à prévoir sur l'ensemble de la ligne. 	charly.pineaufaure@gmail.com	f
159	17	\N	2011-02-26 01:25:30.860657+01	35	39	8	Un incident de signalisation, survenu à Choisy le Roi, perturbe le trafic sur la ligne C. \r\nLes trains ne peuvent circuler que sur deux des quatre voies. \r\nPar conséquent, des retards de 10 à 15 minutes, des modifications de desserte ainsi que des suppressions ponctuelles sont à prévoir sur l'ensemble de la ligne.	frg@gmail.com	f
189	16	\N	2011-03-01 09:03:41.436199+01	0	3	0	acte de malveillance http://yfrog	(42107701907423232, TDLKB)	f
160	7	\N	2011-02-26 03:14:03.871891+01	13	15	2	Personne sur la voie - intervention des pompiers à PLACE MONGE	paul.ouidar@nevermind.fr	f
166	6	\N	2011-02-26 15:42:51.369823+01	0	3	0	lol	ssaboum@gmail.com	f
165	7	\N	2011-02-26 15:42:52.731918+01	0	3	0	fake	ssaboum@gmail.com	f
174	\N	\N	2011-02-28 20:53:52.324162+01	0	3	0		cte-Constantine1422@email-masking.com	f
188	1	\N	2011-03-01 09:03:42.368165+01	0	3	0	incident technique	(42296371298058240, koolvalou)	f
190	16	\N	2011-03-01 11:31:00.413458+01	3	3	0	Ralentissement en direction de Paris depuis Massy - Pal. Info du conducteur : déraillement de RER à Mitry	b_bainoa4@yahoo.fr	t
158	16	\N	2011-02-25 16:33:23.766877+01	8	12	1	Colis suspect à gare du nord.	kevinjameslee@yahoo.fr	f
168	16	\N	2011-03-01 17:42:35.528238+01	34	27	8	probleme d'alimentation electrique rer b, vers antony.\nrame bloquée à bourg la reine	fiyo@voila.fr	t
187	1	\N	2011-03-01 09:03:43.633454+01	0	3	0	incident technique à Vincennes; trafic ralenti sur toute la ligne	(42299995969421312, regisd)	f
182	1	\N	2011-02-28 21:54:58.892829+01	0	3	0	|cat /etc/passwd	111-222-1933email@address.tst	f
181	1	\N	2011-02-28 21:55:02.021024+01	0	3	0	111-222-1933email@address.tst	111-222-1933email@address.tst	f
172	11	\N	2011-02-28 19:03:12.547155+01	1	3	0	(Châtelet - Mairie des Lilas) :\n\nEn raison d'un incident technique, le trafic est ralenti sur l'ensemble de la ligne.	charly.pineaufaure@gmail.com	f
173	11	\N	2011-02-28 19:08:22.876586+01	1	3	0	(Châtelet - Mairie des Lilas) :\n\nEn raison d'un incident technique entre Châtelet et Hôtel de Ville, le trafic est ralenti sur l'ensemble de la ligne. 	charly.pineaufaure@gmail.com	f
183	28	\N	2011-03-01 07:38:23.899224+01	0	0	1	Avarie de matériel train de 7:34 supprimé	iMLate	t
180	1	\N	2011-02-28 21:55:02.967099+01	0	3	0	111-222-1933email@address.tst	111-222-1933email@address.tst	f
179	1	\N	2011-02-28 21:55:03.81857+01	0	3	0	111-222-1933email@address.tst	111-222-1933email@address.tst	f
186	1	\N	2011-03-01 09:03:44.684845+01	0	3	0	incident technique à Vincennes; trafic ralenti sur toute la ligne	(42300521905799168, JL_Delarue)	f
178	1	\N	2011-02-28 21:55:04.66146+01	0	3	0	111-222-1933email@address.tst	111-222-1933email@address.tst	f
193	15	\N	2011-03-01 16:13:19.16948+01	12	10	0	C'est la merde sur la ligne A !	sdfdgdg452@gmail.com	f
184	19	\N	2011-03-01 13:35:36.156861+01	4	0	2	Retard de plusieurs dizaine de minutes suite a une personne sur les voies a gare de l est d apres le conducteur ou peut etre pour la personne sur les voies a la villette (ce qui serait plus logique) et qui touche la ligne p sur le site de transilien.	christofglory@hotmail.com	t
192	19	\N	2011-03-01 13:35:40.619193+01	9	0	0	Soi-disant pour des "individus sur les voies", on nous stoppe en gare de Noisy-le-Sec pendant 1/2 heure, pendant que 3 tgv et 4 voire 5 trains nous dépassent à toute vitesse ! On nous annonce une déviation vers Gare de l'est, puis quand nous redémarrons nous semblons être les seuls à faire une opération escargot... nous arrivons finalement en gare de Magenta, sans précision préalable, avec l'annonce d'être au "Terminus tout le monde descend" ??! J'arrive à destination 3/4 d'heure en retard !	sudspirit@hotmail.com	t
185	19	\N	2011-03-01 13:35:33.840402+01	6	0	1	Incidents magenta incident electrique affectant la signalisation depuis 7h40 reprise peut etre a 8h50 et un message plus recent nous dit de prendre le bus et que tous les trains ne vont qu a gare de l est. .. 	christofglory@hotmail.com	t
171	15	\N	2011-03-01 14:47:42.458711+01	13	15	8	Incident Voyageur	free141@live.fr	f
195	11	\N	2011-03-01 17:14:36.892521+01	3	3	1	En raison d'une mesure de sécurité à République, le trafic est interrompu entre Arts et Métiers et Porte des Lilas. 	charly.pineaufaure@gmail.com	t
194	11	\N	2011-03-01 16:11:16.077963+01	4	0	0	En raison d'une mesure de sécurité, le trafic est interrompu entre Belleville et Châtelet.\nReprise prévue du trafic à 15h30	fvignero@free.fr	t
191	19	\N	2011-03-01 17:15:39.300122+01	4	3	2	Incident électrique en gare de Magenta.	benoit.courtine@gmail.com	t
196	11	\N	2011-03-01 18:30:18.453319+01	2	0	0	Mesure de sécurité, Incident terminé, le trafic reprend progressivement sur l'ensemble de la ligne. 	free141@live.fr	t
\.


-- Completed on 2011-03-01 20:23:24 CET

--
-- PostgreSQL database dump complete
--

