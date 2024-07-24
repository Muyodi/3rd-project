words_list = [
 "Apple", "Mela" ,  "Banana", "Banana" ,  "Orange", "Arancia" ,  "Grapes", "Uva" ,  "Watermelon", "Anguria" ,  
 "Pineapple", "Ananas" ,  "Strawberry", "Fragola" ,  "Cherry", "Ciliegia" ,  "Lemon", "Limone" ,  "Peach", 
 "Pesca" ,  "Plum", "Prugna" ,  "Apricot", "Albicocca" ,  "Pear", "Pera" ,  "Fig", "Fico" ,  "Kiwi", "Kiwi" , 
  "Tomato", "Pomodoro" ,  "Cucumber", "Cetriolo" ,  "Carrot", "Carota" ,  "Potato", "Patata" ,  
  "Onion", "Cipolla" ,  "Garlic", "Aglio" ,  "Lettuce", "Lattuga" ,  "Spinach", "Spinaci" , 
   "Broccoli", "Broccoli" ,  "Cauliflower", "Cavolfiore" ,  "Cabbage", "Cavolo" ,  "Pumpkin", "Zucca" , 
    "Mushroom", "Fungo" ,  "Eggplant", "Melanzana" ,  "Zucchini", "Zucchina" ,  "Corn", "Mais" , 
     "Rice", "Riso" ,  "Bread", "Pane" ,  "Butter", "Burro" ,  "Cheese", "Formaggio" ,  "Milk", "Latte" ,  
     "Yogurt", "Yogurt" ,  "Egg", "Uovo" ,  "Chicken", "Pollo" ,  "Beef", "Manzo" ,  "Pork", "Maiale" , 
      "Fish", "Pesce" ,  "Shrimp", "Gamberetto" ,  "Crab", "Granchio" ,  "Lobster", "Aragosta" , 
       "Salmon", "Salmone" ,  "Tuna", "Tonno" ,  "Soup", "Zuppa" ,  "Salad", "Insalata" , 
        "Sandwich", "Panino" ,  "Pizza", "Pizza" ,  "Pasta", "Pasta" ,  "Noodles", "Tagliatelle" , 
         "Coffee", "Caffè" ,  "Tea", "Tè" ,  "Juice", "Succo" ,  "Water", "Acqua" ,  "Wine", "Vino" ,  
         "Beer", "Birra" ,  "Sugar", "Zucchero" ,  "Salt", "Sale" ,  "Pepper", "Pepe" ,  "Vinegar", 
         "Aceto" ,  "Oil", "Olio" ,  "Butter", "Burro" ,  "Honey", "Miele" ,  "Jam", "Marmellata" ,  
         "Chocolate", "Cioccolato" ,  "Cake", "Torta" ,  "Cookie", "Biscotto" ,  "Pie", "Crostata" , 
          "Ice cream", "Gelato" ,  "Candy", "Caramella" ,  "Snack", "Spuntino" ,  "Breakfast", 
          "Colazione" ,  "Lunch", "Pranzo" ,  "Dinner", "Cena" ,  "Meal", "Pasto" ,  "Recipe", 
          "Ricetta" ,  "Knife", "Coltello" ,  "Fork", "Forchetta" ,  "Spoon", "Cucchiaio" ,  
          "Plate", "Piatto" ,  "Bowl", "Ciotola" ,  "Glass", "Bicchiere" ,  "Cup", "Tazza" , 
           "Napkin", "Tovagliolo" ,  "Table", "Tavolo" ,  "Chair", "Sedia" ,  "House", "Casa" ,  
           "Apartment", "Appartamento" ,  "Room", "Stanza" ,  "Kitchen", "Cucina" ,  "Bathroom",
            "Bagno" ,  "Bedroom", "Camera da letto" ,  "Living room", "Soggiorno" ,  "Garden", 
            "Giardino" ,  "Garage", "Garage" ,  "Door", "Porta" ,  "Window", "Finestra" ,  "Floor", 
            "Pavimento" ,  "Ceiling", "Soffitto" ,  "Wall", "Muro" ,  "Roof", "Tetto" ,  "Furniture", 
            "Mobili" ,  "Sofa", "Divano" ,  "Bed", "Letto" ,  "Chair", "Sedia" ,  "Table", "Tavolo" ,  
            "Desk", "Scrivania" ,  "Lamp", "Lampada" ,  "Fan", "Ventilatore" ,  "Computer", "Computer" ,  
            "Phone", "Telefono" ,  "Television", "Televisione" ,  "Radio", "Radio" ,  "Camera", 
            "Macchina fotografica" ,  "Clock", "Orologio" ,  "Watch", "Orologio da polso" ,  "Book", "Libro" ,  
            "Pen", "Penna" ,  "Pencil", "Matita" ,  "Notebook", "Quaderno" ,  "Paper", "Carta" ,  "Scissors", 
            "Forbici" ,  "Glue", "Colla" ,  "Tape", "Nastro adesivo" ,  "Bag", "Borsa" ,  "Backpack", "Zaino" ,  
            "Wallet", "Portafoglio" ,  "Key", "Chiave" ,  "Umbrella", "Ombrello" ,  "Shoe", "Scarpa" ,  "Sock", 
            "Calzino" ,  "Shirt", "Camicia" ,  "T-shirt", "Maglietta" ,  "Pants", "Pantaloni" ,  "Shorts", 
            "Pantaloncini" ,  "Dress", "Vestito" ,  "Skirt", "Gonna" ,  "Coat", "Cappotto" ,  "Jacket", "Giacca" , 
             "Hat", "Cappello" ,  "Gloves", "Guanti" ,  "Scarf", "Sciarpa" ,  "Belt", "Cintura" ,  "Ring", 
             "Anello" ,  "Necklace", "Collana" ,  "Bracelet", "Braccialetto" ,  "Earrings", "Orecchini" ,  
             "Glass", "Bicchiere" ,  "Plastic", "Plastica" ,  "Metal", "Metallo" ,  "Wood", "Legno" ,  "Paper", 
             "Carta" ,  "Fabric", "Tessuto" ,  "Leather", "Pelle" ,  "Stone", "Pietra" ,  "Brick", "Mattone" , 
              "Concrete", "Cemento" ,  "Ceramic", "Ceramica" ,  "Water", "Acqua" ,  "Fire", "Fuoco" ,  "Air",
               "Aria" ,  "Earth", "Terra" ,  "Sun", "Sole" ,  "Moon", "Luna" ,  "Star", "Stella" ,  "Sky", 
               "Cielo" ,  "Cloud", "Nuvola" ,  "Rain", "Pioggia" ,  "Snow", "Neve" ,  "Wind", "Vento" ,  "Storm", 
               "Tempesta" ,  "Thunder", "Tuono" ,  "Lightning", "Fulmine" ,  "Weather", "Meteo" ,  "Temperature", 
               "Temperatura" ,  "Hot", "Caldo" ,  "Cold", "Freddo" ,  "Warm", "Tiepido" ,  "Cool", "Fresco" ,  
               "Day", "Giorno" ,  "Night", "Notte" ,  "Morning", "Mattina" ,  "Afternoon", "Pomeriggio" ,  
               "Evening", "Sera" ,  "Week", "Settimana" ,  "Month", "Mese" ,  "Year", "Anno" ,  "Today", "Oggi" , 
                "Yesterday", "Ieri" ,  "Tomorrow", "Domani" , 
  "Spring", "Primavera" ,  "Summer", "Estate" ,  "Fall", "Autunno" ,  "Winter", 
  "Inverno"

]