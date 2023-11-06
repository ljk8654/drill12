objects = [[] for _ in range(4)]

# fill here
collision_pairs = {} # 'bay:ball' : [boy], [ball1 ,ball2, ...]
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

# fill here
def add_collision_pairs(group, a = None, b = None): # a와 b사이의 충돌검사가 필요하다
    if group not in collision_pairs:
        print(f'New group {group} added____')
        collision_pairs[group] = [[], []]
    if a:
        collision_pairs[group][0].append(a)
    if b:
        collision_pairs[group][1].append(b)

def remove_collision_object(o):
    for pairs in collision_pairs.values():
        if o in pairs[0]:
            pairs[0].remove(o)
        if o in pairs[1]:
            pairs[1].remove(o)
def remove_object(o):
    for layer in objects:
        if o in layer:
            layer.remove(o)
            remove_collision_object(o)
            del o
            return
    raise ValueError('Cannot delete non existing object')

def handle_collisions():
    for group, pair in collision_pairs.items():
        for a in pair[0]:
            for b in pair[1]:
                if collide(a,b):
                    a.handle_collision(group, b)
                    b.handle_collision(group, a)
def clear():
    for layer in objects:
        layer.clear()



# fill here
def collide(a, b):
    la, ba, ra, ta = a.get_bb()
    lb, bb, rb, tb = b.get_bb()

    if la > rb: return False
    if ra < lb: return False
    if ta < bb: return False
    if ba > tb: return False

    return True
