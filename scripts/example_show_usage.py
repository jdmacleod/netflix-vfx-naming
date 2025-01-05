"""Demonstrate example Show usage."""

from netflix_vfx_naming import Scene, Sequence, Shot, Show

show = Show.Show(name="AGM")
sequence = Sequence.Sequence(name="TCC")
scene = Scene.Scene(name="065")
shot = Shot.Shot(name="0010")

print(f"show {show} has name {show.name}")
print(f"sequence {sequence} has name {sequence.name}")
print(f"scene {scene} has name {scene.name}")
print(f"shot {shot} has name {shot.name}")

shot.set_parent(scene)
scene.set_parent(sequence)
sequence.set_parent(show)

print(f"shot {shot} has fullname {shot.get_fullname()}")
