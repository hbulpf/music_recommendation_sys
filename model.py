import os
import pickle
import surprise
from surprise import KNNBaseline,Reader
from surprise import Dataset

def split_file(in_path,out_path,scale):
    f1 = open(in_path,"r")
    f2 = open(out_path,"w")
    context = f1.readlines()
    offset = int(len(context)*scale)
    print("new length:",offset)
    split_context = ""
    for i in range(offset):
        split_context += context[i]
    f2.write(split_context)
    f1.close()
    f2.close()

#data pre-prossess
def parse_playlist_get_info(in_line, playlist_dic, song_dic):
    contents = in_line.strip().split("\t")
    name, tags, playlist_id, subscribed_count = contents[0].split("##")
    playlist_dic[playlist_id] = name
    for song in contents[1:]:
        try:
            song_id, song_name, artist, popularity = song.split(":::")
            song_dic[song_id] = song_name
        except:
            print("song format error")
            print(song+"\n")

def parse_file(in_file, out_playlist, out_song):
    #从歌单id到歌单名称的映射字典
    playlist_dic = {}
    #从歌曲id到歌曲名称的映射字典
    song_dic = {}
    for line in open(in_file):
        parse_playlist_get_info(line, playlist_dic, song_dic)
    #把映射字典保存在二进制文件中
    pickle.dump(playlist_dic, open(out_playlist,"wb"))
    #可以通过 playlist_dic = pickle.load(open("playlist.pkl","rb"))重新载入
    pickle.dump(song_dic, open(out_song,"wb"))


def data_preprocess():

    playlist_id_name_dic_file = "./data/playlist_id_name_dict.pkl"
    song_id_name_dic_file = "./data/song_id_name_dic.pkl"
    input_file = "./data/popular.playlist"
    # 解析文件，保存字典「歌单ID-歌单名称」、字典「歌曲ID-歌曲名称」
    parse_file(in_file=input_file,out_playlist=playlist_id_name_dic_file,out_song=song_id_name_dic_file)
    print("已保存字典「歌单ID-歌单名称」、字典「歌曲ID-歌曲名称」")

def train():
    path = "./data/"
    file_path = os.path.expanduser(path + "popular_music_suprise_format1.txt")
    # 指定文件格式
    reader = Reader(line_format='user item rating timestamp', sep=',')
    # 从文件读取数据
    music_data = Dataset.load_from_file(file_path, reader=reader)

    # 计算歌曲和歌曲之间的相似度
    print("构建数据集...")
    trainset = music_data.build_full_trainset()  # 把全部数据进行训练，不进行交叉验证

    print("开始训练模型...")
    sim_options = {'user_based': False}  # 基于歌曲的协同过滤
    algo = KNNBaseline(sim_options=sim_options)
    # algo = SVD(sim_options=sim_options)

    algo.fit(trainset)
    surprise.dump.dump(path+'KNNBaseline_Item_Recommand.model', algo=algo)


def predict(song_name):
    path = "./data/"
    # 重建歌曲id到歌曲名的映射字典
    song_id_name_dic = pickle.load(open(path + "song_id_name_dic.pkl", "rb"))
    # 重建歌单名到歌单id的映射字典
    song_name_id_dic = {}
    for song_id in song_id_name_dic:
        song_name_id_dic[song_id_name_dic[song_id]] = song_id
    if song_name not in song_name_id_dic.keys():
        return "数据库还没有收录这首歌"

    _,algo = surprise.dump.load(path+'/KNNBaseline_Item_Recommand.model')

    # 取出近邻
    # 映射名字到id
    song_id = song_name_id_dic[song_name]
    print("歌曲id", song_id)
    # 取出来对应的内部item id => to_inner_iid
    song_inner_id = algo.trainset.to_inner_iid(song_id)
    print("歌曲内部id", song_inner_id)

    song_list_neighbors = algo.get_neighbors(song_inner_id, k=10)

    # 把歌曲id转成歌曲名字

    # to_raw_uid映射回去
    song_list_neighbors = (algo.trainset.to_raw_iid(inner_id)
                           for inner_id in song_list_neighbors)
    song_list_neighbors = (song_id_name_dic[song_id]
                           for song_id in song_list_neighbors)

    print()
    print("和歌曲 《", song_name, "》 最接近的10个歌曲为：\n")
    result = "和歌曲 《"+song_name+"》 最接近的10个歌曲为：\n"
    for song_name in song_list_neighbors:
        print(song_name)
        result += song_name+"   "
    return result

if __name__ == '__main__':
    # data_preprocess()
    # file = open("./data/song_id_name_dic.pkl",'rb')
    # song_id_name_dic = pickle.load(file)
    # key = list(song_id_name_dic.keys())[6]
    # print(song_id_name_dic[key])
    # file.close()

    # result = predict("本草纲目")
    # predict(result)
    split_file("./data/popular_music_suprise_format.txt","./data/popular_music_suprise_format1.txt",0.2)
    train()


