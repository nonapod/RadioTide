"""
loader.py
by lcordell

a helper to load in all of the archetypes
"""

def load_archetypes():
  import os, sys
  archetypes = []
  loader_path = os.path.realpath(__file__)
  loader_dir_path = os.path.dirname(loader_path)
  arch_file_path = os.path.join(loader_dir_path, 'archetypes')
  arch_files = os.listdir(arch_file_path)

  for arch_file in arch_files: 
    if not arch_file == "__init__.py":
      arch_name, extension = os.path.splitext(arch_file)
      if extension == ".py":
        pass
        archetype = __import__('src.archetype.archetypes.%s' % arch_name, globals(), [], -1)
        archetypes.append(archetype.SubArchetype)
        
  return archetypes


if __name__ == "__main__":
  load_archetypes()
