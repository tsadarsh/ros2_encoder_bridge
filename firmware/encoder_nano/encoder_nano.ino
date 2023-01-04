#define lA 2
#define rA 3
#define lB 4
#define rB 5

int left;
int right;

void setup() {
  // put your setup code here, to run once:
  attachInterrupt(digitalPinToInterrupt(lA), left_encoder, RISING);
  attachInterrupt(digitalPinToInterrupt(rA), right_encoder, RISING);
  pinMode(lA, INPUT);
  pinMode(rA, INPUT);
  pinMode(rA, INPUT);
  pinMode(lB, INPUT);
  Serial.begin(9600);
} 

void left_encoder() {
  if (digitalRead(lB)==1) {
    left--;
  }
  else {
    left++;
  }
}

void right_encoder() {
  if (digitalRead(rB)==1) {
    right++;
  }
  else {
    right--;
  }
}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.print(left);
  Serial.print(",");
  Serial.print(right);
  Serial.print("\n");
  delay(100);
}
