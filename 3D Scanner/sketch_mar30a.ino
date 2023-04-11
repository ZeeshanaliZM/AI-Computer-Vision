int val;

void setup() {
  Serial.begin(9600);
  pinMode(LED_BUILTIN,OUTPUT);
  digitalWrite(LED_BUILTIN,LOW);
}

void loop() {
  if (Serial.available() > 0){
    val = Serial.read();
    Serial.write("\n");
    if(val=='1'){
      digitalWrite(LED_BUILTIN,HIGH);
      }
    if(val=='0'){
      digitalWrite(LED_BUILTIN,LOW);
      }}}
