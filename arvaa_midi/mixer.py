from pygame import mixer
import random
  
# Starting the mixer
mixer.init()

# Setting the volume
mixer.music.set_volume(0.7)


def valitse_biisi(mids, mids_9kpl):
    r = random.randint(0, len(mids) - 1)
    biisi = mids[r]
    mixer.music.load("mids/" + biisi)
    mids_9kpl.append(biisi)
    mids.pop(r)

    return mids_9kpl, mids

  
