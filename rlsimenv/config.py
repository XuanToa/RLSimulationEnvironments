

SIMULATION_ENVIRONMENTS = """
{
"comment__": "These environments are great for evalauting new RL algorithms and using for learning how to do deepRL",
"NavGame_2D-v0": 
{
    "config_file": "./args/genBiped2D/biped2dfull_flat_with_terrain_features.txt",
    "time_limit": 256,
    "sim_name": "NavGame",
        "comment__": "Possible state bounds to be used for scaling states for networks",
    "state_bounds": [[ -10.0, -10.0],
                       [   10.0,  10.0]],
        "comment__": "Action scaling values to be used to scale values for the network",
    "action_bounds": [[-1.2, -1.2],
                      [ 1.2,  1.2]]
},
"NavGame_5D-v0": 
{
    "config_file": "./args/genBiped2D/biped2dfull_incline_with_terrain_features.txt",
    "time_limit": 256,
    "sim_name": "NavGame",
        "comment__": "Possible state bounds to be used for scaling states for networks",
    "state_bounds": [[ -10.0, -10.0, -10.0, -10.0, -10.0],
                       [   10.0,  10.0,  10.0,  10.0,  10.0]],
        "comment__": "Action scaling values to be used to scale values for the network",
    "action_bounds": [[-1.2, -1.2, -1.2, -1.2, -1.2],
                      [ 1.2,  1.2,  1.2,  1.2,  1.2]]
},
"NavGame_10D-v0": 
{
    "config_file": "./args/genBiped2D/biped2dfull_incline_with_terrain_features.txt",
    "time_limit": 256,
    "sim_name": "NavGame",
        "comment__": "Possible state bounds to be used for scaling states for networks",
    "state_bounds": [[ -10.0, -10.0, -10.0, -10.0, -10.0, -10.0, -10.0, -10.0, -10.0, -10.0],
                       [   10.0,  10.0,  10.0,  10.0,  10.0,  10.0,  10.0,  10.0,  10.0,  10.0 ]],
        "comment__": "Action scaling values to be used to scale values for the network",
    "action_bounds": [[-1.2, -1.2, -1.2, -1.2, -1.2, -1.2, -1.2, -1.2, -1.2, -1.2],
                      [ 1.2,  1.2,  1.2,  1.2,  1.2,  1.2,  1.2,  1.2,  1.2,  1.2]]
},
"NavGameMultiAgent_10D-v0": 
{
    "config_file": "./args/genBiped2D/biped2dfull_incline_with_terrain_features.txt",
    "time_limit": 256,
    "sim_name": "NavGameMultiAgent",
        "comment__": "Possible state bounds to be used for scaling states for networks",
    "state_bounds": [[ -10.0, -10.0, -10.0, -10.0, -10.0, -10.0, -10.0, -10.0, -10.0, -10.0],
                       [   10.0,  10.0,  10.0,  10.0,  10.0,  10.0,  10.0,  10.0,  10.0,  10.0 ]],
        "comment__": "Action scaling values to be used to scale values for the network",
    "action_bounds": [[-1.2, -1.2, -1.2, -1.2, -1.2, -1.2, -1.2, -1.2, -1.2, -1.2],
                      [ 1.2,  1.2,  1.2,  1.2,  1.2,  1.2,  1.2,  1.2,  1.2,  1.2]]
},
"ParticleGame_2D-v0": 
{
    "config_file": "./args/genBiped2D/biped2dfull_flat_with_terrain_features.txt",
    "time_limit": 256,
    "sim_name": "ParticleGame",
        "comment__": "Possible state bounds to be used for scaling states for networks",
    "state_bounds": [[ -10.0, -10.0],
                       [   10.0,  10.0]],
        "comment__": "Action scaling values to be used to scale values for the network",
    "action_bounds": [[-1.2, -1.2],
                      [ 1.2,  1.2]]
},
"ParticleGame_5D-v0": 
{
    "config_file": "./args/genBiped2D/biped2dfull_flat_with_terrain_features.txt",
    "time_limit": 256,
    "sim_name": "ParticleGame",
        "comment__": "Possible state bounds to be used for scaling states for networks",
    "state_bounds": [[ -10.0, -10.0, -10.0, -10.0, -10.0],
                       [   10.0,  10.0,  10.0,  10.0,  10.0]],
        "comment__": "Action scaling values to be used to scale values for the network",
    "action_bounds": [[-1.2, -1.2, -1.2, -1.2, -1.2],
                      [ 1.2,  1.2,  1.2,  1.2,  1.2]]
},
"ParticleGame_10D-v0": 
{
    "config_file": "./args/genBiped2D/biped2dfull_flat_with_terrain_features.txt",
    "time_limit": 256,
    "sim_name": "ParticleGame",
        "comment__": "Possible state bounds to be used for scaling states for networks",
    "state_bounds": [[ -10.0, -10.0, -10.0, -10.0, -10.0, -10.0, -10.0, -10.0, -10.0, -10.0],
                       [   10.0,  10.0,  10.0,  10.0,  10.0,  10.0,  10.0,  10.0,  10.0,  10.0 ]],
        "comment__": "Action scaling values to be used to scale values for the network",
    "action_bounds": [[-1.2, -1.2, -1.2, -1.2, -1.2, -1.2, -1.2, -1.2, -1.2, -1.2],
                      [ 1.2,  1.2,  1.2,  1.2,  1.2,  1.2,  1.2,  1.2,  1.2,  1.2]]
},
"GapGame_2D-v0": 
{
    "config_file": "./args/genBiped2D/biped2dfull_flat_with_terrain_features.txt",
    "time_limit": 256,
    "sim_name": "GapGame2D",
        "comment__": "Possible state bounds to be used for scaling states for networks",
"state_bounds": [[ -0.1        , -0.37297016, -0.46672943, -0.54017961, -0.58633739,
		        -0.60702854, -0.61047834, -0.61517441, -0.61791891, -0.61752486,
		        -0.617975  , -0.61803293, -0.61787361, -0.61744529, -0.61498547,
		        -0.61221796, -0.61348456, -0.60777479, -0.5989843 , -0.59793705,
		        -0.58837491, -0.56604177, -0.52857703, -0.50329661, -0.4804875 ,
		        -0.44727302, -0.44497582, -0.44029403, -0.46672943, -0.48605189,
		        -0.52162254, -0.54260689, -0.56121182, -0.571482  , -0.58493423,
		        -0.59574616, -0.60740525, -0.61016464, -0.61458856, -0.61766642,
		        -0.61735982, -0.61570364, -0.61632252, -0.61752486, -0.61348456,
		        -0.60984409, -0.60849261, -0.59740144, -0.58633739, -0.56971067,
		        -0.54844713, -0.54498154, -0.52584058, -0.53125453, -0.5157795 ,
		        -0.51427841, -0.49491554, -0.49491554, -0.50329661, -0.50491774,
		        -0.52992308, -0.55610031, -0.57321209, -0.58421898, -0.00280175,
		        -0.31568578],
		       [ 0.1        ,  0.46497017,  0.63072944,  0.79617959,  0.94033742,
		         1.03902853,  1.0624783 ,  1.10517442,  1.15791893,  1.14352489,
		         1.17997491,  1.17203295,  1.18587363,  1.14144528,  1.1029855 ,
		         1.07621801,  1.0874846 ,  1.04377484,  0.99498433,  0.98993701,
		         0.94837493,  0.87004179,  0.76657701,  0.70729661,  0.6584875 ,
		         0.59327298,  0.58897585,  0.58029401,  0.63072944,  0.67005187,
		         0.74962252,  0.80260688,  0.85521185,  0.88748199,  0.9349342 ,
		         0.97974616,  1.0414052 ,  1.06016469,  1.09858859,  1.14766645,
		         1.13935983,  1.11170363,  1.12032247,  1.14352489,  1.0874846 ,
		         1.05784416,  1.04849255,  0.98740143,  0.94033742,  0.88171071,
		         0.81844717,  0.80898154,  0.75984055,  0.77325457,  0.73577952,
		         0.73227841,  0.68891555,  0.68891555,  0.70729661,  0.71091777,
		         0.76992309,  0.84010029,  0.89321214,  0.93221897,  0.12903275,
		         2.75996566]],
    "comment__": "Action scaling values to be used to scale values for the network",
"action_bounds": [[-1.0, 2.5],
                  [1.0, 5.0]],
	"terrain_type": "gaps",
	"terrain_scale": 0.1,
	"body_shape": "sphere",
	"body_shape_parameters": {
							"radius": 0.05
							},
	"num_terrain_samples": 64,
	"terrain_parameters": {
							"gap_size": 5,
							"gap_start": 5,
							"comment__": "Need to be careful here for state scaling will be 0-0/0",
							"random_gap_width_range": [4,6],
							"random_gap_start_range": [3,15],
							"distance_till_next_gap": 20,
							"terrain_change": -1.0,
							"terrain_length": 500
						},
	"velocity_bounds": [[0.5, 2.5], [3.5, 5.0]]
},
"CannonGame-v0": 
{
    "config_file": "./args/genBiped2D/biped2dfull_flat_with_terrain_features.txt",
    "time_limit": 256,
    "sim_name": "CannonGame",
        "comment__": "Possible state bounds to be used for scaling states for networks",
"state_bounds": [[ -0.1        , -0.37297016, -0.46672943, -0.54017961, -0.58633739,
                -0.60702854, -0.61047834, -0.61517441],
               [ 0.1        ,  0.46497017,  0.63072944,  0.79617959,  0.94033742,
                 1.03902853,  1.0624783 ,  1.10517442]],
    "comment__": "Action scaling values to be used to scale values for the network",
"action_bounds": [[-1.0, -1.0],
                  [1.0, 1.0]],
    "terrain_type": "gaps",
    "terrain_scale": 0.1,
    "body_shape": "sphere",
    "body_shape_parameters": {
                            "radius": 0.05
                            },
    "num_terrain_samples": 64,
    "terrain_parameters": {
                            "gap_size": 5,
                            "gap_start": 5,
                            "comment__": "Need to be careful here for state scaling will be 0-0/0",
                            "random_gap_width_range": [4,6],
                            "random_gap_start_range": [3,15],
                            "distance_till_next_gap": 20,
                            "terrain_change": -1.0,
                            "terrain_length": 500
                        },
    "velocity_bounds": [[-4.0, -6.0], [4.0, 6.0]],
        "comment__": "Number of times the action is updated per second, fps",
    "action_fps": 50,
        "comment__": "Number of subsampled pose images taken between action updates",
    "timestep_subsampling": 1
},
"CannonGameViz-v0": 
{
    "config_file": "./args/genBiped2D/biped2dfull_flat_with_terrain_features.txt",
    "time_limit": 256,
    "sim_name": "CannonGame",
        "comment__": "Possible state bounds to be used for scaling states for networks",
"state_bounds": [[ -0.1        , -0.37297016, -0.46672943, -0.54017961, -0.58633739,
                -0.60702854, -0.61047834, -0.61517441],
               [ 0.1        ,  0.46497017,  0.63072944,  0.79617959,  0.94033742,
                 1.03902853,  1.0624783 ,  1.10517442]],
    "comment__": "Action scaling values to be used to scale values for the network",
"action_bounds": [[-1.0, -1.0],
                  [1.0, 1.0]],
    "terrain_type": "gaps",
    "terrain_scale": 0.1,
    "body_shape": "sphere",
    "body_shape_parameters": {
                            "radius": 0.05
                            },
    "num_terrain_samples": 64,
    "terrain_parameters": {
                            "gap_size": 5,
                            "gap_start": 5,
                            "comment__": "Need to be careful here for state scaling will be 0-0/0",
                            "random_gap_width_range": [4,6],
                            "random_gap_start_range": [3,15],
                            "distance_till_next_gap": 20,
                            "terrain_change": -1.0,
                            "terrain_length": 500
                        },
    "velocity_bounds": [[-4.0, -6.0], [4.0, 6.0]],
    "process_visual_data": true,
        "comment__": "Number of times the action is updated per second, fps",
    "action_fps": 50,
        "comment__": "Number of subsampled pose images taken between action updates",
    "timestep_subsampling": 3,
        "comment__": "Area that will be clipped from the rendering using glReadPixels [x, y, width, height]",
    "image_clipping_area": [578, 178, 48, 48],
        "comment__": "Amount of downsampling that will be done to the image",
    "downsample_image": [4, 4, 1],
        "comment__": "Whether or not to convert the image to grayscale",
    "convert_to_greyscale": true,
        "comment__" : "Whether or not to collect imitation visual data as well (skip for efficiency)",
    "also_imitation_visual_data": true,
        "comment__": "Enable headless rendering",
    "headless_render": false
},
"CannonGameViz2-v0": 
{
    "config_file": "./args/genBiped2D/biped2dfull_flat_with_terrain_features.txt",
    "time_limit": 256,
    "sim_name": "CannonGame",
        "comment__": "Possible state bounds to be used for scaling states for networks",
"state_bounds": [[ -0.1        , -0.37297016, -0.46672943, -0.54017961,
                -0.1        , -0.37297016, -0.46672943, -0.54017961, -0.58633739,
                -0.60702854, -0.61047834, -0.61517441],
               [ 0.1        ,  0.46497017,  0.63072944,  0.79617959,
               0.1        ,  0.46497017,  0.63072944,  0.79617959,  0.94033742,
                 1.03902853,  1.0624783 ,  1.10517442]],
    "comment__": "Action scaling values to be used to scale values for the network",
"action_bounds": [[-1.0, -1.0],
                  [1.0, 1.0]],
    "terrain_type": "gaps",
    "terrain_scale": 0.1,
    "body_shape": "sphere",
    "body_shape_parameters": {
                            "radius": 0.05
                            },
    "num_terrain_samples": 64,
    "terrain_parameters": {
                            "gap_size": 5,
                            "gap_start": 5,
                            "comment__": "Need to be careful here for state scaling will be 0-0/0",
                            "random_gap_width_range": [4,6],
                            "random_gap_start_range": [3,15],
                            "distance_till_next_gap": 20,
                            "terrain_change": -1.0,
                            "terrain_length": 500
                        },
    "velocity_bounds": [[-4.0, -6.0], [4.0, 6.0]],
    "process_visual_data": true,
        "comment__": "Number of times the action is updated per second, fps",
    "action_fps": 50,
        "comment__": "Number of subsampled pose images taken between action updates",
    "timestep_subsampling": 3,
        "comment__": "Area that will be clipped from the rendering using glReadPixels [x, y, width, height]",
    "image_clipping_area": [578, 178, 48, 48],
        "comment__": "Amount of downsampling that will be done to the image",
    "downsample_image": [4, 4, 1],
        "comment__": "Whether or not to convert the image to grayscale",
    "convert_to_greyscale": true,
        "comment__" : "Whether or not to collect imitation visual data as well (skip for efficiency)",
    "also_imitation_visual_data": true,
        "comment__": "Enable headless rendering",
    "headless_render": false,
        "comment__": "Mix different state discription types, used for debugging visual imitation learning",
    "use_dual_state_representations": true
    },
"ProjectileGameViz-DualState-v0": 
{
    "config_file": "./args/genBiped2D/biped2dfull_flat_with_terrain_features.txt",
    "time_limit": 256,
    "sim_name": "ProjectileGame",
        "comment__": "Possible state bounds to be used for scaling states for networks",
"state_bounds": [[ -0.1        , -0.37297016, -0.46672943, -0.54017961,
                -0.1        , -0.37297016, -0.46672943, -0.54017961, -0.58633739,
                -0.60702854, -0.61047834, -0.61517441],
               [ 0.1        ,  0.46497017,  0.63072944,  0.79617959,
               0.1        ,  0.46497017,  0.63072944,  0.79617959,  0.94033742,
                 1.03902853,  1.0624783 ,  1.10517442]],
    "comment__": "Action scaling values to be used to scale values for the network",
"action_bounds": [[-1.0, -1.0],
                  [1.0, 1.0]],
    "terrain_type": "gaps",
    "terrain_scale": 0.1,
    "body_shape": "sphere",
    "body_shape_parameters": {
                            "radius": 0.05
                            },
    "num_terrain_samples": 64,
    "terrain_parameters": {
                            "gap_size": 5,
                            "gap_start": 5,
                            "comment__": "Need to be careful here for state scaling will be 0-0/0",
                            "random_gap_width_range": [4,6],
                            "random_gap_start_range": [3,15],
                            "distance_till_next_gap": 20,
                            "terrain_change": -1.0,
                            "terrain_length": 500
                        },
    "velocity_bounds": [[-4.0, -6.0], [4.0, 6.0]],
    "process_visual_data": true,
        "comment__": "Number of times the action is updated per second, fps",
    "action_fps": 50,
        "comment__": "Number of subsampled pose images taken between action updates",
    "timestep_subsampling": 3,
        "comment__": "Area that will be clipped from the rendering using glReadPixels [x, y, width, height]",
    "image_clipping_area": [440, 450, 128, 128],
        "comment__": "Amount of downsampling that will be done to the image",
    "downsample_image": [8, 8, 1],
        "comment__": "Whether or not to convert the image to grayscale",
    "convert_to_greyscale": true,
        "comment__" : "Whether or not to collect imitation visual data as well (skip for efficiency)",
    "also_imitation_visual_data": true,
        "comment__": "Enable headless rendering",
    "headless_render": false,
        "comment__": "Mix different state discription types, used for debugging visual imitation learning",
    "use_dual_state_representations": true
    }
}
"""
