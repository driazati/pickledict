import subprocess
import dataclasses
import time
import pyarkbench


@dataclasses.dataclass
class Result:
    duration: float
    size: int


@dataclasses.dataclass
class TestCase:
    description: str
    text: str

    def run(self):
        pyarkbench.cleanup()

        with pyarkbench.Timer() as base64_timer:
            base64_result = subprocess.run(
                "base64", input=self.text.encode("utf-8"), stdout=subprocess.PIPE
            )
        base64_len = len(base64_result.stdout)

        pyarkbench.cleanup()

        with pyarkbench.Timer() as baseMEOW_timer:
            # baseMEOW_result = subprocess.run(
            #     "baseMEOW", input=self.text.encode("utf-8"), stdout=subprocess.PIPE
            # )
            baseMEOW_result = subprocess.run(
                "./src/a.out", input=self.text.encode("utf-8"), stdout=subprocess.PIPE
            )
        baseMEOW_len = len(baseMEOW_result.stdout)

        return Result(base64_timer.ms_duration, base64_len), Result(
            baseMEOW_timer.ms_duration, baseMEOW_len
        )


tests = [
    # TestCase("10 characters", "a" * 10),
    TestCase("1000 characters", "a" * 1000),
    # TestCase("10000 characters", "a" * 10000),
    # TestCase("1000000 characters", "a" * 1000000),
]


table = [
    [
        "test case",
        "base64 runtime (ms)",
        "baseMEOW runtime (ms)",
        "base64 size (bytes)",
        "baseMEOW size (bytes)",
    ]
]
table.append(["---" for _ in table[0]])

for test in tests:
    base64_result, baseMEOW_result = test.run()
    table.append(
        [
            test.description,
            round(base64_result.duration, 2),
            round(baseMEOW_result.duration, 2),
            base64_result.size,
            baseMEOW_result.size,
        ]
    )
    test.run()


for row in table:
    print("|".join([str(x) for x in row]))
