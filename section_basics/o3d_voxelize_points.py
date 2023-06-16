import sys
import open3d as o3d

filename = "C:/Users/konfi/Desktop/3dpcp_book_codes/3rdparty/Open3D/examples/test_data/fragment.ply"
s = float(0.03)
print("Loading a point cloud from", filename)
pcd = o3d.io.read_point_cloud(filename)
print(pcd)

o3d.visualization.draw_geometries([pcd], zoom=0.3412,
                                  front=[0.4257, -0.2125, -0.8795],
                                  lookat=[2.6172, 2.0475, 1.532],
                                  up=[-0.0694, -0.9768, 0.2024])

downpcd = pcd.voxel_down_sample(voxel_size=s)
print(downpcd)

o3d.visualization.draw_geometries([downpcd], zoom=0.3412,
                                  front=[0.4257, -0.2125, -0.8795],
                                  lookat=[2.6172, 2.0475, 1.532],
                                  up=[-0.0694, -0.9768, 0.2024])
