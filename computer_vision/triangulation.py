import cv2
import numpy as np
from scipy.spatial.transform import Rotation


FOCAL_LENGTH_X = 270
FOCAL_LENGTH_Y = 270
IMAGE_WIDTH = 640
IMAGE_HEIGHT = 480

def get_intrinsic_matrix_from_cam_params(
    image_height, 
    image_width, 
    focal_length_x, 
    focal_length_y
):
    return np.array([
        [focal_length_x, 0.0, image_width / 2], 
        [0.0, focal_length_y, image_height / 2], 
        [0.0, 0.0, 1.0]
    ])


def get_world_in_cam_from_planar_rotation(rotation_in_world_z, translation_in_world):
    rotation_matrix = Rotation.from_euler('z', np.radians(rotation_in_world_z)).as_dcm()
    rotation_matrix_in_place_x = Rotation.from_euler('x', np.radians(-90)).as_dcm()
    cam_in_world = np.eye(4, 4)
    cam_in_world[:3, :3] = rotation_matrix @ rotation_matrix_in_place_x
    cam_in_world[:3, 3] =  translation_in_world
    return np.linalg.inv(cam_in_world)


def get_projection_matrix(intrinsics_matrix, extrinsics_matrix):
    projection_matrix = intrinsics_matrix @ extrinsics_matrix[:3, :]  # we get rid of the last row in the pose
    return projection_matrix


def triangulate_points(projection_matrix_cam1, projection_matrix_cam2, point_cam1, point_cam2):
    error_matrix = np.array(
        [
            point_cam1[1] * projection_matrix_cam1[2, :] - projection_matrix_cam1[1, :],
            projection_matrix_cam1[0, :] - point_cam1[0] * projection_matrix_cam1[2, :], 
            point_cam2[1] * projection_matrix_cam2[2, :] - projection_matrix_cam2[1, :],
            projection_matrix_cam2[0, :] - point_cam2[0] * projection_matrix_cam2[2, :],
        ]
    )
    _, _, v = np.linalg.svd(error_matrix)
    # division is for the scaling factor. Last row for the eigen vector with the lowest variance.
    return v[-1, :] / v[-1, -1] 


def run_direct_projection_tests(
    focal_length_x=FOCAL_LENGTH_X, 
    focal_length_y=FOCAL_LENGTH_Y, 
    image_width=IMAGE_WIDTH, 
    image_height=IMAGE_HEIGHT,
):
    """Check if intrinsics projections make sense"""
    cam1_intrisic_matrix = get_intrinsic_matrix_from_cam_params(
        image_height=image_height,
        image_width=image_width,
        focal_length_x=focal_length_x,
        focal_length_y=focal_length_y
    ) 
    
    principal_point = np.array([0.0, 0.0, focal_length_x])
    homogenous_point1_in_cam = cam1_intrisic_matrix @ principal_point

    principal_point_ray_point = np.array([0.0, 0.0, 2 * focal_length_x])
    homogenous_point2_in_cam = cam1_intrisic_matrix @ principal_point

    assert np.allclose(homogenous_point1_in_cam / homogenous_point1_in_cam[-1], homogenous_point2_in_cam / homogenous_point2_in_cam[-1])


def run_triangulation_test(
    cam1_detection=np.array([360., 300.]), 
    cam2_detection=np.array([140., 404.]), 
    focal_length_x=FOCAL_LENGTH_X, 
    focal_length_y=FOCAL_LENGTH_Y, 
    image_width=IMAGE_WIDTH, 
    image_height=IMAGE_HEIGHT,
    cam1_translation=np.array([5, 2, 1]),
    cam2_translation=np.array([8.5, 2.5, 2]),
    cam1_rotation_z=-20,
    cam2_rotation_z=30,
):
    cam1_intrisic_matrix = get_intrinsic_matrix_from_cam_params(
        image_height=image_height,
        image_width=image_width,
        focal_length_x=focal_length_x,
        focal_length_y=focal_length_y
    ) 
    cam2_intrisic_matrix = get_intrinsic_matrix_from_cam_params(
        image_height=image_height,
        image_width=image_width,
        focal_length_x=focal_length_x,
        focal_length_y=focal_length_y
    ) 
    cam1_extrinsics = get_world_in_cam_from_planar_rotation(
        rotation_in_world_z=cam1_rotation_z, 
        translation_in_world=cam1_translation
    )
    cam2_extrinsics = get_world_in_cam_from_planar_rotation(
        rotation_in_world_z=cam2_rotation_z, 
        translation_in_world=cam2_translation
    )
    cam1_projection_matrix = get_projection_matrix(
        cam1_intrisic_matrix, 
        cam1_extrinsics
    )
    cam2_projection_matrix = get_projection_matrix(
        cam2_intrisic_matrix, 
        cam2_extrinsics
    )
    
    world_point_location = triangulate_points(
        projection_matrix_cam1=cam1_projection_matrix, 
        projection_matrix_cam2= cam2_projection_matrix, 
        point_cam1=cam1_detection, 
        point_cam2=cam2_detection
    )
    print(f"World point location from our method: {world_point_location}")

    cam1_projected_point = cam1_projection_matrix @ world_point_location
    print(f"point in cam1: {cam1_extrinsics @ world_point_location}")
    projection_point1 = (cam1_projected_point / cam1_projected_point[-1])[:2]
    print(
        f"reconstructed point1: {projection_point1}, detected_point:"
        f"{cam1_detection} reprojection error: {np.linalg.norm(projection_point1 - cam1_detection)}"
    )

    b = cam2_projection_matrix @ world_point_location
    projection_point2 = (b / b[-1])[:2]

    print(
        f"reconstructed point2: {projection_point2}, detected_point:" 
        f"{cam2_detection}, reprojection error: {np.linalg.norm(projection_point2 - cam2_detection)}"
    )

    X_opencv = cv2.triangulatePoints(
        cam1_projection_matrix, 
        cam2_projection_matrix, 
        cam1_detection, 
        cam2_detection
    )
    X_opencv = cv2.convertPointsFromHomogeneous(X_opencv.T)
    print('Triangulated world point from openCV: \n', X_opencv)


if __name__ == "__main__":
    run_triangulation_test()
    run_direct_projection_tests()
