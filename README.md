# Custom-Arpeggiator
This project is a prototype for a gesture-based MIDI controller using a microcontroller and ultrasonic sensors. The controller can be used to manipulate various parameters of a MIDI instrument, such as pitch, volume, and modulation, using hand gestures.

Connections

![circuit-2](https://user-images.githubusercontent.com/104531498/233992351-a5d492df-4758-493b-9e37-fcb789d8b96e.png)

The ultrasonic sensor is used to detect the distance between the user's hand and the controller, and this distance is used to control the depth of the MIDI instrument's sound. Potentiometers are used to manipulate other parameters, such as modulation and volume, while buttons are used to activate arpeggiator functions.

Set up

To use the PD patch, select multiple midi devices. The first one is set to be the device's midi out and the second one for any midi keyboard.

![image](https://user-images.githubusercontent.com/104531498/233993218-65319066-5693-4c19-ad46-efc7fb443bc0.png)

Also, the folloing image shows the notes input from the midi keyboard. In this case the channel is 17 but every midi controller have its specific channel configuration so make sure to set that up.

![image](https://user-images.githubusercontent.com/104531498/233993611-73ecbc33-fe19-4fd3-96d1-ee9926dc8494.png)

Inspiration

This project was inspired by the theremin and other hand-controlled instruments. The goal was to create a similar experience using modern technology.

Links

[Blog](https://medium.com/@santiagohoyos999/list/microbit-gesture-controlled-arpeggiator-project-d704334a929e)
[Demonstration video](https://www.youtube.com/watch?v=Q4Mgr6wT-YU)
