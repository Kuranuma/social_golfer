import sys
import copy
import itertools
from scipy import special

# ユーザー一覧
USERS = []
# マッチテーブル(ユーザー毎のマッチ回数)
MATCH_TABLE = []
# 目標値( (グループ人数-1) * 回数 / (ユーザー数 - 1) で算出する)
OBJECT_VALUE = 0

def main():
    args = sys.argv
    if(len(sys.argv) != 4):
        print("python social_golfer.py [グループ人数] [グループ数] [回数]")
        print("例：python social_golfer.py 4 3 8")
        return
        
    print("グループ人数:" + args[1])
    print("グループ数:" + args[2])
    print("回数:" + args[3])
    group_user_num, group_num, time = int(args[1]), int(args[2]), int(args[3])

    global USERS
    global MATCH_TABLE
    global OBJECT_VALUE
    USERS = [i for i in range(group_user_num * group_num)]
    MATCH_TABLE = [[0 for i in range(len(USERS))] for j in range(len(USERS))]
    OBJECT_VALUE = round((group_user_num - 1) * time / (len(USERS) - 1))

    all_groups = []
    for t in range(time):
        all_groups.append(make_groups(group_user_num, group_num))

    for i in range(len(all_groups)):
        for group in all_groups[i]:
            print("{:3d} {}".format(i + 1," ".join([num2alpha(u + 1) for u in group])))

# グループ群作成
def make_groups(group_user_num, group_num):
    global USERS
    groups = []
    remaining_users = copy.copy(USERS)

    for i in range(group_num - 1):
        group_top_user = remaining_users.pop(0)
        # 残ユーザーのうちの先頭ユーザーを基準に最適なグループ一覧を取得する
        # 先頭ユーザー+先頭以外の残ユーザーの全組み合わせを候補とする
        best_users_list = get_best_users([[group_top_user] + list(u) for u in itertools.combinations(remaining_users, group_user_num - 1)], special.comb(len(remaining_users), group_user_num - 1, True))
        # 結果が1つならそれを結果として確定する
        if(len(best_users_list) == 1):
            groups.append(best_users_list[0])
            remaining_users = list(set(remaining_users) - set(best_users_list[0]))
            continue

        # 残りのユーザーの組み合わせから最適な組み合わせを割り出す
        # (現在のグループを確定させた後のユーザー群に最適な組み合わせが残るようにする)
        temp_users_list = get_best_users([list(set(remaining_users) - set(u)) for u in best_users_list], special.comb(len(remaining_users) - group_user_num - 1, group_user_num, True))
        best_users = [group_top_user] + list(set(remaining_users) - set(temp_users_list[0]))
        groups.append(best_users)
        remaining_users = list(set(remaining_users) - set(best_users))

    # グループ数-1の組み合わせが完了したら残りのユーザーをグループとして確定させる
    groups.append(remaining_users)
    add_match_table(groups)
    return groups

# 最適なグループ一覧を返す(同価値のグループが複数返される)
def get_best_users(users_list, combinationCount):
    best_score = -sys.maxsize - 1 
    best_users = []
    for users in users_list:
        score = evaluation_score(users, combinationCount)
        if best_score < score:
            best_score = score
            best_users = [users]
        elif best_score == score:
            best_users.append(users)

    return best_users

# スコア計算
def evaluation_score(users, combinationCount):
    global MATCH_TABLE
    global OBJECT_VALUE
    global USERS
    score = 0
    for j in range(len(users) - 1):
        for u in users[j + 1:]:
            match_count = MATCH_TABLE[users[j]][u]
            if(match_count < OBJECT_VALUE):
                # 組み合わせ数を底とするのは、指数の1の差を最大にするため(全て+1の組より、+2が一つでもある組が優先されるようにする)
                score += pow(combinationCount, OBJECT_VALUE - match_count)
            else:
                # 指数に目標値を加算することで、0よりもマイナス度合いを高くする
                score -= pow(combinationCount, match_count + 1)
    return score

# マッチテーブルにグループ群を適用する
def add_match_table(groups):
    global MATCH_TABLE
    for group in groups:
        sorted_group = sorted(group)
        for i in range(len(sorted_group) - 1):
            for u in sorted_group[i + 1:]:
                MATCH_TABLE[sorted_group[i]][u] += 1

# 名前作成
def num2alpha(num):
    if num <= 26:
        return chr(64 + num)
    elif num % 26 == 0:
        return num2alpha(num // 26 - 1) + chr(90)
    else:
        return num2alpha(num // 26) + chr(64 + num % 26)

if __name__ == '__main__':
    main()