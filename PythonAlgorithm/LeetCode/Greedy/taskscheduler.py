from collections import Counter


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        result = 0
        while True:
            sub_cnt = 0
            for task, _ in counter.most_common(n + 1):
                sub_cnt += 1
                result += 1

                counter.subtract(task)
                # 0 이하인 아이템을 목록에서 제거
                counter += Counter()
            if not counter:
                break
            result += n - sub_cnt + 1
        return result