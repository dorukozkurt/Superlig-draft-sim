import tkinter as tk
from tkinter import messagebox
import random

# Süper Lig takımları listesi
teams = [
    "Galatasaray", "Fenerbahçe", "Beşiktaş", "Trabzonspor", "Başakşehir",
    "Antalyaspor", "Alanyaspor", "Konyaspor", "Kayserispor", "Sivasspor",
    "Rizespor", "Kasımpaşa", "Hatayspor", "Gaziantep FK", "Adana Demirspor",
    "Eyüpspor", "Göztepe", "Samsunspor", "Bodrum FK"
]

# Oyuncular listesi (ad, takım, pozisyon)
players = [    
    ("Fernando Muslera", "Galatasaray", "Kaleci"),
    ("Günay Güvenç", "Galatasaray", "Kaleci"),
    ("Atakan Nuri Ordu", "Galatasaray", "Kaleci"),
    ("Jankat Yılmaz", "Galatasaray", "Kaleci"),
    ("Davinson Sánchez", "Galatasaray", "Stoper"),
    ("Carlos Cuesta", "Galatasaray", "Stoper"),
    ("Abdülkerim Bardakcı", "Galatasaray", "Stoper"),
    ("Kaan Ayhan", "Galatasaray", "Stoper"),
    ("Arda Ünyay", "Galatasaray", "Stoper"),
    ("Ismail Jakobs", "Galatasaray", "Sol Bek"),
    ("Eren Elmalı", "Galatasaray", "Sol Bek"),
    ("Elias Jelert", "Galatasaray", "Sağ Bek"),
    ("Gabriel Sara", "Galatasaray", "Orta saha"),
    ("Lucas Torreira", "Galatasaray", "Orta Saha"),
    ("Kerem Demirbay", "Galatasaray", "Orta Saha"),
    ("Berkan Kutlu", "Galatasaray", "Orta Saha"),
    ("Mario Lemina", "Galatasaray", "Orta Saha"),
    ("Dries Mertens", "Galatasaray", "10 Numara"),
    ("Barış Alper Yılmaz", "Galatasaray", "Sağ Kanat"),
    ("Yunus Akgün", "Galatasaray", "Sağ Kanat"),
    ("Mauro İcardi", "Galatasaray", "Forvet"),
    ("Victor Osimhen", "Galatasaray", "Forvet"),
    ("Álvaro Morata", "Galatasaray", "Forvet") ,
    ("Dominik Livaković", "Fenerbahçe", "Kaleci"),
    ("İrfan Can Eğribayat", "Fenerbahçe", "Kaleci"),
    ("Ertuğrul Çetin", "Fenerbahçe", "Kaleci"),
    ("Alexander Djiku", "Fenerbahçe", "Stoper"),
    ("Rodrigo Becão", "Fenerbahçe", "Stoper"),
    ("Çağlar Söyüncü", "Fenerbahçe", "Stoper"),
    ("Mert Müldür", "Fenerbahçe", "Sağ Bek"),
    ("Jayden Oosterwolde", "Fenerbahçe", "Sol Bek"),
    ("Bright Osayi-Samuel", "Fenerbahçe", "Sağ Bek"),
    ("Levent Mercan", "Fenerbahçe", "Sol Bek"),
    ("Milan Skriniar", "Fenerbahçe", "Stoper"),
    ("Fred", "Fenerbahçe", "Orta Saha"),
    ("Sofyan Amrabat", "Fenerbahçe", "Orta Saha"),
    ("İsmail Yüksek", "Fenerbahçe", "Orta Saha"),
    ("Mert Hakan Yandaş", "Fenerbahçe", "Orta Saha"),
    ("Sebastian Szymański", "Fenerbahçe", "Orta Saha"),
    ("İrfan Can Kahveci", "Fenerbahçe", "Orta Saha"),
    ("Bartuğ Elmaz", "Fenerbahçe", "Orta Saha"),
    ("Jin-ho Jo", "Fenerbahçe", "Orta Saha"),
    ("Edin Džeko", "Fenerbahçe", "Forvet"),
    ("Youssef En-Nesyri", "Fenerbahçe", "Forvet"),
    ("Cenk Tosun", "Fenerbahçe", "Forvet"),
    ("Dušan Tadić", "Fenerbahçe", "Sol Kanat"),
    ("Cengiz Ünder", "Fenerbahçe", "Sağ Kanat"),
    ("Allan Saint-Maximin", "Fenerbahçe", "Sol Kanat"),
    ("Anderson Talisca", "Fenerbahçe", "10 Numara"),
    ("Oğuz Aydın", "Fenerbahçe", "Sağ Kanat"),
    ("Philip Kostic", "Fenerbahçe", "Orta Saha") ,
     ("Mert Günok", "Beşiktaş", "Kaleci"),
    ("Ersin Destanoğlu", "Beşiktaş", "Kaleci"),
    ("Göktuğ Baytekin", "Beşiktaş", "Kaleci"),
    ("Emir Yaşar", "Beşiktaş", "Kaleci"),
    ("Arthur Masuaku", "Beşiktaş", "Sol Bek"),
    ("Tayyip Talha Sanuç", "Beşiktaş", "Stoper"),
    ("Felix Uduokhai", "Beşiktaş", "Stoper"),
    ("Gabriel Paulista", "Beşiktaş", "Stoper"),
    ("Jonas Svensson", "Beşiktaş", "Sağ Bek"),
    ("Onur Bulut", "Beşiktaş", "Sağ Bek"),
    ("Emirhan Topçu", "Beşiktaş", "Defansif Orta Saha"),
    ("Arda Berk Özüarap", "Beşiktaş", "Defansif Orta Saha"),
    ("Baktiyor Zainutdinov", "Beşiktaş", "Sol Bek"),
    ("Al Musrati", "Beşiktaş", "Orta Saha"),
    ("Gedson Fernandes", "Beşiktaş", "Orta Saha"),
    ("Salih Uçan", "Beşiktaş", "Orta Saha"),
    ("Amir Hadžiahmetović", "Beşiktaş", "Orta Saha"),
    ("Fahri Kerem Ay", "Beşiktaş", "Orta Saha"),
    ("Milot Rashica", "Beşiktaş", "Sağ Kanat"),
    ("Rafa Silva", "Beşiktaş", "Sol Kanat"),
    ("Ciro Immobile", "Beşiktaş", "Forvet"),
    ("João Mário", "Beşiktaş", "Orta Saha"),
    ("Ernest Muçi", "Beşiktaş", "Forvet"),
    ("Jean Onana", "Beşiktaş", "Orta Saha"),
    ("Cher Ndour", "Beşiktaş", "Orta Saha"),
    ("Can Keleş", "Beşiktaş", "Sağ Kanat"),
    ("Emrecan Terzi", "Beşiktaş", "Orta Saha"),
    ("Mustafa Erhan Hekimoğlu", "Beşiktaş", "Forvet"),
    ("Uğurcan Çakır", "Trabzonspor", "Kaleci"),
    ("Onuralp Çevikkan", "Trabzonspor", "Kaleci"),
    ("Muhammet Taha Tepe", "Trabzonspor", "Kaleci"),
    ("Ahmet Doğan Yıldırım", "Trabzonspor", "Kaleci"),
    ("Hüseyin Türkmen", "Trabzonspor", "Stoper"),
    ("Stefano Denswil", "Trabzonspor", "Stoper"),
    ("Eren Elmalı", "Trabzonspor", "Sol Bek"),
    ("Borna Barišić", "Trabzonspor", "Sol Bek"),
    ("Pedro Malheiro", "Trabzonspor", "Sağ Bek"),
    ("Stefan Savić", "Trabzonspor", "Stoper"),
    ("Arseniy Batagov", "Trabzonspor", "Stoper"),
    ("Serkan Asan", "Trabzonspor", "Sağ Bek"),
    ("Serdar Saatçı", "Trabzonspor", "Stoper"),
    ("Arif Boşluk", "Trabzonspor", "Stoper"),
    ("Enis Bardhi", "Trabzonspor", "Orta Saha"),
    ("Cihan Çanak", "Trabzonspor", "Orta Saha"),
    ("Umut Güneş", "Trabzonspor", "Orta Saha"),
    ("John Lundstram", "Trabzonspor", "Orta Saha"),
    ("Batista Mendy", "Trabzonspor", "Orta Saha"),
    ("Ozan Tufan", "Trabzonspor", "Orta Saha"),
    ("Edin Višća", "Trabzonspor", "Orta Saha"),
    ("Okay Yokuşlu", "Trabzonspor", "Orta Saha"),
    ("Muhammed Cham", "Trabzonspor", "Orta Saha"),
    ("Salih Malkoçoğlu", "Trabzonspor", "Orta Saha"),
    ("Umut Bozok", "Trabzonspor", "Forvet"),
    ("Enis Destan", "Trabzonspor", "Forvet"),
    ("Denis Drăguș", "Trabzonspor", "Forvet"),
    ("Anthony Nwakaeme", "Trabzonspor", "Forvet"),
    ("Simon Banza", "Trabzonspor", "Forvet"),
    ("Okan Kocuk", "Samsunspor", "Kaleci"),
    ("Halil Yeral", "Samsunspor", "Kaleci"),
    ("Taha Tosun", "Samsunspor", "Kaleci"),
    ("Efe Berat Töruz", "Samsunspor", "Kaleci"),
    ("Timur Bülbül", "Samsunspor", "Kaleci"),
    ("Rick van Drongelen", "Samsunspor", "Stoper"),
    ("Marc Bola", "Samsunspor", "Sol Bek"),
    ("Zeki Yavru", "Samsunspor", "Sağ Bek"),
    ("Soner Gönül", "Samsunspor", "Sol Bek"),
    ("Yunus Emre Çift", "Samsunspor", "Stoper"),
    ("Bedirhan Çetin", "Samsunspor", "Stoper"),
    ("Lubomír Šatka", "Samsunspor", "Stoper"),
    ("Ali Tarkan", "Samsunspor", "Stoper"),
    ("Berat Eser", "Samsunspor", "Stoper"),
    ("Kerem Fidan", "Samsunspor", "Sol Bek"),
    ("Eulânio Ângelo Chipela Gomes (Nanu)", "Samsunspor", "Sağ Bek"),
    ("Carlo Holse", "Samsunspor", "Orta Saha"),
    ("Youssef Aït Bennasser", "Samsunspor", "Orta Saha"),
    ("Olivier Ntcham", "Samsunspor", "Orta Saha"),
    ("Flavien Tait", "Samsunspor", "Orta Saha"),
    ("Celil Yüksel", "Samsunspor", "Orta Saha"),
    ("Soner Aydoğdu", "Samsunspor", "Orta Saha"),
    ("Emre Kılınç", "Samsunspor", "Orta Saha"),
    ("Kingsley Schindler", "Samsunspor", "Orta Saha"),
    ("Muhammet Ali Özbağcı", "Samsunspor", "Orta Saha"),
    ("Alper Efe Pazar", "Samsunspor", "Orta Saha"),
    ("Marius Mouandilmadji", "Samsunspor", "Forvet"),
    ("Landry Dimata", "Samsunspor", "Forvet"),
    ("Arbnor Muja", "Samsunspor", "Forvet"),
    ("Emre Kılınç", "Samsunspor", "Forvet"),
    ("Mustafa Yıldırım", "Samsunspor", "Forvet"),
    ("Gökhan Ünal", "Samsunspor", "Forvet"),
    ("Berhan Deniz", "Samsunspor", "Forvet"),
    ("Ali Kılıç", "Samsunspor", "Forvet"),
    ("Ercan Kara", "Samsunspor", "Forvet"),
    ("Haluk Mustafa Tan", "Samsunspor", "Forvet"),
     ("Volkan Babacan", "Başakşehir", "Kaleci"),
    ("Muhammed Şengezer", "Başakşehir", "Kaleci"),
    ("Yusuf Yılmaz", "Başakşehir", "Kaleci"),
    ("Deniz Dilmen", "Başakşehir", "Kaleci"),
    ("Jerome Opoku", "Başakşehir", "Stoper"),
    ("Léo Duarte", "Başakşehir", "Stoper"),
    ("Ousseynou Ba", "Başakşehir", "Stoper"),
    ("Hamza Güreler", "Başakşehir", "Stoper"),
    ("Halit Emre Acun", "Başakşehir", "Stoper"),
    ("Christopher Opéri", "Başakşehir", "Sol Bek"),
    ("Lucas Lima", "Başakşehir", "Sol Bek"),
    ("Festy Ebosele", "Başakşehir", "Sağ Bek"),
    ("Ömer Ali Şahiner", "Başakşehir", "Sağ Bek"),
    ("Burak Sefa Kavraz", "Başakşehir", "Sağ Bek"),
    ("Berat Özdemir", "Başakşehir", "Orta Saha"),
    ("Onur Ergün", "Başakşehir", "Orta Saha"),
    ("Miguel Crespo", "Başakşehir", "Orta Saha"),
    ("Matchoi Djaló", "Başakşehir", "Orta Saha"),
    ("Olivier Kemen", "Başakşehir", "Orta Saha"),
    ("Umut Güneş", "Başakşehir", "Orta Saha"),
    ("Serdar Gürler", "Başakşehir", "Orta Saha"),
    ("Metin Emre Karaal", "Başakşehir", "Orta Saha"),
    ("Ömer Faruk Beyaz", "Başakşehir", "Orta Saha"),
    ("João Figueiredo", "Başakşehir", "Forvet"),
    ("Krzysztof Piątek", "Başakşehir", "Forvet"),
    ("Patryk Szysz", "Başakşehir", "Forvet"),
    ("Philippe Paulin Keny", "Başakşehir", "Forvet"),
    ("Yusuf Sarı", "Başakşehir", "Forvet"),
    ("Berke Özer", "Eyüpspor", "Kaleci"),
    ("Birkan Tetik", "Eyüpspor", "Kaleci"),
    ("Alp Köseer", "Eyüpspor", "Kaleci"),
    ("Umut Meraş", "Eyüpspor", "Sol Bek"),
    ("Tayfur Bingöl", "Eyüpspor", "Sağ Bek"),
    ("Rúben Vezo", "Eyüpspor", "Stoper"),
    ("Léo Dubois", "Eyüpspor", "Sağ Bek"),
    ("Hamza Akman", "Eyüpspor", "Stoper"),
    ("Berzan Akkaya", "Eyüpspor", "Sağ Bek"),
    ("Kadirhan Atagün", "Eyüpspor", "Ön Libero"),
    ("Emre Gedik", "Eyüpspor", "Sol Bek"),
    ("Hamit Aydın", "Eyüpspor", "Merkez Orta Saha"),
    ("Metehan Baltacı", "Eyüpspor", "Stoper"),
    ("Dorukhan Toköz", "Eyüpspor", "Orta Saha"),
    ("Jonjo Shelvey", "Eyüpspor", "Orta Saha"),
    ("Emre Mor", "Eyüpspor", "Sağ Kanat"),
    ("Fredy", "Eyüpspor", "Orta Saha"),
    ("Mustafa Erdilman", "Eyüpspor", "Orta Saha"),
    ("Tunahan Akpınar", "Eyüpspor", "Orta Saha"),
    ("Metin Emre Karaal", "Eyüpspor", "Orta Saha"),
    ("Alper Efe Pazar", "Eyüpspor", "Orta Saha"),
    ("Muhammet Ali Özbağcı", "Eyüpspor", "Orta Saha"),
    ("Mame Thiam", "Eyüpspor", "Forvet"),
    ("Umut Bozok", "Eyüpspor", "Forvet"),
    ("Kamil Çörekçi", "Eyüpspor", "Forvet"),
    ("Berhan Deniz", "Eyüpspor", "Forvet"),
    ("Gökhan Ünal", "Eyüpspor", "Forvet"),
    ("Ali Kılıç", "Eyüpspor", "Forvet"),
    ("Ercan Kara", "Eyüpspor", "Forvet"),
    ("Haluk Mustafa Tan", "Eyüpspor", "Forvet"),
    ("Berhan Deniz", "Eyüpspor", "Forvet"),
    ("Ali Kılıç", "Eyüpspor", "Forvet"),
    ("Mateusz Lis", "Göztepe", "Kaleci"),
    ("Arda Özçimen", "Göztepe", "Kaleci"),
    ("Emircan Seçgin", "Göztepe", "Kaleci"),
    ("Arda Ercan", "Göztepe", "Kaleci"),
    ("Taha Altıkardeş", "Göztepe", "Stoper"),
    ("Furkan Bayır", "Göztepe", "Stoper"),
    ("Ogün Bayrak", "Göztepe", "Sağ Bek"),
    ("Malcom Bokele", "Göztepe", "Stoper"),
    ("Novatus Dismas Miroshi", "Göztepe", "Sol Bek"),
    ("Koray Günter", "Göztepe", "Stoper"),
    ("Héliton", "Göztepe", "Stoper"),
    ("Lasse Nielsen", "Göztepe", "Sağ Bek"),
    ("Nazım Sangaré", "Göztepe", "Sağ Bek"),
    ("İsmail Köybaşı", "Göztepe", "Sol Bek"),
    ("Ege Yıldırım", "Göztepe", "Stoper"),
    ("Victor Hugo", "Göztepe", "Orta Saha"),
    ("Kuryu Matsuki", "Göztepe", "Orta Saha"),
    ("Ahmed İldız", "Göztepe", "Orta Saha"),
    ("Anthony Dennis", "Göztepe", "Orta Saha"),
    ("David Tijaniç", "Göztepe", "Orta Saha"),
    ("Djalma Silva", "Göztepe", "Orta Saha"),
    ("Lasse Nielsen", "Göztepe", "Orta Saha"),
    ("İsmail Köybaşı", "Göztepe", "Orta Saha"),
    ("Rômulo José Cardoso da Cruz (Rômulo)", "Göztepe", "Forvet"),
    ("Juan Santos da Silva (Juan)", "Göztepe", "Forvet"),
    ("Kubilay Kanatsızkuş", "Göztepe", "Forvet"),
    ("Emersonn Correia da Silva", "Göztepe", "Forvet"),
    ("Tibet Durakçay", "Göztepe", "Forvet"),
    ("Doğan Erdoğan", "Göztepe", "Forvet"),
    ("Isaac Sandor Solet Bomawoko", "Göztepe", "Forvet"),
    ("David Datro Fofana", "Göztepe", "Forvet"),
    ("Yalçın Kayan", "Göztepe", "Forvet"),
    ("Novatosu Dismas Miroshi", "Göztepe", "Forvet"),
     ("Andreas Gianniotis", "Kasımpaşa", "Kaleci"),
    ("Sinan Bolat", "Kasımpaşa", "Kaleci"),
    ("Ali Emre Yanar", "Kasımpaşa", "Kaleci"),
    ("Ege Albayrak", "Kasımpaşa", "Kaleci"),
    ("Şant Kazancı", "Kasımpaşa", "Kaleci"),
    ("Kamil Piątkowski", "Kasımpaşa", "Stoper"),
    ("Kevin Rodrigues", "Kasımpaşa", "Sol Bek"),
    ("Nicholas Opoku", "Kasımpaşa", "Stoper"),
    ("Sadık Çiftpınar", "Kasımpaşa", "Stoper"),
    ("Taylan Utku Aydın", "Kasımpaşa", "Stoper"),
    ("Yasin Özcan", "Kasımpaşa", "Stoper"),
    ("Yunus Emre Atakaya", "Kasımpaşa", "Stoper"),
    ("Adnan Aktaş", "Kasımpaşa", "Stoper"),
    ("Berkay Muratoğlu", "Kasımpaşa", "Stoper"),
    ("Serhat Akçay", "Kasımpaşa", "Stoper"),
    ("Ömer Ecin", "Kasımpaşa", "Stoper"),
    ("Ege Ketahte", "Kasımpaşa", "Stoper"),
    ("Furkan Ulupınar", "Kasımpaşa", "Stoper"),
    ("Haris Hajradinović", "Kasımpaşa", "Orta Saha"),
    ("Cafu", "Kasımpaşa", "Orta Saha"),
    ("Aytaç Kara", "Kasımpaşa", "Orta Saha"),
    ("Antonín Barák", "Kasımpaşa", "Orta Saha"),
    ("Josip Brekalo", "Kasımpaşa", "Orta Saha"),
    ("Gökhan Gül", "Kasımpaşa", "Orta Saha"),
    ("Yaman Suakar", "Kasımpaşa", "Orta Saha"),
    ("Yusuf İnci", "Kasımpaşa", "Orta Saha"),
    ("Bahtiyar Aras Özden", "Kasımpaşa", "Orta Saha"),
    ("Atakan Müjde", "Kasımpaşa", "Orta Saha"),
    ("Emirhan Yiğit", "Kasımpaşa", "Orta Saha"),
    ("Nuno Da Costa", "Kasımpaşa", "Forvet"),
    ("Mamadou Fall", "Kasımpaşa", "Forvet"),
    ("Sinan Alkaş", "Kasımpaşa", "Forvet"),
    ("Erdem Çetinkaya", "Kasımpaşa", "Forvet"),
    ("Sarp Yavrucu", "Kasımpaşa", "Forvet"),
    ("Bünyamin Çetinkaya", "Kasımpaşa", "Forvet"),
    ("Daghan Erdoğan", "Kasımpaşa", "Forvet"),
    ("Beraat Yıldız", "Kasımpaşa", "Forvet"),
    ("Deniz Ertaş", "Konyaspor", "Kaleci"),
    ("Jakub Słowik", "Konyaspor", "Kaleci"),
    ("Ahmet Daş", "Konyaspor", "Kaleci"),
    ("Egemen Aydın", "Konyaspor", "Kaleci"),
    ("Riechedly Bazoer", "Konyaspor", "Defans"),
    ("Nikola Boranijašević", "Konyaspor", "Defans"),
    ("Josip Čalušić", "Konyaspor", "Defans"),
    ("Filip Damjanović", "Konyaspor", "Defans"),
    ("Adil Demirbağ", "Konyaspor", "Defans"),
    ("Guilherme", "Konyaspor", "Defans"),
    ("Yaşar Kavas", "Konyaspor", "Defans"),
    ("Mert Korkmaz", "Konyaspor", "Defans"),
    ("Utku Eriş", "Konyaspor", "Defans"),
    ("Marko Jevtović", "Konyaspor", "Orta Saha"),
    ("Morten Bjørlo", "Konyaspor", "Orta Saha"),
    ("Emmanuel Boateng", "Konyaspor", "Orta Saha"),
    ("Pedrinho", "Konyaspor", "Orta Saha"),
    ("Danijel Aleksić", "Konyaspor", "Orta Saha"),
    ("Melih İbrahimoğlu", "Konyaspor", "Orta Saha"),
    ("Yusuf Erdoğan", "Konyaspor", "Orta Saha"),
    ("Melih Bostan", "Konyaspor", "Orta Saha"),
    ("Tunahan Taşçı", "Konyaspor", "Orta Saha"),
    ("Hamidou Keyta", "Konyaspor", "Orta Saha"),
    ("Kaan Akyazı", "Konyaspor", "Orta Saha"),
    ("Emirhan Subaş", "Konyaspor", "Orta Saha"),
    ("Çağdaş Şendur", "Konyaspor", "Orta Saha"),
    ("Zeki Kaan Satıoğlu", "Konyaspor", "Orta Saha"),
    ("Mehmet Deveci", "Konyaspor", "Orta Saha"),
    ("Abdurrahman Üresin", "Konyaspor", "Orta Saha"),
    ("Mehmet Güneş", "Konyaspor", "Orta Saha"),
    ("Berke Çelik", "Konyaspor", "Orta Saha"),
    ("Ufuk Akyol", "Konyaspor", "Orta Saha"),
    ("Ata Berk Karababa", "Konyaspor", "Orta Saha"),
    ("Emrehan Gedikli", "Konyaspor", "Orta Saha"),
    ("Ahmet Karademir", "Konyaspor", "Orta Saha"),
    ("Semih Kocatürk", "Konyaspor", "Orta Saha"),
    ("Hüseyin Mert Uyanıker", "Konyaspor", "Orta Saha"),
    ("Oğulcan Ülgün", "Konyaspor", "Orta Saha"),
    ("Blaž Kramer", "Konyaspor", "Forvet"),
    ("Umut Nayir", "Konyaspor", "Forvet"),
    ("Alassane Ndao", "Konyaspor", "Forvet"),
    ("Tarık Çetin", "Çaykur Rizespor", "Kaleci",),
    ("Efe Doğan", "Çaykur Rizespor", "Kaleci",),
    ("Ivo Grbić", "Çaykur Rizespor", "Kaleci", "Hırvatistan"),
    ("Khusniddin Alikulov", "Çaykur Rizespor", "Defans", "Özbekistan"),
    ("Attila Mocsi", "Çaykur Rizespor", "Defans", "Macaristan"),
    ("Samet Akaydin", "Çaykur Rizespor", "Defans", "Türkiye"),
    ("Casper Højer Nielsen", "Çaykur Rizespor", "Defans", "Danimarka"),
    ("Eray Korkmaz", "Çaykur Rizespor", "Defans", "Türkiye"),
    ("Ayberk Karapo", "Çaykur Rizespor", "Defans", "Türkiye"),
    ("Anıl Yaşar", "Çaykur Rizespor", "Defans", "Türkiye"),
    ("Habil Özbakır", "Çaykur Rizespor", "Defans", "Türkiye"),
    ("Muhammet Taha Şahin", "Çaykur Rizespor", "Defans", "Türkiye"),
    ("Halil İbrahim Pehlivan", "Çaykur Rizespor", "Defans", "Türkiye"),
    ("Giannis Papanikolaou", "Çaykur Rizespor", "Orta Saha", "Yunanistan"),
    ("Amir Hadžiahmetović", "Çaykur Rizespor", "Orta Saha", "Bosna-Hersek"),
    ("Dal Varešanović", "Çaykur Rizespor", "Orta Saha", "Bosna-Hersek"),
    ("İbrahim Olawoyin", "Çaykur Rizespor", "Orta Saha", "Nijerya"),
    ("Berkay Özcan", "Çaykur Rizespor", "Orta Saha", "Türkiye"),
    ("Abdülkadir Ömür", "Çaykur Rizespor", "Orta Saha", "Türkiye"),
    ("Muhamed Buljubašić", "Çaykur Rizespor", "Orta Saha", "Bosna-Hersek"),
    ("Efe Geçim", "Çaykur Rizespor", "Orta Saha", "Türkiye"),
    ("Ali Sowe", "Çaykur Rizespor", "Forvet", "Gambiya"),
    ("Altın Zeqiri", "Çaykur Rizespor", "Forvet", "Kosova"),
    ("David Akintola", "Çaykur Rizespor", "Forvet", "Nijerya"),
    ("Rachid Ghezzal", "Çaykur Rizespor", "Forvet", "Cezayir"),
    ("Mithat Pala", "Çaykur Rizespor", "Forvet", "Türkiye"),
    ("Vaclav Jurečka", "Çaykur Rizespor", "Forvet", "Çek Cumhuriyeti"),
    ("Oumar Diouf", "Çaykur Rizespor", "Forvet", "Senegal"),
    ("Emrecan Bulut", "Çaykur Rizespor", "Forvet", "Türkiye"),
    ("Doganay Avcı", "Çaykur Rizespor", "Forvet", "Türkiye") , 
     ("Bilal Bayazıt", "Kayserispor", "Kaleci", "Türkiye"),
    ("Onurcan Piri", "Kayserispor", "Kaleci", "Türkiye"),
    ("Mehmet Şamil Öztürk", "Kayserispor", "Kaleci", "Türkiye"),
    ("Joseph Attamah", "Kayserispor", "Defans", "Gana"),
    ("Dimitrios Kolovetsios", "Kayserispor", "Defans", "Yunanistan"),
    ("Majid Hosseini", "Kayserispor", "Defans", "İran"),
    ("Julian Jeanvier", "Kayserispor", "Defans", "Gine"),
    ("Lionel Carole", "Kayserispor", "Defans", "Fransa"),
    ("Hasan Ali Kaldırım", "Kayserispor", "Defans", "Türkiye"),
    ("Arif Kocaman", "Kayserispor", "Defans", "Türkiye"),
    ("Batuhan Özgan", "Kayserispor", "Defans", "Türkiye"),
    ("Kayra Cihan", "Kayserispor", "Defans", "Türkiye"),
    ("Gökhan Sazdağı", "Kayserispor", "Defans", "Türkiye"),
    ("Bilal Ceylan", "Kayserispor", "Defans", "Türkiye"),
    ("Ali Karimi", "Kayserispor", "Orta Saha", "İran"),
    ("Mehdi Bourabia", "Kayserispor", "Orta Saha", "Fas"),
    ("Miguel Cardoso", "Kayserispor", "Orta Saha", "Portekiz"),
    ("Duckens Nazon", "Kayserispor", "Orta Saha", "Haiti"),
    ("Carlos Mané", "Kayserispor", "Orta Saha", "Gine-Bisau"),
    ("Yaw Ackah", "Kayserispor", "Orta Saha", "Gana"),
    ("Ali Baran Gezek", "Kayserispor", "Orta Saha", "Türkiye"),
    ("Berat İşkol", "Kayserispor", "Orta Saha", "Türkiye"),
    ("Ramazan Civelek", "Kayserispor", "Orta Saha", "Türkiye"),
    ("Mehmet Eray Özbek", "Kayserispor", "Orta Saha", "Türkiye"),
    ("Stéphane Bahoken", "Kayserispor", "Forvet", "Kamerun"),
    ("Talha Sarıarslan", "Kayserispor", "Forvet", "Türkiye"),
    ("Nurettin Korkmaz", "Kayserispor", "Forvet", "Türkiye") , 
    ("Sokratis Dioudis", "Gaziantep FK", "Kaleci", "Yunanistan"),
    ("Mustafa Burak Bozan", "Gaziantep FK", "Kaleci", "Türkiye"),
    ("Halil Bağcı", "Gaziantep FK", "Kaleci", "Türkiye"),
    ("Emre Taşdemir", "Gaziantep FK", "Defans", "Türkiye"),
    ("Anel Husić", "Gaziantep FK", "Defans", "İsviçre"),
    ("Semih Güler", "Gaziantep FK", "Defans", "Türkiye"),
    ("Bruno Viana", "Gaziantep FK", "Defans", "Brezilya"),
    ("Arda Kızıldağ", "Gaziantep FK", "Defans", "Türkiye"),
    ("Salem M’Bakata", "Gaziantep FK", "Defans", "Fransa/Kongo DC"),
    ("Godfrey Bitok Stephen", "Gaziantep FK", "Defans", "Nijerya"),
    ("Ömürcan Artan", "Gaziantep FK", "Defans", "Türkiye"),
    ("Alexandru Maxim", "Gaziantep FK", "Orta Saha", "Romanya"),
    ("Deian Sorescu", "Gaziantep FK", "Orta Saha", "Romanya"),
    ("Kacper Kozłowski", "Gaziantep FK", "Orta Saha", "Polonya"),
    ("Papa Alioune N’Diaye", "Gaziantep FK", "Orta Saha", "Senegal"),
    ("Quentin Daubin", "Gaziantep FK", "Orta Saha", "Fransa"),
    ("Furkan Soyalp", "Gaziantep FK", "Orta Saha", "Türkiye"),
    ("Ogün Özçiçek", "Gaziantep FK", "Orta Saha", "Türkiye"),
    ("İzzet Erdal", "Gaziantep FK", "Orta Saha", "Türkiye") , 
    ("Halil Dervişoğlu", "Gaziantep FK", "Forvet", "Türkiye"),
    ("David Okereke", "Gaziantep FK", "Forvet", "Nijerya"),
    ("Emmanuel Boateng", "Gaziantep FK", "Forvet", "Gana"),
    ("Kenan Kodro", "Gaziantep FK", "Forvet", "Bosna-Hersek"),
    ("Christophe Lungoyi", "Gaziantep FK", "Forvet", "Belçika") ,
    ("Kenan Pirić", "Antalyaspor", "Kaleci", "Bosna-Hersek"),
    ("Abdullah Yiğiter", "Antalyaspor", "Kaleci", "Türkiye"),
    ("Doğukan Özkan", "Antalyaspor", "Kaleci", "Türkiye"),
    ("Thalisson Kelven", "Antalyaspor", "Defans", "Brezilya"),
    ("Bahadır Öztürk", "Antalyaspor", "Defans", "Türkiye"),
    ("Amar Gerxhaliu", "Antalyaspor", "Defans", "Kosova"),
    ("Bünyamin Balcı", "Antalyaspor", "Defans", "Türkiye"),
    ("Güray Vural", "Antalyaspor", "Defans", "Türkiye"),
    ("Emrecan Uzunhan", "Antalyaspor", "Defans", "Türkiye"),
    ("Mert Yılmaz", "Antalyaspor", "Defans", "Türkiye"),
    ("Yigit Üstün", "Antalyaspor", "Defans", "Türkiye"),
    ("Abdurrahim Dursun", "Antalyaspor", "Defans", "Türkiye"),
    ("Veysel Sarı", "Antalyaspor", "Defans", "Türkiye"),
    ("Soner Dikmen", "Antalyaspor", "Orta Saha", "Türkiye"),
    ("Erdal Rakip", "Antalyaspor", "Orta Saha", "Kuzey Makedonya"),
    ("Ramzi Safuri", "Antalyaspor", "Orta Saha", "İsrail"),
    ("Sam Larsson", "Antalyaspor", "Orta Saha", "İsveç"),
    ("Moussa Djenepo", "Antalyaspor", "Orta Saha", "Mali"),
    ("Oleksandr Petrusenko", "Antalyaspor", "Orta Saha", "Ukrayna"),
    ("Erdoğan Yeşilyurt", "Antalyaspor", "Orta Saha", "Almanya"),
    ("Jakub Kałuziński", "Antalyaspor", "Orta Saha", "Polonya"),
    ("Emre Uzun", "Antalyaspor", "Orta Saha", "Türkiye"),
    ("Sander van de Streek", "Antalyaspor", "Orta Saha", "Hollanda"),
    ("Andros Townsend", "Antalyaspor", "Orta Saha", "İngiltere"),
    ("Hasan Ürkmez", "Antalyaspor", "Orta Saha", "Türkiye"),
    ("Berkay Topdemir", "Antalyaspor", "Orta Saha", "Türkiye"),
    ("Deni Milošević", "Antalyaspor", "Orta Saha", "Bosna-Hersek"),
    ("Mevlüt Han Ekelik", "Antalyaspor", "Orta Saha", "Türkiye"),
    ("Adolfo Gaich", "Antalyaspor", "Forvet", "Arjantin"),
    ("Moussa Djenepo", "Antalyaspor", "Forvet", "Mali"),
    ("Jakub Kałuziński", "Antalyaspor", "Forvet", "Polonya"),
    ("Sam Larsson", "Antalyaspor", "Forvet", "İsveç"),
    ("Sander van de Streek", "Antalyaspor", "Forvet", "Hollanda"),
    ("Andros Townsend", "Antalyaspor", "Forvet", "İngiltere"),
    ("Hasan Ürkmez", "Antalyaspor", "Forvet", "Türkiye"),
    ("Berkay Topdemir", "Antalyaspor", "Forvet", "Türkiye"),
    ("Deni Milošević", "Antalyaspor", "Forvet", "Bosna-Hersek"),
    ("Mevlüt Han Ekelik", "Antalyaspor", "Forvet", "Türkiye"),
    ("Ertuğrul Taşkıran", "Alanyaspor", "Kaleci", "Türkiye"),
    ("Mert Furkan Bayram", "Alanyaspor", "Kaleci", "Türkiye"),
    ("Yusuf Karagöz", "Alanyaspor", "Kaleci", "Türkiye"),
    ("Nuno Lima", "Alanyaspor", "Defans", "Portekiz"),
    ("Fidan Aliti", "Alanyaspor", "Defans", "Kosova"),
    ("Umut Mert Toy", "Alanyaspor", "Defans", "Türkiye"),
    ("Yusuf Özdemir", "Alanyaspor", "Defans", "Türkiye"),
    ("Jure Balkovec", "Alanyaspor", "Defans", "Slovenya"),
    ("Fatih Aksoy", "Alanyaspor", "Defans", "Türkiye"),
    ("Florent Hadergjonaj", "Alanyaspor", "Defans", "Kosova"),
    ("Gaïus Makouta", "Alanyaspor", "Orta Saha", "Kongo Cumhuriyeti"),
    ("Richard", "Alanyaspor", "Orta Saha", "Brezilya"),
    ("Nicolas Janvier", "Alanyaspor", "Orta Saha", "Fransa"),
    ("Buluthan Bulut", "Alanyaspor", "Orta Saha", "Türkiye"),
    ("Tonny Vilhena", "Alanyaspor", "Orta Saha", "Hollanda"),
    ("Yusuf Kurt", "Alanyaspor", "Orta Saha", "Türkiye"),
    ("Eren Altıntaş", "Alanyaspor", "Orta Saha", "Türkiye"),
    ("Muhammed Emin Sarıgül", "Alanyaspor", "Orta Saha", "Türkiye"),
    ("Bera Çeken", "Alanyaspor", "Orta Saha", "Türkiye"),
    ("Andraž Šporar", "Alanyaspor", "Forvet", "Slovenya"),
    ("Sergio Córdova", "Alanyaspor", "Forvet", "Venezuela"),
    ("Hwang Ui-jo", "Alanyaspor", "Forvet", "Güney Kore"),
    ("Arda Usluoğlu", "Alanyaspor", "Forvet", "Türkiye"),
    ("Veysel Karani Ünal", "Alanyaspor", "Forvet", "Türkiye"),
    ("Cem Çelik", "Alanyaspor", "Forvet", "Türkiye"),
    ("Diogo Sousa", "Bodrumspor", "Kaleci", "Portekiz"),
    ("Gökhan Akkan", "Bodrumspor", "Kaleci", "Türkiye"),
    ("Kerem Ersunar", "Bodrumspor", "Kaleci", "Türkiye"),
    ("Rüzgar Adıyaman", "Bodrumspor", "Kaleci", "Türkiye"),
    ("Arlind Ajeti", "Bodrumspor", "Defans", "Arnavutluk"),
    ("Christophe Hérelle", "Bodrumspor", "Defans", "Martinik"),
    ("Ali Aytemur", "Bodrumspor", "Defans", "Türkiye"),
    ("Ondřej Čelůstka", "Bodrumspor", "Defans", "Çek Cumhuriyeti"),
    ("Süleyman Özdamar", "Bodrumspor", "Defans", "Türkiye"),
    ("Oğulcan Başol", "Bodrumspor", "Defans", "Türkiye"),
    ("Cenk Şen", "Bodrumspor", "Defans", "Türkiye"),
    ("Ege Bilsel", "Bodrumspor", "Defans", "Türkiye"),
    ("Üzeyir Ergün", "Bodrumspor", "Defans", "Türkiye"),
    ("Musah Mohammed", "Bodrumspor", "Defans", "Gana"),
    ("Ahmet Aslan", "Bodrumspor", "Defans", "Türkiye"),
    ("Erkan Değişmez", "Bodrumspor", "Defans", "Türkiye"),
    ("Fredy", "Bodrumspor", "Orta Saha", "Angola"),
    ("Enes Öğrüce", "Bodrumspor", "Orta Saha", "Türkiye"),
    ("Mustafa Erdilman", "Bodrumspor", "Orta Saha", "Türkiye"),
    ("Tunahan Akpınar", "Bodrumspor", "Orta Saha", "Türkiye"),
    ("Bilal Güven", "Bodrumspor", "Orta Saha", "Türkiye"),
    ("Enis Bardhi", "Bodrumspor", "Orta Saha", "Kuzey Makedonya"),
    ("Jonathan Okita", "Bodrumspor", "Orta Saha", "Kongo DC / Almanya"),
    ("Kenan Özer", "Bodrumspor", "Orta Saha", "Türkiye"),
    ("Samet Yalçın", "Bodrumspor", "Orta Saha", "Türkiye"),
    ("Celal Dumanlı", "Bodrumspor", "Orta Saha", "Türkiye"),
    ("Altin Zeqiri", "Bodrumspor", "Orta Saha", "Arnavutluk"),
    ("David Akintola", "Bodrumspor", "Orta Saha", "Nijerya"),
    ("Rachid Ghezzal", "Bodrumspor", "Orta Saha", "Cezayir"),
    ("Ali Sowe", "Bodrumspor", "Orta Saha", "Gine-Bissau"),
    ("Zdravko Dimitrov", "Bodrumspor", "Orta Saha", "Bulgaristan"),
    ("Dal Varešanović", "Bodrumspor", "Orta Saha", "Bosna-Hersek"),
    ("İbrahim Pehlivan", "Bodrumspor", "Orta Saha", "Türkiye"),
    ("Pedro Brazão", "Bodrumspor", "Orta Saha", "Portekiz"),
    ("Altin Zeqiri", "Bodrumspor", "Forvet", "Arnavutluk"),
    ("David Akintola", "Bodrumspor", "Forvet", "Nijerya"),
    ("Rachid Ghezzal", "Bodrumspor", "Forvet", "Cezayir"),
    ("Ali Sowe", "Bodrumspor", "Forvet", "Gine-Bissau"),
    ("Zdravko Dimitrov", "Bodrumspor", "Forvet", "Bulgaristan"),
    ("Dal Varešanović", "Bodrumspor", "Forvet", "Bosna-Hersek"),
    ("İbrahim Pehlivan", "Bodrumspor", "Forvet", "Türkiye"),
    ("Pedro Brazão", "Bodrumspor", "Forvet", "Portekiz"),
    ("Ömer Faruk Beyaz", "Sivaspor", "Kaleci", "Türkiye"),
    ("Erencan Yardımcı", "Sivaspor", "Kaleci", "Türkiye"),
    ("Fatih Öztürk", "Sivaspor", "Kaleci", "Türkiye"),
    ("Furkan Bayır", "Sivaspor", "Defans", "Türkiye"),
    ("Kaan Kanak", "Sivaspor", "Defans", "Türkiye"),
    ("Adem Doğan", "Sivaspor", "Defans", "Türkiye"),
    ("Anderson Esiti", "Sivaspor", "Defans", "Nijerya"),
    ("Mert Çetin", "Sivaspor", "Defans", "Türkiye"),
    ("Aykut Akgün", "Sivaspor", "Defans", "Türkiye"),
    ("Mustafa Yumlu", "Sivaspor", "Defans", "Türkiye"),
    ("Ozan İpek", "Sivaspor", "Defans", "Türkiye"),
    ("Emirhan Aydoğan", "Sivaspor", "Orta Saha", "Türkiye"),
    ("Ali Şaşal Vural", "Sivaspor", "Orta Saha", "Türkiye"),
    ("Yunus Akgün", "Sivaspor", "Orta Saha", "Türkiye"),
    ("Bruno Mendes", "Sivaspor", "Orta Saha", "Brezilya"),
    ("İsmail Çokçalış", "Sivaspor", "Orta Saha", "Türkiye"),
    ("Joseph Attamah", "Sivaspor", "Orta Saha", "Gana"),
    ("Fatih Tekke", "Sivaspor", "Orta Saha", "Türkiye"),
    ("João Pedro", "Sivaspor", "Orta Saha", "Brezilya"),
    ("Bernard Mensah", "Sivaspor", "Forvet", "Gana"),
    ("Ali Çamdalı", "Sivaspor", "Forvet", "Türkiye"),
    ("Maxi Gomez", "Sivaspor", "Forvet", "Uruguay"),
    ("Abdülkerim Bardakcı", "Sivaspor", "Forvet", "Türkiye"),
    ("Mamadou Niang", "Sivaspor", "Forvet", "Senegal"),
    ("Batuhan Ahmet Şen", "Hatayspor", "Kaleci"),
    ("Korcan Çelikay", "Hatayspor", "Kaleci"),
    ("Yusuf Kelleci", "Hatayspor", "Kaleci"),
    ("Evans Kangwa", "Hatayspor", "Defans"),
    ("Leandrinho", "Hatayspor", "Defans"),
    ("Ravil Tagir", "Hatayspor", "Defans"),
    ("Ahmet Karadağ", "Hatayspor", "Defans"),
    ("Berat Ayberk Özdemir", "Hatayspor", "Defans"),
    ("Boffin Ben", "Hatayspor", "Defans"),
    ("Halil Akbunar", "Hatayspor", "Defans"),
    ("Bekir İrtegün", "Hatayspor", "Defans"),
    ("Ferhat Kaplan", "Hatayspor", "Orta Saha"),
    ("Oğuzhan Kayar", "Hatayspor", "Orta Saha"),
    ("Salih Dursun", "Hatayspor", "Orta Saha"),
    ("Fıratcan Üzüm", "Hatayspor", "Orta Saha"),
    ("Serkan Asan", "Hatayspor", "Orta Saha"),
    ("Edin Visca", "Hatayspor", "Orta Saha"),
    ("Abdülkadir Ömür", "Hatayspor", "Orta Saha"),
    ("Batuhan Kör", "Hatayspor", "Orta Saha"),
    ("Jhon Murillo", "Hatayspor", "Forvet"),
    ("Alassane Ndao", "Hatayspor", "Forvet"),
    ("Deniz Kadah", "Hatayspor", "Forvet"),
    ("Bruno Lopes", "Hatayspor", "Forvet"),
    ("Lassana Coulibaly", "Hatayspor", "Forvet"),
    
]

MAX_PLAYERS_PER_TEAM = 22
TOTAL_ROUNDS = MAX_PLAYERS_PER_TEAM

class DraftApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Süper Lig Draft Simülatörü")

        self.draft_result = {team: [] for team in teams}
        self.remaining_players = players.copy()

        self.round_number = 1
        self.turn_order = []
        
        self.info_label = tk.Label(root, text="", font=("Arial", 16, "bold"), justify=tk.LEFT, width=60, height=4, wraplength=500)
        self.info_label.pack(pady=10)

        self.result_text = tk.Text(root, width=70, height=25)
        self.result_text.pack(padx=10, pady=10)

        self.next_round_button = tk.Button(root, text="Sonraki Tur", command=self.next_round)
        self.next_round_button.pack(pady=10)

        self.start_draft()

    def start_draft(self):
        self.draft_result = {team: [] for team in teams}
        self.remaining_players = players.copy()
        self.round_number = 1
        self.next_round_button.config(state=tk.NORMAL)
        self.prepare_turn_order()
        self.info_label.config(text=f"TUR {self.round_number} - Sıra: {', '.join(self.turn_order)}")
        self.result_text.delete(1.0, tk.END)
        self.show_results()

    def prepare_turn_order(self):
        self.turn_order = teams[:]
        random.shuffle(self.turn_order)

    def next_round(self):
        if self.round_number > TOTAL_ROUNDS:
            messagebox.showinfo("Bilgi", "Draft tamamlandı!")
            self.next_round_button.config(state=tk.DISABLED)
            return

        self.prepare_turn_order()
        self.info_label.config(text=f"TUR {self.round_number} - Sıra: {', '.join(self.turn_order)}")

        for team in self.turn_order:
            if len(self.draft_result[team]) >= MAX_PLAYERS_PER_TEAM:
                continue
            # Takımın kendi oyuncularını seçemeyeceği kuralı
            available = [p for p in self.remaining_players if p[1] != team]
            if not available:
                messagebox.showinfo("Bilgi", f"{team} için seçilebilecek oyuncu kalmadı!")
                continue
            selected_player = random.choice(available)
            self.draft_result[team].append(selected_player)
            self.remaining_players.remove(selected_player)

        self.round_number += 1
        self.show_results()

        if self.round_number > TOTAL_ROUNDS:
            self.next_round_button.config(state=tk.DISABLED)
            messagebox.showinfo("Bilgi", "Draft tamamlandı!")

    def show_results(self):
        self.result_text.delete(1.0, tk.END)
        for team in teams:
            self.result_text.insert(tk.END, f"{team} seçilen oyuncular ({len(self.draft_result[team])}):\n")
            for p in self.draft_result[team]:
                self.result_text.insert(tk.END, f" - {p[0]} ({p[2]}) [{p[1]}]\n")
            self.result_text.insert(tk.END, "\n")


if __name__ == "__main__":
    root = tk.Tk()
    app = DraftApp(root)
    root.mainloop()

#El Turco©
#https://guns.lol/dorukozkurt
