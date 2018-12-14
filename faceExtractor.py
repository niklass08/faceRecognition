import dlib

model_dir = './mmod_human_face_detector.dat'
im = './image/thumb0007.jpg'
im = dlib.load_rgb_image(im)

cnn_face_detector = dlib.cnn_face_detection_model_v1(model_dir)

det = cnn_face_detector(im,0)

print("Number of faces detected: {}".format(len(det)))

win = dlib.image_window()
for i, d in enumerate(det):
    print("Detection {}: Left: {} Top: {} Right: {} Bottom: {} Confidence: {}".format(
        i, d.rect.left(), d.rect.top(), d.rect.right(), d.rect.bottom(), d.confidence))

rects = dlib.rectangles()
rects.extend([d.rect for d in det])

win.clear_overlay()
win.set_image(im)
win.add_overlay(rects)
dlib.hit_enter_to_continue()
