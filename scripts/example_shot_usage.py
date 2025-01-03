"""Demonstrate example Shot usage."""

from netflix_vfx_naming import Shot

shot = Shot.Shot()

print(f"shot {shot} has name {shot.name}")
print(f"shot {shot} has fullname {shot.get_fullname()}")
