# Name: ABUBAKARI ABDUL-HAMID THOMAH
# Index Number: 6950521
# CE257 ASSIGNMENT 3
#GITHUB ACCOUNT: ATH-PURE

# a sript to determine the prices of cars of different brands available
# carPrices are in U.S Dollars,$
#types of cars available
carTypes=['limousine', 'convertible', 'microCars', 'cityCars', 'hatchbacks', 'SUV',
          'sedans', 'CUV','subcompactCars','familyCars', 'estateCars', 'grandTower',
          'muscleCars', 'superCars','roadsters', 'minivan', 'pickup', 'coupe', 
          'sportsCar', 'raceCars', 'stationWagon', 'van','jeep', 'luxuryCars',
          'compactCars', 'BMW', 'commercialVehicles', 'mercedesBenz', 'kia',
          'chevrolet']
''''car brand with it equivalent price'''
carPrices={'tesla':96000,'ferrari':12000,'ford':35000,'porsche':5000,'honda':4500,
           'lamborhhini':98000,'toyota':6000,'bentley':10000,'maserati':9700,
           'subaru':8000,'hyundai':9000,'cadillac':8500,'nissan':15000,'acura':5500,
           'jaguar':7000,'scania':6500,'dodge':4700,'daimler':7300,'lexus':6700,
           'saleen':8900,'mazda':5600,'tata':4300,'saturn':71000,'KTM':8800,
           'lotus':25000,'hummer':111000,'pagani':3800,'rover':21000,'hino':5400,
           'packard':6600,'scion':4400,'mayback':7200,'audi':7600}
name=input('What is your name? ')
print()
print('hello! ' + name )
a=input('please which type of car do you want? ')
b=input('please specify the brand name ')
print()
if b in carPrices:
    print(f'The price of {a} with brand name {b} is ${carPrices[b]:,}')
else:
    print('sorry the brand specified is currently not available ')

         