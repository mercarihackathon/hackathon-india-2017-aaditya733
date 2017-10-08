#Created by Aaditya Sanjay Boob, IIT Kharagpur.

tag = [None] * 100
social_unit = [None] * 100
leisure_unit = [None] * 100
work_unit = [None] * 100
health_unit = [None] * 100
uncategorized_unit = [None] * 100
time_spent = [0] * 100

workeff = 1

inf = 10000

#Function for updating Google Maps API initial values

def update_values(index,tag_name,social,leisure,work,health,uncategorized):
	tag[index] = tag_name
	social_unit[index] = social
	leisure_unit[index] = leisure
	work_unit[index] = work
	health_unit[index] = health
	uncategorized_unit[index] = uncategorized

#Google Maps API places classification values initialsed

update_values(0,"null",0,0,0,0,0)
update_values(1,"accounting",0,0,20,0,10)
update_values(2,"airport",0,10,10,0,10)
update_values(3,"amusement_park",30,60,0,0,0)
update_values(4,"aquarium",0,40,0,0,0)
update_values(5,"art_gallery",0,40,0,0,0)
update_values(6,"atm",0,0,0,0,10)
update_values(7,"bakery",0,0,0,0,15)
update_values(8,"bank",0,0,30,0,0)
update_values(9,"bar",40,20,0,0,0)
update_values(10,"beauty_salon",0,20,0,0,0)
update_values(11,"bicycle_store",0,10,0,0,40)
update_values(12,"book_store",0,10,0,0,20)
update_values(13,"bowling_alley",35,15,0,0,0)
update_values(14,"bus_station",0,0,0,0,10)
update_values(15,"cafe",60,0,0,0,0)
update_values(16,"campground",55,25,0,10,0)
update_values(17,"car_dealer",0,0,0,0,50)
update_values(18,"car_rental",0,0,0,0,50)
update_values(19,"car_repair",0,0,0,0,30)
update_values(20,"car_wash",0,0,0,0,20)
update_values(21,"casino",0,80,0,0,0)
update_values(22,"cemetery",-80,0,0,0,0)
update_values(23,"church",30,10,0,0,0)
update_values(24,"city_hall",100,0,0,0,0)
update_values(25,"clothing_store",0,40,0,0,0)
update_values(26,"convenience_store",0,0,0,0,15)
update_values(27,"courthouse",-40,0,-30,0,0)
update_values(28,"dentist",0,0,-30,0,0)
update_values(29,"department_store",0,0,0,0,15)
update_values(30,"doctor",0,0,0,0,-50)
update_values(31,"electrician",0,0,0,0,40)
update_values(32,"electronics_store",0,0,0,0,50)
update_values(33,"embassy",0,0,0,0,100)
update_values(34,"establishment",0,0,0,0,30)
update_values(35,"finance",0,0,30,0,0)
update_values(36,"fire_station",-50,0,0,0,0)
update_values(37,"florist",10,0,0,0,0)
update_values(38,"food",60,0,0,0,0)
update_values(39,"funeral_home",-100,0,0,0,0)
update_values(40,"furniture_store",0,30,0,0,0)
update_values(41,"gas_station",0,0,0,0,10)
update_values(42,"general_contractor",0,0,0,0,30)
update_values(43,"grocery_or_supermarpket",0,0,0,0,15)
update_values(44,"gym",0,0,0,100,0)
update_values(45,"hair_care",0,20,0,0,0)
update_values(46,"hardware_store",0,0,0,0,30)
update_values(47,"health",0,0,0,90,0)
update_values(48,"hindu_temple",30,10,0,0,0)
update_values(49,"home_goods_store",0,40,0,0,0)
update_values(50,"hospital",0,0,0,-100,0)
update_values(51,"insurance_agency",0,0,20,0,0)
update_values(52,"jewelry_store",0,40,0,0,0)
update_values(53,"laundry",0,0,0,0,15)
update_values(54,"lawyer",-15,0,-25,0,0)
update_values(55,"library",0,30,20,0,0)
update_values(56,"liquor_store",0,0,0,0,25)
update_values(57,"local_government_office",0,0,30,0,0)
update_values(58,"locksmith",0,0,0,0,60)
update_values(59,"lodging",50,0,0,0,0)
update_values(60,"meal_delivery",0,25,0,0,0)
update_values(61,"meal_takeaway",0,25,0,0,0)
update_values(62,"mosque",30,10,0,0,0)
update_values(63,"movie_rental",0,50,0,0,0)
update_values(64,"movie_theater",0,70,0,0,0)
update_values(65,"moving_company",0,0,0,0,50)
update_values(66,"museum",0,40,0,0,0)
update_values(67,"night_club",10,80,0,0,0)
update_values(68,"painter",0,0,0,0,70)
update_values(69,"park",20,0,45,0,0)
update_values(70,"parking",0,0,0,0,10)
update_values(71,"pet_store",0,10,0,0,0)
update_values(72,"pharmacy",0,0,0,-10,0)
update_values(73,"physiotherapist",0,0,0,-30,0)
update_values(74,"place_of_worship",30,10,0,0,0)
update_values(75,"plumber",0,0,0,0,40)
update_values(76,"police",-75,0,-25,0,0)
update_values(77,"post_office",0,0,0,0,30)
update_values(78,"real_estate_agency",0,0,0,0,40)
update_values(79,"restaurant",40,20,0,0,0)
update_values(80,"roofing_contractor",0,0,0,0,40)
update_values(81,"rv_park",0,0,0,0,20)
update_values(82,"school",10,0,0,0,30)
update_values(83,"shoe_store",0,30,0,0,0)
update_values(84,"shopping_mall",10,40,0,0,0)
update_values(85,"spa",0,40,0,0,0)
update_values(86,"stadium",0,20,0,40,0)
update_values(87,"storage",0,0,0,0,30)
update_values(88,"store",0,0,0,0,15)
update_values(89,"subway_station",0,0,0,0,10)
update_values(90,"synagogue",100,0,0,0,0)
update_values(91,"taxi_stand",0,0,0,0,10)
update_values(92,"train_station",0,0,0,0,10)
update_values(93,"transit_station",0,0,0,0,10)
update_values(94,"travel_agency",0,0,0,0,50)
update_values(95,"university",10,0,20,0,10)
update_values(96,"veterinary_care",0,0,0,0,70)
update_values(97,"zoo",40,20,0,0,0)
update_values(98,"home_bookmark",10,75,0,5,10)
update_values(99,"work_bookmark",0,0,workeff*100,0,(1-workeff)*100)

# for i in range(100):
# 	print tag[i]+"\t"+ str(social_unit[i]) +"\t"+ str(leisure_unit[i]) +"\t"+ str(work_unit[i]) +"\t"+ str(health_unit[i]) +"\t"+ str(uncategorized_unit[i]) + "\n"

social_time = 0.0
social_score = 0.0
leisure_time = 0.0
leisure_score = 0.0
work_time = 0.0
work_score = 0.0
health_time = 0.0
health_score = 0.0
uncategorized_time = 0.0
uncategorized_score = 0.0

#Updating above values from user's input

F = open("input2.txt","r")
all_visited = F.readlines()
for i in range(len(all_visited)):
	place = all_visited[i].split()[0]
	time = int(all_visited[i].split()[1])
	time_spent[tag.index(place)] += time

for i in range(1,len(tag)):
	social_score += time_spent[i]*social_unit[i]
	leisure_score += time_spent[i]*leisure_unit[i]
	work_score += time_spent[i]*work_unit[i]
	health_score += time_spent[i]*health_unit[i]
	uncategorized_score += time_spent[i]*uncategorized_unit[i]
	social_time += time_spent[i]*(1.0*abs(social_unit[i])/(abs(social_unit[i])+abs(leisure_unit[i])+abs(health_unit[i])+abs(work_unit[i])+abs(uncategorized_unit[i])))
	leisure_time += time_spent[i]*(1.0*abs(leisure_unit[i])/(abs(social_unit[i])+abs(leisure_unit[i])+abs(health_unit[i])+abs(work_unit[i])+abs(uncategorized_unit[i])))
	work_time += time_spent[i]*(1.0*abs(work_unit[i])/(abs(social_unit[i])+abs(leisure_unit[i])+abs(health_unit[i])+abs(work_unit[i])+abs(uncategorized_unit[i])))
	health_time += time_spent[i]*(1.0*abs(health_unit[i])/(abs(social_unit[i])+abs(leisure_unit[i])+abs(health_unit[i])+abs(work_unit[i])+abs(uncategorized_unit[i])))
	uncategorized_time += time_spent[i]*(1.0*abs(uncategorized_unit[i])/(abs(social_unit[i])+abs(leisure_unit[i])+abs(health_unit[i])+abs(work_unit[i])+abs(uncategorized_unit[i])))

print "Social Score:" + "\t" + str(social_score) + "\t" + "Social Time:" + "\t" + str(social_time)
print "Work Score:" + "\t" + str(work_score) + "\t" + "Work Time:" + "\t" + str(work_time)
print "leisure Score:" + "\t" + str(leisure_score) + "\t" + "Leisure Time:" + "\t" + str(leisure_time)
print "Health Score:" + "\t" + str(health_score) + "\t" + "Health Time:" + "\t" + str(health_time)
print "Uncategorized Score:" + "\t" + str(uncategorized_score) + "\t" + "Uncategorized Time:" + "\t" + str(uncategorized_time)

#Trapeziodal Membership Functions

def value(var,input):
	if(input < var[0]):
		return 0.0
	elif(input>var[0] and input<= var[1]):
		return 1.0*(input-var[0])/(var[1]-var[0])
	elif(input>var[1] and input<= var[2]):
		return 1.0
	elif(input>var[2] and input<=var[3]):
		return 1.0*(var[3]-input)/(var[3]-var[2])
	else:
		return 0.0

# Updating & Calling Membership Functions

def update_function(index,name,nodes):
	member[index] = name;
	endpoints[index] = nodes;

member = [None] * 29
endpoints = []
mem_values = [None] * 29

for i in range(len(member)):
	endpoints.append([None]*4)

update_function(0,"social_reserve",[-inf,-inf,90,120])
mem_values[0] = value(endpoints[0],social_time)
update_function(1,"social_sociable",[60,120,180,270])
mem_values[1] = value(endpoints[1],social_time)
update_function(2,"social_over-social",[180,240,inf,inf])
mem_values[2] = value(endpoints[2],social_time)

update_function(3,"leisure_hectic",[-inf,-inf,420,540])
mem_values[3] = value(endpoints[3],leisure_time)
update_function(4,"leisure_ideal",[480,600,720,840])
mem_values[4] = value(endpoints[4],leisure_time)
update_function(5,"leisure_lazy",[780,960,inf,inf])
mem_values[5] = value(endpoints[5],leisure_time)

update_function(6,"work_lethargic",[-inf,-inf,240,360])
mem_values[6] = value(endpoints[6],work_time)
update_function(7,"work_hard-working",[300,420,480,600])
mem_values[7] = value(endpoints[7],work_time)
update_function(8,"work_industrious",[540,660,inf,inf])
mem_values[8] = value(endpoints[8],work_time)

update_function(9,"health_unfit",[-inf,-inf,45,60])
mem_values[9] = value(endpoints[9],health_time)
update_function(10,"health_fit",[30,120,180,255])
mem_values[10] = value(endpoints[10],health_time)
update_function(11,"health_proactive",[165,240,inf,inf])
mem_values[11] = value(endpoints[11],health_time)

update_function(12,"uncatogerized_productive",[-inf,-inf,90,150])
mem_values[12] = value(endpoints[12],uncategorized_time)
update_function(13,"uncatogerized_not-productive",[120,180,inf,inf])
mem_values[13] = value(endpoints[13],uncategorized_time)

update_function(14,"social_low",[-inf,-inf,2700,4200])
mem_values[14] = value(endpoints[14],social_score)
update_function(15,"social_ideal",[1800,4800,7200,8100])
mem_values[15] = value(endpoints[15],social_score)
update_function(16,"social_high",[7200,8400,inf,inf])
mem_values[16] = value(endpoints[16],social_score)

update_function(17,"leisure_low",[-inf,-inf,30000,40000])
mem_values[17] = value(endpoints[17],leisure_score)
update_function(18,"leisure_ideal",[35000,45000,50000,60000])
mem_values[18] = value(endpoints[18],leisure_score)
update_function(19,"leisure_high",[55000,65000,inf,inf])
mem_values[19] = value(endpoints[19],leisure_score)

update_function(20,"work_low",[-inf,-inf,30000,36000])
mem_values[20] = value(endpoints[20],work_score)
update_function(21,"work_ideal",[35000,37500,42000,48000])
mem_values[21] = value(endpoints[21],work_score)
update_function(22,"work_high",[40000,60000,inf,inf])
mem_values[22] = value(endpoints[22],work_score)

update_function(23,"health_low",[-inf,-inf,3000,4000])
mem_values[23] = value(endpoints[23],health_score)
update_function(24,"health_ideal",[3500,6000,8000,9000])
mem_values[24] = value(endpoints[24],health_score)
update_function(25,"health_high",[7000,10000,inf,inf])
mem_values[25] = value(endpoints[25],health_score)

update_function(26,"uncategorized_low",[-inf,-inf,2100,2400])
mem_values[26] = value(endpoints[26],uncategorized_score)
update_function(27,"uncategorized_ideal",[1800,2400,3000,3300])
mem_values[27] = value(endpoints[27],uncategorized_score)
update_function(28,"uncategorized_high",[2700,3600,inf,inf])
mem_values[28] = value(endpoints[28],uncategorized_score)

#Setting up Recommendatons

rec_message = ['Catch up up a movie this evening','Work is Worship','Family Matters','Hit the Gym']
recommedation = [None]*len(rec_message)
fuzzy_score = [0]*len(rec_message)
recommedation[0] = ['leisure_low','leisure_hectic','work_industrious','work_high']
recommedation[1] = ['work_lethargic','work_low','leisure_lazy','leisure_high']
recommedation[2] = ['social_reserve','social_low']
recommedation[3] = ['health_unfit','health_low']

#Displaying best possible recommendation

for i in range(len(rec_message)):
	for j in range(len(recommedation[i])):
		fuzzy_score[i] += mem_values[member.index(recommedation[i][j])]
	fuzzy_score[i] /= len(recommedation[i])*1.0

print "Recommendation:" + rec_message[fuzzy_score.index(max(fuzzy_score))]	