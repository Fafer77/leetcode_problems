class Solution:
    def countCollisions(self, directions: str) -> int:
        collision_left = False
        going_right = 0
        collisions_cnt = 0

        for c in directions:
            if c == 'R':
                going_right += 1
            elif c == 'S':
                collision_left = True
                collisions_cnt += going_right
                going_right = 0
            elif c == 'L':
                if collision_left or going_right > 0:
                    collisions_cnt += going_right + 1
                    going_right = 0
                    collision_left = True
        
        return collisions_cnt

