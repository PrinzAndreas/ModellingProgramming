## SLX description of Room

[SLX (Simulation Language with eXtensibility)](https://wolverinesoftware.com/SLXOverview.html) is a language to describe simulations.
It is used in the book to describe the room model and run experiments with it.

The [SLX model description](https://github.com/PrinzAndreas/ModellingProgramming/tree/main/ModelDescriptions/RoomModelSLX) includes the following files.

* [HeatingModel.slx](https://github.com/PrinzAndreas/ModellingProgramming/blob/main/ModelDescriptions/RoomModelSLX/HeatingModel.slx) - main program and experiment description
* [HeatingConstants.slx](https://github.com/PrinzAndreas/ModellingProgramming/blob/main/ModelDescriptions/RoomModelSLX/HeatingConstants.slx) - constants used for the heating model
* [TemperatureHistory.slx](https://github.com/PrinzAndreas/ModellingProgramming/blob/main/ModelDescriptions/RoomModelSLX/TemperatureHistory.slx) - historical temperature data

Moreover, the following [SLX tool](../../SLXToolStudents) libraries are used.

* TimeBaseSeconds - establishing seconds as time granularity
* ContinuousSmall - handling of differential equations
* PlotTrace - creating plots for the runs using gnuplot
* ValueTable - using tables of values
* StateMachine - describing discrete behaviour as state machines

The SLX descriptions can be executed using the [SLX tool](../../SLXToolStudents) (courtesy of James O. Henriksen).
