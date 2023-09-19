class Developer:
    def __init__(
        self,
        name: str,
        task_preformed: list,
        work_day: int,
        retaliation: int,
        to_do_task: list,
    ) -> None:
        self._name = name
        self._task_preformed = task_preformed
        self._work_day = work_day
        self._retaliation = retaliation
        self._to_do_task = to_do_task
        self._seniority = 1

    @property
    def name(self) -> str:
        return self._name

    @property
    def task_preformed(self) -> list:
        return self._task_preformed

    @property
    def word_day(self) -> int:
        return self._work_day

    @property
    def retaliation(self) -> int:
        return self._retaliation

    @property
    def to_do_task(self) -> list:
        return self._to_do_task

    @property
    def seniority(self) -> int:
        return self._seniority

    @task_preformed.setter
    def name(self, task) -> None:
        self._task_preformed.append(task)

    @word_day.setter
    def work_day(self, work_day_add: int) -> None:
        self._work_day += work_day_add

    @retaliation.setter
    def retaliation(self, retaliation_add: int) -> None:
        self._retaliation += retaliation_add

    @to_do_task.setter
    def to_do_task(self, task) -> None:
        self._task_preformed.remove(task)

    @seniority.setter
    def seniority(self, seniority_add) -> None:
        self._seniority += seniority_add
