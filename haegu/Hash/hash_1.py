#[해쉬 1번] 완주
import collections


def solution(participant, completion):
    part_dict = collections.Counter(participant)
    comp_dict = collections.Counter(completion)
    unattendant = part_dict - comp_dict

    return list(unattendant)[0]
