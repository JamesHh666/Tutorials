1 如何处理同一批图片和heatmap</br>
参考：[这个](https://github.com/aleju/imgaug/issues/51) | [这个](https://github.com/aleju/imgaug/issues/122)
```python
seq = iaa.Sequential([
    iaa.MotionBlur(k=5),
    iaa.Fliplr(0.5),
    iaa.Affine(scale=(0.5, 1.5), rotate=(-40, 40)),
    iaa.TranslateX(px=(-10, 10)),
    iaa.TranslateY(px=(-10, 10))
])
seqDet = seq.to_deterministic()

vid = []
hmaps = []
for seq, hmap in zip(video_seq, heatmaps):
    seq_aug, hmap_aug = seqDet(images=(seq * 255)[None, ...].astype(np.uint8), heatmaps=hmap[None, ...])
    vid.append(seq_aug)
    hmaps.append(hmap_aug)
video_seq_aug = np.concatenate(vid, axis=0)
heatmaps_aug = np.concatenate(hmaps, axis=0)
```
