
def loadLights(numLights):
    lights = {} 
    for i in range(numLights):
        light = input().split()
        light = [int(x) for x in light]
        lights[light[0]] = {"status":0, "redDuration":light[1], "greenDuration":light[2], "interval":light[1]+light[2]}
    return lights
def updateLights(lights, location, time):
    if location in lights:
        intervalStatus = time % lights[location]["interval"]
        if intervalStatus >= lights[location]["redDuration"]:
            lights[location]["status"] = 1
        else:
            lights[location]["status"] = 0
def calculateTravelDuration(roadLength, lights):
    progress = 0
    time = 0
    while progress != roadLength:
        if progress in lights: 
            while lights[progress]["status"] == 0: # wait while light is red
                time += 1
                updateLights(lights, progress, time)
        progress += 1
        time += 1
        updateLights(lights, progress, time)
    return time

def solve():
    params = input().split()
    numLights = int(params[0])
    roadLength = int(params[1])
    lights = loadLights(numLights)
    print(calculateTravelDuration(roadLength, lights))
solve()

