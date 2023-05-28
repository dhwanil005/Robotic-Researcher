# Purpose
The purpose of this project is to fetch details of the Scientist as any human would do. The robot initially greets the user and introduce itself. It then proceeds to mention the steps it is about to take. After that it fetches the birth_date, death_date and introduction of the Scientist. It also calculates the age as per the birth date and death date and proceeds to print them in a readable manner.

# How to run the project
`pip3 install -r requirements.txt`

`python3 main.py`

# How to run tests and get coverage report
`cd test`

`python3 run_tests.py `

# Directory Structure
 
    -> ROBOTIC_RESEARCHER
        |
        ->test
            |
            ->robotics_test.py
            ->run_tests.py
            ->scientists_test.py
        |
        ->main.py
        ->robotics.oy
        ->scientists.py
    

# File Definitions
    robotics.py -> This class is responsible for everything that the robot is supposed to do
    scientists.py -> This class represents individual Scientists. Also calculates the age of the scientist
    robotics_test.py -> This file tests all the code in robotics.py
    scientists_test.py -> This file tests all the code in scientists.py
    main.py -> Driver code for the entire system
    run_tests.py -> Script to run both robotics.py and scientists.py. It also generates a coverage report and prints it to the terminal.