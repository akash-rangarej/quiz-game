import random,time
from colorama import Fore
science = [
    ['What is the chemical symbol for water?\n a) H2O, b) CO2, c) O2, d) CH4', 'a'],
    ['What is the closest planet to the Sun?\n a) Venus, b) Mars, c) Mercury, d) Earth', 'c'],
    ['What is the powerhouse of the cell?\n a) Nucleus, b) Mitochondria, c) Ribosome, d) Endoplasmic reticulum', 'b'],
    ['Which gas is most abundant in the Earth\'s atmosphere?\n a) Oxygen, b) Nitrogen, c) Carbon dioxide, d) Hydrogen', 'b'],
    ['What is the chemical symbol for gold?\n a) Au, b) Ag, c) Fe, d) Cu', 'a'],
    ['What causes tides on Earth?\n a) Gravitational pull of the Moon, b) Gravitational pull of the Sun, c) Earth\'s rotation, d) Solar winds', 'a'],
    ['What is the largest organ in the human body?\n a) Liver, b) Skin, c) Brain, d) Heart', 'b'],
    ['What is the chemical symbol for iron?\n a) Ir, b) Fe, c) Au, d) Ag', 'b'],
    ['Which planet is known as the "Red Planet"?\n a) Venus, b) Jupiter, c) Mars, d) Saturn', 'c'],
    ['What is the process by which plants make their food?\n a) Respiration, b) Photosynthesis, c) Fermentation, d) Transpiration', 'b'],
    ['What is the hardest natural substance on Earth?\n a) Diamond, b) Graphite, c) Quartz, d) Talc', 'a'],
    ['What is the unit of electric current?\n a) Watt, b) Volt, c) Ampere, d) Ohm', 'c'],
    ['Which metal is liquid at room temperature?\n a) Mercury, b) Aluminum, c) Iron, d) Copper', 'a'],
    ['What is the chemical symbol for oxygen?\n a) O, b) Ox, c) Os, d) O2', 'a'],
    ['What is the largest mammal in the world?\n a) African elephant, b) Blue whale, c) Giraffe, d) Hippopotamus', 'b'],
    ['Which gas do plants absorb during photosynthesis?\n a) Carbon dioxide, b) Oxygen, c) Nitrogen, d) Hydrogen', 'a'],
    ['What is the smallest bone in the human body?\n a) Stapes, b) Femur, c) Tibia, d) Ulna', 'a'],
    ['What is the main component of the Earth\'s core?\n a) Iron, b) Nickel, c) Silicon, d) Aluminum', 'a'],
    ['What is the chemical symbol for sodium?\n a) Sa, b) So, c) Na, d) No', 'c'],
    ['What is the process by which plants release water vapor into the atmosphere?\n a) Transpiration, b) Evaporation, c) Condensation, d) Precipitation', 'a'],
    ['What is the unit of force?\n a) Newton, b) Watt, c) Volt, d) Ampere', 'a'],
    ['What is the chemical symbol for carbon?\n a) Co, b) Cr, c) Ca, d) C', 'd'],
    ['Which gas is known as laughing gas?\n a) Nitrogen, b) Oxygen, c) Nitrous oxide, d) Carbon dioxide', 'c'],
    ['What is the chemical formula for table salt?\n a) NaCl, b) HCl, c) KCl, d) CaCl2', 'a'],
    ['What is the Earth\'s primary source of energy?\n a) Sun, b) Moon, c) Stars, d) Planets', 'a'],
    ['What is the chemical symbol for silver?\n a) Au, b) Ag, c) Si, d) Sr', 'b'],
    ['What is the unit of frequency?\n a) Hertz, b) Watt, c) Volt, d) Ampere', 'a'],
    ['Which animal is known as the "ship of the desert"?\n a) Camel, b) Elephant, c) Horse, d) Giraffe', 'a'],
    ['What is the chemical symbol for helium?\n a) He, b) H, c) Au, d) Ag', 'a'],
    ['What is the largest planet in our solar system?\n a) Jupiter, b) Saturn, c) Mars, d) Earth', 'a'],
    ['Which gas do humans exhale when they breathe?\n a) Oxygen, b) Carbon dioxide, c) Nitrogen, d) Hydrogen', 'b'],
    ['What is the chemical symbol for potassium?\n a) Po, b) Pa, c) P, d) K', 'd'],
    ['What is the process by which water changes from liquid to gas?\n a) Evaporation, b) Condensation, c) Precipitation, d) Sublimation', 'a'],
    ['What is the unit of electric charge?\n a) Coulomb, b) Volt, c) Ampere, d) Ohm', 'a'],
    ['What is the chemical symbol for copper?\n a) Co, b) Cu, c) Cp, d) Cr', 'b'],
    ['What is the hardest natural substance in the human body?\n a) Enamel, b) Bone, c) Cartilage, d) Tooth', 'a'],
    ['What is the chemical symbol for nitrogen?\n a) N, b) Ni, c) Na, d) Ne', 'a'],
    ['What is the process by which plants lose water through their leaves?\n a) Transpiration, b) Respiration, c) Photosynthesis, d) Absorption', 'a'],
    ['What is the unit of power?\n a) Watt, b) Volt, c) Ampere, d) Ohm', 'a'],
    ['Which gas is used in balloons to make them float?\n a) Oxygen, b) Nitrogen, c) Helium, d) Hydrogen', 'c'],
    ['What is the chemical symbol for carbon dioxide?\n a) Co, b) Co2, c) Cd, d) Ca', 'b'],
    ['What is the unit of luminous intensity?\n a) Candela, b) Lux, c) Lumen, d) Watt', 'a'],
    ['Which gas is essential for respiration?\n a) Oxygen, b) Nitrogen, c) Carbon dioxide, d) Hydrogen', 'a'],
    ['What is the chemical symbol for silicon?\n a) Si, b) S, c) Se, d) Sr', 'a'],
    ['What is the largest bone in the human body?\n a) Femur, b) Humerus, c) Tibia, d) Ulna', 'a'],
    ['What is the chemical symbol for lead?\n a) Le, b) L, c) Pb, d) P', 'c'],
    ['What is the process by which a liquid changes into a gas?\n a) Evaporation, b) Condensation, c) Sublimation, d) Freezing', 'a'],
    ['What is the unit of magnetic flux?\n a) Weber, b) Tesla, c) Gauss, d) Newton', 'a'],
    ['Which gas do plants release during photosynthesis?\n a) Oxygen, b) Carbon dioxide, c) Nitrogen, d) Hydrogen', 'a'],
    ['What is the chemical symbol for mercury?\n a) Hg, b) Me, c) Mg, d) He', 'a'],
    ['What is the unit of capacitance?\n a) Farad, b) Coulomb, c) Henry, d) Ohm', 'a']
]

geography = [
    ['Which is the longest river in the world?\n a) Nile, b) Amazon, c) Yangtze, d) Mississippi', 'a'],
    ['Which is the largest ocean on Earth?\n a) Pacific Ocean, b) Atlantic Ocean, c) Indian Ocean, d) Arctic Ocean', 'a'],
    ['Which country is known as the Land of the Rising Sun?\n a) Japan, b) China, c) India, d) Australia', 'a'],
    ['What is the capital of Canada?\n a) Ottawa, b) Toronto, c) Vancouver, d) Montreal', 'a'],
    ['What is the capital of Australia?\n a) Sydney, b) Melbourne, c) Canberra, d) Brisbane', 'c'],
    ['Which is the largest desert in the world?\n a) Sahara Desert, b) Arabian Desert, c) Gobi Desert, d) Kalahari Desert', 'a'],
    ['Which country is known as the Land of the Midnight Sun?\n a) Norway, b) Finland, c) Sweden, d) Iceland', 'a'],
    ['Which is the highest mountain peak in the world?\n a) Mount Everest, b) K2, c) Kanchenjunga, d) Lhotse', 'a'],
    ['What is the largest continent by land area?\n a) Asia, b) Africa, c) North America, d) South America', 'a'],
    ['Which country is the smallest in terms of land area?\n a) Vatican City, b) Monaco, c) Nauru, d) Tuvalu', 'a'],
    ['What is the capital of Brazil?\n a) Rio de Janeiro, b) Sao Paulo, c) Brasilia, d) Salvador', 'c'],
    ['What is the capital of France?\n a) Paris, b) Marseille, c) Lyon, d) Nice', 'a'],
    ['Which is the longest mountain range in the world?\n a) Andes, b) Himalayas, c) Rockies, d) Alps', 'a'],
    ['Which country is known as the Land of Fire and Ice?\n a) Iceland, b) Greenland, c) Norway, d) New Zealand', 'a'],
    ['What is the capital of South Africa?\n a) Johannesburg, b) Cape Town, c) Pretoria, d) Durban', 'c'],
    ['Which is the largest lake in Africa?\n a) Lake Victoria, b) Lake Tanganyika, c) Lake Malawi, d) Lake Chad', 'a'],
    ['Which is the largest island in the world?\n a) Greenland, b) New Guinea, c) Borneo, d) Madagascar', 'a'],
    ['What is the capital of Italy?\n a) Rome, b) Milan, c) Naples, d) Turin', 'a'],
    ['Which is the largest city in the world by population?\n a) Tokyo, b) Delhi, c) Shanghai, d) Mumbai', 'a'],
    ['What is the capital of Argentina?\n a) Buenos Aires, b) Cordoba, c) Rosario, d) Mendoza', 'a'],
    ['Which is the largest bay in the world?\n a) Hudson Bay, b) Bay of Bengal, c) Bay of Biscay, d) Chesapeake Bay', 'a'],
    ['What is the capital of Saudi Arabia?\n a) Riyadh, b) Jeddah, c) Mecca, d) Medina', 'a'],
    ['Which is the largest river in India?\n a) Ganges, b) Yamuna, c) Brahmaputra, d) Godavari', 'a'],
    ['What is the capital of China?\n a) Beijing, b) Shanghai, c) Guangzhou, d) Shenzhen', 'a'],
    ['Which is the highest waterfall in the world?\n a) Angel Falls, b) Victoria Falls, c) Niagara Falls, d) Iguazu Falls', 'a'],
    ['What is the capital of Spain?\n a) Madrid, b) Barcelona, c) Valencia, d) Seville', 'a'],
    ['Which is the largest coral reef system in the world?\n a) Great Barrier Reef, b) Belize Barrier Reef, c) Red Sea Coral Reef, d) New Caledonia Barrier Reef', 'a'],
    ['What is the capital of Russia?\n a) Moscow, b) Saint Petersburg, c) Novosibirsk, d) Yekaterinburg', 'a'],
    ['Which is the largest archipelago in the world?\n a) Indonesia, b) Philippines, c) Japan, d) Maldives', 'a'],
    ['What is the capital of Egypt?\n a) Cairo, b) Alexandria, c) Luxor, d) Giza', 'a'],
    ['Which is the largest peninsula in the world?\n a) Arabian Peninsula, b) Indian Peninsula, c) Scandinavian Peninsula, d) Iberian Peninsula', 'a'],
    ['What is the capital of Turkey?\n a) Ankara, b) Istanbul, c) Izmir, d) Bursa', 'a'],
    ['Which is the largest glacier in the world?\n a) Lambert Glacier, b) Siachen Glacier, c) Vatnajokull Glacier, d) Biafo Glacier', 'a'],
    ['What is the capital of South Korea?\n a) Seoul, b) Busan, c) Incheon, d) Daegu', 'a'],
    ['Which is the largest hot desert in the world?\n a) Sahara Desert, b) Arabian Desert, c) Gobi Desert, d) Kalahari Desert', 'a'],
    ['What is the capital of Nigeria?\n a) Abuja, b) Lagos, c) Kano, d) Ibadan', 'a'],
    ['Which is the largest gulf in the world?\n a) Gulf of Mexico, b) Persian Gulf, c) Gulf of Guinea, d) Gulf of Alaska', 'a'],
    ['What is the capital of Thailand?\n a) Bangkok, b) Chiang Mai, c) Pattaya, d) Phuket', 'a'],
    ['Which is the largest lake in India?\n a) Chilika Lake, b) Vembanad Lake, c) Pulicat Lake, d) Wular Lake', 'a'],
    ['What is the capital of Indonesia?\n a) Jakarta, b) Surabaya, c) Bandung, d) Medan', 'a'],
    ['Which is the largest bay in India?\n a) Bay of Bengal, b) Arabian Sea, c) Gulf of Kutch, d) Gulf of Khambhat', 'a'],
    ['What is the capital of Argentina?\n a) Buenos Aires, b) Cordoba, c) Rosario, d) Mendoza', 'a'],
    ['Which is the longest canal in the world?\n a) Grand Canal (China), b) Suez Canal, c) Panama Canal, d) Rhine-Main-Danube Canal', 'a'],
    ['What is the capital of United Kingdom?\n a) London, b) Manchester, c) Birmingham, d) Liverpool', 'a'],
    ['Which is the highest plateau in the world?\n a) Tibetan Plateau, b) Deccan Plateau, c) Colorado Plateau, d) Patagonian Plateau', 'a'],
    ['What is the capital of Iran?\n a) Tehran, b) Isfahan, c) Shiraz, d) Tabriz', 'a'],
    ['Which is the largest delta in the world?\n a) Ganges Delta, b) Mississippi Delta, c) Nile Delta, d) Mekong Delta', 'a'],
    ['Which is the only sea without any coast?\n a) Sargasso Sea, b) Arabian Sea, c) Mediterranean Sea, d) Yellow Sea', 'a'],
    ['What is the largest desert in Asia?\n a) Arabian Desert, b) Gobi Desert, c) Thar Desert, d) Karakum Desert', 'b'],
    ['Which river is known as the "River of Sorrow"?\n a) Nile River, b) Amazon River, c) Yellow River, d) Indus River', 'c'],
    ['What is the largest glacier in the world?\n a) Siachen Glacier, b) Perito Moreno Glacier, c) Lambert Glacier, d) Gangotri Glacier', 'c']
]

history = [
    ['Who was the Maratha ruler known as the "Hindu Pad Padshahi"?\n a) Baji Rao I, b) Chhatrapati Shivaji Maharaj, c) Balaji Vishwanath, d) Peshwa Madhavrao I', 'b'],
    ['Which Indian state was ruled by the Ahom dynasty?\n a) Manipur, b) Assam, c) Tripura, d) Meghalaya', 'b'],
    ['Who was the founder of the Gupta Empire, often referred to as the "Golden Age" of ancient India?\n a) Chandragupta II, b) Chandragupta I, c) Samudragupta, d) Kumaragupta I', 'b'],
    ['Which ancient Indian kingdom was ruled by the Sunga dynasty?\n a) Kalinga, b) Magadha, c) Gandhara, d) Mathura', 'b'],
    ['Who was the medieval Indian ruler known for his introduction of the "Din-i Ilahi", a syncretic religion blending elements of Islam and Hinduism?\n a) Jahangir, b) Aurangzeb, c) Akbar, d) Babur', 'c'],
    ['Which Indian philosopher is credited with the composition of the work "Vedanta Sutra", a foundational text of Vedanta philosophy?\n a) Swami Vivekananda, b) Ramanuja, c) Adi Shankaracharya, d) Madhvacharya', 'c'],
    ['Who was the Mughal emperor known for his policy of "Sulh-i kul" or "universal peace", promoting religious tolerance?\n a) Aurangzeb, b) Shah Jahan, c) Jahangir, d) Akbar', 'd'],
    ['Which Indian king established the "Four Pillars of Deshkal System" for the effective governance of his empire?\n a) Samudragupta, b) Chandragupta Maurya, c) Harsha, d) Chandragupta II', 'b'],
    ['Who was the medieval Indian ruler known as the "Lion of Mewar" for his resistance against the Mughal emperor Akbar?\n a) Rana Pratap Singh, b) Rana Sanga, c) Rana Kumbha, d) Rana Hammir Singh', 'a'],
    ['Which ancient Indian text contains the earliest known references to the concept of zero?\n a) Arthashastra, b) Upanishads, c) Rigveda, d) Jain Agamas', 'c'],
    ['Who was the Indian mathematician who provided an early approximation of the value of pi and laid the foundation for calculus?\n a) Brahmagupta, b) Bhaskara II, c) Aryabhata, d) Varahamihira', 'c'],
    ['Which Indian ruler is known for his establishment of the Mauryan Empire and his propagation of Buddhism?\n a) Ashoka the Great, b) Chandragupta Maurya, c) Harsha, d) Kanishka', 'b'],
    ['Which Indian king defeated the Greek invader Alexander the Great during his campaign in India?\n a) Chandragupta Maurya, b) Ashoka the Great, c) Kanishka, d) Porus', 'd'],
    ['Who was the Mughal emperor known for his patronage of art and architecture, including the construction of the Red Fort and Jama Masjid in Delhi?\n a) Akbar, b) Aurangzeb, c) Jahangir, d) Shah Jahan', 'd'],
    ['Which Indian emperor is known for his establishment of the Gupta Empire, considered a period of great cultural and scientific achievements?\n a) Chandragupta II, b) Samudragupta, c) Kumaragupta I, d) Chandragupta I', 'd'],
    ['Which ancient Indian ruler is known for his role in the spread of Buddhism and the construction of the Great Stupa at Sanchi?\n a) Chandragupta Maurya, b) Harsha, c) Kanishka, d) Ashoka the Great', 'd'],
    ['Who was the Indian saint and philosopher known for his teachings on Bhakti (devotion) to Lord Krishna, popularizing the Krishna Bhakti movement?\n a) Chaitanya Mahaprabhu, b) Mirabai, c) Vallabha Acharya, d) Ramanuja', 'a'],
    ['Which Indian kingdom was ruled by the Chola dynasty, known for its maritime prowess and extensive trade networks?\n a) Pallava, b) Pandya, c) Chera, d) Chola', 'd'],
    ['Who was the Indian emperor known for his military campaigns against the Greek successors of Alexander the Great in northwest India?\n a) Ashoka the Great, b) Chandragupta Maurya, c) Kanishka, d) Harsha', 'b'],
    ['Which Indian king is known for his patronage of the famous Nalanda University and his efforts to spread Buddhism?\n a) Ashoka the Great, b) Chandragupta Maurya, c) Kanishka, d) Harsha', 'b'],
    ['Who was the medieval Indian ruler known for his construction of the Qutub Minar and establishment of the Delhi Sultanate?\n a) Alauddin Khalji, b) Razia Sultan, c) Muhammad bin Tughluq, d) Qutb-ud-din Aibak', 'd'],
    ['Which ancient Indian text contains the earliest known reference to the concept of "Ahimsa" or non-violence?\n a) Upanishads, b) Rigveda, c) Jain Agamas, d) Mahabharata', 'c'],
    ['Who was the Indian emperor known for his conversion to Buddhism after the Kalinga War and his efforts to spread the teachings of Buddha?\n a) Chandragupta Maurya, b) Ashoka the Great, c) Kanishka, d) Harsha', 'b'],
    ['Which Indian dynasty is known for its extensive maritime trade and cultural exchanges with Southeast Asia, China, and Africa?\n a) Maurya, b) Gupta, c) Pallava, d) Chola', 'd'],
    ['Who was the Indian king known for his military victories against the Greek king Seleucus I Nicator and the expansion of his empire?\n a) Ashoka the Great, b) Chandragupta Maurya, c) Kanishka, d) Harsha', 'b'],
    ['Who was the Maratha ruler known as the "Hindu Pad Padshahi"?\n a) Baji Rao I, b) Chhatrapati Shivaji Maharaj, c) Balaji Vishwanath, d) Peshwa Madhavrao I', 'b'],
    ['Which ancient Indian kingdom was ruled by the Sunga dynasty?\n a) Kalinga, b) Magadha, c) Gandhara, d) Mathura', 'b'],
    ['Who was the founder of the Gupta Empire, often referred to as the "Golden Age" of ancient India?\n a) Chandragupta II, b) Chandragupta I, c) Samudragupta, d) Kumaragupta I', 'b'],
    ['Who was the Indian ruler known for his patronage of the famous Nalanda University and his efforts to spread Buddhism?\n a) Chandragupta Maurya, b) Ashoka the Great, c) Harsha, d) Kanishka', 'b'],
    ['Who was the medieval Indian ruler known as the "Lion of Mewar" for his resistance against the Mughal emperor Akbar?\n a) Rana Pratap Singh, b) Rana Sanga, c) Rana Kumbha, d) Rana Hammir Singh', 'a'],
    ['Who was the founder of the Maurya Empire, often considered the first empire in ancient India?\n a) Chandragupta Maurya, b) Ashoka the Great, c) Bindusara, d) Chandragupta II', 'b'],
    ['Which Indian emperor is known for his policy of "Sulh-i kul" or "universal peace", promoting religious tolerance?\n a) Aurangzeb, b) Shah Jahan, c) Jahangir, d) Akbar', 'd'],
    ['Which ancient Indian text contains the earliest known references to the concept of zero?\n a) Arthashastra, b) Upanishads, c) Rigveda, d) Jain Agamas', 'c'],
    ['Who was the Indian mathematician who provided an early approximation of the value of pi and laid the foundation for calculus?\n a) Brahmagupta, b) Bhaskara II, c) Aryabhata, d) Varahamihira', 'c'],
    ['Which Indian ruler is known for his establishment of the Mauryan Empire and his propagation of Buddhism?\n a) Ashoka the Great, b) Chandragupta Maurya, c) Harsha, d) Kanishka', 'b'],
    ['Who was the Indian emperor known for his policy of "Dharma Vijaya", which promoted the spread of Buddhism beyond the Indian subcontinent?\n a) Ashoka the Great, b) Chandragupta Maurya, c) Harsha, d) Kanishka', 'd'],
    ['Which Indian king established the Nalanda University, one of the world\'s first residential universities and a center for Buddhist learning?\n a) Ashoka the Great, b) Chandragupta Maurya, c) Harsha, d) Kumaragupta I', 'a'],
    ['Who was the Mughal emperor known for his architectural masterpiece, the Taj Mahal, built in memory of his wife Mumtaz Mahal?\n a) Akbar, b) Aurangzeb, c) Jahangir, d) Shah Jahan', 'd'],
    ['Which Indian dynasty is known for its patronage of art and literature, as evidenced by the construction of the Ellora and Ajanta caves?\n a) Gupta, b) Maurya, c) Pallava, d) Chola', 'c'],
    ['Who was the Indian ruler known for his military campaigns against the Greek successors of Alexander the Great in northwest India?\n a) Ashoka the Great, b) Chandragupta Maurya, c) Kanishka, d) Harsha', 'b'],
    ['Which Indian king is known for his patronage of the famous Nalanda University and his efforts to spread Buddhism?\n a) Ashoka the Great, b) Chandragupta Maurya, c) Kanishka, d) Harsha', 'b'],
    ['Who was the medieval Indian ruler known as the "Lion of Mewar" for his resistance against the Mughal emperor Akbar?\n a) Rana Pratap Singh, b) Rana Sanga, c) Rana Kumbha, d) Rana Hammir Singh', 'a'],
    ['Who was the founder of the Maurya Empire, often considered the first empire in ancient India?\n a) Chandragupta Maurya, b) Ashoka the Great, c) Bindusara, d) Chandragupta II', 'a'],
    ['Which Indian emperor is known for his policy of "Sulh-i kul" or "universal peace", promoting religious tolerance?\n a) Aurangzeb, b) Shah Jahan, c) Jahangir, d) Akbar', 'd'],
    ['Which ancient Indian text contains the earliest known references to the concept of zero?\n a) Arthashastra, b) Upanishads, c) Rigveda, d) Jain Agamas', 'c'],
    ['Who was the Indian mathematician who provided an early approximation of the value of pi and laid the foundation for calculus?\n a) Brahmagupta, b) Bhaskara II, c) Aryabhata, d) Varahamihira', 'c'],
    ['Which Indian ruler is known for his establishment of the Mauryan Empire and his propagation of Buddhism?\n a) Ashoka the Great, b) Chandragupta Maurya, c) Harsha, d) Kanishka', 'b'],
    ['Which Indian king defeated the Greek invader Alexander the Great during his campaign in India?\n a) Chandragupta Maurya, b) Ashoka the Great, c) Kanishka, d) Porus', 'd'],
    ['Who was the Mughal emperor known for his patronage of art and architecture, including the construction of the Red Fort and Jama Masjid in Delhi?\n a) Akbar, b) Aurangzeb, c) Jahangir, d) Shah Jahan', 'd'],
    ['Which Indian emperor is known for his establishment of the Gupta Empire, considered a period of great cultural and scientific achievements?\n a) Chandragupta II, b) Samudragupta, c) Kumaragupta I, d) Chandragupta I', 'd'],
    ['Which ancient Indian ruler is known for his role in the spread of Buddhism and the construction of the Great Stupa at Sanchi?\n a) Chandragupta Maurya, b) Harsha, c) Kanishka, d) Ashoka the Great', 'd'],
    ['Who was the Indian saint and philosopher known for his teachings on Bhakti (devotion) to Lord Krishna, popularizing the Krishna Bhakti movement?\n a) Chaitanya Mahaprabhu, b) Mirabai, c) Vallabha Acharya, d) Ramanuja', 'a'],
    ['Which Indian kingdom was ruled by the Chola dynasty, known for its maritime prowess and extensive trade networks?\n a) Pallava, b) Pandya, c) Chera, d) Chola', 'd'],
    ['Who was the Indian emperor known for his military campaigns against the Greek successors of Alexander the Great in northwest India?\n a) Ashoka the Great, b) Chandragupta Maurya, c) Kanishka, d) Harsha', 'b'],
    ['What was the name of the ancient Indian university which is one of the earliest centers of higher learning in the world?\n a) Nalanda, b) Takshashila, c) Vikramashila, d) Vallabhi', 'b']
]

programming = [
    ['In Python, what is the difference between the "is" and "==" operators?\n a) "is" checks for object identity while "==" checks for equality, b) "is" checks for equality while "==" checks for object identity, c) There is no difference, they are interchangeable, d) "is" is used for comparison while "==" is used for assignment', 'a'],
    ['In C, what is the purpose of the "volatile" keyword?\n a) It indicates that the variable can be modified unexpectedly by external sources, b) It specifies that the variable\'s value cannot be changed after initialization, c) It tells the compiler to optimize the variable for faster access, d) It ensures that the variable is only accessible within the current scope', 'a'],
    ['In Java, what is the difference between "ArrayList" and "LinkedList"?\n a) ArrayList is faster for random access while LinkedList is faster for sequential access, b) LinkedList is faster for random access while ArrayList is faster for sequential access, c) They both have the same performance characteristics, d) ArrayList is implemented using arrays while LinkedList is implemented using linked nodes', 'a'],
    ['What is the purpose of the keyword "yield" in Python?\n a) It is used to exit a loop or function, b) It is used to generate a sequence of values lazily, c) It is used to raise an exception, d) It is used to define a generator function', 'b'],
    ['In C, what is the difference between "malloc()" and "calloc()" functions?\n a) "malloc()" allocates memory and leaves it uninitialized while "calloc()" allocates memory and initializes it to zero, b) "calloc()" is used for allocating memory for arrays while "malloc()" is used for individual variables, c) "malloc()" is used for static memory allocation while "calloc()" is used for dynamic memory allocation, d) There is no difference, they are interchangeable', 'a'],
    ['What is a "lambda" function in Python?\n a) It is a small anonymous function defined using the "lambda" keyword, b) It is a built-in function for sorting lists, c) It is a function used for handling exceptions, d) It is a function that returns another function', 'a'],
    ['In Java, what is the purpose of the "finally" block in a try-catch-finally statement?\n a) It is executed if an exception is thrown within the try block, b) It is executed regardless of whether an exception is thrown or not, c) It is executed if no exceptions are thrown within the try block, d) It is executed before the try block', 'b'],
    ['In C, what does the "->" operator do when used with pointers?\n a) It is used for arithmetic operations on pointers, b) It is used for accessing members of a structure through a pointer, c) It is used for bitwise operations on pointers, d) It is used for dereferencing a pointer', 'b'],
    ['What is the purpose of the keyword "static" in Java?\n a) It is used to specify that a variable or method belongs to the class rather than instances of the class, b) It is used to declare constants, c) It is used to prevent inheritance, d) It is used to indicate that a method can throw exceptions', 'a'],
    ['In Python, what does the "global" keyword do?\n a) It is used to define global variables, b) It is used to access variables defined in outer scopes, c) It is used to import global modules, d) It is used to define global functions', 'a'],
    ['What is the purpose of the "const" keyword in C?\n a) It is used to specify that a variable cannot be modified after initialization, b) It is used to declare a constant variable, c) It is used to define constants, d) It is used to specify that a variable is immutable', 'a'],
    ['In Java, what is the difference between "equals()" and "==" for comparing objects?\n a) "equals()" compares the values of objects while "==" compares object references, b) "==" compares the values of objects while "equals()" compares object references, c) They both have the same functionality, d) "==" compares objects using their hash codes while "equals()" compares their values', 'a'],
    ['What is a "tuple" in Python?\n a) It is an immutable sequence of elements, b) It is a mutable sequence of elements, c) It is a dictionary with unique keys, d) It is a function that returns multiple values', 'a'],
    ['In C, what is the purpose of the "sizeof" operator?\n a) It is used to calculate the size of a variable or data type in bytes, b) It is used to determine the number of elements in an array, c) It is used to allocate memory for a variable, d) It is used to define the size of a data structure', 'a'],
    ['What is a "package" in Java?\n a) It is a collection of classes and interfaces, b) It is a data structure for storing objects, c) It is a way to organize source code files, d) It is a built-in module for handling files', 'a'],
    ['In Python, what is the purpose of the "enumerate()" function?\n a) It is used to generate a sequence of numbers, b) It is used to iterate over a sequence while keeping track of the index, c) It is used to remove duplicates from a sequence, d) It is used to sort elements in a sequence', 'b'],
    ['What is the purpose of the "volatile" keyword in Java?\n a) It indicates that a variable\'s value may be modified unexpectedly by multiple threads, b) It specifies that a variable\'s value cannot be changed after initialization, c) It tells the compiler to optimize the variable for faster access, d) It ensures that the variable is only accessible within the current scope', 'a'],
    ['In C, what does the "typedef" keyword do?\n a) It is used to create aliases for data types, b) It is used to declare a variable, c) It is used to define constants, d) It is used to specify the return type of a function', 'a'],
    ['What is a "hashmap" in Java?\n a) It is a data structure that stores key-value pairs and allows fast retrieval based on the key, b) It is a function for computing hash codes, c) It is a built-in module for handling files, d) It is a way to organize source code files', 'a'],
    ['In Python, what is the purpose of the "map()" function?\n a) It is used to apply a function to each item in a sequence and return a list of the results, b) It is used to concatenate two or more sequences, c) It is used to filter items in a sequence based on a condition, d) It is used to remove duplicates from a sequence', 'a'],
    ['What is the purpose of the "try" block in a try-catch statement?\n a) It is used to handle exceptions that may occur within the block of code, b) It is used to define the code to be executed if no exceptions occur, c) It is used to define the code to be executed if an exception occurs, d) It is used to define the cleanup code to be executed regardless of whether an exception occurs or not', 'a'],
    ['In C, what is the difference between "++i" and "i++"?\n a) "++i" increments the value of i and returns the new value, while "i++" returns the value of i and then increments it, b) "i++" increments the value of i and returns the new value, while "++i" returns the value of i and then increments it, c) They both have the same functionality, d) "++i" increments the value of i by 1, while "i++" increments it by 2', 'a'],
    ['What is a "constructor" in Java?\n a) It is a method used to destroy objects, b) It is a method used to create objects, c) It is a keyword used to declare constants, d) It is a function for sorting arrays', 'b'],
    ['In Python, what is the purpose of the "__init__" method?\n a) It is a built-in function for initializing variables, b) It is a special method called when an object is created, c) It is a method for converting objects to strings, d) It is a method for adding elements to a list', 'b'],
    ['What is the purpose of the "break" statement in loops?\n a) It is used to exit the loop immediately, b) It is used to skip the current iteration of the loop, c) It is used to restart the loop from the beginning, d) It is used to execute the loop indefinitely', 'a'],
    ['In Java, what is the purpose of the "super" keyword?\n a) It is used to call the constructor of the superclass, b) It is used to access the superclass\' methods and variables, c) It is used to define a method that overrides a superclass method, d) It is used to indicate that a class implements an interface', 'a'],
    ['What is the purpose of the "const" keyword in Java?\n a) It is used to specify that a variable cannot be modified after initialization, b) It is used to declare a constant variable, c) It is used to define constants, d) It is used to specify that a variable is immutable', 'a'],
    ['In C, what is the difference between "struct" and "union"?\n a) "struct" is used to define a data structure that contains members with different data types, while "union" is used to define a data structure that contains members with the same data type, b) "struct" is used for dynamic memory allocation while "union" is used for static memory allocation, c) "struct" is used to define constants while "union" is used to declare variables, d) "struct" is used for bitwise operations while "union" is used for arithmetic operations', 'a'],
    ['What is a "thread" in Java?\n a) It is a lightweight process that shares the same memory space, b) It is a data structure for storing objects, c) It is a built-in module for handling files, d) It is a way to organize source code files', 'a'],
    ['In Python, what is the purpose of the "filter()" function?\n a) It is used to remove duplicates from a sequence, b) It is used to apply a function to each item in a sequence and return a list of the results, c) It is used to filter items in a sequence based on a condition, d) It is used to concatenate two or more sequences', 'c'],
    ['What is the purpose of the "const" keyword in C?\n a) It is used to specify that a variable cannot be modified after initialization, b) It is used to declare a constant variable, c) It is used to define constants, d) It is used to specify that a variable is immutable', 'a'],
    ['In Java, what is the purpose of the "extends" keyword in inheritance?\n a) It is used to define a subclass that inherits from a superclass, b) It is used to declare constants, c) It is used to prevent inheritance, d) It is used to define the size of a data structure', 'a'],
    ['What is a "lambda expression" in Java?\n a) It is an anonymous function that can have zero or more parameters and a single expression, b) It is a function for computing hash codes, c) It is a function used for handling exceptions, d) It is a function that returns another function', 'a'],
    ['In Python, what is the purpose of the "__doc__" attribute?\n a) It is used to access the documentation string of a function, class, or module, b) It is used to access the parent class of an object, c) It is used to access the attributes of an object, d) It is used to access the current module', 'a'],
    ['What is the purpose of the "sizeof" operator in C?\n a) It is used to calculate the size of a variable or data type in bytes, b) It is used to determine the number of elements in an array, c) It is used to allocate memory for a variable, d) It is used to define the size of a data structure', 'a'],
    ['In Java, what is the difference between "ArrayList" and "LinkedList"?\n a) ArrayList is faster for random access while LinkedList is faster for sequential access, b) LinkedList is faster for random access while ArrayList is faster for sequential access, c) They both have the same performance characteristics, d) ArrayList is implemented using arrays while LinkedList is implemented using linked nodes', 'a'],
    ['What is the purpose of the "super" keyword in Python?\n a) It is used to access the superclass\' methods and variables, b) It is used to call the constructor of the superclass, c) It is used to define a method that overrides a superclass method, d) It is used to indicate that a class implements an interface', 'a'],
    ['In C, what is the difference between "strcpy()" and "strncpy()" functions?\n a) "strcpy()" copies the entire string while "strncpy()" copies a specified number of characters, b) "strcpy()" is used for copying strings while "strncpy()" is used for concatenating strings, c) "strcpy()" copies a specified number of characters while "strncpy()" copies the entire string, d) They both have the same functionality', 'a'],
    ['What is a "hashmap" in Java?\n a) It is a data structure that stores key-value pairs and allows fast retrieval based on the key, b) It is a function for computing hash codes, c) It is a built-in module for handling files, d) It is a way to organize source code files', 'a'],
    ['In Python, what is the purpose of the "strip()" method?\n a) It is used to remove leading and trailing whitespace from a string, b) It is used to split a string into a list of substrings, c) It is used to concatenate two or more strings, d) It is used to convert a string to lowercase', 'a'],
    ['In Python, what is the purpose of the "range()" function?\n a) It is used to generate a sequence of numbers, b) It is used to iterate over a sequence while keeping track of the index, c) It is used to filter items in a sequence based on a condition, d) It is used to remove duplicates from a sequence', 'a'],
    ['What is a "pointer" in C?\n a) It is a variable that stores the memory address of another variable, b) It is a variable that stores the value of another variable, c) It is a function that returns a memory address, d) It is a data structure for storing objects', 'a'],
    ['In Java, what is the purpose of the "this" keyword?\n a) It is used to access the superclass\' methods and variables, b) It is used to call the constructor of the superclass, c) It is used to access the current object\'s methods and variables, d) It is used to indicate that a class implements an interface', 'c'],
    ['What is the purpose of the "try" block in a try-catch statement?\n a) It is used to handle exceptions that may occur within the block of code, b) It is used to define the code to be executed if no exceptions occur, c) It is used to define the code to be executed if an exception occurs, d) It is used to define the cleanup code to be executed regardless of whether an exception occurs or not', 'a'],
    ['In C, what is the difference between "++i" and "i++"?\n a) "++i" increments the value of i and returns the new value, while "i++" returns the value of i and then increments it, b) "i++" increments the value of i and returns the new value, while "++i" returns the value of i and then increments it, c) They both have the same functionality, d) "++i" increments the value of i by 1, while "i++" increments it by 2', 'a'],
    ['What is a "constructor" in Java?\n a) It is a method used to destroy objects, b) It is a method used to create objects, c) It is a keyword used to declare constants, d) It is a function for sorting arrays', 'b'],
    ['In Python, what is the purpose of the "__init__" method?\n a) It is a built-in function for initializing variables, b) It is a special method called when an object is created, c) It is a method for converting objects to strings, d) It is a method for adding elements to a list', 'b'],
    ['What is the purpose of the "break" statement in loops?\n a) It is used to exit the loop immediately, b) It is used to skip the current iteration of the loop, c) It is used to restart the loop from the beginning, d) It is used to execute the loop indefinitely', 'a'],
    ['In Java, what is the purpose of the "super" keyword?\n a) It is used to call the constructor of the superclass, b) It is used to access the superclass\' methods and variables, c) It is used to define a method that overrides a superclass method, d) It is used to indicate that a class implements an interface', 'a'],
    ['What is the purpose of the "const" keyword in Java?\n a) It is used to specify that a variable cannot be modified after initialization, b) It is used to declare a constant variable, c) It is used to define constants, d) It is used to specify that a variable is immutable', 'a'],
    ['In C, what is the difference between "struct" and "union"?\n a) "struct" is used to define a data structure that contains members with different data types, while "union" is used to define a data structure that contains members with the same data type, b) "struct" is used for dynamic memory allocation while "union" is used for static memory allocation, c) "struct" is used to define constants while "union" is used to declare variables, d) "struct" is used for bitwise operations while "union" is used for arithmetic operations', 'a'],
]

gk_questions = [
    ['What is the capital of Bhutan?\n a) Thimphu, b) Kathmandu, c) Ulaanbaatar, d) Male', 'c'],
    ['Who was the first woman to fly solo across the Atlantic Ocean?\n a) Amelia Earhart, b) Bessie Coleman, c) Sally Ride, d) Valentina Tereshkova', 'b'],
    ['Which river is the longest in the world?\n a) Nile, b) Amazon, c) Mississippi, d) Yangtze', 'c'],
    ['Who discovered penicillin?\n a) Alexander Fleming, b) Louis Pasteur, c) Jonas Salk, d) Marie Curie', 'b'],
    ['Which planet is known as the "Red Planet"?\n a) Mars, b) Venus, c) Jupiter, d) Saturn', 'a'],
    ['What is the chemical symbol for gold?\n a) Au, b) Ag, c) Fe, d) Cu', 'c'],
    ['Who wrote "1984"?\n a) George Orwell, b) Aldous Huxley, c) Ray Bradbury, d) F. Scott Fitzgerald', 'c'],
    ['What is the capital of Kazakhstan?\n a) Nur-Sultan, b) Astana, c) Bishkek, d) Tashkent', 'a'],
    ['Who composed the famous classical music piece "The Four Seasons"?\n a) Antonio Vivaldi, b) Johann Sebastian Bach, c) Wolfgang Amadeus Mozart, d) Ludwig van Beethoven', 'c'],
    ['In Greek mythology, who is the god of the sea?\n a) Poseidon, b) Zeus, c) Apollo, d) Hades', 'b'],
    ['What is the largest desert in the world?\n a) Sahara Desert, b) Arabian Desert, c) Gobi Desert, d) Antarctic Desert', 'd'],
    ['Which country has the largest population in the world?\n a) China, b) India, c) United States, d) Indonesia', 'd'],
    ['Who is often credited with the invention of the first practical telephone?\n a) Alexander Graham Bell, b) Thomas Edison, c) Nikola Tesla, d) Guglielmo Marconi', 'b'],
    ['What is the chemical symbol for silver?\n a) Ag, b) Au, c) Cu, d) Fe', 'b'],
    ['Who painted the famous artwork "The Starry Night"?\n a) Vincent van Gogh, b) Pablo Picasso, c) Claude Monet, d) Salvador Dali', 'd'],
    ['Which of Shakespeare\'s plays is the longest?\n a) Hamlet, b) Macbeth, c) King Lear, d) Antony and Cleopatra', 'b'],
    ['What is the capital of New Zealand?\n a) Wellington, b) Auckland, c) Christchurch, d) Sydney', 'a'],
    ['Who was the first woman to win a Nobel Prize?\n a) Marie Curie, b) Mother Teresa, c) Ada Lovelace, d) Rosalind Franklin', 'a'],
    ['In which year did the Berlin Wall fall?\n a) 1989, b) 1991, c) 1987, d) 1993', 'a'],
    ['Who wrote "Don Quixote"?\n a) Miguel de Cervantes, b) Leo Tolstoy, c) Fyodor Dostoevsky, d) Gabriel Garcia Marquez', 'a'],
    ['What is the capital of Mongolia?\n a) Ulaanbaatar, b) Astana, c) Seoul, d) Bangkok', 'c'],
    ['Who composed the famous classical music piece "The Marriage of Figaro"?\n a) Wolfgang Amadeus Mozart, b) Ludwig van Beethoven, c) Johann Sebastian Bach, d) Franz Schubert', 'a'],
    ['What is the chemical symbol for iron?\n a) Fe, b) Ir, c) In, d) I', 'a'],
    ['Who painted "The Scream"?\n a) Edvard Munch, b) Pablo Picasso, c) Vincent van Gogh, d) Leonardo da Vinci', 'a'],
    ['What is the capital of Australia?\n a) Canberra, b) Sydney, c) Melbourne, d) Brisbane', 'a'],
    ['Who was the first man to walk on the moon?\n a) Neil Armstrong, b) Buzz Aldrin, c) Alan Shepard, d) Yuri Gagarin', 'a'],
    ['Which animal is known as the "King of the Jungle"?\n a) Lion, b) Tiger, c) Elephant, d) Gorilla', 'a'],
    ['What is the chemical symbol for hydrogen?\n a) H, b) He, c) Hy, d) Ho', 'a'],
    ['Who wrote "Pride and Prejudice"?\n a) Jane Austen, b) Emily Bronte, c) Charlotte Bronte, d) Charles Dickens', 'a'],
    ['What is the capital of Brazil?\n a) Brasília, b) Rio de Janeiro, c) São Paulo, d) Salvador', 'a'],
    ['Who composed the famous opera "Madame Butterfly"?\n a) Giacomo Puccini, b) Georges Bizet, c) Giuseppe Verdi, d) Richard Wagner', 'a'],
    ['What is the chemical symbol for calcium?\n a) Ca, b) Cl, c) Cm, d) Ce', 'a'],
    ['Who painted the ceiling of the Sistine Chapel?\n a) Michelangelo, b) Leonardo da Vinci, c) Raphael, d) Donatello', 'a'],
    ['What is the capital of Canada?\n a) Ottawa, b) Toronto, c) Montreal, d) Vancouver', 'a'],
    ['Who composed the famous classical music piece "Moonlight Sonata"?\n a) Ludwig van Beethoven, b) Wolfgang Amadeus Mozart, c) Johann Sebastian Bach, d) Franz Schubert', 'a'],
    ['What is the chemical symbol for nitrogen?\n a) N, b) Ni, c) Ne, d) No', 'a'],
    ['Who wrote "To Kill a Mockingbird"?\n a) Harper Lee, b) Mark Twain, c) F. Scott Fitzgerald, d) Ernest Hemingway', 'a'],
    ['What is the capital of South Africa?\n a) Pretoria, b) Cape Town, c) Johannesburg, d) Durban', 'a'],
    ['Who composed the famous opera "The Barber of Seville"?\n a) Gioachino Rossini, b) Wolfgang Amadeus Mozart, c) Ludwig van Beethoven, d) Giuseppe Verdi', 'a'],
    ['What is the chemical symbol for oxygen?\n a) O, b) Ox, c) On, d) Om', 'a'],
    ['Who wrote "Moby-Dick"?\n a) Herman Melville, b) Nathaniel Hawthorne, c) Edgar Allan Poe, d) Ralph Waldo Emerson', 'a'],
    ['What is the capital of Italy?\n a) Rome, b) Milan, c) Florence, d) Venice', 'a'],
    ['Who composed the famous classical music piece "The Nutcracker"?\n a) Pyotr Ilyich Tchaikovsky, b) Johann Sebastian Bach, c) Ludwig van Beethoven, d) Franz Schubert', 'a'],
    ['What is the chemical symbol for carbon dioxide?\n a) CO2, b) CO, c) OC, d) CC', 'a'],
    ['Who wrote "The Great Gatsby"?\n a) F. Scott Fitzgerald, b) Ernest Hemingway, c) John Steinbeck, d) William Faulkner', 'a'],
    ['What is the capital of France?\n a) Paris, b) Marseille, c) Lyon, d) Toulouse', 'a'],
    ['Who composed the famous opera "La Bohème"?\n a) Giacomo Puccini, b) Georges Bizet, c) Giuseppe Verdi, d) Richard Wagner', 'a'],
    ['What is the chemical symbol for helium?\n a) He, b) Hm, c) Hl, d) Hn', 'a'],
    ['Who wrote "War and Peace"?\n a) Leo Tolstoy, b) Fyodor Dostoevsky, c) Anton Chekhov, d) Ivan Turgenev', 'a'],
    ['What is the capital of Germany?\n a) Berlin, b) Munich, c) Hamburg, d) Frankfurt', 'a'],
    ['Who composed the famous opera "Tosca"?\n a) Giacomo Puccini, b) Georges Bizet, c) Giuseppe Verdi, d) Richard Wagner', 'a'],
    ['What is the chemical symbol for silver nitrate?\n a) AgNO3, b) Ag2NO2, c) Ag2O, d) Ag3N', 'a'],
    ['Who wrote "The Catcher in the Rye"?\n a) J.D. Salinger, b) Ernest Hemingway, c) F. Scott Fitzgerald, d) Mark Twain', 'a'],
    ['What is the capital of India?\n a) New Delhi, b) Mumbai, c) Kolkata, d) Chennai', 'a'],
    ['Who composed the famous classical music piece "Eine kleine Nachtmusik"?\n a) Wolfgang Amadeus Mozart, b) Ludwig van Beethoven, c) Johann Sebastian Bach, d) Franz Schubert', 'a'],
    ['What is the chemical symbol for water?\n a) H2O, b) HO, c) H, d) OH', 'a'],
    ['Who wrote "The Odyssey"?\n a) Homer, b) Virgil, c) Ovid, d) Aesop', 'a'],
    ['What is the capital of Japan?\n a) Tokyo, b) Kyoto, c) Osaka, d) Hiroshima', 'a'],
    ['Who composed the famous opera "Rigoletto"?\n a) Giuseppe Verdi, b) Wolfgang Amadeus Mozart, c) Richard Wagner, d) Ludwig van Beethoven', 'a'],
    ['What is the chemical symbol for lead?\n a) Pb, b) Pd, c) Ld, d) Le', 'a']
]
occurance=[]
while True:
    topic=input(Fore.LIGHTYELLOW_EX+"CHOOSE YOUR TOPIC\nscience\ngeography\nhistory\nprogramming\ngk\n")
    if topic == 'science':
        occurance=science                                           
        break
    elif topic == 'geography':
        occurance=geography
        break
    elif topic == 'history':
        occurance=history
        break
    elif topic== 'programming':
        occurance=programming
        break
    elif topic == 'gk':
        occurance=gk_questions
        break
    else:
        print(Fore.RED+"invalid option")
        continue
att,i,score,n=0,0,0,0
seen=[]

while n<15 :
        r1=random.randint(0,50)
        if occurance[r1][0] not in seen:
            time.sleep(0.5)
            print(Fore.LIGHTMAGENTA_EX+occurance[r1][0])            
            seen.append(occurance[r1][0])
            ans=input(Fore.CYAN+"choose the option (A,B,C,D):")
            if ans==occurance[r1][-1]:
                    print(Fore.GREEN+"correct ans!")
                    att+=1
                    score+=10
            elif ans!='a' and ans!='b' and ans!='c' and ans!='d':
                while ans!='a' and ans!='b' and ans!='c' and ans!='d':
                    print(Fore.RESET+"invalid choice")
                    ans=input(Fore.CYAN+"choose the option (A,B,C,D):")
                if ans==occurance[r1][-1]:
                    print(Fore.GREEN+"correct ans!")
                    att+=1
                    score+=10
                else:
                    print(Fore.RED+"wrong answer!")
                    print(Fore.LIGHTYELLOW_EX+f"the ans is:{occurance[r1][-1]}")
            else:
                print(Fore.RED+"wrong answer!")
                print(Fore.LIGHTYELLOW_EX+f"the ans is:{occurance[r1][-1]}")
        elif occurance[r1][0] in seen:
            continue
        n+=1
print(Fore.LIGHTGREEN_EX+f"you guessed {att} ans correctly")
print(Fore.LIGHTGREEN_EX+f"you score is :{score}/150")
perc=(score/150)*100
print(Fore.LIGHTGREEN_EX+f"the obtained percentage:{perc}")

                
