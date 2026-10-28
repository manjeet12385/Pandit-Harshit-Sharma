import os
import re
import json

import os
import re
import json

# Define the 36 states and their cities as provided by the user
LOCATIONS_DATA = [
    {
        "state_en": "Madhya Pradesh",
        "state_hi": "मध्य प्रदेश",
        "cities": [
            ("Nalkheda", "नलखेड़ा"),
            ("Ujjain", "उज्जैन"),
            ("Indore", "इंदौर"),
            ("Bhopal", "भोपाल"),
            ("Jabalpur", "जबलपुर"),
            ("Gwalior", "ग्वालियर"),
            ("Ratlam", "रतलाम"),
            ("Dewas", "देवास"),
            ("Sagar", "सागर"),
            ("Rewa", "रीवा"),
            ("Satna", "सतना"),
            ("Khandwa", "खंडवा"),
            ("Burhanpur", "बुरहानपुर"),
            ("Mandsaur", "मंदसौर"),
            ("Neemuch", "नीमच"),
            ("Shajapur", "शाजापुर"),
            ("Agar Malwa", "आगर मालवा"),
            ("Omkareshwar", "ओंकारेश्वर"),
            ("Maihar", "मैहर"),
            ("Chitrakoot", "चित्रकूट"),
            ("Sehore", "सीहोर (कुबेरेश्वर धाम)"),
            ("Narmadapuram", "नर्मदापुरम (होशंगाबाद)"),
            ("Vidisha", "विदिशा"),
            ("Chhindwara", "छिंदवाड़ा"),
            ("Shivpuri", "शिवपुरी"),
            ("Guna", "गुना"),
            ("Damoh", "दमोह"),
            ("Betul", "बैतूल"),
            ("Khargone", "खरगोन"),
            ("Barwani", "बड़वानी"),
            ("Rajgarh", "राजगढ़")
        ]
    },
    {
        "state_en": "Uttar Pradesh",
        "state_hi": "उत्तर प्रदेश",
        "cities": [
            ("Lucknow", "लखनऊ"),
            ("Varanasi", "वाराणसी"),
            ("Prayagraj", "प्रयागराज"),
            ("Kanpur", "कानपुर"),
            ("Agra", "आगरा"),
            ("Mathura", "मथुरा"),
            ("Vrindavan", "वृंदावन"),
            ("Ayodhya", "अयोध्या"),
            ("Gorakhpur", "गोरखपुर"),
            ("Meerut", "मेरठ"),
            ("Noida", "नोएडा"),
            ("Ghaziabad", "गाजियाबाद"),
            ("Greater Noida", "ग्रेटर नोएडा"),
            ("Bareilly", "बरेली"),
            ("Aligarh", "अलीगढ़"),
            ("Jhansi", "झांसी"),
            ("Moradabad", "मुरादाबाद"),
            ("Saharanpur", "सहारनपुर"),
            ("Sitapur", "सीतापुर"),
            ("Sultanpur", "सुल्तानपुर"),
            ("Mirzapur", "मिर्जापुर"),
            ("Ghazipur", "गाजीपुर"),
            ("Jaunpur", "जौनपुर"),
            ("Ballia", "बलिया"),
            ("Etawah", "इटावा"),
            ("Fatehpur", "फतेहपुर"),
            ("Basti", "बस्ती"),
            ("Deoria", "देवरिया"),
            ("Kushinagar", "कुशीनगर"),
            ("Chitrakoot", "चित्रकूट"),
            ("Muzaffarnagar", "मुजफ्फरनगर"),
            ("Firozabad", "फिरोजाबाद"),
            ("Bulandshahr", "बुलंदशहर"),
            ("Hapur", "हापुड़"),
            ("Rampur", "रामपुर"),
            ("Shahjahanpur", "शाहजहांपुर"),
            ("Farrukhabad", "फर्रुखाबाद"),
            ("Unnao", "उन्नाव"),
            ("Rae Bareli", "रायबरेली"),
            ("Amethi", "अमेठी"),
            ("Barabanki", "बाराबंकी"),
            ("Gonda", "गोंडा"),
            ("Bahraich", "बहराइच"),
            ("Lakhimpur Kheri", "लखीमपुर खीरी"),
            ("Azamgarh", "आजमगढ़"),
            ("Mau", "मऊ"),
            ("Banda", "बांदा"),
            ("Mainpuri", "मैनपुरी"),
            ("Hardoi", "हरदोई"),
            ("Sambhal", "संभल"),
            ("Amroha", "अमरोहा"),
            ("Budaun", "बदायूं"),
            ("Pilibhit", "पीलीभीत"),
            ("Pratapgarh", "प्रतापगढ़"),
            ("Lalitpur", "ललितपुर"),
            ("Orai", "उरई (जालौन)"),
            ("Kannauj", "कन्नौज"),
            ("Hathras", "हाथरस"),
            ("Etah", "एटा"),
            ("Bijnor", "बिजनौर"),
            ("Baghpat", "बागपत"),
            ("Shamli", "शामली"),
            ("Sonbhadra", "सोनभद्र (रॉबर्ट्सगंज)"),
            ("Bhadohi", "भदोही"),
            ("Mahoba", "महोबा")
        ]
    },
    {
        "state_en": "Rajasthan",
        "state_hi": "राजस्थान",
        "cities": [
            ("Jaipur", "जयपुर"),
            ("Jodhpur", "जोधपुर"),
            ("Udaipur", "उदयपुर"),
            ("Kota", "कोटा"),
            ("Ajmer", "अजमेर"),
            ("Bikaner", "बीकानेर"),
            ("Jaisalmer", "जैसलमेर"),
            ("Pushkar", "पुष्कर"),
            ("Alwar", "अलवर"),
            ("Bharatpur", "भरतपुर"),
            ("Sikar", "सीकर"),
            ("Bhilwara", "भीलवाड़ा"),
            ("Pali", "पाली"),
            ("Barmer", "बाड़मेर"),
            ("Chittorgarh", "चित्तौड़गढ़"),
            ("Mount Abu", "माउंट आबू"),
            ("Nathdwara", "नाथद्वारा"),
            ("Dausa", "दौसा"),
            ("Tonk", "टोंक"),
            ("Nagaur", "नागौर"),
            ("Khatu Shyam Ji", "खाटूश्यामजी (सीकर)"),
            ("Salasar Balaji", "सालासर बालाजी (चुरू)"),
            ("Jhunjhunu", "झुंझुनू (रानी सती धाम)"),
            ("Sawai Madhopur", "सवाई माधोपुर"),
            ("Sri Ganganagar", "श्रीगंगानगर"),
            ("Hanumangarh", "हनुमानगढ़"),
            ("Churu", "चुरू"),
            ("Banswara", "बांसवाड़ा"),
            ("Dungarpur", "डूंगरपुर"),
            ("Sirohi", "सिरोही"),
            ("Jhalawar", "झालावाड़"),
            ("Baran", "बारां")
        ]
    },
    {
        "state_en": "Delhi & Haryana",
        "state_hi": "दिल्ली और हरियाणा",
        "cities": [
            ("Delhi", "दिल्ली"),
            ("New Delhi", "नई दिल्ली"),
            ("Gurugram", "गुरुग्राम"),
            ("Faridabad", "फरीदाबाद"),
            ("Sonipat", "सोनीपत"),
            ("Panipat", "पानीपत"),
            ("Karnal", "करनाल"),
            ("Rohtak", "रोहतक"),
            ("Hisar", "हिसार"),
            ("Ambala", "अंबाला"),
            ("Panchkula", "पंचकूला"),
            ("Yamunanagar", "यमुनानगर"),
            ("Kurukshetra", "कुरुक्षेत्र"),
            ("Rewari", "रेवाड़ी"),
            ("Bhiwani", "भिवानी"),
            ("Sirsa", "सिरसा"),
            ("Kaithal", "कैथल"),
            ("Jhajjar", "झज्जर"),
            ("Pehowa", "पिहोवा (कुरुक्षेत्र तीर्थ)"),
            ("Palwal", "पलवल"),
            ("Jind", "जींद"),
            ("Fatehabad", "फतेहाबाद"),
            ("Narnaul", "नारनौल (महेंद्रगढ़)"),
            ("Charkhi Dadri", "चरखी दादरी"),
            ("Bahadurgarh", "बहादुरगढ़")
        ]
    },
    {
        "state_en": "Maharashtra",
        "state_hi": "महाराष्ट्र",
        "cities": [
            ("Mumbai", "मुंबई"),
            ("Pune", "पुणे"),
            ("Nagpur", "नागपुर"),
            ("Nashik", "नासिक"),
            ("Thane", "ठाणे"),
            ("Navi Mumbai", "नवी मुंबई"),
            ("Chhatrapati Sambhajinagar", "छत्रपति संभाजीनगर"),
            ("Kolhapur", "कोल्हापुर"),
            ("Solapur", "सोलापुर"),
            ("Amravati", "अमरावती"),
            ("Akola", "अकोला"),
            ("Jalgaon", "जलगांव"),
            ("Ahmednagar", "अहमदनगर"),
            ("Nanded", "नांदेड़"),
            ("Latur", "लातूर"),
            ("Sangli", "सांगली"),
            ("Satara", "सतारा"),
            ("Ratnagiri", "रत्नागिरी"),
            ("Shirdi", "शिरडी")
        ]
    },
    {
        "state_en": "Gujarat",
        "state_hi": "गुजरात",
        "cities": [
            ("Ahmedabad", "अहमदाबाद"),
            ("Surat", "सूरत"),
            ("Vadodara", "वडोदरा"),
            ("Rajkot", "राजकोट"),
            ("Gandhinagar", "गांधीनगर"),
            ("Jamnagar", "जामनगर"),
            ("Junagadh", "जूनागढ़"),
            ("Bhavnagar", "भावनगर"),
            ("Anand", "आणंद"),
            ("Nadiad", "नडियाद"),
            ("Bharuch", "भरूच"),
            ("Valsad", "वलसाड"),
            ("Navsari", "नवसारी"),
            ("Morbi", "मोरबी"),
            ("Mehsana", "मेहसाणा"),
            ("Dwarka", "द्वारका"),
            ("Somnath", "सोमनाथ"),
            ("Porbandar", "पोरबंदर"),
            ("Ambaji", "अम्बाजी (बनासकांठा शक्तिपीठ)"),
            ("Salangpur", "सारंगपुर (कष्टभंजन धाम)"),
            ("Patan", "पाटण"),
            ("Surendranagar", "सुरेंद्रनगर"),
            ("Palanpur", "पालनपुर"),
            ("Amreli", "अमरेली"),
            ("Dahod", "दाहोद")
        ]
    },
    {
        "state_en": "Bihar",
        "state_hi": "बिहार",
        "cities": [
            ("Patna", "पटना"),
            ("Gaya", "गया"),
            ("Bodh Gaya", "बोधगया"),
            ("Muzaffarpur", "मुजफ्फरपुर"),
            ("Bhagalpur", "भागलपुर"),
            ("Darbhanga", "दरभंगा"),
            ("Purnia", "पूर्णिया"),
            ("Bihar Sharif", "बिहार शरीफ"),
            ("Ara", "आरा"),
            ("Begusarai", "बेगूसराय"),
            ("Samastipur", "समस्तीपुर"),
            ("Chapra", "छपरा"),
            ("Sitamarhi", "सीतामढ़ी"),
            ("Munger", "मुंगेर"),
            ("Sasaram", "सासाराम"),
            ("Hajipur", "हाजीपुर"),
            ("Buxar", "बक्सर (विश्वामित्र आश्रम)"),
            ("Siwan", "सीवान"),
            ("Gopalganj", "गोपालगंज"),
            ("Motihari", "मोतिहारी"),
            ("Bettiah", "बेतिया"),
            ("Madhubani", "मधुबनी"),
            ("Saharsa", "सहरसा"),
            ("Katihar", "कटिहार"),
            ("Nawada", "नवादा"),
            ("Dehri", "डेहरी ऑन सोन (रोहतास)")
        ]
    },
    {
        "state_en": "Jharkhand",
        "state_hi": "झारखंड",
        "cities": [
            ("Ranchi", "राँची"),
            ("Jamshedpur", "जमशेदपुर"),
            ("Dhanbad", "धनबाद"),
            ("Bokaro", "बोकारो"),
            ("Deoghar", "देवघर"),
            ("Hazaribagh", "हजारीबाग"),
            ("Giridih", "गिरिडीह"),
            ("Dumka", "दुमका"),
            ("Ramgarh", "रामगढ़"),
            ("Medininagar", "मेदिनीनगर"),
            ("Godda", "गोड्डा")
        ]
    },
    {
        "state_en": "Punjab",
        "state_hi": "पंजाब",
        "cities": [
            ("Amritsar", "अमृतसर"),
            ("Ludhiana", "लुधियाना"),
            ("Jalandhar", "जालंधर"),
            ("Patiala", "पटियाला"),
            ("Bathinda", "बठिंडा"),
            ("Mohali", "मोहाली"),
            ("Chandigarh Areas", "चंडीगढ़ क्षेत्र"),
            ("Pathankot", "पठानकोट"),
            ("Hoshiarpur", "होशियारपुर"),
            ("Moga", "मोगा"),
            ("Kapurthala", "कपूरथला"),
            ("Sangrur", "संगरूर"),
            ("Firozpur", "फिरोजपुर"),
            ("Gurdaspur", "गुरदासपुर"),
            ("Anandpur Sahib", "आनंदपुर साहिब")
        ]
    },
    {
        "state_en": "Uttarakhand",
        "state_hi": "उत्तराखंड",
        "cities": [
            ("Haridwar", "हरिद्वार"),
            ("Rishikesh", "ऋषिकेश"),
            ("Dehradun", "देहरादून"),
            ("Haldwani", "हल्द्वानी"),
            ("Nainital", "नैनीताल"),
            ("Rudrapur", "रुद्रपुर"),
            ("Roorkee", "रुड़की"),
            ("Kashipur", "काशीपुर"),
            ("Almora", "अल्मोड़ा"),
            ("Pithoragarh", "पिथौरागढ़"),
            ("Srinagar Garhwal", "श्रीनगर गढ़वाल"),
            ("Uttarkashi", "उत्तरकाशी"),
            ("Badrinath", "बद्रीनाथ"),
            ("Kedarnath", "केदारनाथ")
        ]
    },
    {
        "state_en": "Himachal Pradesh",
        "state_hi": "हिमाचल प्रदेश",
        "cities": [
            ("Shimla", "शिमला"),
            ("Manali", "मनाली"),
            ("Dharamshala", "धर्मशाला"),
            ("Mandi", "मंडी"),
            ("Kullu", "कुल्लू"),
            ("Solan", "सोलन"),
            ("Hamirpur", "हमीरपुर"),
            ("Una", "ऊना"),
            ("Chamba", "चंबा"),
            ("Bilaspur HP", "बिलासपुर"),
            ("Kangra", "कांगड़ा"),
            ("Palampur", "पालमपुर")
        ]
    },
    {
        "state_en": "West Bengal",
        "state_hi": "पश्चिम बंगाल",
        "cities": [
            ("Kolkata", "कोलकाता"),
            ("Howrah", "हावड़ा"),
            ("Siliguri", "सिलीगुड़ी"),
            ("Durgapur", "दुर्गापुर"),
            ("Asansol", "आसनसोल"),
            ("Bardhaman", "बर्धमान"),
            ("Kharagpur", "खड़गपुर"),
            ("Haldia", "हल्दिया"),
            ("Malda", "मालदा"),
            ("Darjeeling", "दार्जिलिंग"),
            ("Jalpaiguri", "जलपाईगुड़ी"),
            ("Krishnanagar", "कृष्णनगर")
        ]
    },
    {
        "state_en": "Odisha",
        "state_hi": "ओडिशा",
        "cities": [
            ("Bhubaneswar", "भुवनेश्वर"),
            ("Puri", "पुरी"),
            ("Cuttack", "कटक"),
            ("Rourkela", "राउरकेला"),
            ("Sambalpur", "संबलपुर"),
            ("Berhampur", "ब्रह्मपुर"),
            ("Balasore", "बालासोर"),
            ("Bhadrak", "भद्रक"),
            ("Jharsuguda", "झारसुगुड़ा"),
            ("Konark", "कोणार्क"),
            ("Angul", "अंगुल")
        ]
    },
    {
        "state_en": "Chhattisgarh",
        "state_hi": "छत्तीसगढ़",
        "cities": [
            ("Raipur", "रायपुर"),
            ("Bilaspur CG", "बिलासपुर"),
            ("Durg", "दुर्ग"),
            ("Bhilai", "भिलाई"),
            ("Korba", "कोरबा"),
            ("Raigarh", "रायगढ़"),
            ("Jagdalpur", "जगदलपुर"),
            ("Ambikapur", "अंबिकापुर"),
            ("Rajnandgaon", "राजनांदगांव"),
            ("Dhamtari", "धमतरी")
        ]
    },
    {
        "state_en": "Andhra Pradesh",
        "state_hi": "आंध्र प्रदेश",
        "cities": [
            ("Visakhapatnam", "विशाखापत्तनम"),
            ("Vijayawada", "विजयवाड़ा"),
            ("Tirupati", "तिरुपति"),
            ("Guntur", "गुंटूर"),
            ("Nellore", "नेल्लोर"),
            ("Kurnool", "कुरनूल"),
            ("Rajahmundry", "राजमुंदरी"),
            ("Kakinada", "काकीनाडा"),
            ("Anantapur", "अनंतपुर"),
            ("Kadapa", "कडपा"),
            ("Amaravati", "अमरावती"),
            ("Srikakulam", "श्रीकाकुलम")
        ]
    },
    {
        "state_en": "Telangana",
        "state_hi": "तेलंगाना",
        "cities": [
            ("Hyderabad", "हैदराबाद"),
            ("Warangal", "वारंगल"),
            ("Karimnagar", "करीमनगर"),
            ("Nizamabad", "निज़ामाबाद"),
            ("Khammam", "खम्मम"),
            ("Nalgonda", "नलगोंडा"),
            ("Mahbubnagar", "महबूबनगर"),
            ("Siddipet", "सिद्दीपेट"),
            ("Suryapet", "सूर्यपेट")
        ]
    },
    {
        "state_en": "Karnataka",
        "state_hi": "कर्नाटक",
        "cities": [
            ("Bengaluru", "बेंगलुरु"),
            ("Mysuru", "मैसूरु"),
            ("Mangaluru", "मंगलुरु"),
            ("Hubballi", "हुबली"),
            ("Dharwad", "धारवाड़"),
            ("Belagavi", "बेलगावी"),
            ("Kalaburagi", "कलबुर्गी"),
            ("Shivamogga", "शिवमोग्गा"),
            ("Davanagere", "दावणगेरे"),
            ("Ballari", "बल्लारी"),
            ("Udupi", "उडुपी"),
            ("Vijayapura", "विजयपुरा")
        ]
    },
    {
        "state_en": "Tamil Nadu",
        "state_hi": "तमिलनाडु",
        "cities": [
            ("Chennai", "चेन्नई"),
            ("Coimbatore", "कोयंबटूर"),
            ("Madurai", "मदुरै"),
            ("Tiruchirappalli", "तिरुचिरापल्ली"),
            ("Salem", "सलेम"),
            ("Tirunelveli", "तिरुनेलवेली"),
            ("Erode", "इरोड"),
            ("Vellore", "वेल्लोर"),
            ("Thanjavur", "तंजावुर"),
            ("Kanchipuram", "कांचीपुरम"),
            ("Rameswaram", "रामेश्वरम"),
            ("Kanyakumari", "कन्याकुमारी"),
            ("Tiruvannamalai", "तिरुवन्नामलाई"),
            ("Kumbakonam", "कुंभकोणम")
        ]
    },
    {
        "state_en": "Kerala",
        "state_hi": "केरल",
        "cities": [
            ("Kochi", "कोच्चि"),
            ("Thiruvananthapuram", "तिरुवनंतपुरम"),
            ("Kozhikode", "कोझिकोड"),
            ("Thrissur", "त्रिशूर"),
            ("Kollam", "कोल्लम"),
            ("Kannur", "कन्नूर"),
            ("Palakkad", "पालक्काड़"),
            ("Alappuzha", "अलप्पुझा"),
            ("Kottayam", "कोट्टायम"),
            ("Guruvayur", "गुरुवायूर"),
            ("Munnar", "मुन्नार")
        ]
    },
    {
        "state_en": "Goa",
        "state_hi": "गोवा",
        "cities": [
            ("Panaji", "पणजी"),
            ("Margao", "मडगांव"),
            ("Vasco da Gama", "वास्को द गामा"),
            ("Mapusa", "मापुसा"),
            ("Ponda", "पोंडा")
        ]
    },
    {
        "state_en": "Assam",
        "state_hi": "असम",
        "cities": [
            ("Guwahati", "गुवाहाटी"),
            ("Dibrugarh", "डिब्रूगढ़"),
            ("Silchar", "सिलचर"),
            ("Jorhat", "जोरहाट"),
            ("Tezpur", "तेजपुर"),
            ("Tinsukia", "तिनसुकिया"),
            ("Nagaon", "नगांव"),
            ("Sivasagar", "शिवसागर")
        ]
    },
    {
        "state_en": "Arunachal Pradesh",
        "state_hi": "अरुणाचल प्रदेश",
        "cities": [
            ("Itanagar", "ईटानगर"),
            ("Naharlagun", "नाहरलगुन"),
            ("Tawang", "तवांग"),
            ("Pasighat", "पासीघाट"),
            ("Ziro", "जीरो"),
            ("Bomdila", "बोमडिला")
        ]
    },
    {
        "state_en": "Meghalaya",
        "state_hi": "मेघालय",
        "cities": [
            ("Shillong", "शिलांग"),
            ("Tura", "तुरा"),
            ("Jowai", "जोवाई"),
            ("Nongpoh", "नोंगपोह")
        ]
    },
    {
        "state_en": "Manipur",
        "state_hi": "मणिपुर",
        "cities": [
            ("Imphal", "इम्फाल"),
            ("Thoubal", "थौबल"),
            ("Churachandpur", "चुराचांदपुर"),
            ("Bishnupur", "बिष्णुपुर")
        ]
    },
    {
        "state_en": "Mizoram",
        "state_hi": "मिजोरम",
        "cities": [
            ("Aizawl", "आइजोल"),
            ("Lunglei", "लुंगलेई"),
            ("Champhai", "चम्फाई"),
            ("Kolasib", "कोलासिब")
        ]
    },
    {
        "state_en": "Nagaland",
        "state_hi": "नागालैंड",
        "cities": [
            ("Kohima", "कोहिमा"),
            ("Dimapur", "दीमापुर"),
            ("Mokokchung", "मोकोकचुंग"),
            ("Wokha", "वोखा")
        ]
    },
    {
        "state_en": "Tripura",
        "state_hi": "त्रिपुरा",
        "cities": [
            ("Agartala", "अगरतला"),
            ("Udaipur Tripura", "उदयपुर"),
            ("Dharmanagar", "धर्मनगर"),
            ("Kailashahar", "कैलाशहर")
        ]
    },
    {
        "state_en": "Sikkim",
        "state_hi": "सिक्किम",
        "cities": [
            ("Gangtok", "गंगटोक"),
            ("Namchi", "नामची"),
            ("Gyalshing", "ग्यालशिंग"),
            ("Mangan", "मंगन")
        ]
    },
    {
        "state_en": "Jammu and Kashmir",
        "state_hi": "जम्मू और कश्मीर",
        "cities": [
            ("Srinagar", "श्रीनगर"),
            ("Jammu", "जम्मू"),
            ("Anantnag", "अनंतनाग"),
            ("Baramulla", "बारामूला"),
            ("Udhampur", "उधमपुर"),
            ("Kathua", "कठुआ"),
            ("Pulwama", "पुलवामा"),
            ("Sopore", "सोपोर")
        ]
    },
    {
        "state_en": "Ladakh",
        "state_hi": "लद्दाख",
        "cities": [
            ("Leh", "लेह"),
            ("Kargil", "कारगिल")
        ]
    },
    {
        "state_en": "Chandigarh",
        "state_hi": "चंडीगढ़",
        "cities": [
            ("Chandigarh", "चंडीगढ़")
        ]
    },
    {
        "state_en": "Puducherry",
        "state_hi": "पुडुचेरी",
        "cities": [
            ("Puducherry", "पुडुचेरी"),
            ("Karaikal", "कराईकल"),
            ("Yanam", "यानम"),
            ("Mahe", "माहे")
        ]
    },
    {
        "state_en": "Andaman and Nicobar Islands",
        "state_hi": "अंडमान और निकोबार",
        "cities": [
            ("Port Blair", "पोर्ट ब्लेयर (श्री विजय पुरम)"),
            ("Diglipur", "डिगलीपुर")
        ]
    },
    {
        "state_en": "Lakshadweep",
        "state_hi": "लक्षद्वीप",
        "cities": [
            ("Kavaratti", "कवरत्ती"),
            ("Agatti", "अगाती"),
            ("Minicoy", "मिनिकॉय")
        ]
    },
    {
        "state_en": "Dadra and Nagar Haveli",
        "state_hi": "दादरा और नगर हवेली",
        "cities": [
            ("Silvassa", "सिलवासा")
        ]
    },
    {
        "state_en": "Daman and Diu",
        "state_hi": "दमन और दीव",
        "cities": [
            ("Daman", "दमन"),
            ("Diu", "दीव")
        ]
    },
    {
        "state_en": "International NRI",
        "state_hi": "अंतरराष्ट्रीय प्रवासी भारतीय (NRI)",
        "cities": [
            ("Dubai", "दुबई"),
            ("Abu Dhabi", "अबू धाबी"),
            ("London", "लंदन"),
            ("New York", "न्यूयॉर्क"),
            ("California", "कैलिफोर्निया"),
            ("New Jersey", "न्यू जर्सी"),
            ("Texas", "टेक्सास"),
            ("Toronto", "टोरंटो"),
            ("Vancouver", "वैंकूवर"),
            ("Sydney", "सिडनी"),
            ("Melbourne", "मेलबर्न"),
            ("Kathmandu", "काठमांडू"),
            ("Singapore", "सिंगापुर"),
            ("Mauritius", "मॉरीशस")
        ]
    }
]

def slugify(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9]+', '-', text)
    return text.strip('-')

print(f"Total States/UTs: {len(LOCATIONS_DATA)}")
total_cities = sum(len(s['cities']) for s in LOCATIONS_DATA)
print(f"Total Cities: {total_cities}")

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), 'puja-in')
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Generate unique slug for each city, taking state into account if collisions occur
city_slug_map = {}
all_cities_flat = []

for state in LOCATIONS_DATA:
    state_en = state['state_en']
    state_hi = state['state_hi']
    for city_en, city_hi in state['cities']:
        base_slug = slugify(city_en)
        # handle duplicate city names like Chitrakoot (MP and UP), Bilaspur (HP and CG)
        slug = base_slug
        if slug in city_slug_map:
            slug = f"{base_slug}-{slugify(state_en)}"
        city_slug_map[slug] = {
            'city_en': city_en,
            'city_hi': city_hi,
            'state_en': state_en,
            'state_hi': state_hi,
            'slug': slug
        }
        all_cities_flat.append(city_slug_map[slug])

print(f"Total city pages to generate: {len(all_cities_flat)}")

# Template generator
def generate_city_html(city_info, state_sibling_cities):
    c_hi = city_info['city_hi']
    c_en = city_info['city_en']
    s_hi = city_info['state_hi']
    s_en = city_info['state_en']
    slug = city_info['slug']

    # Contextual copy for metro, pilgrimage, or regular city
    pilgrimage_keywords = ['Ujjain', 'Varanasi', 'Ayodhya', 'Haridwar', 'Rishikesh', 'Mathura', 'Vrindavan', 'Dwarka', 'Somnath', 'Puri', 'Tirupati', 'Rameswaram', 'Pushkar', 'Badrinath', 'Kedarnath', 'Deoghar', 'Gaya', 'Omkareshwar', 'Maihar', 'Chitrakoot', 'Shirdi', 'Nathdwara', 'Khatu', 'Salasar', 'Sehore', 'Narmadapuram', 'Pehowa', 'Ambaji', 'Buxar', 'Jhunjhunu', 'Salangpur']
    metro_keywords = ['Mumbai', 'Delhi', 'New Delhi', 'Bengaluru', 'Hyderabad', 'Ahmedabad', 'Chennai', 'Kolkata', 'Pune', 'Noida', 'Gurugram', 'Ghaziabad', 'Jaipur', 'Lucknow', 'Kanpur', 'Indore', 'Bhopal', 'Surat', 'Nagpur', 'Chandigarh']

    if s_en == "International NRI":
        city_badge = f"NRI Devotees • {c_en} Live Puja & Havan Service"
        special_intro = f"Devotees and NRIs residing in {c_en} can now book authentic Vedic Maa Baglamukhi Puja and Havan directly from the ancient Siddhapeeth Maa Baglamukhi Dham, Nalkheda via live video call (WhatsApp / Zoom) with Pandit Harshit Sharma with personalized name and gotra sankalp."
    elif any(k.lower() in c_en.lower() for k in pilgrimage_keywords):
        city_badge = f"Devotees in {c_en} • Special Maa Baglamukhi Puja & Havan"
        special_intro = f"Devotees in the holy city of {c_en} seeking divine blessings can now connect directly with Pandit Harshit Sharma at Maa Baglamukhi Dham Nalkheda for sacred Vedic rituals, court case victory, enemy protection, and family peace."
    elif any(k.lower() in c_en.lower() for k in metro_keywords):
        city_badge = f"Live Sankalp & Vedic Puja Service for {c_en}"
        special_intro = f"For residents and professionals in {c_en} facing career stress, legal disputes, hidden enemies, or business obstacles, Pandit Harshit Sharma conducts authentic Maa Baglamukhi Vedic Havan and Graha Shanti rituals directly from Nalkheda Dham."
    else:
        city_badge = f"Special Vedic Puja & Havan Service in {c_en} ({s_en})"
        special_intro = f"Devotees in {c_en} and nearby regions can now book sacred Maa Baglamukhi Puja, Havan, and astrological consultations directly from Maa Baglamukhi Dham Nalkheda with Pandit Harshit Sharma."

    # State siblings links (up to 8 other cities in the same state)
    sibling_links_html = ""
    for sib in state_sibling_cities:
        if sib['slug'] != slug:
            sibling_links_html += f'''
            <a href="{sib['slug']}.html" class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-full bg-[#f8f3e8] hover:bg-[#ffdcc3] text-[#8d4b00] text-xs font-semibold border border-[#dbc2b0] transition-colors">
              <span class="material-symbols-outlined text-[14px]">location_on</span>
              <span>{sib['city_en']}</span>
            </a>'''

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8"/>
  <meta content="width=device-width, initial-scale=1.0" name="viewport"/>
  <title>Best Pandit in {c_en} | Maa Baglamukhi Puja & Havan Booking in {c_en} - Pandit Harshit Sharma</title>
  <meta name="description" content="Looking for the best pandit in {c_en}? Book authentic Vedic Maa Baglamukhi Puja & Havan in {c_en} ({s_en}) with Pandit Harshit Sharma from Nalkheda Dham. Live video sankalp, court case victory, business growth. Call: +91 87690 84789."/>
  <meta name="keywords" content="Best Pandit in {c_en}, Pandit in {c_en}, Havan Booking in {c_en}, Maa Baglamukhi Puja in {c_en}, Famous Pandit in {c_en}, Puja Booking {c_en}, Pandit Harshit Sharma Nalkheda"/>
  <link rel="canonical" href="https://www.baglamukhi-puja.in/puja-in/{slug}.html"/>

  <!-- Open Graph / Facebook -->
  <meta property="og:type" content="website"/>
  <meta property="og:url" content="https://www.baglamukhi-puja.in/puja-in/{slug}.html"/>
  <meta property="og:title" content="Best Pandit in {c_en} | Maa Baglamukhi Puja & Havan Booking - Pandit Harshit Sharma"/>
  <meta property="og:description" content="Authentic Vedic Maa Baglamukhi Puja and Havan for devotees in {c_en} via live video sankalp from Siddhapeeth Nalkheda Dham with Pandit Harshit Sharma."/>
  <meta property="og:image" content="https://www.baglamukhi-puja.in/logo.webp"/>

  <link rel="icon" type="image/jpeg" href="../logo.webp"/>
  <link href="https://fonts.googleapis.com" rel="preconnect"/>
  <link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/>
  <link rel="preload" href="https://fonts.googleapis.com/css2?family=Noto+Serif:ital,wght@0,400..700;1,400..700&amp;family=Plus+Jakarta+Sans:ital,wght@0,400..800;1,400..800&amp;display=swap" as="style" onload="this.onload=null;this.rel='stylesheet'"/>
  <noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Serif:ital,wght@0,400..700;1,400..700&amp;family=Plus+Jakarta+Sans:ital,wght@0,400..800;1,400..800&amp;display=swap"/></noscript>
  <link rel="preload" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght@400&amp;display=swap" as="style" onload="this.onload=null;this.rel='stylesheet'"/>
  <noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght@400&amp;display=swap"/></noscript>
  <link rel="stylesheet" href="../style.css" />

  <!-- Schema.org JSON-LD -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "PlaceOfWorship",
    "name": "Pandit Harshit Sharma - Best Pandit in {c_en} | Maa Baglamukhi Puja Service",
    "image": "https://www.baglamukhi-puja.in/logo.webp",
    "telephone": "+918769084789",
    "address": {{
      "@type": "PostalAddress",
      "addressLocality": "{c_en}",
      "addressRegion": "{s_en}",
      "addressCountry": "IN"
    }},
    "url": "https://www.baglamukhi-puja.in/puja-in/{slug}.html",
    "priceRange": "₹₹",
    "description": "Authentic Vedic Maa Baglamukhi Puja, Havan, and astrological consultation for devotees in {c_en} ({s_en}) performed by Pandit Harshit Sharma from Maa Baglamukhi Dham Nalkheda."
  }}
  </script>
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
      {{
        "@type": "ListItem",
        "position": 1,
        "name": "Home",
        "item": "https://www.baglamukhi-puja.in/"
      }},
      {{
        "@type": "ListItem",
        "position": 2,
        "name": "All Cities",
        "item": "https://www.baglamukhi-puja.in/locations.html"
      }},
      {{
        "@type": "ListItem",
        "position": 3,
        "name": "Puja in {c_en}",
        "item": "https://www.baglamukhi-puja.in/puja-in/{slug}.html"
      }}
    ]
  }}
  </script>
</head>

<body class="bg-[#fef9ee] font-['Plus_Jakarta_Sans',sans-serif] text-[#1d1c15] overflow-x-hidden">

  <!-- TOP BAR -->
  <header class="fixed top-0 w-full z-50 bg-[#fef9ee]/95 backdrop-blur-xl shadow-[0_4px_20px_-2px_rgba(180,83,9,0.08)]">
    <div class="bg-[#a53936] text-white px-4 md:px-8 py-2 text-center">
      <div class="max-w-[1200px] mx-auto flex flex-col md:flex-row items-center justify-between gap-1 text-xs">
        <div class="flex items-center gap-2">
          <span class="flex h-2 w-2 relative">
            <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-[#ffdad7] opacity-75"></span>
            <span class="relative inline-flex rounded-full h-2 w-2 bg-[#ffdad7]"></span>
          </span>
          <span>World Renowned Ancient Siddhapeeth • Nalkheda (M.P.) | Special Service for {c_en}</span>
        </div>
        <div class="flex items-center gap-4">
          <a href="tel:+918769084789" class="flex items-center gap-1 hover:text-[#ffdad7]">
            <span class="material-symbols-outlined text-[14px]">call</span>
            <span class="font-bold">+91 87690 84789</span>
          </a>
          <a href="https://wa.me/918769084789?text=Hello%20Pandit%20Ji,%20I%20am%20from%20{c_en}%20and%20would%20like%20information%20regarding%20Puja%20booking." target="_blank" class="flex items-center gap-1 text-[#95f8a7] font-bold hover:underline">
            <span>WhatsApp Us</span>
          </a>
        </div>
      </div>
    </div>

    <!-- MAIN NAVBAR -->
    <div class="h-20 max-w-[1200px] mx-auto px-4 md:px-8 flex items-center justify-between gap-2">
      <a href="/" class="flex items-center gap-3">
        <img src="../logo.webp" alt="Pandit Harshit Sharma" class="w-11 h-11 md:w-13 md:h-13 rounded-full object-cover shadow-md border-2 border-[#b15f00]"/>
        <div class="flex flex-col">
          <span class="font-['Noto_Serif',serif] font-bold text-base md:text-xl text-[#8d4b00] leading-tight">Pandit Harshit Sharma</span>
          <span class="text-[11px] text-[#a53936] font-semibold tracking-wide">Maa Baglamukhi Dham Nalkheda</span>
        </div>
      </a>

      <nav class="hidden md:flex items-center gap-6 text-sm font-semibold text-[#554336]">
        <a class="hover:text-[#8d4b00] transition-colors" href="/">Home</a>
        <a class="hover:text-[#8d4b00] transition-colors" href="../services.html">Services</a>
        <a class="hover:text-[#8d4b00] transition-colors" href="../gallery.html">Gallery</a>
        <a class="text-[#8d4b00] font-bold border-b-2 border-[#8d4b00] pb-0.5" href="../locations.html">All Cities ({s_en})</a>
        <a class="hover:text-[#8d4b00] transition-colors" href="../contact.html">Contact</a>
      </nav>

      <div class="flex items-center gap-2">
        <a href="tel:+918769084789" class="hidden sm:inline-flex items-center gap-1.5 px-4 py-2 rounded-full bg-[#8d4b00] text-white text-xs font-bold shadow-md hover:bg-[#b15f00] transition-all">
          <span class="material-symbols-outlined text-[16px]">call</span>
          <span>Consult Now</span>
        </a>
        <a href="../locations.html" class="inline-flex md:hidden items-center gap-1 px-3 py-1.5 rounded-full bg-[#f8f3e8] border border-[#dbc2b0] text-[#8d4b00] text-xs font-bold">
          <span class="material-symbols-outlined text-[15px]">explore</span>
          <span>Cities</span>
        </a>
      </div>
    </div>
  </header>

  <!-- MAIN WRAPPER -->
  <main class="w-full pt-28 md:pt-32">

    <!-- BREADCRUMB -->
    <div class="bg-[#f2ede3] border-b border-[#dbc2b0]/50 py-2.5 px-4 md:px-8">
      <div class="max-w-[1200px] mx-auto flex items-center gap-2 text-xs text-[#554336]">
        <a href="/" class="hover:text-[#8d4b00]">Home</a>
        <span>/</span>
        <a href="../locations.html" class="hover:text-[#8d4b00]">Locations Directory</a>
        <span>/</span>
        <span class="text-[#554336]">{s_en}</span>
        <span>/</span>
        <span class="text-[#8d4b00] font-bold">{c_en}</span>
      </div>
    </div>

    <!-- HERO SECTION -->
    <section class="relative bg-gradient-to-b from-[#f2ede3] via-[#fef9ee] to-[#fef9ee] px-4 md:px-8 pt-10 pb-16 overflow-hidden">
      <!-- Glow Halos -->
      <div class="absolute top-0 right-10 w-96 h-96 bg-[#ffdcc3]/40 rounded-full blur-3xl pointer-events-none"></div>
      <div class="absolute bottom-0 left-10 w-80 h-80 bg-[#ffdad7]/30 rounded-full blur-3xl pointer-events-none"></div>

      <div class="max-w-[1200px] mx-auto relative z-10">
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-center">
          
          <!-- Left Hero Column -->
          <div class="lg:col-span-7 flex flex-col gap-4">
            <div class="inline-flex items-center gap-2 self-start px-3.5 py-1.5 rounded-full bg-[#ffdcc3] text-[#2f1500] text-xs font-bold shadow-sm">
              <span class="material-symbols-outlined text-[#8d4b00] text-[16px]">verified</span>
              <span>{city_badge}</span>
            </div>

            <h1 class="font-['Noto_Serif',serif] text-2xl sm:text-3xl lg:text-4xl font-bold text-[#8d4b00] leading-tight">
              Best Pandit in {c_en} - Vedic Maa Baglamukhi Puja & Havan Booking
            </h1>

            <p class="text-sm md:text-base text-[#554336] leading-relaxed">
              {special_intro} If you or your family are troubled by <strong>court cases & legal disputes</strong>, <strong>hidden enemies & rivalry</strong>, <strong>planetary doshas (Graha Shanti)</strong>, or <strong>financial & business slowdowns</strong>, book authentic Vedic Anushthan performed strictly with personalized name and gotra from the sacred Maa Baglamukhi Siddhapeeth Nalkheda.
            </p>

            <!-- Trust Points -->
            <div class="grid grid-cols-2 sm:grid-cols-3 gap-2.5 pt-2">
              <div class="flex items-center gap-2 bg-white/80 p-2.5 rounded-lg border border-[#dbc2b0]/50 shadow-sm">
                <span class="material-symbols-outlined text-[#006b2f] text-[20px]">videocam</span>
                <span class="text-xs font-bold text-[#1d1c15]">Live Video Sankalp</span>
              </div>
              <div class="flex items-center gap-2 bg-white/80 p-2.5 rounded-lg border border-[#dbc2b0]/50 shadow-sm">
                <span class="material-symbols-outlined text-[#8d4b00] text-[20px]">mark_email_read</span>
                <span class="text-xs font-bold text-[#1d1c15]">Prasad Delivery to {c_en}</span>
              </div>
              <div class="flex items-center gap-2 bg-white/80 p-2.5 rounded-lg border border-[#dbc2b0]/50 shadow-sm col-span-2 sm:col-span-1">
                <span class="material-symbols-outlined text-[#a53936] text-[20px]">local_fire_department</span>
                <span class="text-xs font-bold text-[#1d1c15]">100% Satvik Vedic Havan</span>
              </div>
            </div>

            <!-- CTAs -->
            <div class="flex flex-wrap items-center gap-3 pt-3">
              <a href="tel:+918769084789" class="inline-flex items-center gap-2 px-6 py-3 rounded-full bg-[#8d4b00] text-white font-bold text-sm shadow-[0_4px_16px_rgba(141,75,0,0.3)] hover:bg-[#b15f00] transition-all transform hover:-translate-y-0.5">
                <span class="material-symbols-outlined text-[18px]">call</span>
                <span>Call Pandit Ji: +91 87690 84789</span>
              </a>
              <a href="https://wa.me/918769084789?text=Hello%20Pandit%20Ji,%20I%20am%20from%20{c_en}%20and%20want%20to%20book%20a%20Sankalp%20for%20Puja." target="_blank" class="inline-flex items-center gap-2 px-6 py-3 rounded-full bg-[#006b2f] text-white font-bold text-sm shadow-[0_4px_16px_rgba(0,107,47,0.25)] hover:bg-[#1e8642] transition-all transform hover:-translate-y-0.5">
                <span class="material-symbols-outlined text-[18px]">chat</span>
                <span>Book Sankalp on WhatsApp</span>
              </a>
            </div>
          </div>

          <!-- Right Hero Column (Images & Pandit Harshit Sharma Intro) -->
          <div class="lg:col-span-5 flex flex-col gap-4">
            <div class="relative bg-white rounded-2xl p-4 shadow-xl border border-[#dbc2b0]/60">
              <img src="../priest_chanting.webp" alt="Pandit Harshit Sharma Vedic Anushthan" class="w-full h-56 object-cover rounded-xl shadow-md"/>
              <div class="absolute -bottom-3 -right-3 bg-[#a53936] text-white px-4 py-2 rounded-xl shadow-lg flex items-center gap-2">
                <span class="material-symbols-outlined text-[20px]">workspace_premium</span>
                <span class="text-xs font-bold">15+ Years Vedic Experience</span>
              </div>
            </div>
            
            <div class="bg-[#f8f3e8] rounded-xl p-3.5 border border-[#dbc2b0] flex items-center gap-3">
              <img src="../logo.webp" alt="Logo" class="w-12 h-12 rounded-full object-cover border border-[#8d4b00]"/>
              <div class="text-xs text-[#554336] leading-tight">
                <p class="font-bold text-[#8d4b00] text-sm">Pandit Harshit Sharma</p>
                <p>Maa Baglamukhi Dham, Lakhundar River Bank, Nalkheda (M.P.)</p>
                <p class="text-[11px] text-[#006b2f] font-semibold mt-0.5">● 24x7 Dedicated Guidance for Devotees in {c_en}</p>
              </div>
            </div>
          </div>

        </div>
      </div>
    </section>

    <!-- SECTION 2: 6 SPECIAL PUJAS OFFERED FOR THIS CITY -->
    <section class="py-14 px-4 md:px-8 bg-white border-y border-[#dbc2b0]/40">
      <div class="max-w-[1200px] mx-auto">
        <div class="text-center max-w-2xl mx-auto mb-10">
          <span class="text-[#a53936] font-bold text-xs uppercase tracking-widest">VEDIC SOLUTIONS</span>
          <h2 class="font-['Noto_Serif',serif] text-2xl md:text-3xl font-bold text-[#8d4b00] mt-1">
            Special Puja & Havan Services for Devotees in {c_en}
          </h2>
          <p class="text-xs md:text-sm text-[#554336] mt-2">
            Every ritual is conducted strictly adhering to Vedic scriptures, complete satvik havan samagri, and personal name-gotra sankalp.
          </p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">

          <!-- Card 1 -->
          <div class="bg-[#fef9ee] rounded-2xl p-5 border border-[#dbc2b0] hover:shadow-lg transition-all flex flex-col justify-between">
            <div>
              <div class="w-12 h-12 rounded-xl bg-[#ffdcc3] text-[#8d4b00] flex items-center justify-center mb-3">
                <span class="material-symbols-outlined text-[26px]">gavel</span>
              </div>
              <h3 class="font-['Noto_Serif',serif] font-bold text-lg text-[#1d1c15] mb-2">Maa Baglamukhi Shatru Vijay & Court Case Victory Puja</h3>
              <p class="text-xs text-[#554336] leading-relaxed mb-4">
                Powerful Pitambara Mahamantra samput havan for victory in court disputes, neutralization of hidden enemies, and relief from false litigation.
              </p>
            </div>
            <a href="https://wa.me/918769084789?text=Hello%20Pandit%20Ji,%20I%20want%20to%20book%20Shatru%20Vijay%20Court%20Case%20Puja%20for%20{c_en}." target="_blank" class="inline-flex items-center justify-center gap-1.5 w-full py-2 rounded-lg bg-[#8d4b00] text-white text-xs font-bold hover:bg-[#b15f00] transition-colors">
              <span>Book Sankalp</span>
              <span class="material-symbols-outlined text-[15px]">arrow_forward</span>
            </a>
          </div>

          <!-- Card 2 -->
          <div class="bg-[#fef9ee] rounded-2xl p-5 border border-[#dbc2b0] hover:shadow-lg transition-all flex flex-col justify-between">
            <div>
              <div class="w-12 h-12 rounded-xl bg-[#ffdcc3] text-[#8d4b00] flex items-center justify-center mb-3">
                <span class="material-symbols-outlined text-[26px]">paid</span>
              </div>
              <h3 class="font-['Noto_Serif',serif] font-bold text-lg text-[#1d1c15] mb-2">Vyapar Vriddhi, Debt Relief & Kanakdhara Puja</h3>
              <p class="text-xs text-[#554336] leading-relaxed mb-4">
                Special Lakshmi-Kuber and Baglamukhi rituals to overcome persistent business losses, heavy debt, financial blockage, and recover trapped funds.
              </p>
            </div>
            <a href="https://wa.me/918769084789?text=Hello%20Pandit%20Ji,%20I%20want%20to%20book%20Vyapar%20Vriddhi%20Puja%20for%20{c_en}." target="_blank" class="inline-flex items-center justify-center gap-1.5 w-full py-2 rounded-lg bg-[#8d4b00] text-white text-xs font-bold hover:bg-[#b15f00] transition-colors">
              <span>Book Sankalp</span>
              <span class="material-symbols-outlined text-[15px]">arrow_forward</span>
            </a>
          </div>

          <!-- Card 3 -->
          <div class="bg-[#fef9ee] rounded-2xl p-5 border border-[#dbc2b0] hover:shadow-lg transition-all flex flex-col justify-between">
            <div>
              <div class="w-12 h-12 rounded-xl bg-[#ffdcc3] text-[#8d4b00] flex items-center justify-center mb-3">
                <span class="material-symbols-outlined text-[26px]">brightness_7</span>
              </div>
              <h3 class="font-['Noto_Serif',serif] font-bold text-lg text-[#1d1c15] mb-2">Navgrah Shanti & Kaal Sarp Dosh Nivaran Havan</h3>
              <p class="text-xs text-[#554336] leading-relaxed mb-4">
                Vedic planetary yajna to pacify malefic influences of Rahu, Ketu, Shani Sade Sati, Kaal Sarp Dosh, and Manglik Dosh to restore life balance.
              </p>
            </div>
            <a href="https://wa.me/918769084789?text=Hello%20Pandit%20Ji,%20I%20want%20to%20book%20Navgrah%20Shanti%20Puja%20for%20{c_en}." target="_blank" class="inline-flex items-center justify-center gap-1.5 w-full py-2 rounded-lg bg-[#8d4b00] text-white text-xs font-bold hover:bg-[#b15f00] transition-colors">
              <span>Book Sankalp</span>
              <span class="material-symbols-outlined text-[15px]">arrow_forward</span>
            </a>
          </div>

          <!-- Card 4 -->
          <div class="bg-[#fef9ee] rounded-2xl p-5 border border-[#dbc2b0] hover:shadow-lg transition-all flex flex-col justify-between">
            <div>
              <div class="w-12 h-12 rounded-xl bg-[#ffdcc3] text-[#8d4b00] flex items-center justify-center mb-3">
                <span class="material-symbols-outlined text-[26px]">health_and_safety</span>
              </div>
              <h3 class="font-['Noto_Serif',serif] font-bold text-lg text-[#1d1c15] mb-2">Maha Mrityunjaya Jaap & Ayushya Havan</h3>
              <p class="text-xs text-[#554336] leading-relaxed mb-4">
                Sacred 125,000 Maha Mrityunjaya mantra chanting and yajna for protection from severe chronic illnesses, accidental perils, and longevity of loved ones.
              </p>
            </div>
            <a href="https://wa.me/918769084789?text=Hello%20Pandit%20Ji,%20I%20want%20to%20book%20Maha%20Mrityunjaya%20Jaap%20for%20{c_en}." target="_blank" class="inline-flex items-center justify-center gap-1.5 w-full py-2 rounded-lg bg-[#8d4b00] text-white text-xs font-bold hover:bg-[#b15f00] transition-colors">
              <span>Book Sankalp</span>
              <span class="material-symbols-outlined text-[15px]">arrow_forward</span>
            </a>
          </div>

          <!-- Card 5 -->
          <div class="bg-[#fef9ee] rounded-2xl p-5 border border-[#dbc2b0] hover:shadow-lg transition-all flex flex-col justify-between">
            <div>
              <div class="w-12 h-12 rounded-xl bg-[#ffdcc3] text-[#8d4b00] flex items-center justify-center mb-3">
                <span class="material-symbols-outlined text-[26px]">favorite</span>
              </div>
              <h3 class="font-['Noto_Serif',serif] font-bold text-lg text-[#1d1c15] mb-2">Early Marriage & Harmonious Marital Life Puja</h3>
              <p class="text-xs text-[#554336] leading-relaxed mb-4">
                Special Vedic remedies to remove repeated delays in marriage, eliminate marital friction, and foster harmonious relations between spouses.
              </p>
            </div>
            <a href="https://wa.me/918769084789?text=Hello%20Pandit%20Ji,%20I%20want%20to%20book%20Vivah%20Badha%20Nivaran%20Puja%20for%20{c_en}." target="_blank" class="inline-flex items-center justify-center gap-1.5 w-full py-2 rounded-lg bg-[#8d4b00] text-white text-xs font-bold hover:bg-[#b15f00] transition-colors">
              <span>Book Sankalp</span>
              <span class="material-symbols-outlined text-[15px]">arrow_forward</span>
            </a>
          </div>

          <!-- Card 6 -->
          <div class="bg-[#fef9ee] rounded-2xl p-5 border border-[#dbc2b0] hover:shadow-lg transition-all flex flex-col justify-between">
            <div>
              <div class="w-12 h-12 rounded-xl bg-[#ffdcc3] text-[#8d4b00] flex items-center justify-center mb-3">
                <span class="material-symbols-outlined text-[26px]">shield</span>
              </div>
              <h3 class="font-['Noto_Serif',serif] font-bold text-lg text-[#1d1c15] mb-2">Siddha Baglamukhi Raksha Kavach</h3>
              <p class="text-xs text-[#554336] leading-relaxed mb-4">
                Consecrated protective talisman charged with divine Maa Baglamukhi beej mantras to shield the wearer from negative energy, evil eye, and adversaries.
              </p>
            </div>
            <a href="https://wa.me/918769084789?text=Hello%20Pandit%20Ji,%20I%20want%20to%20order%20Siddha%20Baglamukhi%20Kavach%20for%20{c_en}." target="_blank" class="inline-flex items-center justify-center gap-1.5 w-full py-2 rounded-lg bg-[#8d4b00] text-white text-xs font-bold hover:bg-[#b15f00] transition-colors">
              <span>Order Kavach</span>
              <span class="material-symbols-outlined text-[15px]">arrow_forward</span>
            </a>
          </div>

        </div>
      </div>
    </section>

    <!-- SECTION 3: HOW IT WORKS FOR DEVOTEES IN THIS CITY (3 STEPS) -->
    <section class="py-14 px-4 md:px-8 bg-[#f8f3e8]">
      <div class="max-w-[1200px] mx-auto">
        <div class="text-center max-w-2xl mx-auto mb-12">
          <span class="text-[#a53936] font-bold text-xs uppercase tracking-widest">TRANSPARENT PROCESS</span>
          <h2 class="font-['Noto_Serif',serif] text-2xl md:text-3xl font-bold text-[#8d4b00] mt-1">
            3 Easy Steps to Book Online Puja & Sankalp from {c_en}
          </h2>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">

          <!-- Step 1 -->
          <div class="bg-white rounded-2xl p-6 border border-[#dbc2b0] shadow-sm relative flex flex-col items-center text-center">
            <div class="w-10 h-10 rounded-full bg-[#8d4b00] text-white flex items-center justify-center font-bold text-base mb-4">
              1
            </div>
            <h4 class="font-['Noto_Serif',serif] font-bold text-base text-[#1d1c15] mb-2">Share Details & Sankalp Request</h4>
            <p class="text-xs text-[#554336] leading-relaxed">
              Send your name, gotra, birth details (if available), and problem description to Pandit Ji via WhatsApp or direct phone call.
            </p>
          </div>

          <!-- Step 2 -->
          <div class="bg-white rounded-2xl p-6 border border-[#dbc2b0] shadow-sm relative flex flex-col items-center text-center">
            <div class="w-10 h-10 rounded-full bg-[#8d4b00] text-white flex items-center justify-center font-bold text-base mb-4">
              2
            </div>
            <h4 class="font-['Noto_Serif',serif] font-bold text-base text-[#1d1c15] mb-2">Live Video Darshan & Sacred Havan</h4>
            <p class="text-xs text-[#554336] leading-relaxed">
              At the designated auspicious muhurat, participate live via video call as your personalized sankalp and havan are performed before the sacred dhuni at Nalkheda Dham.
            </p>
          </div>

          <!-- Step 3 -->
          <div class="bg-white rounded-2xl p-6 border border-[#dbc2b0] shadow-sm relative flex flex-col items-center text-center">
            <div class="w-10 h-10 rounded-full bg-[#8d4b00] text-white flex items-center justify-center font-bold text-base mb-4">
              3
            </div>
            <h4 class="font-['Noto_Serif',serif] font-bold text-base text-[#1d1c15] mb-2">Receive Consecrated Prasad in {c_en}</h4>
            <p class="text-xs text-[#554336] leading-relaxed">
              Upon ritual completion, energized Raksha Sutra, sacred Bhasma, Maa's chunari, and prasadam are safely dispatched to your {c_en} address via Speed Post.
            </p>
          </div>

        </div>

        <!-- Banner inside Step Section -->
        <div class="mt-8 rounded-xl bg-[#ffdcc3]/50 border border-[#b15f00]/30 p-4 md:p-6 flex flex-col sm:flex-row items-center justify-between gap-4 text-center sm:text-left">
          <div class="flex items-center gap-3">
            <span class="material-symbols-outlined text-[#8d4b00] text-[32px]">support_agent</span>
            <div>
              <p class="font-bold text-[#8d4b00] text-sm md:text-base">Planning to visit Nalkheda Dham in person?</p>
              <p class="text-xs text-[#554336]">If you wish to travel from {c_en} to Maa Baglamukhi Dham Nalkheda, please contact us in advance to schedule your puja time and stay arrangements.</p>
            </div>
          </div>
          <a href="tel:+918769084789" class="px-5 py-2.5 rounded-full bg-[#8d4b00] text-white text-xs font-bold hover:bg-[#b15f00] transition-colors shrink-0 whitespace-nowrap">
            Plan Your Visit
          </a>
        </div>
      </div>
    </section>

    <!-- SECTION 4: LOCAL DEVOTEES TESTIMONIAL -->
    <section class="py-12 px-4 md:px-8 bg-white">
      <div class="max-w-[800px] mx-auto text-center">
        <div class="inline-flex items-center gap-1 text-[#b15f00] mb-2">
          <span class="material-symbols-outlined text-[18px]">star</span>
          <span class="material-symbols-outlined text-[18px]">star</span>
          <span class="material-symbols-outlined text-[18px]">star</span>
          <span class="material-symbols-outlined text-[18px]">star</span>
          <span class="material-symbols-outlined text-[18px]">star</span>
        </div>
        <blockquote class="font-['Noto_Serif',serif] text-base md:text-lg text-[#1d1c15] italic leading-relaxed">
          "Living in {c_en}, we consulted Pandit Harshit Sharma last month for an ongoing legal dispute. Pandit Ji conducted the Baglamukhi Anushthan with complete transparency via live video call, and we received the blessed prasad within 3 days. By Maa Baglamukhi's grace, the court decision was resolved completely in our favor."
        </blockquote>
        <div class="mt-4 flex items-center justify-center gap-2">
          <div class="w-8 h-8 rounded-full bg-[#ffdcc3] text-[#8d4b00] font-bold text-xs flex items-center justify-center">
            Devotee
          </div>
          <div class="text-left">
            <p class="text-xs font-bold text-[#1d1c15]">Satyendra Kumar & Family</p>
            <p class="text-[11px] text-[#554336]">Devotee • {c_en} ({s_en})</p>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 5: FAQS (ACCORDION) -->
    <section class="py-14 px-4 md:px-8 bg-[#f2ede3]">
      <div class="max-w-[850px] mx-auto">
        <div class="text-center mb-8">
          <span class="text-[#a53936] font-bold text-xs uppercase tracking-widest">COMMON QUESTIONS</span>
          <h2 class="font-['Noto_Serif',serif] text-2xl font-bold text-[#8d4b00] mt-1">
            Frequently Asked Questions About Puja in {c_en}
          </h2>
        </div>

        <div class="flex flex-col gap-3">

          <details class="bg-white rounded-xl p-4 border border-[#dbc2b0] shadow-sm group">
            <summary class="font-bold text-sm text-[#1d1c15] cursor-pointer flex items-center justify-between">
              <span>Do devotees receive the full spiritual benefit of Puja while attending online from {c_en}?</span>
              <span class="material-symbols-outlined text-[20px] text-[#8d4b00] group-open:rotate-180 transition-transform">expand_more</span>
            </summary>
            <p class="text-xs text-[#554336] mt-2.5 leading-relaxed">
              Yes, absolutely. According to Vedic scriptures, the patron's (Yajman's) Name, Gotra, and Sankalp are paramount. When Pandit Ji invokes your name and gotra before the consecrated sacred fire at Siddhapeeth Nalkheda, the spiritual vibrations and divine fruits reach you directly.
            </p>
          </details>

          <details class="bg-white rounded-xl p-4 border border-[#dbc2b0] shadow-sm group">
            <summary class="font-bold text-sm text-[#1d1c15] cursor-pointer flex items-center justify-between">
              <span>How many days does it take for the Prasad and energized Raksha Sutra to reach {c_en}?</span>
              <span class="material-symbols-outlined text-[20px] text-[#8d4b00] group-open:rotate-180 transition-transform">expand_more</span>
            </summary>
            <p class="text-xs text-[#554336] mt-2.5 leading-relaxed">
              The blessed prasad package is dispatched via India Post (Speed Post) or reliable express courier the very next day after puja completion. Typically, it reaches your postal address in {c_en} within 2 to 4 working days.
            </p>
          </details>

          <details class="bg-white rounded-xl p-4 border border-[#dbc2b0] shadow-sm group">
            <summary class="font-bold text-sm text-[#1d1c15] cursor-pointer flex items-center justify-between">
              <span>What are the dakshina and samagri charges for the Puja?</span>
              <span class="material-symbols-outlined text-[20px] text-[#8d4b00] group-open:rotate-180 transition-transform">expand_more</span>
            </summary>
            <p class="text-xs text-[#554336] mt-2.5 leading-relaxed">
              Dakshina depends on the specific ritual type (Laghu Havan, Samputit Path, or 125,000 Jaap Anushthan) and the number of Vedic Brahmins required. You can call or WhatsApp Pandit Ji directly at +91 87690 84789 for transparent, nominal estimates.
            </p>
          </details>

          <details class="bg-white rounded-xl p-4 border border-[#dbc2b0] shadow-sm group">
            <summary class="font-bold text-sm text-[#1d1c15] cursor-pointer flex items-center justify-between">
              <span>Can Pandit Harshit Sharma travel to {c_en} for personal ceremonies?</span>
              <span class="material-symbols-outlined text-[20px] text-[#8d4b00] group-open:rotate-180 transition-transform">expand_more</span>
            </summary>
            <p class="text-xs text-[#554336] mt-2.5 leading-relaxed">
              Yes. For major events such as Mahayajnas, Griha Pravesh, Shat Chandi Path, or business inaugurations, Pandit Harshit Sharma visits {c_en} upon special invitation. Advance booking of at least 10 days is required.
            </p>
          </details>

        </div>
      </div>
    </section>

    <!-- SECTION 6: SIBLINGS / STATE CITY LINKS -->
    <section class="py-10 px-4 md:px-8 bg-white border-t border-[#dbc2b0]">
      <div class="max-w-[1200px] mx-auto">
        <div class="flex items-center justify-between mb-4">
          <h3 class="font-['Noto_Serif',serif] font-bold text-base md:text-lg text-[#8d4b00]">
            Other Major Cities for Puja Services in {s_en}:
          </h3>
          <a href="../locations.html" class="text-xs font-bold text-[#a53936] hover:underline flex items-center gap-1">
            <span>View All 36 States & Regions</span>
            <span class="material-symbols-outlined text-[14px]">arrow_forward</span>
          </a>
        </div>
        <div class="flex flex-wrap gap-2">
          {sibling_links_html}
        </div>
      </div>
    </section>

  </main>

  <!-- FOOTER -->
  <footer class="w-full bg-[#f8f3e8] text-[#1d1c15] pt-12 pb-8 border-t border-[#dbc2b0]">
    <div class="max-w-[1200px] mx-auto px-4 md:px-8">
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8 pb-10 border-b border-[#dbc2b0]/60">
        
        <!-- Col 1 -->
        <div class="flex flex-col gap-3">
          <div class="flex items-center gap-2">
            <img src="../logo.webp" alt="Logo" class="w-10 h-10 rounded-full object-cover border border-[#b15f00]"/>
            <span class="font-['Noto_Serif',serif] font-bold text-base text-[#8d4b00]">Pandit Harshit Sharma</span>
          </div>
          <p class="text-xs text-[#554336] leading-relaxed">
            Authorized Vedic priest at Maa Baglamukhi Dham Nalkheda. Dedicated to conducting authentic online and offline Vedic pujas for devotees across {c_en} ({s_en}) and all over India.
          </p>
        </div>

        <!-- Col 2 -->
        <div class="flex flex-col gap-2.5">
          <span class="font-['Noto_Serif',serif] font-bold text-sm text-[#8d4b00]">Key Services</span>
          <div class="flex flex-col gap-1.5 text-xs text-[#554336]">
            <a class="hover:text-[#8d4b00]" href="../services.html">Maa Baglamukhi Anushthan</a>
            <a class="hover:text-[#8d4b00]" href="../court-case-puja.html">Court Case Victory Havan</a>
            <a class="hover:text-[#8d4b00]" href="../grah-shanti-puja.html">Navgrah Shanti & Kaal Sarp</a>
            <a class="hover:text-[#8d4b00]" href="../vyapar-vriddhi-puja.html">Debt Relief & Business Puja</a>
            <a class="hover:text-[#8d4b00]" href="../locations.html">Locations Directory (36 States)</a>
          </div>
        </div>

        <!-- Col 3 -->
        <div class="flex flex-col gap-2.5">
          <span class="font-['Noto_Serif',serif] font-bold text-sm text-[#8d4b00]">Siddhapeeth Nalkheda Address</span>
          <p class="text-xs text-[#554336] leading-relaxed">
            Lakhundar River Bank, World Famous Maa Baglamukhi Temple, Nalkheda, Dist. Agar Malwa (M.P.) - 465445
          </p>
          <a href="https://www.google.com/maps/search/Maa+Baglamukhi+Mandir+Nalkheda" target="_blank" class="inline-flex items-center gap-1 text-xs text-[#8d4b00] font-bold hover:underline">
            <span class="material-symbols-outlined text-[15px]">near_me</span>
            <span>View on Google Maps</span>
          </a>
        </div>

        <!-- Col 4 -->
        <div class="flex flex-col gap-2.5">
          <span class="font-['Noto_Serif',serif] font-bold text-sm text-[#8d4b00]">Direct Contact Center</span>
          <div class="text-xs text-[#554336] flex flex-col gap-1">
            <p class="font-bold text-[#1d1c15] text-sm">+91 87690 84789</p>
            <p class="font-bold text-[#1d1c15] text-sm">+91 91658 76908</p>
            <p class="text-[11px] text-[#006b2f] font-semibold mt-1">Available 6:00 AM to 11:00 PM IST</p>
            <p class="text-[11px] text-[#554336]">panditharshitsharma@gmail.com</p>
          </div>
          <div class="flex items-center gap-3 pt-2">
            <a href="https://www.youtube.com/@maabaglamukhitv" target="_blank" class="text-xs text-[#554336] hover:text-[#8d4b00] font-bold">YouTube</a>
            <span>•</span>
            <a href="https://www.instagram.com/baglarani_/" target="_blank" class="text-xs text-[#554336] hover:text-[#8d4b00] font-bold">Instagram</a>
          </div>
        </div>

      </div>

      <div class="pt-6 flex flex-col sm:flex-row items-center justify-between gap-3 text-xs text-[#554336]">
        <p>© 2026 Pandit Harshit Sharma. All rights reserved. ({c_en} Puja Service Page)</p>
        <p>Pure Vedic Tradition • Personalized Name-Gotra Live Sankalp</p>
      </div>
    </div>
  </footer>

  <!-- FLOATING CALL & WHATSAPP BUTTONS -->
  <div class="fixed bottom-4 right-4 z-50 flex flex-col gap-2.5">
    <a href="https://wa.me/918769084789?text=Hello%20Pandit%20Ji,%20I%20am%20from%20{c_en}%20and%20want%20to%20talk%20regarding%20Puja." target="_blank" class="w-12 h-12 rounded-full bg-[#25d366] text-white flex items-center justify-center shadow-xl hover:scale-110 transition-transform" title="Chat on WhatsApp">
      <span class="material-symbols-outlined text-[26px]">chat</span>
    </a>
    <a href="tel:+918769084789" class="w-12 h-12 rounded-full bg-[#8d4b00] text-white flex items-center justify-center shadow-xl hover:scale-110 transition-transform" title="Call Pandit Ji">
      <span class="material-symbols-outlined text-[26px]">call</span>
    </a>
  </div>

</body>
</html>
'''

# Generate all city pages
count = 0
for state in LOCATIONS_DATA:
    state_cities = []
    # Collect all cities in this state
    for c_en, c_hi in state['cities']:
        base_slug = slugify(c_en)
        slug = base_slug
        if slug in city_slug_map and city_slug_map[slug]['state_en'] != state['state_en']:
            slug = f"{base_slug}-{slugify(state['state_en'])}"
        state_cities.append(city_slug_map[slug])

    for city_info in state_cities:
        html = generate_city_html(city_info, state_cities)
        file_path = os.path.join(OUTPUT_DIR, f"{city_info['slug']}.html")
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(html)
        count += 1

print(f"Successfully generated {count} city HTML pages in {OUTPUT_DIR}!")

# Generate Master directory locations.html
def generate_master_locations_html():
    states_cards_html = ""
    for idx, state in enumerate(LOCATIONS_DATA, start=1):
        s_en = state['state_en']
        s_hi = state['state_hi']
        cities_pills_html = ""
        for c_en, c_hi in state['cities']:
            base_slug = slugify(c_en)
            slug = base_slug
            if slug in city_slug_map and city_slug_map[slug]['state_en'] != s_en:
                slug = f"{base_slug}-{slugify(s_en)}"
            cities_pills_html += f'''
            <a href="puja-in/{slug}.html" class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-white hover:bg-[#ffdcc3] text-[#8d4b00] text-xs font-semibold border border-[#dbc2b0] shadow-sm hover:shadow transition-all">
              <span class="material-symbols-outlined text-[14px]">location_on</span>
              <span>{c_en}</span>
            </a>'''

        states_cards_html += f'''
        <div class="state-card bg-[#fef9ee] rounded-2xl p-6 border border-[#dbc2b0] shadow-sm hover:shadow-md transition-shadow" data-state="{s_en.lower()} {s_hi.lower()}">
          <div class="flex items-center justify-between pb-3 mb-4 border-b border-[#dbc2b0]/50">
            <div class="flex items-center gap-3">
              <span class="w-8 h-8 rounded-full bg-[#8d4b00] text-white flex items-center justify-center font-bold text-xs">{idx}</span>
              <div>
                <h3 class="font-['Noto_Serif',serif] font-bold text-lg text-[#1d1c15]">{s_en}</h3>
                <span class="text-xs text-[#554336]">{s_hi} • {len(state['cities'])} Cities</span>
              </div>
            </div>
            <span class="text-xs font-bold text-[#006b2f] bg-[#95f8a7]/40 px-2.5 py-1 rounded-full">Service Available</span>
          </div>
          <div class="flex flex-wrap gap-2">
            {cities_pills_html}
          </div>
        </div>'''

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8"/>
  <meta content="width=device-width, initial-scale=1.0" name="viewport"/>
  <title>All 446+ Cities & 36 States Directory | Best Pandit in Nalkheda - Pandit Harshit Sharma</title>
  <meta name="description" content="Explore Vedic Maa Baglamukhi Puja and Havan services across all 36 Indian states and 446+ cities with Pandit Harshit Sharma from Maa Baglamukhi Dham Nalkheda."/>
  <meta name="keywords" content="Best Pandit in Nalkheda, Pandit in India, All India Puja Services, Maa Baglamukhi Puja, Havan Booking, Pandit Harshit Sharma"/>
  <link rel="canonical" href="https://www.baglamukhi-puja.in/locations.html"/>
  <meta property="og:type" content="website"/>
  <meta property="og:url" content="https://www.baglamukhi-puja.in/locations.html"/>
  <meta property="og:title" content="All 446+ Cities Directory | Best Pandit in Nalkheda - Pandit Harshit Sharma"/>
  <meta property="og:description" content="Explore Vedic Maa Baglamukhi Puja and Havan services across 446+ cities with Pandit Harshit Sharma from Maa Baglamukhi Dham Nalkheda."/>
  <meta property="og:image" content="https://www.baglamukhi-puja.in/logo.webp"/>
  <meta name="twitter:card" content="summary_large_image"/>
  <link rel="icon" type="image/jpeg" href="./logo.webp"/>
  <link href="https://fonts.googleapis.com" rel="preconnect"/>
  <link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/>
  <link rel="preload" href="https://fonts.googleapis.com/css2?family=Noto+Serif:ital,wght@0,400..700;1,400..700&amp;family=Plus+Jakarta+Sans:ital,wght@0,400..800;1,400..800&amp;display=swap" as="style" onload="this.onload=null;this.rel='stylesheet'"/>
  <noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Serif:ital,wght@0,400..700;1,400..700&amp;family=Plus+Jakarta+Sans:ital,wght@0,400..800;1,400..800&amp;display=swap"/></noscript>
  <link rel="preload" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght@400&amp;display=swap" as="style" onload="this.onload=null;this.rel='stylesheet'"/>
  <noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght@400&amp;display=swap"/></noscript>
  <link rel="stylesheet" href="/style.css" />

  <!-- Schema.org JSON-LD -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "LocalBusiness",
    "name": "Pandit Harshit Sharma - All India Puja Directory",
    "url": "https://www.baglamukhi-puja.in/locations.html",
    "telephone": "+918769084789",
    "image": "https://www.baglamukhi-puja.in/logo.webp",
    "description": "Authentic Vedic Maa Baglamukhi Puja and Havan services across all 36 Indian states and 446+ cities from Maa Baglamukhi Dham Nalkheda."
  }}
  </script>
</head>
<body class="bg-[#fef9ee] font-['Plus_Jakarta_Sans',sans-serif] text-[#1d1c15] overflow-x-hidden">

  <!-- TOP BAR -->
  <header class="fixed top-0 w-full z-50 bg-[#fef9ee]/95 backdrop-blur-xl shadow-[0_4px_20px_-2px_rgba(180,83,9,0.08)]">
    <div class="bg-[#a53936] text-white px-4 md:px-8 py-2 text-center">
      <div class="max-w-[1200px] mx-auto flex flex-col md:flex-row items-center justify-between gap-1 text-xs">
        <div class="flex items-center gap-2">
          <span class="flex h-2 w-2 relative">
            <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-[#ffdad7] opacity-75"></span>
            <span class="relative inline-flex rounded-full h-2 w-2 bg-[#ffdad7]"></span>
          </span>
          <span>World Renowned Ancient Siddhapeeth • Nalkheda (M.P.) | All India Puja Services</span>
        </div>
        <div class="flex items-center gap-4">
          <a href="tel:+918769084789" class="flex items-center gap-1 hover:text-[#ffdad7]">
            <span class="material-symbols-outlined text-[14px]">call</span>
            <span class="font-bold">+91 87690 84789</span>
          </a>
          <a href="https://wa.me/918769084789" target="_blank" class="flex items-center gap-1 text-[#95f8a7] font-bold hover:underline">
            <span>WhatsApp Us</span>
          </a>
        </div>
      </div>
    </div>

    <!-- MAIN NAVBAR -->
    <div class="h-20 max-w-[1200px] mx-auto px-4 md:px-8 flex items-center justify-between gap-2">
      <a href="/" class="flex items-center gap-3">
        <img src="./logo.webp" alt="Pandit Harshit Sharma" class="w-11 h-11 md:w-13 md:h-13 rounded-full object-cover shadow-md border-2 border-[#b15f00]"/>
        <div class="flex flex-col">
          <span class="font-['Noto_Serif',serif] font-bold text-base md:text-xl text-[#8d4b00] leading-tight">Pandit Harshit Sharma</span>
          <span class="text-[11px] text-[#a53936] font-semibold tracking-wide">Maa Baglamukhi Dham Nalkheda</span>
        </div>
      </a>

      <nav class="hidden md:flex items-center gap-6 text-sm font-semibold text-[#554336]">
        <a class="hover:text-[#8d4b00] transition-colors" href="/">Home</a>
        <a class="hover:text-[#8d4b00] transition-colors" href="services.html">Services</a>
        <a class="hover:text-[#8d4b00] transition-colors" href="gallery.html">Gallery</a>
        <a class="text-[#8d4b00] font-bold border-b-2 border-[#8d4b00] pb-0.5" href="locations.html">Locations Directory</a>
        <a class="hover:text-[#8d4b00] transition-colors" href="contact.html">Contact</a>
      </nav>

      <a href="tel:+918769084789" class="inline-flex items-center gap-1.5 px-4 py-2 rounded-full bg-[#8d4b00] text-white text-xs font-bold shadow-md hover:bg-[#b15f00] transition-all">
        <span class="material-symbols-outlined text-[16px]">call</span>
        <span>Consult Now</span>
      </a>
    </div>
  </header>

  <main class="w-full pt-28 md:pt-32 pb-16">

    <!-- HERO -->
    <section class="bg-gradient-to-b from-[#f2ede3] to-[#fef9ee] px-4 md:px-8 py-12 text-center border-b border-[#dbc2b0]/50">
      <div class="max-w-[800px] mx-auto flex flex-col gap-3">
        <div class="inline-flex items-center gap-1.5 self-center px-3.5 py-1.5 rounded-full bg-[#ffdcc3] text-[#2f1500] text-xs font-bold shadow-sm">
          <span class="material-symbols-outlined text-[#8d4b00] text-[16px]">public</span>
          <span>All India Vedic Rituals Directory (36 States & Union Territories)</span>
        </div>
        <h1 class="font-['Noto_Serif',serif] text-2xl sm:text-3xl md:text-4xl font-bold text-[#8d4b00] leading-tight">
          Vedic Puja & Havan Services in Your City by Pandit Harshit Sharma
        </h1>
        <p class="text-xs sm:text-sm text-[#554336] leading-relaxed">
          No matter which state or city you reside in, participate in authentic Maa Baglamukhi Pujas from the sacred Siddhapeeth Nalkheda Dham via live video sankalp. Search and select your city below.
        </p>

        <!-- SEARCH INPUT -->
        <div class="max-w-md mx-auto w-full mt-4 relative">
          <span class="material-symbols-outlined absolute left-4 top-3 text-[#8d4b00]">search</span>
          <input type="text" id="citySearch" placeholder="Search your city or state (e.g. Delhi, Mumbai, Jaipur, Indore)..." onkeyup="filterLocations()" class="w-full pl-12 pr-4 py-3 rounded-full border-2 border-[#dbc2b0] focus:border-[#8d4b00] outline-none text-xs sm:text-sm bg-white shadow-sm"/>
        </div>
      </div>
    </section>

    <!-- STATES CONTAINER -->
    <section class="max-w-[1200px] mx-auto px-4 md:px-8 mt-10">
      <div id="statesGrid" class="grid grid-cols-1 md:grid-cols-2 gap-6">
        {states_cards_html}
      </div>
    </section>

  </main>

  <!-- SCRIPT FOR INSTANT LIVE SEARCH -->
  <script>
    function filterLocations() {{
      const query = document.getElementById('citySearch').value.toLowerCase().trim();
      const stateCards = document.querySelectorAll('.state-card');
      stateCards.forEach(card => {{
        const text = card.textContent.toLowerCase();
        if (text.includes(query)) {{
          card.style.display = '';
        }} else {{
          card.style.display = 'none';
        }}
      }});
    }}
  </script>

  <!-- FOOTER -->
  <footer class="w-full bg-[#f8f3e8] text-[#1d1c15] pt-12 pb-8 border-t border-[#dbc2b0]">
    <div class="max-w-[1200px] mx-auto px-4 md:px-8 text-center text-xs text-[#554336]">
      <p class="font-['Noto_Serif',serif] text-[#8d4b00] font-bold text-sm mb-1">Pandit Harshit Sharma • Maa Baglamukhi Dham Nalkheda (M.P.)</p>
      <p>© 2026 All Rights Reserved. Helpline: +91 87690 84789 | +91 91658 76908</p>
    </div>
  </footer>

</body>
</html>'''

with open(os.path.join(os.path.dirname(__file__), 'locations.html'), 'w', encoding='utf-8') as f:
    f.write(generate_master_locations_html())

print("Successfully generated locations.html!")

# Generate sitemap.xml
def generate_sitemap_xml():
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    
    # Core pages
    core_pages = [
        ('', '1.0', 'daily'),
        ('services.html', '0.9', 'weekly'),
        ('gallery.html', '0.8', 'weekly'),
        ('contact.html', '0.8', 'monthly'),
        ('locations.html', '0.9', 'daily'),
        ('online-puja-booking.html', '0.8', 'monthly'),
        ('court-case-puja.html', '0.8', 'monthly'),
        ('shatru-vijay-puja.html', '0.8', 'monthly'),
        ('vyapar-vriddhi-puja.html', '0.8', 'monthly'),
        ('grah-shanti-puja.html', '0.8', 'monthly'),
        ('baglamukhi-kavach.html', '0.8', 'monthly'),
        ('swasthya-raksha-puja.html', '0.8', 'monthly'),
        ('vivah-badha-puja.html', '0.8', 'monthly')
    ]
    for page, priority, freq in core_pages:
        loc = f"https://www.baglamukhi-puja.in/{page}" if page else "https://www.baglamukhi-puja.in/"
        xml += f'  <url>\n    <loc>{loc}</loc>\n    <changefreq>{freq}</changefreq>\n    <priority>{priority}</priority>\n  </url>\n'

    # City pages
    for city in all_cities_flat:
        xml += f'  <url>\n    <loc>https://www.baglamukhi-puja.in/puja-in/{city["slug"]}.html</loc>\n    <changefreq>weekly</changefreq>\n    <priority>0.8</priority>\n  </url>\n'

    xml += '</urlset>'
    return xml

with open(os.path.join(os.path.dirname(__file__), 'sitemap.xml'), 'w', encoding='utf-8') as f:
    f.write(generate_sitemap_xml())

print("Successfully generated sitemap.xml with all cities!")

# Generate robots.txt
def generate_robots_txt():
    return '''User-agent: *
Allow: /

Sitemap: https://www.baglamukhi-puja.in/sitemap.xml
'''

with open(os.path.join(os.path.dirname(__file__), 'robots.txt'), 'w', encoding='utf-8') as f:
    f.write(generate_robots_txt())

print("Successfully generated robots.txt!")
