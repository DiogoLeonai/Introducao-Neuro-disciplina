import os
from neuron import h

def loadCell(template):

    h.load_file("stdrun.hoc")
    h.load_file("import3d.hoc")

    # Directory containing this wrapper
    wrapper_dir = os.path.dirname(os.path.abspath(__file__))

    # HOC template file
    hoc_file = os.path.join(wrapper_dir, "models", f"{template}_template.hoc")

    print("Loading cell:", template)
    print("HOC file:", hoc_file)
    print("Exists:", os.path.isfile(hoc_file))

    h.xopen(hoc_file)

    cell = getattr(h, template)(0)

    print(f"Creating a generic {template} cell from Pospischil2008 template")

    return cell