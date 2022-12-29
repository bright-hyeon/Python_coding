import json
import pandas as pd

file_path = "./evaluate.json"


with open(file_path, 'r') as file:
    data = json.load(file)

# print(type(data))
# print(json.dumps(data, ensure_ascii=False, indent=3))
evaluate = data["evaluate"]
# print(len(evaluate))


df = pd.DataFrame(columns=['이미지 파일명', 'label', 'tp_count', 'fp_count', 'fn_count', 'tp_iou_avg', 'fp_iou_avg','tp_iou_sum','fp_iou_sum'])


print('================ START: change to dataframe =================')
for keys in range(0,len(evaluate)) :
    base_zl = list(evaluate.keys())[keys]
    print(keys , '>> ', evaluate[base_zl])

    temp = evaluate[base_zl]

    label = temp["01110200"]["label"]
    tp_count = temp["01110200"]["tp_count"]
    fp_count = temp["01110200"]["fp_count"]
    fn_count = temp["01110200"]["fn_count"]
    tp_iou_avg = temp["01110200"]["tp_iou_avg"]
    fp_iou_avg = temp["01110200"]["fp_iou_avg"]
    tp_iou_sum = temp["01110200"]["tp_iou_sum"]
    fp_iou_sum = temp["01110200"]["fp_iou_sum"]

    # sample = [(base_zl+'.png', label, tp_count, fp_count, fn_count, tp_iou_avg, fp_iou_avg)]

    df.loc[keys]=[base_zl+'.png', label, tp_count, fp_count, fn_count, tp_iou_avg, fp_iou_avg, tp_iou_sum, fp_iou_sum]

    # break

print('================ END: change to dataframe')
print('================ START: save excel')
    
df.to_excel('./unet_evaluate_AGAIN.xlsx', encoding = 'utf-8', index = False)

print('================ END: save excel')
    



