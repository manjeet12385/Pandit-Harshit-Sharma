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
        city_badge = f"प्रवासी भारतीय (NRI) यजमान • {c_hi} ({c_en}) लाइव पूजा सेवा"
        special_intro = f"{c_hi} ({c_en}) में निवास कर रहे सभी प्रवासी भारतीय श्रद्धालु अब भारत के महाभारत कालीन सिद्धपीठ माँ बगलामुखी धाम नलखेड़ा से अपने नाम, गोत्र और भारतीय जन्म विवरण के साथ लाइव वीडियो कॉल (WhatsApp / Zoom) द्वारा विशेष अनुष्ठान एवं हवन करवा सकते हैं।"
    elif any(k.lower() in c_en.lower() for k in pilgrimage_keywords):
        city_badge = f"पवित्र धर्मक्षेत्र {c_hi} के श्रद्धालुओं हेतु माँ बगलामुखी विशेष अनुष्ठान"
        special_intro = f"धर्म और आस्था की पावन नगरी {c_hi} के सभी श्रद्धालु अब माँ बगलामुखी के प्राचीन सिद्धपीठ नलखेड़ा धाम से अपनी मनोकामना पूर्ति हेतु सीधे पंडित हर्षित शर्मा जी से विशेष तांत्रिक एवं वैदिक अनुष्ठान संपन्न करा सकते हैं।"
    elif any(k.lower() in c_en.lower() for k in metro_keywords):
        city_badge = f"महानगर {c_hi} के यजमानों हेतु लाइव संकल्प व पूजा सेवा"
        special_intro = f"{c_hi} की व्यस्त दिनचर्या और व्यावसायिक तनाव के बीच, अपने जीवन की गंभीर समस्याओं, शत्रु बाधा, कोर्ट कचहरी विवाद व धन-व्यापारिक रुकावटों के निवारण के लिए नलखेड़ा धाम से लाइव वैदिक हवन करवाएं।"
    else:
        city_badge = f"{c_hi} ({s_hi}) के श्रद्धालुओं हेतु विशेष वैदिक अनुष्ठान"
        special_intro = f"{c_hi} एवं आसपास के सभी भक्तजन अब माँ बगलामुखी सिद्धपीठ नलखेड़ा से अपने नाम एवं गोत्र पर विधि-विधान से विशेष हवन, ग्रह शांति और बगलामुखी महा अनुष्ठान करा सकते हैं।"

    # State siblings links (up to 8 other cities in the same state)
    sibling_links_html = ""
    for sib in state_sibling_cities:
        if sib['slug'] != slug:
            sibling_links_html += f'''
            <a href="{sib['slug']}.html" class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-full bg-[#f8f3e8] hover:bg-[#ffdcc3] text-[#8d4b00] text-xs font-semibold border border-[#dbc2b0] transition-colors">
              <span class="material-symbols-outlined text-[14px]">location_on</span>
              <span>{sib['city_hi']} ({sib['city_en']})</span>
            </a>'''

    return f'''<!DOCTYPE html>
<html lang="hi">
<head>
  <meta charset="utf-8"/>
  <meta content="width=device-width, initial-scale=1.0" name="viewport"/>
  <title>{c_hi} में पंडित हर्षित शर्मा | माँ बगलामुखी अनुष्ठान, हवन एवं ज्योतिष सेवा</title>
  <meta name="description" content="{c_hi} ({s_hi}) में श्रेष्ठ वैदिक पुरोहित पंडित हर्षित शर्मा। माँ बगलामुखी धाम नलखेड़ा से लाइव संकल्प पूजा, शत्रु विजय, ग्रह शांति व व्यापार वृद्धि हवन। परामर्श हेतु संपर्क करें: +91 87690 84789."/>
  <meta name="keywords" content="{c_hi} में पंडित जी, Pandit in {c_en}, Best Pandit in {c_en}, Maa Baglamukhi Puja in {c_en}, Havan in {c_en}, {c_hi} Puja Booking, Nalkheda Dham Pandit"/>
  <link rel="canonical" href="https://panditharshitsharma.com/puja-in/{slug}.html"/>

  <!-- Open Graph / Facebook -->
  <meta property="og:type" content="website"/>
  <meta property="og:url" content="https://panditharshitsharma.com/puja-in/{slug}.html"/>
  <meta property="og:title" content="{c_hi} में पंडित हर्षित शर्मा | माँ बगलामुखी धाम नलखेड़ा पूजा सेवा"/>
  <meta property="og:description" content="{c_hi} के यजमानों के लिए माँ बगलामुखी सिद्धपीठ नलखेड़ा से विशेष लाइव वीडियो संकल्प पूजा, ग्रह शांति व शत्रु निवारण हवन।"/>
  <meta property="og:image" content="https://panditharshitsharma.com/logo.webp"/>

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
    "name": "पंडित हर्षित शर्मा - माँ बगलामुखी पूजा सेवा {c_hi}",
    "image": "https://panditharshitsharma.com/logo.webp",
    "telephone": "+918769084789",
    "address": {{
      "@type": "PostalAddress",
      "addressLocality": "{c_en}",
      "addressRegion": "{s_en}",
      "addressCountry": "IN"
    }},
    "url": "https://panditharshitsharma.com/puja-in/{slug}.html",
    "priceRange": "₹₹",
    "description": "{c_hi} ({s_hi}) के श्रद्धालुओं के लिए माँ बगलामुखी धाम नलखेड़ा से विशेष वैदिक अनुष्ठान एवं लाइव संकल्प पूजा सेवाएं।"
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
        "name": "होम",
        "item": "https://panditharshitsharma.com/"
      }},
      {{
        "@type": "ListItem",
        "position": 2,
        "name": "सभी शहर",
        "item": "https://panditharshitsharma.com/locations.html"
      }},
      {{
        "@type": "ListItem",
        "position": 3,
        "name": "{c_hi} में पूजा",
        "item": "https://panditharshitsharma.com/puja-in/{slug}.html"
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
          <span>महाभारत कालीन विश्व प्रसिद्ध सिद्धपीठ • नलखेड़ा (म.प्र.) | {c_hi} विशेष सेवा</span>
        </div>
        <div class="flex items-center gap-4">
          <a href="tel:+918769084789" class="flex items-center gap-1 hover:text-[#ffdad7]">
            <span class="material-symbols-outlined text-[14px]">call</span>
            <span class="font-bold">+91 87690 84789</span>
          </a>
          <a href="https://wa.me/918769084789?text=प्रणाम%20पंडित%20जी,%20मैं%20{c_hi}%20से%20पूजा%20के%20संबंध%20में%20जानकारी%20चाहता/चाहती%20हूँ।" target="_blank" class="flex items-center gap-1 text-[#95f8a7] font-bold hover:underline">
            <span>WhatsApp करें</span>
          </a>
        </div>
      </div>
    </div>

    <!-- MAIN NAVBAR -->
    <div class="h-20 max-w-[1200px] mx-auto px-4 md:px-8 flex items-center justify-between gap-2">
      <a href="../index.html" class="flex items-center gap-3">
        <img src="../logo.webp" alt="पंडित हर्षित शर्मा" class="w-11 h-11 md:w-13 md:h-13 rounded-full object-cover shadow-md border-2 border-[#b15f00]"/>
        <div class="flex flex-col">
          <span class="font-['Noto_Serif',serif] font-bold text-base md:text-xl text-[#8d4b00] leading-tight">पंडित हर्षित शर्मा</span>
          <span class="text-[11px] text-[#a53936] font-semibold tracking-wide">माँ बगलामुखी धाम नलखेड़ा</span>
        </div>
      </a>

      <nav class="hidden md:flex items-center gap-6 text-sm font-semibold text-[#554336]">
        <a class="hover:text-[#8d4b00] transition-colors" href="../index.html">होम</a>
        <a class="hover:text-[#8d4b00] transition-colors" href="../services.html">सेवाएं</a>
        <a class="hover:text-[#8d4b00] transition-colors" href="../gallery.html">गैलरी</a>
        <a class="text-[#8d4b00] font-bold border-b-2 border-[#8d4b00] pb-0.5" href="../locations.html">सभी शहर ({s_hi})</a>
        <a class="hover:text-[#8d4b00] transition-colors" href="../contact.html">संपर्क</a>
      </nav>

      <div class="flex items-center gap-2">
        <a href="tel:+918769084789" class="hidden sm:inline-flex items-center gap-1.5 px-4 py-2 rounded-full bg-[#8d4b00] text-white text-xs font-bold shadow-md hover:bg-[#b15f00] transition-all">
          <span class="material-symbols-outlined text-[16px]">call</span>
          <span>परामर्श लें</span>
        </a>
        <a href="../locations.html" class="inline-flex md:hidden items-center gap-1 px-3 py-1.5 rounded-full bg-[#f8f3e8] border border-[#dbc2b0] text-[#8d4b00] text-xs font-bold">
          <span class="material-symbols-outlined text-[15px]">explore</span>
          <span>शहर</span>
        </a>
      </div>
    </div>
  </header>

  <!-- MAIN WRAPPER -->
  <main class="w-full pt-28 md:pt-32">

    <!-- BREADCRUMB -->
    <div class="bg-[#f2ede3] border-b border-[#dbc2b0]/50 py-2.5 px-4 md:px-8">
      <div class="max-w-[1200px] mx-auto flex items-center gap-2 text-xs text-[#554336]">
        <a href="../index.html" class="hover:text-[#8d4b00]">होम</a>
        <span>/</span>
        <a href="../locations.html" class="hover:text-[#8d4b00]">स्थान निर्देशिका</a>
        <span>/</span>
        <span class="text-[#554336]">{s_hi}</span>
        <span>/</span>
        <span class="text-[#8d4b00] font-bold">{c_hi} ({c_en})</span>
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
              {c_hi} में पंडित हर्षित शर्मा जी द्वारा विशेष पूजा, अनुष्ठान एवं वैदिक हवन
            </h1>

            <p class="text-sm md:text-base text-[#554336] leading-relaxed">
              {special_intro} यदि आप या आपका परिवार किसी भी प्रकार के <strong>न्यायालय विवाद (Court Case)</strong>, <strong>गुप्त शत्रु बाधा</strong>, <strong>ग्रह दोष</strong>, <strong>व्यापार में मंदी</strong> अथवा <strong>पारिवारिक क्लेश</strong> से परेशान हैं, तो माँ पीताम्बरा के पावन सिद्धपीठ से अपने नाम-गोत्र पर संपूर्ण सात्विक विधि से अनुष्ठान कराएं।
            </p>

            <!-- Trust Points -->
            <div class="grid grid-cols-2 sm:grid-cols-3 gap-2.5 pt-2">
              <div class="flex items-center gap-2 bg-white/80 p-2.5 rounded-lg border border-[#dbc2b0]/50 shadow-sm">
                <span class="material-symbols-outlined text-[#006b2f] text-[20px]">videocam</span>
                <span class="text-xs font-bold text-[#1d1c15]">लाइव वीडियो संकल्प</span>
              </div>
              <div class="flex items-center gap-2 bg-white/80 p-2.5 rounded-lg border border-[#dbc2b0]/50 shadow-sm">
                <span class="material-symbols-outlined text-[#8d4b00] text-[20px]">mark_email_read</span>
                <span class="text-xs font-bold text-[#1d1c15]">{c_hi} में प्रसाद डिलीवरी</span>
              </div>
              <div class="flex items-center gap-2 bg-white/80 p-2.5 rounded-lg border border-[#dbc2b0]/50 shadow-sm col-span-2 sm:col-span-1">
                <span class="material-symbols-outlined text-[#a53936] text-[20px]">local_fire_department</span>
                <span class="text-xs font-bold text-[#1d1c15]">100% सात्विक हवन</span>
              </div>
            </div>

            <!-- CTAs -->
            <div class="flex flex-wrap items-center gap-3 pt-3">
              <a href="tel:+918769084789" class="inline-flex items-center gap-2 px-6 py-3 rounded-full bg-[#8d4b00] text-white font-bold text-sm shadow-[0_4px_16px_rgba(141,75,0,0.3)] hover:bg-[#b15f00] transition-all transform hover:-translate-y-0.5">
                <span class="material-symbols-outlined text-[18px]">call</span>
                <span>पंडित जी से बात करें: +91 87690 84789</span>
              </a>
              <a href="https://wa.me/918769084789?text=प्रणाम%20पंडित%20जी,%20मैं%20{c_hi}%20से%20बात%20कर%20रहा/रही%20हूँ।%20मुझे%20पूजा%20के%20लिए%20संकल्प%20लेना%20है।" target="_blank" class="inline-flex items-center gap-2 px-6 py-3 rounded-full bg-[#006b2f] text-white font-bold text-sm shadow-[0_4px_16px_rgba(0,107,47,0.25)] hover:bg-[#1e8642] transition-all transform hover:-translate-y-0.5">
                <span class="material-symbols-outlined text-[18px]">chat</span>
                <span>WhatsApp पर संकल्प भेजें</span>
              </a>
            </div>
          </div>

          <!-- Right Hero Column (Images & Pandit Harshit Sharma Intro) -->
          <div class="lg:col-span-5 flex flex-col gap-4">
            <div class="relative bg-white rounded-2xl p-4 shadow-xl border border-[#dbc2b0]/60">
              <img src="../priest_chanting.webp" alt="पंडित हर्षित शर्मा वैदिक अनुष्ठान" class="w-full h-56 object-cover rounded-xl shadow-md"/>
              <div class="absolute -bottom-3 -right-3 bg-[#a53936] text-white px-4 py-2 rounded-xl shadow-lg flex items-center gap-2">
                <span class="material-symbols-outlined text-[20px]">workspace_premium</span>
                <span class="text-xs font-bold">15+ वर्ष वैदिक अनुभव</span>
              </div>
            </div>
            
            <div class="bg-[#f8f3e8] rounded-xl p-3.5 border border-[#dbc2b0] flex items-center gap-3">
              <img src="../logo.webp" alt="Logo" class="w-12 h-12 rounded-full object-cover border border-[#8d4b00]"/>
              <div class="text-xs text-[#554336] leading-tight">
                <p class="font-bold text-[#8d4b00] text-sm">पंडित हर्षित शर्मा</p>
                <p>माँ बगलामुखी धाम, लखुंदर नदी तट, नलखेड़ा (म.प्र.)</p>
                <p class="text-[11px] text-[#006b2f] font-semibold mt-0.5">● {c_hi} के यजमानों हेतु 24x7 निःशुल्क मार्गदर्शन</p>
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
          <span class="text-[#a53936] font-bold text-xs uppercase tracking-widest">वैदिक समाधान</span>
          <h2 class="font-['Noto_Serif',serif] text-2xl md:text-3xl font-bold text-[#8d4b00] mt-1">
            {c_hi} के यजमानों हेतु प्रमुख विशेष अनुष्ठान एवं हवन सेवाएँ
          </h2>
          <p class="text-xs md:text-sm text-[#554336] mt-2">
            प्रत्येक पूजा शास्त्रों के अनुसार, पूर्ण शुद्धता, सात्विक हवन सामग्री एवं आपके नाम-गोत्र के साथ संपन्न की जाती है।
          </p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">

          <!-- Card 1 -->
          <div class="bg-[#fef9ee] rounded-2xl p-5 border border-[#dbc2b0] hover:shadow-lg transition-all flex flex-col justify-between">
            <div>
              <div class="w-12 h-12 rounded-xl bg-[#ffdcc3] text-[#8d4b00] flex items-center justify-center mb-3">
                <span class="material-symbols-outlined text-[26px]">gavel</span>
              </div>
              <h3 class="font-['Noto_Serif',serif] font-bold text-lg text-[#1d1c15] mb-2">माँ बगलामुखी शत्रु विजय एवं कोर्ट केस शांति</h3>
              <p class="text-xs text-[#554336] leading-relaxed mb-4">
                न्यायालयीन विवाद, झूठे मुकदमों, गुप्त शत्रुओं एवं विरोधी षड्यंत्रों के दमन हेतु पीताम्बरा महामंत्र संपुटित हवन।
              </p>
            </div>
            <a href="https://wa.me/918769084789?text=प्रणाम%20पंडित%20जी,%20मुझे%20{c_hi}%20के%20लिए%20शत्रु%20विजय%20बगलामुखी%20हवन%20कराना%20है।" target="_blank" class="inline-flex items-center justify-center gap-1.5 w-full py-2 rounded-lg bg-[#8d4b00] text-white text-xs font-bold hover:bg-[#b15f00] transition-colors">
              <span>संकल्प बुक करें</span>
              <span class="material-symbols-outlined text-[15px]">arrow_forward</span>
            </a>
          </div>

          <!-- Card 2 -->
          <div class="bg-[#fef9ee] rounded-2xl p-5 border border-[#dbc2b0] hover:shadow-lg transition-all flex flex-col justify-between">
            <div>
              <div class="w-12 h-12 rounded-xl bg-[#ffdcc3] text-[#8d4b00] flex items-center justify-center mb-3">
                <span class="material-symbols-outlined text-[26px]">paid</span>
              </div>
              <h3 class="font-['Noto_Serif',serif] font-bold text-lg text-[#1d1c15] mb-2">व्यापार वृद्धि, ऋण मुक्ति व कनकधारा पाठ</h3>
              <p class="text-xs text-[#554336] leading-relaxed mb-4">
                व्यवसाय में लगातार नुकसान, कर्जों का बोझ, धन के अभाव एवं अटके हुए भुगतानों को निकलवाने हेतु विशेष लक्ष्मी कुबेर अनुष्ठान।
              </p>
            </div>
            <a href="https://wa.me/918769084789?text=प्रणाम%20पंडित%20जी,%20मुझे%20{c_hi}%20के%20लिए%20व्यापार%20वृद्धि%20पूजा%20करवानी%20है।" target="_blank" class="inline-flex items-center justify-center gap-1.5 w-full py-2 rounded-lg bg-[#8d4b00] text-white text-xs font-bold hover:bg-[#b15f00] transition-colors">
              <span>संकल्प बुक करें</span>
              <span class="material-symbols-outlined text-[15px]">arrow_forward</span>
            </a>
          </div>

          <!-- Card 3 -->
          <div class="bg-[#fef9ee] rounded-2xl p-5 border border-[#dbc2b0] hover:shadow-lg transition-all flex flex-col justify-between">
            <div>
              <div class="w-12 h-12 rounded-xl bg-[#ffdcc3] text-[#8d4b00] flex items-center justify-center mb-3">
                <span class="material-symbols-outlined text-[26px]">brightness_7</span>
              </div>
              <h3 class="font-['Noto_Serif',serif] font-bold text-lg text-[#1d1c15] mb-2">नवग्रह शांति एवं कालसर्प दोष निवारण</h3>
              <p class="text-xs text-[#554336] leading-relaxed mb-4">
                राहु, केतु, शनि की साढ़ेसाती, कालसर्प दोष एवं मांगलिक दोष के अशुभ प्रभावों को शांत करने हेतु वैदिक ग्रह यज्ञ।
              </p>
            </div>
            <a href="https://wa.me/918769084789?text=प्रणाम%20पंडित%20जी,%20मुझे%20{c_hi}%20के%20लिए%20नवग्रह%20शांति%20हवन%20कराना%20है।" target="_blank" class="inline-flex items-center justify-center gap-1.5 w-full py-2 rounded-lg bg-[#8d4b00] text-white text-xs font-bold hover:bg-[#b15f00] transition-colors">
              <span>संकल्प बुक करें</span>
              <span class="material-symbols-outlined text-[15px]">arrow_forward</span>
            </a>
          </div>

          <!-- Card 4 -->
          <div class="bg-[#fef9ee] rounded-2xl p-5 border border-[#dbc2b0] hover:shadow-lg transition-all flex flex-col justify-between">
            <div>
              <div class="w-12 h-12 rounded-xl bg-[#ffdcc3] text-[#8d4b00] flex items-center justify-center mb-3">
                <span class="material-symbols-outlined text-[26px]">health_and_safety</span>
              </div>
              <h3 class="font-['Noto_Serif',serif] font-bold text-lg text-[#1d1c15] mb-2">महामृत्युंजय जाप एवं अकाल मृत्यु रक्षा</h3>
              <p class="text-xs text-[#554336] leading-relaxed mb-4">
                गंभीर असाध्य रोगों, अचानक दुर्घटनाओं से बचाव एवं परिजनों के दीर्घायु व उत्तम स्वास्थ्य हेतु सवा लाख महामृत्युंजय मंत्र जप।
              </p>
            </div>
            <a href="https://wa.me/918769084789?text=प्रणाम%20पंडित%20जी,%20मुझे%20{c_hi}%20के%20लिए%20महामृत्युंजय%20जाप%20कराना%20है।" target="_blank" class="inline-flex items-center justify-center gap-1.5 w-full py-2 rounded-lg bg-[#8d4b00] text-white text-xs font-bold hover:bg-[#b15f00] transition-colors">
              <span>संकल्प बुक करें</span>
              <span class="material-symbols-outlined text-[15px]">arrow_forward</span>
            </a>
          </div>

          <!-- Card 5 -->
          <div class="bg-[#fef9ee] rounded-2xl p-5 border border-[#dbc2b0] hover:shadow-lg transition-all flex flex-col justify-between">
            <div>
              <div class="w-12 h-12 rounded-xl bg-[#ffdcc3] text-[#8d4b00] flex items-center justify-center mb-3">
                <span class="material-symbols-outlined text-[26px]">favorite</span>
              </div>
              <h3 class="font-['Noto_Serif',serif] font-bold text-lg text-[#1d1c15] mb-2">शीघ्र विवाह एवं दांपत्य सुख शांति अनुष्ठान</h3>
              <p class="text-xs text-[#554336] leading-relaxed mb-4">
                विवाह में आ रही अनावश्यक देरी, रिश्ते तय होकर टूटना या पति-पत्नी के बीच तनाव-कलह को दूर करने के लिए विशेष उपाय।
              </p>
            </div>
            <a href="https://wa.me/918769084789?text=प्रणाम%20पंडित%20जी,%20मुझे%20{c_hi}%20के%20लिए%20विवाह%20बाधा%20निवारण%20पूजा%20करवानी%20है।" target="_blank" class="inline-flex items-center justify-center gap-1.5 w-full py-2 rounded-lg bg-[#8d4b00] text-white text-xs font-bold hover:bg-[#b15f00] transition-colors">
              <span>संकल्प बुक करें</span>
              <span class="material-symbols-outlined text-[15px]">arrow_forward</span>
            </a>
          </div>

          <!-- Card 6 -->
          <div class="bg-[#fef9ee] rounded-2xl p-5 border border-[#dbc2b0] hover:shadow-lg transition-all flex flex-col justify-between">
            <div>
              <div class="w-12 h-12 rounded-xl bg-[#ffdcc3] text-[#8d4b00] flex items-center justify-center mb-3">
                <span class="material-symbols-outlined text-[26px]">shield</span>
              </div>
              <h3 class="font-['Noto_Serif',serif] font-bold text-lg text-[#1d1c15] mb-2">सिद्ध बगलामुखी रक्षा कवच निर्माण</h3>
              <p class="text-xs text-[#554336] leading-relaxed mb-4">
                माँ बगलामुखी की दिव्य शक्ति व बीजाक्षरों से सिद्ध ताबीज एवं रक्षा कवच, जो आपको नकारात्मक ऊर्जा व तंत्र बाधा से सुरक्षित रखता है।
              </p>
            </div>
            <a href="https://wa.me/918769084789?text=प्रणाम%20पंडित%20जी,%20मुझे%20{c_hi}%20के%20लिए%20सिद्ध%20बगलामुखी%20कवच%20चाहिए।" target="_blank" class="inline-flex items-center justify-center gap-1.5 w-full py-2 rounded-lg bg-[#8d4b00] text-white text-xs font-bold hover:bg-[#b15f00] transition-colors">
              <span>कवच ऑर्डर करें</span>
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
          <span class="text-[#a53936] font-bold text-xs uppercase tracking-widest">सरल एवं पारदर्शी प्रक्रिया</span>
          <h2 class="font-['Noto_Serif',serif] text-2xl md:text-3xl font-bold text-[#8d4b00] mt-1">
            घर बैठे {c_hi} से ऑनलाइन संकल्प व पूजा कराने के 3 आसान चरण
          </h2>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">

          <!-- Step 1 -->
          <div class="bg-white rounded-2xl p-6 border border-[#dbc2b0] shadow-sm relative flex flex-col items-center text-center">
            <div class="w-10 h-10 rounded-full bg-[#8d4b00] text-white flex items-center justify-center font-bold text-base mb-4">
              1
            </div>
            <h4 class="font-['Noto_Serif',serif] font-bold text-base text-[#1d1c15] mb-2">विवरण एवं संकल्प जानकारी भेजें</h4>
            <p class="text-xs text-[#554336] leading-relaxed">
              आप अपना नाम, गोत्र, जन्म तिथि (यदि उपलब्ध हो) एवं अपनी समस्या WhatsApp या कॉल द्वारा पंडित जी को बताएं।
            </p>
          </div>

          <!-- Step 2 -->
          <div class="bg-white rounded-2xl p-6 border border-[#dbc2b0] shadow-sm relative flex flex-col items-center text-center">
            <div class="w-10 h-10 rounded-full bg-[#8d4b00] text-white flex items-center justify-center font-bold text-base mb-4">
              2
            </div>
            <h4 class="font-['Noto_Serif',serif] font-bold text-base text-[#1d1c15] mb-2">लाइव दर्शन एवं वैदिक आहुति</h4>
            <p class="text-xs text-[#554336] leading-relaxed">
              शुभ मुहूर्त पर नलखेड़ा सिद्धपीठ की अखंड धूनी के समक्ष आपके नाम से लाइव वीडियो कॉल पर संकल्प एवं हवन संपन्न कराया जाएगा।
            </p>
          </div>

          <!-- Step 3 -->
          <div class="bg-white rounded-2xl p-6 border border-[#dbc2b0] shadow-sm relative flex flex-col items-center text-center">
            <div class="w-10 h-10 rounded-full bg-[#8d4b00] text-white flex items-center justify-center font-bold text-base mb-4">
              3
            </div>
            <h4 class="font-['Noto_Serif',serif] font-bold text-base text-[#1d1c15] mb-2">सिद्ध भस्म व प्रसाद {c_hi} में प्राप्त करें</h4>
            <p class="text-xs text-[#554336] leading-relaxed">
              हवन समाप्ति के बाद अभिमंत्रित रक्षा सूत्र, सिद्ध भस्म, माँ की चुनरी व प्रसाद स्पीड पोस्ट/कूरियर से आपके {c_hi} के पते पर भेजा जाएगा।
            </p>
          </div>

        </div>

        <!-- Banner inside Step Section -->
        <div class="mt-8 rounded-xl bg-[#ffdcc3]/50 border border-[#b15f00]/30 p-4 md:p-6 flex flex-col sm:flex-row items-center justify-between gap-4 text-center sm:text-left">
          <div class="flex items-center gap-3">
            <span class="material-symbols-outlined text-[#8d4b00] text-[32px]">support_agent</span>
            <div>
              <p class="font-bold text-[#8d4b00] text-sm md:text-base">क्या आप व्यक्तिगत रूप से नलखेड़ा धाम आना चाहते हैं?</p>
              <p class="text-xs text-[#554336]">यदि आप {c_hi} से नलखेड़ा धाम आकर पूजा कराना चाहते हैं, तो पूर्व सूचना देकर समय व विश्राम व्यवस्था सुनिश्चित करें।</p>
            </div>
          </div>
          <a href="tel:+918769084789" class="px-5 py-2.5 rounded-full bg-[#8d4b00] text-white text-xs font-bold hover:bg-[#b15f00] transition-colors shrink-0 whitespace-nowrap">
            आगमन हेतु बात करें
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
          "{c_hi} में रहते हुए हमने पिछले महीने कोर्ट विवाद के निवारण हेतु पंडित हर्षित शर्मा जी से बगलामुखी अनुष्ठान करवाया। पंडित जी ने पूरी पारदर्शिता के साथ लाइव वीडियो पर संकल्प कराया और 3 दिन के भीतर प्रसाद हमें स्पीड पोस्ट से मिल गया। माँ की कृपा से फैसला हमारे पक्ष में रहा।"
        </blockquote>
        <div class="mt-4 flex items-center justify-center gap-2">
          <div class="w-8 h-8 rounded-full bg-[#ffdcc3] text-[#8d4b00] font-bold text-xs flex items-center justify-center">
            भक्त
          </div>
          <div class="text-left">
            <p class="text-xs font-bold text-[#1d1c15]">सत्येंद्र कुमार जी एवं परिवार</p>
            <p class="text-[11px] text-[#554336]">यजमान • {c_hi} ({s_hi})</p>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 5: FAQS (ACCORDION) -->
    <section class="py-14 px-4 md:px-8 bg-[#f2ede3]">
      <div class="max-w-[850px] mx-auto">
        <div class="text-center mb-8">
          <span class="text-[#a53936] font-bold text-xs uppercase tracking-widest">शंका समाधान</span>
          <h2 class="font-['Noto_Serif',serif] text-2xl font-bold text-[#8d4b00] mt-1">
            {c_hi} पूजा एवं अनुष्ठान के संबंध में अक्सर पूछे जाने वाले प्रश्न
          </h2>
        </div>

        <div class="flex flex-col gap-3">

          <details class="bg-white rounded-xl p-4 border border-[#dbc2b0] shadow-sm group">
            <summary class="font-bold text-sm text-[#1d1c15] cursor-pointer flex items-center justify-between">
              <span>क्या {c_hi} में रहकर ऑनलाइन वीडियो कॉल पर पूजा का पूरा फल मिलता है?</span>
              <span class="material-symbols-outlined text-[20px] text-[#8d4b00] group-open:rotate-180 transition-transform">expand_more</span>
            </summary>
            <p class="text-xs text-[#554336] mt-2.5 leading-relaxed">
              हाँ, शास्त्रों के अनुसार संकल्प में यजमान का नाम, गोत्र और स्थान सबसे महत्वपूर्ण होता है। जब पंडित जी सिद्ध पीठ नलखेड़ा की जागृत अग्नि में आपके नाम-गोत्र का उच्चारण कर आहुति देते हैं, तो फल साक्षात प्राप्त होता है।
            </p>
          </details>

          <details class="bg-white rounded-xl p-4 border border-[#dbc2b0] shadow-sm group">
            <summary class="font-bold text-sm text-[#1d1c15] cursor-pointer flex items-center justify-between">
              <span>पूजा का प्रसाद और सिद्ध रक्षा सूत्र {c_hi} में कितने दिन में पहुंचेगा?</span>
              <span class="material-symbols-outlined text-[20px] text-[#8d4b00] group-open:rotate-180 transition-transform">expand_more</span>
            </summary>
            <p class="text-xs text-[#554336] mt-2.5 leading-relaxed">
              अनुष्ठान पूर्ण होने के अगले ही दिन भारतीय डाक (Speed Post) अथवा प्रतिष्ठित निजी कूरियर से प्रसाद रवाना कर दिया जाता है। साधारणतया 2 से 4 कार्यदिवसों में {c_hi} स्थित आपके पते पर सामग्री सुरक्षित पहुंच जाती है।
            </p>
          </details>

          <details class="bg-white rounded-xl p-4 border border-[#dbc2b0] shadow-sm group">
            <summary class="font-bold text-sm text-[#1d1c15] cursor-pointer flex items-center justify-between">
              <span>पूजा की दक्षिणा एवं सामग्री का शुल्क क्या रहेगा?</span>
              <span class="material-symbols-outlined text-[20px] text-[#8d4b00] group-open:rotate-180 transition-transform">expand_more</span>
            </summary>
            <p class="text-xs text-[#554336] mt-2.5 leading-relaxed">
              दक्षिणा अनुष्ठान के प्रकार (लघु हवन, संपुटित पाठ, अथवा सवा लाख मंत्र जाप) तथा लगने वाले ब्राह्मणों की संख्या पर निर्भर करती है। पंडित जी से सीधे फोन या WhatsApp (+91 87690 84789) पर बात करके न्यूनतम एवं उचित व्यय की जानकारी प्राप्त कर सकते हैं।
            </p>
          </details>

          <details class="bg-white rounded-xl p-4 border border-[#dbc2b0] shadow-sm group">
            <summary class="font-bold text-sm text-[#1d1c15] cursor-pointer flex items-center justify-between">
              <span>क्या पंडित जी व्यक्तिगत अनुष्ठान हेतु {c_hi} भी आ सकते हैं?</span>
              <span class="material-symbols-outlined text-[20px] text-[#8d4b00] group-open:rotate-180 transition-transform">expand_more</span>
            </summary>
            <p class="text-xs text-[#554336] mt-2.5 leading-relaxed">
              हाँ, विशेष महायज्ञ, गृह प्रवेश, शतचंडी अनुष्ठान अथवा बड़े प्रतिष्ठानों के उद्घाटन हेतु यजमानों के विशेष अनुरोध पर पंडित हर्षित शर्मा जी {c_hi} आकर भी विधिपूर्वक अनुष्ठान संपन्न कराते हैं। इसके लिए कम से कम 10 दिन पूर्व बुकिंग अनिवार्य है।
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
            {s_hi} के अन्य प्रमुख शहरों में पूजा सेवाएं:
          </h3>
          <a href="../locations.html" class="text-xs font-bold text-[#a53936] hover:underline flex items-center gap-1">
            <span>सभी 36 राज्य देखें</span>
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
            <span class="font-['Noto_Serif',serif] font-bold text-base text-[#8d4b00]">पंडित हर्षित शर्मा</span>
          </div>
          <p class="text-xs text-[#554336] leading-relaxed">
            माँ बगलामुखी धाम नलखेड़ा के अधिकृत वैदिक पुरोहित। {c_hi} ({s_hi}) सहित संपूर्ण भारत में ऑनलाइन व ऑफलाइन पूजा संपन्न कराने के लिए समर्पित।
          </p>
        </div>

        <!-- Col 2 -->
        <div class="flex flex-col gap-2.5">
          <span class="font-['Noto_Serif',serif] font-bold text-sm text-[#8d4b00]">प्रमुख सेवाएं</span>
          <div class="flex flex-col gap-1.5 text-xs text-[#554336]">
            <a class="hover:text-[#8d4b00]" href="../services.html">माँ बगलामुखी अनुष्ठान</a>
            <a class="hover:text-[#8d4b00]" href="../services.html">कोर्ट केस विजय हवन</a>
            <a class="hover:text-[#8d4b00]" href="../services.html">नवग्रह शांति व कालसर्प दोष</a>
            <a class="hover:text-[#8d4b00]" href="../services.html">ऋण मुक्ति व व्यापार वृद्धि</a>
            <a class="hover:text-[#8d4b00]" href="../locations.html">स्थान निर्देशिका (36 राज्य)</a>
          </div>
        </div>

        <!-- Col 3 -->
        <div class="flex flex-col gap-2.5">
          <span class="font-['Noto_Serif',serif] font-bold text-sm text-[#8d4b00]">सिद्धपीठ नलखेड़ा का पता</span>
          <p class="text-xs text-[#554336] leading-relaxed">
            लखुंदर नदी तट, विश्व प्रसिद्ध माँ बगलामुखी मंदिर, नलखेड़ा, जिला आगर मालवा (म.प्र.) - 465445
          </p>
          <a href="https://www.google.com/maps/search/Maa+Baglamukhi+Mandir+Nalkheda" target="_blank" class="inline-flex items-center gap-1 text-xs text-[#8d4b00] font-bold hover:underline">
            <span class="material-symbols-outlined text-[15px]">near_me</span>
            <span>Google Maps पर देखें</span>
          </a>
        </div>

        <!-- Col 4 -->
        <div class="flex flex-col gap-2.5">
          <span class="font-['Noto_Serif',serif] font-bold text-sm text-[#8d4b00]">सीधा संपर्क केंद्र</span>
          <div class="text-xs text-[#554336] flex flex-col gap-1">
            <p class="font-bold text-[#1d1c15] text-sm">+91 87690 84789</p>
            <p class="font-bold text-[#1d1c15] text-sm">+91 91658 76908</p>
            <p class="text-[11px] text-[#006b2f] font-semibold mt-1">प्रातः 6:00 से रात्रि 11:00 बजे तक</p>
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
        <p>© 2026 पंडित हर्षित शर्मा। सर्वाधिकार सुरक्षित। ({c_hi} पूजा सेवा पृष्ठ)</p>
        <p>शुद्ध वैदिक सात्विक परंपरा • नाम-गोत्र लाइव संकल्प</p>
      </div>
    </div>
  </footer>

  <!-- FLOATING CALL & WHATSAPP BUTTONS -->
  <div class="fixed bottom-4 right-4 z-50 flex flex-col gap-2.5">
    <a href="https://wa.me/918769084789?text=प्रणाम%20पंडित%20जी,%20मैं%20{c_hi}%20से%20बात%20कर%20रहा/रही%20हूँ।" target="_blank" class="w-12 h-12 rounded-full bg-[#25d366] text-white flex items-center justify-center shadow-xl hover:scale-110 transition-transform" title="WhatsApp पर बात करें">
      <span class="material-symbols-outlined text-[26px]">chat</span>
    </a>
    <a href="tel:+918769084789" class="w-12 h-12 rounded-full bg-[#8d4b00] text-white flex items-center justify-center shadow-xl hover:scale-110 transition-transform" title="फोन पर बात करें">
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
              <span>{c_hi} ({c_en})</span>
            </a>'''

        states_cards_html += f'''
        <div class="state-card bg-[#fef9ee] rounded-2xl p-6 border border-[#dbc2b0] shadow-sm hover:shadow-md transition-shadow" data-state="{s_en.lower()} {s_hi.lower()}">
          <div class="flex items-center justify-between pb-3 mb-4 border-b border-[#dbc2b0]/50">
            <div class="flex items-center gap-3">
              <span class="w-8 h-8 rounded-full bg-[#8d4b00] text-white flex items-center justify-center font-bold text-xs">{idx}</span>
              <div>
                <h3 class="font-['Noto_Serif',serif] font-bold text-lg text-[#1d1c15]">{s_hi}</h3>
                <span class="text-xs text-[#554336]">{s_en} • {len(state['cities'])} प्रमुख शहर</span>
              </div>
            </div>
            <span class="text-xs font-bold text-[#006b2f] bg-[#95f8a7]/40 px-2.5 py-1 rounded-full">सेवा उपलब्ध</span>
          </div>
          <div class="flex flex-wrap gap-2">
            {cities_pills_html}
          </div>
        </div>'''

    return f'''<!DOCTYPE html>
<html lang="hi">
<head>
  <meta charset="utf-8"/>
  <meta content="width=device-width, initial-scale=1.0" name="viewport"/>
  <title>भारत के 36 राज्यों व 446+ शहरों में पूजा सेवाएं | पंडित हर्षित शर्मा नलखेड़ा धाम</title>
  <meta name="description" content="पंडित हर्षित शर्मा जी द्वारा भारत के सभी राज्यों (मध्य प्रदेश, उत्तर प्रदेश, राजस्थान, दिल्ली, महाराष्ट्र, गुजरात आदि) में माँ बगलामुखी धाम नलखेड़ा से विशेष लाइव संकल्प व हवन सेवा।"/>
  <link rel="canonical" href="https://panditharshitsharma.com/locations.html"/>
  <meta property="og:type" content="website"/>
  <meta property="og:url" content="https://panditharshitsharma.com/locations.html"/>
  <meta property="og:title" content="भारत के 36 राज्यों व 446+ शहरों में पूजा सेवाएं | पंडित हर्षित शर्मा"/>
  <meta property="og:description" content="माँ बगलामुखी धाम नलखेड़ा से भारत के सभी राज्यों व 446+ शहरों में विशेष लाइव संकल्प व हवन सेवा।"/>
  <meta property="og:image" content="https://panditharshitsharma.com/logo.webp"/>
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
    "name": "पंडित हर्षित शर्मा - अखिल भारतीय पूजा निर्देशिका",
    "url": "https://panditharshitsharma.com/locations.html",
    "telephone": "+918769084789",
    "image": "https://panditharshitsharma.com/logo.webp",
    "description": "भारत के सभी 36 राज्यों व 446+ शहरों में माँ बगलामुखी धाम नलखेड़ा से विशेष लाइव संकल्प एवं हवन सेवाएं।"
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
          <span>महाभारत कालीन विश्व प्रसिद्ध सिद्धपीठ • नलखेड़ा (म.प्र.) | संपूर्ण भारत में पूजा सेवाएं</span>
        </div>
        <div class="flex items-center gap-4">
          <a href="tel:+918769084789" class="flex items-center gap-1 hover:text-[#ffdad7]">
            <span class="material-symbols-outlined text-[14px]">call</span>
            <span class="font-bold">+91 87690 84789</span>
          </a>
          <a href="https://wa.me/918769084789" target="_blank" class="flex items-center gap-1 text-[#95f8a7] font-bold hover:underline">
            <span>WhatsApp करें</span>
          </a>
        </div>
      </div>
    </div>

    <!-- MAIN NAVBAR -->
    <div class="h-20 max-w-[1200px] mx-auto px-4 md:px-8 flex items-center justify-between gap-2">
      <a href="index.html" class="flex items-center gap-3">
        <img src="./logo.webp" alt="पंडित हर्षित शर्मा" class="w-11 h-11 md:w-13 md:h-13 rounded-full object-cover shadow-md border-2 border-[#b15f00]"/>
        <div class="flex flex-col">
          <span class="font-['Noto_Serif',serif] font-bold text-base md:text-xl text-[#8d4b00] leading-tight">पंडित हर्षित शर्मा</span>
          <span class="text-[11px] text-[#a53936] font-semibold tracking-wide">माँ बगलामुखी धाम नलखेड़ा</span>
        </div>
      </a>

      <nav class="hidden md:flex items-center gap-6 text-sm font-semibold text-[#554336]">
        <a class="hover:text-[#8d4b00] transition-colors" href="index.html">होम</a>
        <a class="hover:text-[#8d4b00] transition-colors" href="services.html">सेवाएं</a>
        <a class="hover:text-[#8d4b00] transition-colors" href="gallery.html">गैलरी</a>
        <a class="text-[#8d4b00] font-bold border-b-2 border-[#8d4b00] pb-0.5" href="locations.html">स्थान निर्देशिका</a>
        <a class="hover:text-[#8d4b00] transition-colors" href="contact.html">संपर्क</a>
      </nav>

      <a href="tel:+918769084789" class="inline-flex items-center gap-1.5 px-4 py-2 rounded-full bg-[#8d4b00] text-white text-xs font-bold shadow-md hover:bg-[#b15f00] transition-all">
        <span class="material-symbols-outlined text-[16px]">call</span>
        <span>परामर्श लें</span>
      </a>
    </div>
  </header>

  <main class="w-full pt-28 md:pt-32 pb-16">

    <!-- HERO -->
    <section class="bg-gradient-to-b from-[#f2ede3] to-[#fef9ee] px-4 md:px-8 py-12 text-center border-b border-[#dbc2b0]/50">
      <div class="max-w-[800px] mx-auto flex flex-col gap-3">
        <div class="inline-flex items-center gap-1.5 self-center px-3.5 py-1.5 rounded-full bg-[#ffdcc3] text-[#2f1500] text-xs font-bold shadow-sm">
          <span class="material-symbols-outlined text-[#8d4b00] text-[16px]">public</span>
          <span>अखिल भारतीय वैदिक अनुष्ठान निर्देशिका (36 राज्य एवं केंद्र शासित प्रदेश)</span>
        </div>
        <h1 class="font-['Noto_Serif',serif] text-2xl sm:text-3xl md:text-4xl font-bold text-[#8d4b00] leading-tight">
          आपके शहर में पंडित हर्षित शर्मा जी की वैदिक पूजा एवं हवन सेवाएं
        </h1>
        <p class="text-xs sm:text-sm text-[#554336] leading-relaxed">
          आप भारत के किसी भी राज्य अथवा शहर में हों, माँ बगलामुखी के पावन सिद्धपीठ नलखेड़ा धाम से अपने नाम-गोत्र पर सीधा लाइव वीडियो संकल्प द्वारा विशेष पूजा संपन्न कराएं। नीचे अपने राज्य अथवा शहर का चयन करें।
        </p>

        <!-- SEARCH INPUT -->
        <div class="max-w-md mx-auto w-full mt-4 relative">
          <span class="material-symbols-outlined absolute left-4 top-3 text-[#8d4b00]">search</span>
          <input type="text" id="citySearch" placeholder="अपने शहर या राज्य का नाम खोजें (उदा. इंदौर, लखनऊ, जयपुर)..." onkeyup="filterLocations()" class="w-full pl-12 pr-4 py-3 rounded-full border-2 border-[#dbc2b0] focus:border-[#8d4b00] outline-none text-xs sm:text-sm bg-white shadow-sm"/>
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
      <p class="font-['Noto_Serif',serif] text-[#8d4b00] font-bold text-sm mb-1">पंडित हर्षित शर्मा • माँ बगलामुखी धाम नलखेड़ा (म.प्र.)</p>
      <p>© 2026 सर्वाधिकार सुरक्षित। हेल्पलाइन: +91 87690 84789 | +91 91658 76908</p>
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
        ('index.html', '1.0', 'daily'),
        ('services.html', '0.9', 'weekly'),
        ('gallery.html', '0.8', 'weekly'),
        ('contact.html', '0.8', 'monthly'),
        ('locations.html', '0.9', 'daily')
    ]
    for page, priority, freq in core_pages:
        xml += f'  <url>\n    <loc>https://panditharshitsharma.com/{page}</loc>\n    <changefreq>{freq}</changefreq>\n    <priority>{priority}</priority>\n  </url>\n'

    # City pages
    for city in all_cities_flat:
        xml += f'  <url>\n    <loc>https://panditharshitsharma.com/puja-in/{city["slug"]}.html</loc>\n    <changefreq>weekly</changefreq>\n    <priority>0.8</priority>\n  </url>\n'

    xml += '</urlset>'
    return xml

with open(os.path.join(os.path.dirname(__file__), 'sitemap.xml'), 'w', encoding='utf-8') as f:
    f.write(generate_sitemap_xml())

print("Successfully generated sitemap.xml with all cities!")

# Generate robots.txt
def generate_robots_txt():
    return '''User-agent: *
Allow: /

Sitemap: https://panditharshitsharma.com/sitemap.xml
'''

with open(os.path.join(os.path.dirname(__file__), 'robots.txt'), 'w', encoding='utf-8') as f:
    f.write(generate_robots_txt())

print("Successfully generated robots.txt!")
