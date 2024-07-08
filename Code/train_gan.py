    train_epochs = 1000
    train_repeat_per_epoch = 10
    total_epochs = train_epochs//train_repeat_per_epoch
    for i in range(total_epochs):
        for _ in range((total_epochs-i) * train_repeat_per_epoch):
            # train discriminator for i epochs
	    # to decide if provided input is real or fake
        for _ in range((i+1) * train_repeat_per_epoch):
            # train generator 
            # to create realistic input samples

