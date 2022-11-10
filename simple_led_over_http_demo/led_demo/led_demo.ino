#include <FastLED.h>
#include "FastLED_RGBW.h"

#define NUM_LEDS 30
#define DATA_PIN 6

#define S_BUF_SIZE 5

CRGBW leds[NUM_LEDS];
CRGB *ledsRGB = (CRGB *) &leds[0];

char buf[S_BUF_SIZE];

void setup() {
  Serial.begin(9600);

  FastLED.addLeds<WS2812B, DATA_PIN, RGB>(ledsRGB, getRGBWsize(NUM_LEDS));
  FastLED.setBrightness(128);
  FastLED.show();
}

void loop() {
  if (Serial.available() > 0) {
    Serial.readBytes(buf, S_BUF_SIZE);

    int ledNo = buf[0];
    leds[ledNo] = CRGBW(buf[1], buf[2], buf[3], buf[4]);
    FastLED.show();
  }
}
