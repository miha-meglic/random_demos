# Simple LED Demo (controlled over HTTP)

This code is intended for an **Arduino Nano** connected to a string od **addressable RGBW SK6812** leds (can easily be adapted to RGB WS2812B).  
The Arduino then communicates with the computer via a **serial interface** (baudrate: 9600).  

On the computer a Python script runs a simple **http endpoint**, which changes the LED stip color on request.

NOTE: *The Arduino side is very naive and depends on the Python server to validate the requests.*
