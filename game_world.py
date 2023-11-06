objects = [[] for _ in range(4)]
collision_pairs = {}

# 충돌체크를 해야하는 관계임을 넣어주는 함수
# init에서 지정
def add_collision_pair(group, a, b):
    if group not in collision_pairs:
        print(f'Added new group {group}')
        collision_pairs[group] = [ [], [] ]
    if a:
        collision_pairs[group][0].append(a)
    if b:
        collision_pairs[group][1].append(b)

# 충돌체크를 이제 하지 않아도 된다고 표시해주는 함수
def remove_collision_object(o):
    for pairs in collision_pairs.values():
        if o in pairs[0]:
            pairs[0].remove(o)
        if o in pairs[1]:
            pairs[1].remove(o)

# 충돌했을 때 충돌한 a와 b에 누구와 충돌했는지 알려주고 그에 맞는 행동을 하도록 하는 함수
def handle_collisions():
    for group, pairs in collision_pairs.items():
        for a in pairs[0]:
            for b in pairs[1]:
                if collide(a, b):
                    a.handle_collision(group, b)
                    b.handle_collision(group, a)

def add_object(o, depth = 0):
    objects[depth].append(o)

def add_objects(ol, depth = 0):
    objects[depth] += ol


def update():
    for layer in objects:
        for o in layer:
            o.update()


def render():
    for layer in objects:
        for o in layer:
            o.draw()

# 충돌 여부 판별해주는 함수
def collide(a, b):
    left_a, battom_a, right_a, top_a = a.get_bb()
    left_b, battom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < battom_b: return False
    if battom_a > top_b: return False

    return True


def remove_object(o):
    for layer in objects:
        if o in layer:
            layer.remove(o)
            remove_collision_object(o)
            del o
            return
    raise ValueError('Cannot delete non existing object')


def clear():
    for layer in objects:
        layer.clear()



# fill here


