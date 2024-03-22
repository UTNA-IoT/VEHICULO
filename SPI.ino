#include "SPI.h"
byte buf[100];
volatile byte pos;
volatile byte slavereceived;
volatile bool received;


void setup() {
  Serial.begin(9600);
  Serial.println("Recepcion desde ESP32");
  pinMode(MISO,OUTPUT);
  SPCR|= _BV(SPE);
  pos=0;
  received=false;
  SPI.attachInterrupt();

}
ISR(SPI_STC_vect){
  byte c = SPDR;
  if(pos < (sizeof(buf)-1)){
    buf[pos++]=c;
  }
  if(c == ';'){
    received=true;
  }
  
}

void loop() {

  if(received){
    String mensaje=String((char*)buf);
    Serial.println(mensaje);
    //delay(200);
    received=false;
    pos=0;
  }
  
}


