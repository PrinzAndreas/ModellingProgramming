## Hints for Exercise Solutions

* Work in progress  
![work in progress](../../images/comingSoon.png "work in progress")

### 2.1 Clock Perspective
<details>
<summary> Task description </summary>
Consider a clock somewhere in your household or school.
The purpose is to read the time.

Which perspective of the clock helps you determine the time? 
Which aspects of reality do you consider, and which do you ignore?
Which precision of the relevant attributes is meaningful?
</details>

<details>
<summary> Solution hints </summary>
There is an analog wall clock in my office.
It has a very simple design with numbers 1 .. 12 and two hands - a short hour hand and a long minute hand.<br/>
* For determining time, I need to look at where the hands of the clock point.<br/>
* I only consider the angle of the hands (two numbers). The following are examples of irrelevant aspects: the colour of the hands and the clock, the shape the numbers, the existence of the numbers, the mechanism that makes the clock work (eletronic versus mechanical), and the position of the clock. There are many more irrelevant aspects.<br/>
* For reading the time it is sufficient to have the angle of the hands with a precision of 6 degrees, such that we can distinguish 60 different directions for the minute hand. For the hour hand, a precision of 30 degrees helps us to distinguish 12 different directions for the hour hand.<br/><br/>
</details>

### 2.2 Alarm Clock System
<details>
<summary> Task description </summary>
Consider an alarm clock somewhere in your household with the purpose of reading the time.

What is the system for this clock? 
What are the parts and attributes of the system? 
Describe at least one system snapshot using these parts and attributes. 
</details>

<details>
<summary> Solution hints </summary>
I have a digital radio controlled alarm clock in my office which I take with me to meetings such that I can read the time without looking at my wrist.
The alarm clock display shows the current temperature, second, hours, minutes, the day and month, and the weekday. The digits are shown with a seven segment display each.
There are four buttons: MODE, UP, DOWN, ALARM. On top there is a SNOOZE button and at the back there is a compartment for the battery.<br/>
* For determining the time, I read the hour digits as the hour and the minute digits as the minute.<br/>
* All other information on the display is irrelevant as is the colour of the display or its lighting. All the electronics behind is not relevant as is the clock casing or placement.<br/>
* As the clock is radio controlled and adjusts austomatically, I do not care for any of the buttons.<br/>
* It is important that the battery has enough power.<br/>
* This boils down to the alarm clock system having three parts: the clock casing including a display, the battery cover, and the battery. It would be possible to consider the display as a separate element.<br/>
* The relevant attributes are the hour and minute on the display, and the charging status of the battery. It is possible to also consider the connection status to the controlling atomic clock.<br/>
* A system snapshot is clock.display.hour=11, clock.display.minute=27, clock.battery.status=64%.
</details>

### 2.3 Alternative Clock Perspective
<details>
<summary> Task description </summary>
Consider a clock on a public building. Choose a purpose which is not reading the time.

Which perspective supports your chosen purpose? What is the system in this new perspective, including parts and attributes? Describe at least one snapshot of this alternative system.
</details>

<details>
<summary> Solution hints </summary>
Work in progress<br>
<img src="https://raw.githubusercontent.com/PrinzAndreas/ModellingProgramming/main/images/comingSoon.png" alt="work in progress" title="work in progress" style="max-width: 100%;">
</details>

### 2.4 Clock Descriptions
<details>
<summary> Task description </summary>
Consider a clock on a public building with the purpose of reading the time.

Create three different snapshot descriptions of such a clock. Then describe possible system executions.
</details>

<details>
<summary> Solution hints </summary>
Work in progress<br>
<img src="https://raw.githubusercontent.com/PrinzAndreas/ModellingProgramming/main/images/comingSoon.png" alt="work in progress" title="work in progress" style="max-width: 100%;">
</details>

### 3.1 Paper plane
<details>
<summary> Task description </summary>
Consider a paper plane, folded out of regular A4 paper.

How is the paper plane a model of a Boeing 737? 
What is the perspective used and what are the behaviours?
</details>

<details>
<summary> Solution hints </summary>
Work in progress<br>
<img src="https://raw.githubusercontent.com/PrinzAndreas/ModellingProgramming/main/images/comingSoon.png" alt="work in progress" title="work in progress" style="max-width: 100%;">
</details>

### 3.2 Music
<details>
<summary> Task description </summary>
Consider descriptions of music in the form of sheet music.

Do the symbols describe the music correctly? Which perspective is applied? How does changing the playing instrument change the correctness of the model?
</details>

<details>
<summary> Solution hints </summary>
Work in progress<br>
<img src="https://raw.githubusercontent.com/PrinzAndreas/ModellingProgramming/main/images/comingSoon.png" alt="work in progress" title="work in progress" style="max-width: 100%;">
</details>

### 3.3 Geocentric Worldview
<details>
<summary> Task description </summary>
The geocentric worldview posits that Earth is at the center of the universe and stars, planets, and the sun, revolve around it.

Is the geocentric worldview a correct model of the movements of the stars and planets?
Which perspective is needed to make it a correct model?
</details>

<details>
<summary> Solution hints </summary>
Work in progress<br>
<img src="https://raw.githubusercontent.com/PrinzAndreas/ModellingProgramming/main/images/comingSoon.png" alt="work in progress" title="work in progress" style="max-width: 100%;">
</details>

### 3.4 Heating Model
<details>
<summary> Task description </summary>
Recheck Episode 11.

Add more implicit assumptions for that case. Determine which of the given and the added assumptions are valid. How could we extend the model\index{model|)} to take care of the invalid assumptions?
</details>

<details>
<summary> Solution hints </summary>
Work in progress<br>
<img src="https://raw.githubusercontent.com/PrinzAndreas/ModellingProgramming/main/images/comingSoon.png" alt="work in progress" title="work in progress" style="max-width: 100%;">
</details>

### 4.1 Time
<details>
<summary> Task description </summary>
Consider a clock as a model of time.

When is a clock a correct model and when is the model incorrect? How is this influenced by the perspective chosen?
</details>

<details>
<summary> Solution hints </summary>
Work in progress<br>
<img src="https://raw.githubusercontent.com/PrinzAndreas/ModellingProgramming/main/images/comingSoon.png" alt="work in progress" title="work in progress" style="max-width: 100%;">
</details>

### 4.2 Architecture
<details>
<summary> Task description </summary>
Architectural drawings describe some aspects of buildings.

Sometimes, the drawing is prepared after the building is finished. Can we say that the building prescribed by the drawing is a model of the real building? Or is it the other way around?
</details>

<details>
<summary> Solution hints </summary>
Work in progress<br>
<img src="https://raw.githubusercontent.com/PrinzAndreas/ModellingProgramming/main/images/comingSoon.png" alt="work in progress" title="work in progress" style="max-width: 100%;">
</details>

### 4.3 Discretization
<details>
<summary> Task description </summary>
Figure 4.4 shows how discrete data can be interpolated to form continuous data.

If we start with continuous data given by the cosine function, how can we extract discrete data at every full minute? How does the perspective influence the result?
</details>

<details>
<summary> Solution hints </summary>
Work in progress<br>
<img src="https://raw.githubusercontent.com/PrinzAndreas/ModellingProgramming/main/images/comingSoon.png" alt="work in progress" title="work in progress" style="max-width: 100%;">
</details>

### 4.4 Darts
<details>
<summary> Task description </summary>
Dart throwing often has a considerable element of luck involved.

What are the reasons for these uncertainties? How could a change of perspective remove some of the randomness? How does the situation change if the player is a world champion?
</details>

<details>
<summary> Solution hints </summary>
Work in progress<br>
<img src="https://raw.githubusercontent.com/PrinzAndreas/ModellingProgramming/main/images/comingSoon.png" alt="work in progress" title="work in progress" style="max-width: 100%;">
</details>

### 5.1 Synchronised Traffic Lights
<details>
<summary> Task description </summary>
A city wants to reprogram the traffic lights to avoid traffic jams. The new programs should be tested in a model before deployment.

What perspective do you propose for the model to capture all relevant elements? 
What are the RTS elements, and how do they relate to the three categories of RTS elements?
</details>

<details>
<summary> Solution hints </summary>
Work in progress<br>
<img src="https://raw.githubusercontent.com/PrinzAndreas/ModellingProgramming/main/images/comingSoon.png" alt="work in progress" title="work in progress" style="max-width: 100%;">
</details>

### 5.2 Compilers and Interpreters
<details>
<summary> Task description </summary>
Suppose we have a machine understanding ML, and a compiler written in ML translating SLX to ML.

Can we use the SLX compiler and the ML machine to create a (virtual) SLX machine, thereby making SLX executable?
</details>

<details>
<summary> Solution hints </summary>
Work in progress<br>
<img src="https://raw.githubusercontent.com/PrinzAndreas/ModellingProgramming/main/images/comingSoon.png" alt="work in progress" title="work in progress" style="max-width: 100%;">
</details>

### 5.3 Testing
<details>
<summary> Task description </summary>
Testing is a way to validate a new system. A number of tests are run in the mental original and in the new system and the results are compared.

Which methods would you propose to test a new chair? Which tests should be selected?
</details>

<details>
<summary> Solution hints </summary>
Work in progress<br>
<img src="https://raw.githubusercontent.com/PrinzAndreas/ModellingProgramming/main/images/comingSoon.png" alt="work in progress" title="work in progress" style="max-width: 100%;">
</details>

### 5.4 Random Numbers
<details>
<summary> Task description </summary>
Pseudo-random numbers are a realization of real random numbers.

How could you verify or validate that they are correct?
</details>

<details>
<summary> Solution hints </summary>
Work in progress<br>
<img src="https://raw.githubusercontent.com/PrinzAndreas/ModellingProgramming/main/images/comingSoon.png" alt="work in progress" title="work in progress" style="max-width: 100%;">
</details>

### 6.1 Flight Simulator
<details>
<summary> Task description </summary>
A flight simulator is software that allows one to experience flying a plane. Simple versions work like games, while advanced versions use real cockpits to recreate the flight feeling as exactly as possible. After extended training in a flight simulator, a real flight is manageable.

Discuss flight simulators in terms of the concepts of this book. What is the associated perspective, what is the modelling involved and where are the programming and descriptions?
</details>

<details>
<summary> Solution hints </summary>
Work in progress<br>
<img src="https://raw.githubusercontent.com/PrinzAndreas/ModellingProgramming/main/images/comingSoon.png" alt="work in progress" title="work in progress" style="max-width: 100%;">
</details>

### 6.2 Maps
<details>
<summary> Task description </summary>
Assume you use a map to plan a hiking trip.

Discuss your plan and the map as a model of the trip in terms of the concepts of this book. What is the associated perspective, what is the modelling involved and where are the programming and descriptions?
</details>

<details>
<summary> Solution hints </summary>
Work in progress<br>
<img src="https://raw.githubusercontent.com/PrinzAndreas/ModellingProgramming/main/images/comingSoon.png" alt="work in progress" title="work in progress" style="max-width: 100%;">
</details>

### 6.3 Human Models
<details>
<summary> Task description </summary>
When you search the Internet for the term \quoted{models}, your first hits will relate to the profession or role to be a model.

Discuss these human models in terms of the concepts of this book. What is the associated perspective, what is the modelling involved and where are the programming and descriptions?
</details>

<details>
<summary> Solution hints </summary>
Work in progress<br>
<img src="https://raw.githubusercontent.com/PrinzAndreas/ModellingProgramming/main/images/comingSoon.png" alt="work in progress" title="work in progress" style="max-width: 100%;">
</details>

### 6.4 Weather forecast
<details>
<summary> Task description </summary>
Consider your favourite weather forecast site. It provides a description of the weather to come and maybe also of the weather that has been.

Discuss weather forecasts in terms of the concepts of this book. What is the associated perspective, what is the modelling involved and where are the programming and descriptions?
</details>

<details>
<summary> Solution hints </summary>
Work in progress<br>
<img src="https://raw.githubusercontent.com/PrinzAndreas/ModellingProgramming/main/images/comingSoon.png" alt="work in progress" title="work in progress" style="max-width: 100%;">
</details>
