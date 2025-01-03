"""Demonstrate example Show usage."""

from netflix_vfx_naming import Scene, Sequence, Shot, Show

show = Show.Show()
sequence = Sequence.Sequence()
scene = Scene.Scene()
shot = Shot.Shot()

print(f"show {show} has name {show.name}")
print(f"sequence {sequence} has name {sequence.name}")
print(f"scene {scene} has name {scene.name}")
print(f"shot {shot} has name {shot.name}")

show.name = "AGM"
sequence.name = "TCC"
scene.name = "065"
shot.name = "0010"

shot.parent = scene
scene.parent = sequence
sequence.parent = show

print(f"shot {shot} has fullname {shot.get_fullname()}")
