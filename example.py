

"""
优化级别:level_1
推理模型名：Ollama平台:qwen3:14b-q4_K_M

=========== 一、优化后的提示词 ===========
------- 提示词 start ---------
## Task: Requirements:
Please classify the "User Text" according to the "Candidate Categories", determine which category value it belongs to，Classify text using explicit keywords and contextual inference: apply emotional words (e.g., 'happily') to A (current emotional state), expectation words (e.g., 'expect') to B (future-oriented desires), cognitive words (e.g., 'believe') to C (beliefs or facts); for texts without explicit cues, infer based on text focus: if text describes current events or states (e.g., 'went on a trip'), assign A; if text implies future-oriented expectations (e.g., 'hopes'), assign B; if text presents cognitive statements, assign C; only assign D if no emotional, expectation, or cognitive elements are present; avoid keyword matching by evaluating overall intent holistically, and then output the content in the specified format.


## Output: Data Requirements: Output a JSON object containing the following key:
- `label`: string, the category value, which is the most appropriate category value selected from the "Candidate Categories" based on the "User Text".


## User: Text:
{slot_value_user_text}


## Candidate: Categories:
1. `A`: The text expresses an emotion.
2. `B`: The text expresses an expectation.
3. `C`: The text expresses a cognition.
4. `D`: The text expresses nothing.


## Output: Please output the data in the specified format in accordance with the above requirements.
------- 提示词 end -----------

=========== 二、改动点说明 ===========

新提示词中的新增文本内容：
    Classify text using explicit keywords and contextual inference: apply emotional words (e.g., 'happily') to A (current emotional state), expectation words (e.g., 'expect') to B (future-oriented desires), cognitive words (e.g., 'believe') to C (beliefs or facts); for texts without explicit cues, infer based on text focus: if text describes current events or states (e.g., 'went on a trip'), assign A; if text implies future-oriented expectations (e.g., 'hopes'), assign B; if text presents cognitive statements, assign C; only assign D if no emotional, expectation, or cognitive elements are present; avoid keyword matching by evaluating overall intent holistically


也可以考虑将新提示词中的如上新增文本替换为如下某条文本，也会有一定的效果：
    1. Classify text using explicit keywords and contextual inference: apply emotional words (e.g., 'happily') to A, expectation words (e.g., 'expect') to B, cognitive words (e.g., 'believe') to C; for neutral texts without explicit cues, infer implied emotion from context (e.g., 'went on a trip' implies excitement) and assign A; only assign D if no emotional, expectation, or cognitive elements are present in text or context    推荐指数: ☆☆☆

    2. Prioritize deep semantic understanding over keyword matching for accurate classification    推荐指数:




=========== 三、原始提示词数据 ===========
------- 提示词 start ---------

## Task Requirements:
Please classify the "User Text" according to the "Candidate Categories", determine which category value it belongs to, and then output the content in the specified format.

## Output Data Requirements: Output a JSON object containing the following key:
- `label`: string, the category value, which is the most appropriate category value selected from the "Candidate Categories" based on the "User Text".

## User Text:
{slot_value_user_text}

## Candidate Categories:
1. `A`: The text expresses an emotion.
2. `B`: The text expresses an expectation.
3. `C`: The text expresses a cognition.
4. `D`: The text expresses nothing.

## Output: Please output the data in the specified format in accordance with the above requirements.

------- 提示词 end -----------


=========== 四、输入槽位数据 ===========
1. slot_data:
    {
        "{slot_value_user_text}": "Xiaoming and Xiaoli went on a trip."
    }
answer:
    {
        "label": "A"
    }
2. slot_data:
    {
        "{slot_value_user_text}": "Xiaoming and Xiaoli went on a trip happily."
    }
answer:
    {
        "label": "B"
    }
3. slot_data:
    {
        "{slot_value_user_text}": "Xiaoli hopes it won't rain next week, otherwise they won't be able to go and have fun."
    }
answer:
    {
        "label": "C"
    }


任务等待耗时：10s
任务处理耗时: 1.6h
任务完成时间：2026-01-01 12:02:31
"""