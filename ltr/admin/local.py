class EnvironmentSettings:
    def __init__(self):
        self.workspace_dir = '/share/xlsun/code/TransT_light/results/TransT_light_500e_bs76'    # Base directory for saving network checkpoints.
        self.tensorboard_dir = self.workspace_dir + '/tensorboard/'    # Directory for tensorboard files.
        self.lasot_dir = '/data01/xlsun/dataset/LaSOT/LaSOTBenchmark'
        self.got10k_dir = '/data01/xlsun/dataset/full_data/train_data'
        self.trackingnet_dir = ''
        self.coco_dir = '/data01/xlsun/dataset/coco2017'
        self.lvis_dir = ''
        self.sbd_dir = ''
        self.imagenet_dir = ''
        self.imagenetdet_dir = ''
        self.ecssd_dir = ''
        self.hkuis_dir = ''
        self.msra10k_dir = ''
        self.davis_dir = ''
        self.youtubevos_dir = ''
        self.got10k_ssh_dir = '/data/sunxiaolou/dataset/full_data/train_data'
