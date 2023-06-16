
import numpy as np
import open3d as o3d

filename = "C:/Users/konfi/Desktop/3dpcp_book_codes/3rdparty/Open3D/examples/test_data/fragment.ply"

print("Loading a point cloud from", filename)
pcd = o3d.io.read_point_cloud(filename)

print(f'pcd:{pcd}')
print(np.asarray(pcd.points))

o3d.visualization.draw_geometries([pcd])
 