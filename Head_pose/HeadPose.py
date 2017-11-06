import cv2
import numpy as np

im = cv2.imread("headPose2.jpg");
size = im.shape

#小池百合子の顔の各パーツの位置
image_points = np.array([
                            (417, 248),     # 鼻先
                            (393, 317),     # アゴ
                            (375, 200),     # 左目の左端
                            (449, 213),     # 右目の右端
                            (372, 263),     # 口の左端
                            (416, 275)      # 口の右端
                        ], dtype="double")

#一般的な人の顔を大まかに表現した3Dモデル
model_points = np.array([
                            (0.0, 0.0, 0.0),             # 鼻先
                            (0.0, -330.0, -65.0),        # アゴ
                            (-225.0, 170.0, -135.0),     # 左目の左端
                            (225.0, 170.0, -135.0),      # 右目の右端
                            (-150.0, -150.0, -125.0),    # 口の左端
                            (150.0, -150.0, -125.0)      # 口の右端
                         
                        ])

#焦点距離は画像の横幅と仮定
focal_length = size[1]

#光学中心の座標を画像の中心と仮定
center = (size[1]/2, size[0]/2)

#カメラマトリックスを作成
camera_matrix = np.array(
                         [[focal_length, 0, center[0]],
                         [0, focal_length, center[1]],
                         [0, 0, 1]], dtype = "double"
                         )

print ("Camera Matrix : {0}".format(camera_matrix))

dist_coeffs = np.zeros((4,1)) # 歪み(?)を0と仮定

 
(success, rotation_vector, translation_vector) = cv2.solvePnP(model_points, image_points, camera_matrix, dist_coeffs, flags=cv2.SOLVEPNP_ITERATIVE)

(nose_end_point2D, jacobian) = cv2.projectPoints(np.array([(0.0, 0.0, 1000.0)]), rotation_vector, translation_vector, camera_matrix, dist_coeffs)

for p in image_points:
    cv2.circle(im, (int(p[0]), int(p[1])), 3, (0,0,255), -1)

p1 = ( int(image_points[0][0]), int(image_points[0][1]))
p2 = ( int(nose_end_point2D[0][0][0]), int(nose_end_point2D[0][0][1]))

cv2.line(im, p1, p2, (255,0,0), 2)

cv2.imshow("Output", im)
cv2.waitKey(0)

print ("Rotation Vector: {0}".format(rotation_vector))
print ("Translation Vector: {0}".format(translation_vector))
