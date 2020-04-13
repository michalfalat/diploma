    # Camera matrix calcualtion
    focal_length = input_image[1]
    center = (input_image[1]/2, input_image[0]/2)
    camera_matrix = np.array(
        [
            [focal_length,  0,            center[0]],
            [0,             focal_length, center[1]],
            [0,             0,            1       ]
        ], dtype="double"
    )