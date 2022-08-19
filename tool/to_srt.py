# -*- coding: utf-8 -*-
from tool.time_format import ms_to_hours
import subprocess
def make_srt(srt_txt, file_name):
    file_name = file_name
    subprocess.check_call(['touch', file_name], shell=False)
    f = open(file_name, 'w')
    f.write(srt_txt)
    f.close()


def to_srt(src_txt):
    flag_word = ["。", "？", "！", "，"]
    basic_line = 15
    srt_txt = ""
    count = 1
    for i in range(len(src_txt)):
        current_sentence = src_txt[i]["FinalSentence"]
        last_time = ms_to_hours(src_txt[i]["StartMs"])
        len_rec = len(current_sentence)
        if len_rec > basic_line:
            start_rec = 0
            last_time = ms_to_hours(src_txt[i]["StartMs"])
            while(len_rec > basic_line):
                flag = True
                for j in flag_word:
                    if j in current_sentence[start_rec:start_rec+basic_line]:
                        loc_rec = current_sentence.index(j, start_rec, start_rec+basic_line) + 1
                        flag = False
                        break
                if flag:
                    loc_rec = start_rec + basic_line
                current_txt = current_sentence[start_rec:loc_rec] + "\n"
                start_time = last_time
                end_time = ms_to_hours(src_txt[i]["Words"][loc_rec]["OffsetEndMs"]+src_txt[i]["StartMs"])
                if current_sentence[start_rec:] != "" and current_sentence[start_rec:] != None:
                    srt_txt = srt_txt + str(count) + "\n" + start_time + "-->" + end_time + "\n" + current_txt + "\n"
                    count += 1
                start_rec = loc_rec
                last_time = end_time
                len_rec = len(current_sentence[loc_rec:])
            current_txt = current_sentence[start_rec:] + "\n"
            start_time = last_time
            end_time = ms_to_hours(src_txt[i]["EndMs"])
            if current_sentence[start_rec:] != "" and current_sentence[start_rec:] != None:
                srt_txt = srt_txt + str(count) + "\n" + start_time + "-->" + end_time + "\n" + current_txt + "\n"
                count += 1
        else:
            start_time = last_time
            end_time = ms_to_hours(src_txt[i]["EndMs"])
            srt_txt = srt_txt + str(count) + "\n" + start_time + "-->" + end_time + "\n" + current_sentence + "\n"+"\n"
            count += 1
    return srt_txt