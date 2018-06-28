{"filter":false,"title":"logger_ex.py","tooltip":"/logger_example/src/logger_ex.py","undoManager":{"mark":1,"position":1,"stack":[[{"start":{"row":0,"column":0},"end":{"row":22,"column":25},"action":"insert","lines":["#! /usr/bin/env python","","import rospy","import random","import time","","# Options: DEBUG, INFO, WARN, ERROR, FATAL","rospy.init_node('log_demo', log_level=rospy.DEBUG)","rate = rospy.Rate(0.5)","","# In Kinetic ROS you can use this periodic log publication. We are using Indigo here, so not useable yet.","#rospy.loginfo_throttle(120, \"DeathStars Minute info: \"+str(time.time()))","","while not rospy.is_shutdown():","    rospy.logdebug(\"There is a missing droid\")","    rospy.loginfo(\"The Emperors Capuchino is done\")","    rospy.logwarn(\"The Revels are coming time \"+str(time.time()))","    exhaust_number = random.randint(1,100)","    port_number = random.randint(1,100)","    rospy.logerr(\" The thermal exhaust port %s, right below the main port %s\", exhaust_number, port_number)","    rospy.logfatal(\"The DeathStar Is EXPLODING\")","    rate.sleep()","    rospy.logfatal(\"END\")"],"id":1}],[{"start":{"row":0,"column":2},"end":{"row":0,"column":3},"action":"remove","lines":[" "],"id":2}],[{"start":{"row":7,"column":47},"end":{"row":7,"column":48},"action":"insert","lines":["N"],"id":6}],[{"start":{"row":7,"column":46},"end":{"row":7,"column":47},"action":"insert","lines":["R"],"id":6}],[{"start":{"row":7,"column":45},"end":{"row":7,"column":46},"action":"insert","lines":["A"],"id":7}],[{"start":{"row":7,"column":44},"end":{"row":7,"column":49},"action":"remove","lines":["DEBUG"],"id":8},{"start":{"row":7,"column":44},"end":{"row":7,"column":45},"action":"insert","lines":["W"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":9,"column":0},"end":{"row":9,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":0,"state":"start","mode":"ace/mode/python"}},"timestamp":1529760082000,"hash":"996c62510e83d505dfa428fdaa2f424402ed26e3"}