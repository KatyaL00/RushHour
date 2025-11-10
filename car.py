from rectangle import rectangle
from traffic_light import traffic_light

class direction:
    UP_DOWN = 1
    DOWN_UP = 2

class car:
    car_rectangle = None
    color = "blue"
    step = 0
    final_point = 0
    route = None
    canvas = None
    light = None

    def __init__(self, canvas, road_box, car_box, route, light):
        self.route = route
        self.canvas = canvas
        self.light = light
        self.car_rectangle = canvas.create_rectangle(
            car_box.x0,
            car_box.y0,
            car_box.x1,
            car_box.y1,
            fill=self.color
        )

        if self.route == direction.UP_DOWN:
            move_x = road_box.x0 + (road_box.width() // 4) * 3 - (car_box.width() // 2)
            move_y = 0
            self.step = 10
            self.final_point = road_box.height() + car_box.height()
        else:
            move_x = road_box.x0 + (road_box.width() // 4) - (car_box.width() // 2)
            move_y = road_box.y1 - car_box.height()
            self.step = -10
            self.final_point = 0
        self.canvas.move(self.car_rectangle, move_x, move_y)

    def is_reached_endpoint(self, car_pos) -> bool:
        current_y = car_pos[3]  # Bottom y-coordinate of the car
        
        # Check if car has reached its endpoint based on direction
        has_reached_endpoint = False
        if self.route == direction.UP_DOWN:
            if current_y > self.final_point:
                has_reached_endpoint = True
        else:  # direction.DOWN_UP
            if current_y < self.final_point:
                has_reached_endpoint = True
        
        if has_reached_endpoint:
            self.canvas.delete(self.car_rectangle)
            return False
        return True
    
    def can_pass_intersection(self, car_pos) -> bool:
        color = self.light.get_color()
        if color == "green":
            return True
        return False
        
        #position = self.light.get_position()
        #new_car_pos = car_pos + self.step  
        # Implement logic to determine if the car can pass the intersection

        pass

    def move(self) -> bool:
        car_pos = self.canvas.coords(self.car_rectangle)

        if self.is_reached_endpoint(car_pos) == False:
            return False

        if self.can_pass_intersection(car_pos) == False:
            return True

        #if self.dtance_to_next_car_avaliable(car_pos) == False:
        #    return True

        # Move the car one step in its direction
        self.canvas.move(self.car_rectangle, 0, self.step)
        return True