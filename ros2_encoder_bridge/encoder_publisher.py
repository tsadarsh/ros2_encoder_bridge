import rclpy
from rclpy.node import Node
import serial

from std_msgs.msg import Int16

SERIAL_ID = "/dev/ttyUSB0"


class EncoderPublisher(Node):
    
    def __init__(self) -> None:
        super().__init__('encoder_publisher')
        self.lwheel_publisher_ = self.create_publisher(Int16, 'lwheel', 10)
        self.rwheel_publisher_ = self.create_publisher(Int16, 'rwheel', 10)
        timer_period = 0.1
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.ser = None
    
    def timer_callback(self):
        lwheel_ticks = Int16()
        rwheel_ticks = Int16()
        serial_data = self.serial_read()
        lwheel_ticks.data = serial_data[0]
        rwheel_ticks.data = serial_data[1]
        self.lwheel_publisher_.publish(lwheel_ticks)
        self.rwheel_publisher_.publish(rwheel_ticks)

    def serial_read(self):
        if not self.ser:
            self.ser = serial.Serial(SERIAL_ID, baudrate=9600)
        data = [int(x) for x in self.ser.readline().decode()[:-1].split(',')]
        self.get_logger().info(f"Data received {data}")
        return data
    

def main(args=None):
    rclpy.init(args=args)

    encoder_publisher = EncoderPublisher()

    rclpy.spin(encoder_publisher)

    encoder_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
