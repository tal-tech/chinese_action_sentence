import sys
from module.description import Description

if __name__ == "__main__":
    desc = Description()
    state, description = desc.init()
    print(state, description)
    if state < 0:
        sys.exit(0)

    sentence_list = [
        # '几次尝试下来，燕子风筝只是奋力向上跃了几下，很快就摇摇晃晃、无精打采地落了下来。'
        '一个例子一个例子一个例子一个例子一个例子。'
    ]
    state,desc_info = desc.get_all_descriptions(sentence_list)
    if desc_info['num'] > 0:
        print("是动作描写")
    else :
        print("不是动作描写") 

