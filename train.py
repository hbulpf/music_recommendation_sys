from model import *

if __name__ == '__main__':
    split_file("./data/popular_music_suprise_format.txt", "./data/popular_music_suprise_format1.txt", 0.08)
    train_baseon_item()
    train_baseon_playlist()