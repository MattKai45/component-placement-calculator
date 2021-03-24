#!/usr/bin/python

import sys, getopt, math


def main(argv):
   num = 0
   radius = 0
   xOffset = 0
   yOffset = 0
   degree = 0

   try:
      opts, args = getopt.getopt(
         argv,
         "hi:n:r:x:y:d:",
         ["num=", "radius=", "xOffset=", "yOffset=", "degrees="],
      )
   except getopt.GetoptError:
      print("Error")
      sys.exit(2)
   for opt, arg in opts:
      if opt == "-h":
         print("test.py -n <numComponents> -r <radius> -x <xOffset> -y <yOffset>")
         sys.exit()
      elif opt in ("-n", "--num"):
         num = int(arg)
      elif opt in ("-r", "--radius"):
         radius = float(arg)
      elif opt in ("-x", "--xOffset"):
         offset_x = float(arg)
      elif opt in ("-y", "--yOffset"):
         offset_y = float(arg)
      elif opt in ("-d", "--degrees"):
         degree = float(arg)

   Components_x = [0] * num
   Components_y = [0] * num
   Components_r = [0] * num

   print("Num Components is ", num)
   print("Radius is ", radius)
   print("X offset is ", offset_x)
   print("Y offset is ", offset_y)
   print("degrees is ", degree)

   radSteps = math.radians(360 / num)
   radStart = math.radians(degree)

   for i in range(num):
      Components_x[i] = round((radius * math.sin(radStart + (radSteps*i))) + offset_x,2)
      Components_y[i] = round((radius * math.cos(radStart + (radSteps*i))) + offset_y,2)
      Components_r[i] = round(math.degrees(radStart + (radSteps*i)),2)
      print("Component " + str(i+1) + "\tpos=[" + "{:.2f}".format(Components_x[i]) + ", " + "{:.2f}".format(Components_y[i]) + "]\trot=" + "{:.2f}".format(Components_r[i]) + " degrees")

if __name__ == "__main__":
   main(sys.argv[1:])