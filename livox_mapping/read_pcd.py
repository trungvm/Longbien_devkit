import open3d as o3d 
pcd = o3d.io.read_point_cloud("surf.pcd")
# aabb = o3d.geometry.AxisAlignedBoundingBox(min_bound=(0.1, 0.1, 0.1),
#                                            max_bound=(10, 10, 10))
# cropped_pcd = pcd.crop(aabb)                                           
o3d.visualization.draw_geometries([pcd])