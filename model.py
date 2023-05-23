mport math

def calculate_orbital_velocity(altitude):
    #constants
    G = 6.67430e-11  # Gravitational constant in m^3/kg/s^2
    M = 5.97219e24   # Mass of the Earth in kg
    R = 6371000      # Radius of the Earth in meters

    #calculate the distance between the sat and the earth
    r=R+altitude
    #calculate the orbital velocity

    v=math.sqrt((G*M)/r)

    return v

#prompt the user to enter the altitude in metres
altitude=float(input("What is the height of this satellite above the earth's surface?"))
#calculate the orbital velocity
orbital_velocity = calculate_orbital_velocity(altitude)
#diplay the result
print("this satellite is orbiting the earth at a velocity of  :", orbital_velocity,"m/s")

               
