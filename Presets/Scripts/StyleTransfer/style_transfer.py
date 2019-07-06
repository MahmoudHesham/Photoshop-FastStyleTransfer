# This script copyrights belong to 3deep.org and the used solutions authors as mentioned.
# And it's available for academic and non-commercial use only.

# this solution is cloned from this repo
# https://github.com/lengstrom/fast-style-transfer
# and the copyrights belongs to it's authors as mentioned there

import sys
import tempfile
import numpy as np, os
import tensorflow as tf
from utils import net, save_img, get_img
from send_to_photoshop import send_to_ps

def fast_style_transfer(data_in, paths_out, checkpoint_dir, device_t='/gpu:0', batch_size=4):

    is_paths = type(data_in[0]) == str
    
    if is_paths:
        img_shape = get_img(data_in[0]).shape
    else:
        img_shape = X[0].shape

    g = tf.Graph()
    batch_size = min(len(paths_out), batch_size)
    curr_num = 0
    soft_config = tf.ConfigProto(allow_soft_placement=True)
    soft_config.gpu_options.allow_growth = True
    
    with g.as_default(), g.device(device_t), tf.Session(config=soft_config) as sess:
        
        batch_shape = (batch_size,) + img_shape
        img_placeholder = tf.placeholder(tf.float32, shape=batch_shape, name='img_placeholder')

        preds = net(img_placeholder)
        saver = tf.train.Saver()
        
        saver.restore(sess, checkpoint_dir)
        num_iters = int(len(paths_out)/batch_size)

        for i in range(num_iters):

            pos = i * batch_size
            curr_batch_out = paths_out[pos:pos+batch_size]

            if is_paths:
                curr_batch_in = data_in[pos:pos+batch_size]
                X = np.zeros(batch_shape, dtype=np.float32)
                for j, path_in in enumerate(curr_batch_in):
                    img = get_img(path_in)
                    X[j] = img
            else:
                X = data_in[pos:pos+batch_size]

            _preds = sess.run(preds, feed_dict={img_placeholder:X})
            for j, path_out in enumerate(curr_batch_out):
                save_img(path_out, _preds[j])
                
        remaining_in = data_in[num_iters*batch_size:]
        remaining_out = paths_out[num_iters*batch_size:]
    
    if len(remaining_in) > 0:
        fast_style_transfer(remaining_in, remaining_out, checkpoint_dir, device_t=device_t, batch_size=1)

    print("style transfer completed.")
    send_to_ps(paths_out[0])

    # clear temp folder
    temppath = os.path.dirname(data_in[0])
    ([os.remove(os.path.join(temppath, f)) for f in  os.listdir(temppath)])

tempname = next(tempfile._get_candidate_names()) + ".jpg"
scriptpath = os.path.dirname(os.path.realpath(__file__))

image_in = [sys.argv[-1]]
image_out = ['{0}\\output_images\\{1}'.format(scriptpath, tempname)]
style = sys.argv[-2].replace("jpg", "ckpt")

fast_style_transfer(image_in, image_out, style)