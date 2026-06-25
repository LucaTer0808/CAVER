_base_ = ["base.py"]

args = dict(
    base_seed=112358,
    batch_size=8,
    print_freq=20,
    epoch_num=100,
    use_amp=True,
    iter_num=21840,
    epoch_based=True,
)

optimizers = dict(
    lr=0.005,
    strategy="all",
    optimizer="sgd",
    optimizer_candidates=dict(
        sgd=dict(
            momentum=0.9,
            weight_decay=5e-4,
            nesterov=False,
        ),
    ),
)

schedulers = dict(
    sche_usebatch=True,
    strategy="cos",
    scheduler_candidates=dict(
        cos=dict(
            warmup_length=1,
            min_coef=0.001,
            max_coef=1,
        ),
    ),
)

data = dict(
    test=dict(
        name=[
            "DUT_OMRON_GEN_DEPTH",
            "DUTS_GEN_DEPTH",
            "LFSD",
            "NJUD_GEN_DEPTH",
            "PASCAL_S_GEN_DEPTH",
            "REDWEB_S",
            "SIP_GEN_DEPTH",
            "STERE",
            "STERE_GEN_DEPTH",
            "DUT_RGBD",
            "ECSSD_GEN_DEPTH",
            "LFSD_GEN_DEPTH",
            "NLPR",
            "RGBD135",
            "REDWEB_S_GEN_DEPTH",
            "SSD",
            "STEREO",
            "DUT_RGBD_GEN_DEPTH",
            "HKU_IS_GEN_DEPTH",
            "NJUD",
            "NLPR_GEN_DEPTH",
            "RGBD135_GEN_DEPTH",
            "SIP",
            "SSD_GEN_DEPTH",
            "STEREO_GEN_DEPTH",
        ],
        shape=dict(h=256, w=256),
    ),
)