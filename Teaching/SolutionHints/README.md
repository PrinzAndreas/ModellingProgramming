## Hints for Exercise Solutions

This page presents ideas to solve the reflection exercises of the book.
As the tasks are formulated very openly, there is not just one solution to each of them.
Rather, they are starting points to discover different models and perspectives.

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
* For reading the time it is sufficient to have the angle of the hands with a precision of 6 degrees, such that we can distinguish 60 different directions for the minute hand. For the hour hand, a precision of 30 degrees helps us to distinguish 12 different directions for the hour hand.
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
In Grimstad, there is a church with a clock on its tower. It is widely visible and shows the time. It also has a bell and in former times it would ring regularly to announce the time.
We will look at the clock as a means of navigation for the boats that are sailing around Grimstad. The visual clock is obviously to small to aid in navigation - the clock tower is better suited for that purpose.
However, the bell of the clock is a good means of navigation, in particular in the case of fog. It provides an approximate direction for the harbour, which can be improved with visual clues when one approaches the shore.<br/>
* For navigation, the frequency of the bell signal is essential as well as its pattern.<br/>
* The placement of the clock is important in order to know the direction.<br/>
* Differences in sound to other bells in the vicinity are also important to know such that the clock is identifiable.<br/>
* When hearing the bell, the direction from where it comes is important and maybe the strength of the sound.<br/>
* We do not care for the hands or the colour of the clock or even the time it shows.<br/>
* In this perspectivem, the clock is a defined point in space which has a regular acoustic signal.<br/>
* Possible attributes are its location, the direction from where the signal came, the frequency of the signal, and the delay until the next signal.<br/>
* A possible system state is location: 58.34314231863526, 8.59555405017648, direction: 320&deg;, frequency: 15', delay: 6'
</details>

### 2.4 Clock Descriptions
<details>
<summary> Task description </summary>
Consider a clock on a public building with the purpose of reading the time.

Create three different snapshot descriptions of such a clock. Then describe possible system executions.
</details>

<details>
<summary> Solution hints </summary>
We consider the clock of Big Ben, which is the Great Clock of Westminster at the north end of the Palace of Westminster in London, England.
The clock is an analogue clock and is shown in four directions. This means a system status contains four clock readings, which all should be the same at all times.
This is normally ensured by the mechanics inside the tower. Each clock reading can be represented by the angle of its hour and minute hands with the precision of integers.
We only look at the north clock now.
If we use degrees for the angle starting from the hands pointing up, then we can identify three situations as follows.<br><br>
bigben.clock.north.hour=0, bigben.clock.north.minute=0 <br>
bigben.clock.north.hour=160, bigben.clock.north.minute=120 <br>
bigben.clock.north.hour=81, bigben.clock.north.minute=253<br><br>
We can translate these states into digital time readings as follows: 12:00, 5:20, 2:42.<br>
When we consider a discrete execution, then the minute hand would advance by 6 degrees every minute, while the hour hand would advance by 1 degree every other minute. We consider all angles modulo 360 degrees.<br>
A continuous execution will advance the minute hand continuously and constantly such that one minute yields 6 degrees. The hour hand is increased similarly to increase by 1 degree every other minute.
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
For a model, we need a shared perspective. As the Boeing 737 is more complex, we adapt the perspective to the paper plane.
We consider one body, two wings, and the possibility to be airborne. For this, we consider the 3D position of the plane, its speed and the direction it is facing.
We ignore the material, the inside of the body, and the wheels. If we want, we can consider flaps.<br>

Now we can map between 3D paper plane and Boeing 747 movements. With some scaling, we can get the movements to match. 
Obviously, we can only consider scenarios where the plane descends, as the paper plane does not any thrust.
We can look at gliding ond maybe landing.
</details>

### 3.2 Music
<details>
<summary> Task description </summary>
Consider descriptions of music in the form of sheet music.

Do the symbols describe the music correctly? Which perspective is applied? How does changing the playing instrument change the correctness of the model?
</details>

<details>
<summary> Solution hints </summary>
Music is a very complex phenomenon involving arrangements of sound, see <a href="https://en.wikipedia.org/wiki/Music">Wikipedia</a>. To make it tangible, we can look at some of its elements: pitch, melody, harmony, rhythm, texture, timbre, expression, and form.<br>
Even though the underlying phenomenon is sound, we do not look at the physics of sound waves, but consider the perception of sound, see <a href="https://en.wikipedia.org/wiki/Sound">Wikipedia</a>. Again, there are several possible elements to consider: pitch, duration, loudness, timbre, texture, and spatial location.<br>
We select a restricted perspective and consider pitch, duration, and loudness. We measure the pitch as the frequency of the sound wave, duration as the time it takes from start to end and the loudness by the pressure level in decibel.<br>
Notes in sheet music can express pitch, duration, and loudness. This way, notes can describe music on our perspective. As we often create music in terms on notes, these notes describe the music correctly.<br>
However, we know that musical notes are not able to describe all possible changes in pitch, duration, and loudness. 
The expressible pitches are limited, related to a reference frequency (concert pitch).
Also the expressible durations are limited, given in fractions of the musical meter.
For loudness, expressivity is even less.
That means not all musical ideas can be expressed with musical notes.<br>
Different instruments are similar under our perspective. We might need an extended perspective to distinguish them.<br>
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
As with all models, the question is about the purpose of the model. We want to account for the movements of the stars and the planets.
First, it must be noted that for the movements of the stars there is basically no difference between a geocentric and a heliocentric worldview, because all stars are very far apart from our solar system.
When it comes to the planets, there are very early methods to predict the movements of the planets, the sun and the moon.
There are even <a href="https://en.wikipedia.org/wiki/Antikythera_mechanism">physical models</a> for that.
Due to the placement of the Earth in the center, various corrections have to be applied to ensure correctness.
With those, the model can predict the planet movements with reasonable precision.<br/>
However, the model gets much simpler when using a heliocentric perspective.
</details>

### 3.4 Heating Model
<details>
<summary> Task description </summary>
Recheck Episode 11.

Add more implicit assumptions for that case. Determine which of the given and the added assumptions are valid. How could we extend the model to take care of the invalid assumptions?
</details>

<details>
<summary> Solution hints </summary>
Obviously, there are many more implicit assumption to add. We consider just three of them: Charlies movements in the room are irrelevant. The furniture can be ignored. The floor isolation is ideal.<br/>
Validity of the assumptions is related to the purpose of the model and the implied data accuracy. Although Charlies movements influence the temperature distribution in the room, the effect is not visible because we only have one data item for the room temperature and our temperature accuracy of 1 degree is not fine enough to register Charlies influence. The furniture could make a difference, but this is not visible as we only have one data item for the room temperature. The floor isolation is not relevant as the room below Charlies room is also heated and has almost the same temperature as Charlies room.<br/>
When we want to consider the distribution of temperature in the room, we need more temperature measurement spots and a model for the heat diffusion in the room.
</details>

### 4.1 Time
<details>
<summary> Task description </summary>
Consider a clock as a model of time.

When is a clock a correct model and when is the model incorrect? How is this influenced by the perspective chosen?
</details>

<details>
<summary> Solution hints </summary>
In our understanding, time is the inherent ordering of snapshots. This means we can understand time as IDs for snapshots.
A clock is a way to provide these IDs inside of snapshots. A simple correctness understanding would say that the clock should equal the time, which implies that the clock is incorrect when it does not equal the time.<br/>
However, care is needed, because equality depends on the perspective, in particular the accuracy and precision of the clock.
The precision of the clock introduces an extra challenge, because any precision means that clock readings are discrete instead of continuous.
In this sense, it is impossible to have a real continuous clock. Again, the perspective decides whether this is acceptable or not.
</details>

### 4.2 Architecture
<details>
<summary> Task description </summary>
Architectural drawings describe some aspects of buildings.

Sometimes, the drawing is prepared after the building is finished. Can we say that the building prescribed by the drawing is a model of the real building? Or is it the other way around?
</details>

<details>
<summary> Solution hints </summary>
Obviously, the answer to the question depends on the perspective chosen. Let us assume that the perspective for the drawing and for the building coincide.
Then the measurements in the building should match the data available in the drawing, and hence model-of can go in both ways.<br/>
On this basis, we should check what was the original. If the original was the drawing, and the building is based later, then the building can be considered the model. Otherwise, the prescribed building by the drawing can be considered the model.
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
