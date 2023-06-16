# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 13:31:03 2023

@author: konfi

"""
import numpy as np
import copy
import open3d as o3d


path =  "C:/Users/konfi/Desktop/3dpcp_book_codes/3rdparty/Open3D/examples/test_data/ICP/"
source = o3d.io.read_point_cloud(path+"cloud_bin_0.pcd")
target = o3d.io.read_point_cloud(path+"cloud_bin_1.pcd")

source.paint_uniform_color([0.5, 0.5, 1.0])
target.paint_uniform_color([1.0, 0.5, 0.5])
initial_trans = np.identity(4)
initial_trans[0,3] = -0.3

#print point cloud function
def draw_registration_resurt(source, target, transformation):
    pcds = list()
    for s in source:
        temp = copy.deepcopy(s)
        pcds.append( temp.transform(transformation) )
    pcds += target
    o3d.visualization.draw_geometries(pcds, zoom=0.8,
                                      front = [0.024, -0.225, -0.973],
                                      lookat = [0.488, 1.722, 1.556],
                                      up = [0.047, -0.972, 0.226])
    
draw_registration_resurt([source], [target], initial_trans)

#Feature detection
def keypoint_and_feature_extravtion( pcd, voxel_size ):
    keypoints = pcd.voxel_down_sample(voxel_size)
    
    viewpoint = np.array([0., 0., 0.], dtype='float64')
    radius_normal = 2.0*voxel_size
    
    keypoints.estimate_normals(
        o3d.geometry.KDTreeSearchParamHybrid(radius=radius_normal, max_nn=30))
    keypoints.orient_normals_towards_camera_location( viewpoint )
    
    radius_feature = 5.0*voxel_size
    feature = o3d.pipelines.registration.compute_fpfh_feature(
        keypoints, 
        o3d.geometry.KDTreeSearchParamHybrid(radius=radius_feature, max_nn=100))
    return keypoints, feature


voxel_size = 0.1 
s_kp, s_feature = keypoint_and_feature_extravtion(source, voxel_size)
t_kp, t_feature = keypoint_and_feature_extravtion(target, voxel_size)

s_kp.paint_uniform_color([0,1,0])
t_kp.paint_uniform_color([0,1,0])

draw_registration_resurt([source,s_kp], [target,t_kp], initial_trans)