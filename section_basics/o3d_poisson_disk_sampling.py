import sys
import open3d as o3d

filename = "C:/Users/konfi/Desktop/3dpcp_book_codes/3rdparty/Open3D/examples/test_data/knot.ply"
k = int(500)
print("Loading a triangle mesh from", filename)
mesh = o3d.io.read_triangle_mesh(filename)
print(mesh)2

o3d.visualization.draw_geometries([mesh], mesh_show_wireframe=True)

downpcd = mesh.sample_points_poisson_disk(number_of_points=k)
print(downpcd)

o3d.visualization.draw_geometries([downpcd])
