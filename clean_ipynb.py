import nbformat

file_name = "ARX_Problem_2_Smart_Radio_Mesh_Management_with_UGVs.ipynb"
output_file = "CLEANED_" + file_name

with open(file_name, 'r', encoding='utf-8') as f:
    nb = nbformat.read(f, as_version=4)

# Remove broken widget metadata
for cell in nb.cells:
    if 'metadata' in cell and 'widgets' in cell['metadata']:
        del cell['metadata']['widgets']

with open(output_file, 'w', encoding='utf-8') as f:
    nbformat.write(nb, f)

print(f"✅ Cleaned notebook saved as: {output_file}")

