"""
Destination knowledge base and metadata for the Travel Recommendation System.
Provides rich descriptions, recommended activities, best time to visit, climate suitability,
and curated fallback imagery with Unsplash attribution.
"""

DESTINATIONS_DATA = {
    "Manali": {
        "name": "Manali",
        "state": "Himachal Pradesh",
        "region": "North India",
        "tagline": "Himalayan Adventure & Snow Paradise",
        "description": "Nestled in the Beas River Valley, Manali is a premier Himalayan hill resort surrounded by majestic pine forests, snow-clad peaks, and thrilling adventure hubs like Solang Valley and Rohtang Pass.",
        "best_time_to_visit": "October to February (Snow & Winter Sports) | March to June (Pleasant Summer)",
        "season_suitability": "Winter & Summer",
        "climate_type": "Alpine / Mountainous",
        "budget_level": "Medium to High",
        "ideal_duration": "4 to 7 Days",
        "recommended_activities": [
            "Snowboarding & Skiing at Solang Valley",
            "White Water River Rafting in Beas River",
            "Scenic Excursion to Rohtang Pass / Atal Tunnel",
            "Trek to Jogini Waterfalls & Vashisht Hot Springs",
            "Café Hopping & Live Music in Old Manali"
        ],
        "top_attractions": [
            "Hadimba Temple",
            "Solang Valley",
            "Rohtang Pass",
            "Atal Tunnel",
            "Jogini Waterfall"
        ],
        "search_query": "Manali mountains Himalayas India travel",
        "fallback_image": {
            "url": "https://images.unsplash.com/photo-1626621341517-bbf3d9990a23?auto=format&fit=crop&w=1200&q=80",
            "photographer": "Ashwini Chaudhary",
            "photographer_url": "https://unsplash.com/@ashwinichaudhary"
        }
    },
    "Goa": {
        "name": "Goa",
        "state": "Goa",
        "region": "West India",
        "tagline": "Sun-Kissed Beaches, Vibrant Nightlife & Portuguese Charm",
        "description": "India's pocket-sized paradise along the Arabian Sea, world-renowned for golden sand beaches, thrilling water sports, historic Portuguese churches, spice plantations, and vibrant beach shacks.",
        "best_time_to_visit": "November to February (Beach & Water Sports) | July to September (Lush Monsoon)",
        "season_suitability": "Winter, Monsoon & Summer",
        "climate_type": "Tropical Coastal",
        "budget_level": "Medium to High",
        "ideal_duration": "4 to 6 Days",
        "recommended_activities": [
            "Parasailing, Jet Skiing & Scuba Diving at Calangute & Grand Island",
            "Sunset Catamaran Cruise on Mandovi River",
            "Exploring Portuguese Heritage Quarters in Fontainhas, Panaji",
            "Jeep Safari & Trek to Dudhsagar Waterfalls",
            "Beachfront Dining & Live Music at Anjuna & Vagator"
        ],
        "top_attractions": [
            "Baga Beach",
            "Fort Aguada",
            "Basilica of Bom Jesus",
            "Dudhsagar Falls",
            "Fontainhas Latin Quarter"
        ],
        "search_query": "Goa beach palm trees sunset India travel",
        "fallback_image": {
            "url": "https://images.unsplash.com/photo-1512343879784-a960bf40e7f2?auto=format&fit=crop&w=1200&q=80",
            "photographer": "Sumit Sourav",
            "photographer_url": "https://unsplash.com/@sumitsourav"
        }
    },
    "Araku Valley": {
        "name": "Araku Valley",
        "state": "Andhra Pradesh",
        "region": "South India",
        "tagline": "Aromatic Coffee Hills & Million-Year-Old Caves",
        "description": "A tranquil hill station nestled in the Eastern Ghats, celebrated for its organic coffee plantations, verdant green valleys, rich tribal heritage, and the spectacular million-year-old Borra Caves.",
        "best_time_to_visit": "October to March (Pleasant, Misty & Cool)",
        "season_suitability": "Winter & Monsoon",
        "climate_type": "Mild Hill Station",
        "budget_level": "Low to Medium",
        "ideal_duration": "2 to 4 Days",
        "recommended_activities": [
            "Exploring the million-year-old stalactites at Borra Caves",
            "Coffee Tasting & Plantation Tour at Araku Tribal Museum",
            "Trek through lush greenery to Katiki & Chaparai Cascades",
            "Scenic Vista Dome train ride through Eastern Ghats tunnels",
            "Sampling traditional bamboo chicken and local tribal delicacies"
        ],
        "top_attractions": [
            "Borra Caves",
            "Araku Tribal Museum & Coffee House",
            "Katiki Waterfalls",
            "Padmapuram Botanical Gardens",
            "Chaparai Water Cascades"
        ],
        "search_query": "Araku Valley green hills coffee plantation India travel",
        "fallback_image": {
            "url": "https://images.unsplash.com/photo-1589182373726-e4f658ab50f0?auto=format&fit=crop&w=1200&q=80",
            "photographer": "Aditya Chache",
            "photographer_url": "https://unsplash.com/@adityachache"
        }
    },
    "Munnar": {
        "name": "Munnar",
        "state": "Kerala",
        "region": "South India",
        "tagline": "Emerald Tea Valleys & Misty Western Ghats",
        "description": "Situated at the confluence of three mountain streams in God's Own Country, Munnar features sprawling carpet-like tea estates, cascading waterfalls, mist-shrouded peaks, and the endangered Nilgiri Tahr.",
        "best_time_to_visit": "September to March (Crisp & Scenic) | June to August (Romantic Monsoon)",
        "season_suitability": "Winter, Monsoon & Spring",
        "climate_type": "Subtropical Highland",
        "budget_level": "Medium to High",
        "ideal_duration": "3 to 5 Days",
        "recommended_activities": [
            "Guided strolls through verdant Tea Estates & Tea Museum tour",
            "Wildlife safari spotting Nilgiri Tahr at Eravikulam National Park",
            "Speed boating and kayaking at Mattupetty Dam & Kundala Lake",
            "Panoramic 360-degree viewpoint photography at Top Station",
            "Ayurvedic wellness rejuvenation and spice plantation trails"
        ],
        "top_attractions": [
            "Eravikulam National Park",
            "Mattupetty Dam",
            "Top Station",
            "Tea Museum",
            "Attukal Waterfalls"
        ],
        "search_query": "Munnar tea plantations green hills Kerala India travel",
        "fallback_image": {
            "url": "https://images.unsplash.com/photo-1593693397690-362cb9666fc2?auto=format&fit=crop&w=1200&q=80",
            "photographer": "Dheen Raj",
            "photographer_url": "https://unsplash.com/@dheenraj"
        }
    },
    "Jaipur": {
        "name": "Jaipur",
        "state": "Rajasthan",
        "region": "North India",
        "tagline": "The Regal Pink City of Forts & Palaces",
        "description": "Part of India's famed Golden Triangle, Jaipur is an architectural wonderland of royal terracotta palaces, magnificent hilltop fortresses, bustling colorful gemstone bazaars, and opulent heritage.",
        "best_time_to_visit": "October to March (Royal Winter & Festive Season)",
        "season_suitability": "Winter & Spring",
        "climate_type": "Semi-Arid Heritage",
        "budget_level": "Medium to High",
        "ideal_duration": "3 to 4 Days",
        "recommended_activities": [
            "Ascending Amer Fort on an elephant or heritage jeep safari",
            "Photographing the honeycomb architecture of Hawa Mahal",
            "Astronomical wonder tour at UNESCO Jantar Mantar",
            "Bazaar hopping in Johari and Bapu Bazaars for handicrafts",
            "Authentic Rajasthani royal dining and folk dance at Chokhi Dhani"
        ],
        "top_attractions": [
            "Amer Fort",
            "Hawa Mahal (Palace of Winds)",
            "City Palace",
            "Jantar Mantar",
            "Nahargarh Fort Sunset Point"
        ],
        "search_query": "Jaipur Hawa Mahal palace Rajasthan India travel",
        "fallback_image": {
            "url": "https://images.unsplash.com/photo-1599661046289-e31897846e41?auto=format&fit=crop&w=1200&q=80",
            "photographer": "Annie Spratt",
            "photographer_url": "https://unsplash.com/@anniespratt"
        }
    },
    "Ooty": {
        "name": "Ooty",
        "state": "Tamil Nadu",
        "region": "South India",
        "tagline": "Queen of the Nilgiri Hill Stations",
        "description": "Nestled in the blue Nilgiri Mountains, Ooty charms visitors with cool mountain air, colonial-era heritage, the UNESCO Nilgiri Mountain Railway toy train, sprawling botanical gardens, and scenic lakes.",
        "best_time_to_visit": "October to June (Pleasant Summers & Flower Shows)",
        "season_suitability": "Summer, Spring & Winter",
        "climate_type": "Cool Temperate Highland",
        "budget_level": "Low to Medium",
        "ideal_duration": "3 to 5 Days",
        "recommended_activities": [
            "Riding the historic UNESCO Nilgiri Toy Train from Mettupalayam",
            "Boating amidst eucalyptus groves on Ooty Lake",
            "Panoramic views from Doddabetta Peak (highest in Nilgiris)",
            "Strolling through 20,000+ varieties in the Government Botanical Garden",
            "Speed boating at Pykara Lake and visiting Pykara Falls"
        ],
        "top_attractions": [
            "Nilgiri Mountain Railway",
            "Doddabetta Peak",
            "Government Botanical Garden",
            "Ooty Lake & Boat House",
            "Pykara Waterfalls"
        ],
        "search_query": "Ooty hills Nilgiri tea garden India travel",
        "fallback_image": {
            "url": "https://images.unsplash.com/photo-1589182373726-e4f658ab50f0?auto=format&fit=crop&w=1200&q=80",
            "photographer": "Karthik Sridhar",
            "photographer_url": "https://unsplash.com/@karthiksridhar"
        }
    },
    "Mysore": {
        "name": "Mysore",
        "state": "Karnataka",
        "region": "South India",
        "tagline": "City of Royal Palaces, Sandalwood & Silk",
        "description": "The cultural capital of Karnataka, celebrated for the dazzling Indo-Saracenic Mysore Palace illuminated by 100,000 lights, centuries-old silk weaving traditions, fragrant sandalwood, and grand Dasara pageantry.",
        "best_time_to_visit": "September to March (Grand Dussehra Festivities & Winter)",
        "season_suitability": "Autumn & Winter",
        "climate_type": "Tropical Savanna",
        "budget_level": "Low to Medium",
        "ideal_duration": "2 to 3 Days",
        "recommended_activities": [
            "Grand tour of the illuminated Mysore Palace and Golden Throne",
            "Ascending Chamundi Hill to visit the Chamundeshwari Temple & Nandi",
            "Evening musical fountain show at Brindavan Gardens",
            "Shopping for authentic pure Mysore Silk and aromatic sandalwood oils",
            "Experiencing authentic Mysore Pak sweets at century-old sweet shops"
        ],
        "top_attractions": [
            "Mysore Palace (Amba Vilas)",
            "Chamundi Hills & Temple",
            "Brindavan Gardens",
            "St. Philomena's Cathedral",
            "Devaraja Heritage Market"
        ],
        "search_query": "Mysore Palace illumination Karnataka India travel",
        "fallback_image": {
            "url": "https://images.unsplash.com/photo-1600100397608-f010f443b718?auto=format&fit=crop&w=1200&q=80",
            "photographer": "Aayush Srivastava",
            "photographer_url": "https://unsplash.com/@aayushsrivastava"
        }
    },
    "Hyderabad": {
        "name": "Hyderabad",
        "state": "Telangana",
        "region": "South India",
        "tagline": "The City of Pearls, Nizams & World-Famous Biryani",
        "description": "A dynamic metropolis where four centuries of opulent Qutb Shahi and Nizami heritage seamlessly meet cutting-edge innovation hubs, world-renowned Dum Biryani, and the world's largest film studio city.",
        "best_time_to_visit": "October to March (Pleasant & Breezy)",
        "season_suitability": "Winter & Autumn",
        "climate_type": "Semi-Arid Heritage Metropolis",
        "budget_level": "Low to Medium",
        "ideal_duration": "2 to 4 Days",
        "recommended_activities": [
            "Climbing Charminar and shopping for lacquer bangles in Laad Bazaar",
            "Exploring the acoustic engineering and sound show at Golconda Fort",
            "Feasting on authentic Hyderabadi Dum Biryani, Haleem, and Irani Chai",
            "Full-day cinematic adventure tour at Ramoji Film City",
            "Sunset boat cruise on Hussain Sagar Lake around the monolithic Buddha"
        ],
        "top_attractions": [
            "Charminar",
            "Golconda Fort",
            "Ramoji Film City",
            "Chowmahalla Palace",
            "Hussain Sagar Lake & Buddha Statue"
        ],
        "search_query": "Hyderabad Charminar Golconda fort India travel",
        "fallback_image": {
            "url": "https://images.unsplash.com/photo-1605649487212-47bdab064df7?auto=format&fit=crop&w=1200&q=80",
            "photographer": "Praveen Thirumurugan",
            "photographer_url": "https://unsplash.com/@praveent"
        }
    },
    "Rishikesh": {
        "name": "Rishikesh",
        "state": "Uttarakhand",
        "region": "North India",
        "tagline": "Yoga Capital of the World & Himalayan Adventure Hub",
        "description": "Where the sacred River Ganges leaves the Himalayas to enter the plains, Rishikesh is a soulful haven of spiritual ashrams, river rapids, cliff jumping, bungee jumps, and serene evening Ganga Aarti rituals.",
        "best_time_to_visit": "September to November | March to May (Rafting & Camping Season)",
        "season_suitability": "Spring, Autumn & Summer",
        "climate_type": "Subtropical Mountain Foothills",
        "budget_level": "Low to Medium",
        "ideal_duration": "3 to 5 Days",
        "recommended_activities": [
            "Grade III & IV White Water River Rafting along the holy Ganges",
            "India's highest 83m Bungee Jump & Giant Swing at Mohan Chatti",
            "Attending the mesmerizing evening Maha Ganga Aarti at Triveni Ghat",
            "Exploring the iconic graffiti and meditation halls at Beatles Ashram",
            "Riverside camping with bonfires, cliff jumping, and sunrise yoga"
        ],
        "top_attractions": [
            "Laxman Jhula & Ram Jhula",
            "Triveni Ghat Aarti",
            "Beatles Ashram (Chaurasi Kutia)",
            "Neelkanth Mahadev Temple",
            "Shivpuri River Beach"
        ],
        "search_query": "Rishikesh Ganges river rafting yoga India travel",
        "fallback_image": {
            "url": "https://images.unsplash.com/photo-1544735716-392fe2489ffa?auto=format&fit=crop&w=1200&q=80",
            "photographer": "Saurabh Kumar",
            "photographer_url": "https://unsplash.com/@saurabhkumar"
        }
    },
    "Darjeeling": {
        "name": "Darjeeling",
        "state": "West Bengal",
        "region": "East India",
        "tagline": "Queen of the Hills & World Capital of Fine Tea",
        "description": "Perched amidst rolling emerald tea gardens with breathtaking panoramic views of Mount Kanchenjunga (world's 3rd highest peak), Darjeeling is famed for heritage toy trains, Tibetan monasteries, and crisp mountain breezes.",
        "best_time_to_visit": "March to May (Spring Blooms) | October to December (Crystal Clear Vistas)",
        "season_suitability": "Spring, Autumn & Summer",
        "climate_type": "Subtropical Highland Alpine",
        "budget_level": "Medium to High",
        "ideal_duration": "4 to 6 Days",
        "recommended_activities": [
            "Witnessing golden sunrise over Mount Kanchenjunga from Tiger Hill",
            "Riding the UNESCO Darjeeling Himalayan Railway Toy Train through Batasia Loop",
            "Plucking tea leaves and tasting muscatel tea at Happy Valley Tea Estate",
            "Visiting Tibetan Buddhist Peace Pagoda and Ghoom Monastery",
            "Exploring Himalayan Mountaineering Institute and Snow Leopard Zoo"
        ],
        "top_attractions": [
            "Tiger Hill Viewpoint",
            "Batasia Loop & War Memorial",
            "Darjeeling Himalayan Railway",
            "Happy Valley Tea Estate",
            "Japanese Peace Pagoda"
        ],
        "search_query": "Darjeeling Kanchenjunga tea mountains India travel",
        "fallback_image": {
            "url": "https://images.unsplash.com/photo-1544735716-392fe2489ffa?auto=format&fit=crop&w=1200&q=80",
            "photographer": "Anirban Bhattacharya",
            "photographer_url": "https://unsplash.com/@anirbanb"
        }
    },
    "Varanasi": {
        "name": "Varanasi",
        "state": "Uttar Pradesh",
        "region": "North India",
        "tagline": "The Eternal Spiritual Heartbeat of India",
        "description": "One of the oldest continuously inhabited cities on Earth, Kashi/Varanasi is the sacred spiritual epicenter of Hinduism, where ancient rituals unfold along 84 mystical stone Ghats on the sacred River Ganges.",
        "best_time_to_visit": "October to March (Pleasant Spiritual Winter)",
        "season_suitability": "Winter & Autumn",
        "climate_type": "Humid Subtropical Spiritual City",
        "budget_level": "Low to Medium",
        "ideal_duration": "2 to 4 Days",
        "recommended_activities": [
            "Dawn wooden boat ride along the 84 Ghats during morning prayers",
            "Experiencing the grand evening Maha Aarti at Dashashwamedh Ghat",
            "Darshan at the sacred golden Kashi Vishwanath Temple Corridor",
            "Excursion to sacred Sarnath where Lord Buddha gave his first sermon",
            "Exploring winding ancient alleys, tasting Banarasi Paan, and buying Banarasi Silk"
        ],
        "top_attractions": [
            "Dashashwamedh Ghat",
            "Kashi Vishwanath Corridor",
            "Assi Ghat & Subah-e-Banaras",
            "Manikarnika Ghat",
            "Sarnath Deer Park & Dhamek Stupa"
        ],
        "search_query": "Varanasi Ghats Ganga Aarti temple India travel",
        "fallback_image": {
            "url": "https://images.unsplash.com/photo-1561361513-2d000a50f0dc?auto=format&fit=crop&w=1200&q=80",
            "photographer": "Jeet Dhanoa",
            "photographer_url": "https://unsplash.com/@jeetdhanoa"
        }
    },
    "Udaipur": {
        "name": "Udaipur",
        "state": "Rajasthan",
        "region": "West India",
        "tagline": "The Romantic City of Floating Lakes & Regal Palaces",
        "description": "Often called the 'Venice of the East', Udaipur is a fairytale city of pristine shimmering lakes, opulent white marble palaces, intricately carved havelis, romantic sunsets, and rich Rajput chivalric history.",
        "best_time_to_visit": "October to March (Romantic Winter & Royal Evenings)",
        "season_suitability": "Winter & Spring",
        "climate_type": "Semi-Arid Lake Oasis",
        "budget_level": "Medium to High",
        "ideal_duration": "3 to 5 Days",
        "recommended_activities": [
            "Sunset boat cruise on Lake Pichola past the floating Taj Lake Palace",
            "Exploring the grand courtyards and crystal gallery of City Palace",
            "Panoramic sunset views from the hilltop Monsoon Palace (Sajjangarh)",
            "Dharohar folk dance performance at Bagore Ki Haveli",
            "Candlelit rooftop dining overlooking the illuminated Lake Pichola"
        ],
        "top_attractions": [
            "City Palace Complex",
            "Lake Pichola & Jag Mandir",
            "Saheliyon-ki-Bari",
            "Monsoon Palace (Sajjangarh)",
            "Bagore Ki Haveli"
        ],
        "search_query": "Udaipur City Palace Lake Pichola Rajasthan India travel",
        "fallback_image": {
            "url": "https://images.unsplash.com/photo-1599661046289-e31897846e41?auto=format&fit=crop&w=1200&q=80",
            "photographer": "Yash Bhardwaj",
            "photographer_url": "https://unsplash.com/@yashb"
        }
    },
    "Andaman": {
        "name": "Andaman",
        "state": "Andaman & Nicobar Islands",
        "region": "South India",
        "tagline": "Pristine Tropical Islands & Turquoise Waters",
        "description": "An exotic archipelago of emerald islands ringed by pristine white sandy beaches, turquoise lagoons, untouched coral reefs, and thrilling marine biodiversity in the Bay of Bengal.",
        "best_time_to_visit": "October to May (Calm Seas, Clear Waters & Scuba Diving)",
        "season_suitability": "Winter & Spring",
        "climate_type": "Tropical Maritime Island",
        "budget_level": "High",
        "ideal_duration": "6 to 9 Days",
        "recommended_activities": [
            "Scuba diving and sea walking amidst coral reefs at Elephant Beach (Havelock)",
            "Watching the world-famous golden sunset at Radhanagar Beach (Asia's Best Beach)",
            "Snorkeling & kayaking in the crystal clear turquoise waters of Neil Island",
            "Visiting the historic Cellular Jail and witnessing the patriotic Light & Sound show",
            "Speedboat journey to the natural limestone caves at Baratang Island"
        ],
        "top_attractions": [
            "Radhanagar Beach (Havelock)",
            "Cellular Jail National Memorial",
            "Elephant Beach Coral Reef",
            "Neil Island (Bharatpur Beach)",
            "Baratang Island Limestone Caves"
        ],
        "search_query": "Andaman islands tropical beach ocean turquoise India travel",
        "fallback_image": {
            "url": "https://images.unsplash.com/photo-1589308078059-be1415eab4c3?auto=format&fit=crop&w=1200&q=80",
            "photographer": "Tatiana Zhukova",
            "photographer_url": "https://unsplash.com/@tatiana"
        }
    },
    "Coorg": {
        "name": "Coorg",
        "state": "Karnataka",
        "region": "South India",
        "tagline": "The Scotland of India with Misty Coffee Hills",
        "description": "Also known as Kodagu, Coorg is a picturesque hill district carpeted in lush coffee estates, aromatic spice plantations, thundering waterfalls, misty peaks, and the unique martial culture of the Kodavas.",
        "best_time_to_visit": "October to March (Pleasant & Green) | July to September (Monsoon Splendor)",
        "season_suitability": "Monsoon & Winter",
        "climate_type": "Tropical Monsoon Highland",
        "budget_level": "Medium to High",
        "ideal_duration": "3 to 5 Days",
        "recommended_activities": [
            "Staying at a traditional heritage plantation homestay surrounded by coffee aromas",
            "Bathing and feeding elephants at Dubare Elephant Camp on Cauvery River",
            "Trekking to Abbey Falls and Iruppu Falls in the Western Ghats",
            "Golden sunset views and musical fountains from Raja's Seat",
            "Visiting the golden statues at Namdroling Tibetan Monastery (Bylakuppe)"
        ],
        "top_attractions": [
            "Abbey Falls",
            "Raja's Seat",
            "Dubare Elephant Camp",
            "Namdroling Monastery (Golden Temple)",
            "Mandalpatti Peak 4x4 Jeep Safari"
        ],
        "search_query": "Coorg coffee plantation hills Karnataka India travel",
        "fallback_image": {
            "url": "https://images.unsplash.com/photo-1589182373726-e4f658ab50f0?auto=format&fit=crop&w=1200&q=80",
            "photographer": "Prashant Sharma",
            "photographer_url": "https://unsplash.com/@prashant"
        }
    },
    "Kashmir": {
        "name": "Kashmir",
        "state": "Jammu & Kashmir",
        "region": "North India",
        "tagline": "Paradise on Earth - Valleys, Houseboats & Snow",
        "description": "Revered as 'Heaven on Earth', Kashmir enchants with tranquil Shikara rides on Dal Lake, romantic carved houseboats, world-class ski slopes in Gulmarg, and blooming saffron and tulip meadows.",
        "best_time_to_visit": "April to October (Tulips & Verdant Valleys) | December to February (Snow & Gulmarg Skiing)",
        "season_suitability": "Summer, Winter & Spring",
        "climate_type": "Subtropical Alpine Highland",
        "budget_level": "High",
        "ideal_duration": "5 to 8 Days",
        "recommended_activities": [
            "Sunset Shikara ride and romantic heritage houseboat stay on Dal Lake",
            "Riding Phase 1 & 2 of the world's second-highest Gondola Cable Car in Gulmarg",
            "Horse riding through pine forests in Betaab Valley & Aru Valley (Pahalgam)",
            "Strolling through royal Mughal terraced gardens (Shalimar & Nishat Bagh)",
            "Shopping for authentic Kashmiri Pashmina shawls, saffron, and walnut wood crafts"
        ],
        "top_attractions": [
            "Dal Lake & Floating Market",
            "Gulmarg Gondola & Apharwat Peak",
            "Pahalgam Betaab Valley",
            "Shalimar & Nishat Mughal Gardens",
            "Sonamarg Meadow of Gold"
        ],
        "search_query": "Kashmir Dal Lake shikara Gulmarg snow mountains India travel",
        "fallback_image": {
            "url": "https://images.unsplash.com/photo-1598091383021-15ddea10925d?auto=format&fit=crop&w=1200&q=80",
            "photographer": "Imad Clicks",
            "photographer_url": "https://unsplash.com/@imadclicks"
        }
    }
}
