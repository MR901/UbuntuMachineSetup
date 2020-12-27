###############################################################################################################################
#       Settings below
###############################################################################################################################
import yaml


conf = {
    'cmt01': {
        'output': {
            'show_preview': False,
            'image_saving_dir': '/Users/mohitrajput/Documents/CargillWorkspace/ChickenNuggetProblem/ChickenNugget_CV/_large_files/data/new_data_collection/'
            # '/home/nano/Documents/ComputerVision/_large_files/data/new_data_collection/'
            # '/Users/mohitrajput/Documents/CargillWorkspace/ChickenNuggetProblem/ChickenNugget_CV/_large_files/data/new_data_collection/'
        },
        '''
        ## https://picamera.readthedocs.io/en/release-1.12/fov.html
        ## Video Capability of Camera
        # install package # sudo apt-get install v4l-utils
        # command # v4l2-ctl --list-formats-ext
        ioctl: VIDIOC_ENUM_FMT
            Index       : 0
            Type        : Video Capture
            Pixel Format: 'RG10'
            Name        : 10-bit Bayer RGRG/GBGB
                Size: Discrete 3264x2464	1.324	Interval: Discrete 0.048s (21.000 fps)
                Size: Discrete 3264x1848	1.766	Interval: Discrete 0.036s (28.000 fps)
                Size: Discrete 1920x1080	1.777	Interval: Discrete 0.033s (30.000 fps)
                Size: Discrete 1280x720		1.777	Interval: Discrete 0.017s (60.000 fps)
        '''
        # Working Setting: 60:1920x1080:30 || 60:1280x720:60
        'input_setting': {
            'n_buffer_frames': 60,# # Take this in a multiple of FrameRate # get it approx to 1sec or more
            'frame_width': 1920, #720#1280
            'frame_height': 1080, #1280#720
            'frame_rate': 30,
            'flip_method': 2 #0, 2
        }
    },
            
    'cmt03': {
        'set_param':{
            'which_framework': 'original',
            # options: 'original', 'alexey'
            'training': {
                'input': {
                    ### Adjust filters, num, classes = num/3*(classes+5)
                    ##set filters=(classes + 5)*3   vs filters = num/3*(classes+5)
                    'config_file_path': '../config/darknet_cfgs_convs_weights/custom/yolov3_tiny_training_4grain_pea_peanut_gram_bean.cfg',
                    # 2 label: '../config/darknet_cfgs_convs_weights/custom/YOLOv3-tiny_nugget_training.cfg'
                    # 4 label: '../config/darknet_cfgs_convs_weights/custom/yolov3_tiny_training_4grain_pea_peanut_gram_bean.cfg'
                    'convolution_file_path': '../_large_files/config/darknet_cfgs_convs_weights/default/darknet53.conv.74',
                    'train_size': 0.9,
                    'image_label_dir': '../_large_files/data/dataset_to_send/', 
                    # Here it will search for all the sub and sub-sub dir containing "images_labelled" dir
                },
                'output': {
                    'model_saving_dir': '../models/',
                }
            },
            'testing': {
                'config_file_path': '../config/darknet_cfgs_convs_weights/custom/YOLOv3-tiny_nugget_training.cfg',
                '.data_path': '../config/darknet_cfgs_convs_weights/custom/YOLOv3-tiny_nugget_training.cfg',
                'model_path': '../_large_files/config/darknet_cfgs_convs_weights/default/YOLOv3-tiny.weights',
                'threshold': 0.25,
                'test_image_path': '../data/processed_data/images_labelled/172_0_2834.jpg',

            }
        },

        'framework':{
            'darknet_download_dir': '../tools/frameworks/',
            'original': {
                'git_repo': 'https://github.com/pjreddie/darknet',
                'saving_folder_name': 'darknet_original'
            },
            'alexey': {
                'git_repo': 'https://github.com/AlexeyAB/darknet',
                'saving_folder_name': 'darknet_alexey'
            },
            # elif 'ultralytics_Darknet':
            #     cmd_to_run[0] += 'https://github.com/ultralytics/yolov3'
            # elif 'matterport_Mask_RCNN':
            #     cmd_to_run[0] += 'https://github.com/matterport/Mask_RCNN'

        }
    },
    'cmt04_eval': {
        'prediction': {
            'file_path': {
                ## Coco
    #             'classes_names': '../data/processed_data/darknet_example_data/coco/coco.names',
    #             'model_config': '../config/darknet_cfgs_convs_weights/downloaded/YOLOv3-608.cfg',
    #             'model_weights': '../config/darknet_cfgs_convs_weights/downloaded/YOLOv3-608.weights',
                ## Nugget - Tiny
                'classes_names': '../_large_files/data/dataset_grains/data_ref_file__dataset_grains.names',
                #../data/processed_data/nuggets.names
                'model_config': '../config/darknet_cfgs_convs_weights/custom/YOLOv3-tiny_nugget_training.cfg',
                'model_weights': '../models/grain__peanut_pea_gram_bean/yolov3_tiny_training_4grain_pea_peanut_gram_bean_2800.weights'
            },
            'thresholds': {
                'confidence': 0.1,#0.5,0.1
                'non_maximum_suppression': 0.1#0.4, 0.2
            },
            'output_image': {
                'width': 416,
                'height': 416
            }
        },
        'path': {
            'train_ref_file_path': '../_large_files/data/dataset_grains/data_ref_file__dataset_grains_train_dataset.txt',
            'test_ref_file_path': '../_large_files/data/dataset_grains/data_ref_file__dataset_grains_test_dataset.txt',
            'predicted_labels_saving_dir': '../_large_files/data/dataset_grains/predicted_labels/',
            'output_image_saving_dir': '../_large_files/data/dataset_grains/results/'
        }
    }
        
    
}

### Adjust filters, num, classes = num/3*(classes+5)
## https://medium.com/@manivannan_data/how-to-train-yolov3-to-detect-custom-objects-ccbcafeb13d2
## TRAINING REQUIREMENT
'''
    - CONFIG_TO_USE_FILE_PATH
    - CONVOLUTION_LAYER_FILE_PATH
    - TRAIN_SIZE
    - DOT_DATA_FILE_PATH
    - 
    - 
'''
## TESTING REQUIREMENT
'''
    - CONFIG_TO_USE_FILE_PATH
    - DOT_DATA_FILE_PATH
    - 
    - WEIGHTS_TO_LOAD_FILE_PATH
    - THRESHOLD_TO_USE
'''


## Writing a yml
with open('../config/central_configuration.yml', 'w+') as f:
    f.write(yaml.dump(conf))
# print(yaml.dump(conf))

# with open(face_label_mapping_file_path, 'r') as f:
#     mapper_dict = yaml.load(f.read(), Loader=yaml.FullLoader) # FullLoader, BaseLoader, SafeLoader, UnsafeLoader

