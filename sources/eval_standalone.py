import os

from eval.metrics import meteor

test_output_path = 'test_outputs/'

refs = []
cans = []
with open(os.path.join(test_output_path, 'test_refs.txt'), encoding='utf-8') as ref_file, \
        open(os.path.join(test_output_path, 'test_cans.txt'), encoding='utf-8') as can_file:
    for line in ref_file.readlines():
        refs.append(line.strip().split())
    for line in can_file.readlines():
        cans.append(line.strip().split())
assert len(refs) == len(cans)


meteor_score = meteor(references=refs, candidates=cans)
print(meteor_score)
