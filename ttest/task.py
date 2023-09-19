from developer import Developer
import datetime
import random


class Task:
    def __init__(
        self,
        description: str,
        start_date: datetime,
        project_affiliation: str,
        work_day: int,
        allotment: Developer,
        complete: bool,
    ) -> None:
        self._description = description
        self._start_date = start_date
        self._project_affiliation = project_affiliation
        self._work_day = work_day
        self._end_date = self._start_date + datetime.timedelta(days=self._work_day)
        self._allotment = allotment
        self._complete = complete
        self._complexity = random.randint(1, 5)

        # check if there is no allocation
        if self._allotment == "None":
            self._retaliation = 0
        else:
            self._retaliation = self._allotment.seniority * (
                self._complexity / self._work_day
            )

    @property
    def description(self) -> str:
        return self._description

    @property
    def start_date(self) -> datetime:
        return self._start_date

    @property
    def project_affiliation(self) -> str:
        return self._project_affiliation

    @property
    def work_day(self) -> int:
        return self._work_day

    @property
    def allotment(self):
        return self._allotment

    @property
    def complete(self) -> bool:
        return self._complete

    @property
    def complexity(self) -> int:
        return self._complexity

    @property
    def retaliation(self) -> int:
        return self._retaliation

    @property
    def end_date(self) -> datetime:
        return self._end_date

    @project_affiliation.setter
    def project_affiliation(self, new_project_affiliation: str) -> None:
        self._project_affiliation = new_project_affiliation

    @work_day.setter
    def day_work(self, new_work_day: int) -> None:
        self._work_day = new_work_day

    @end_date.setter
    def end_date(self, new_end_date: datetime) -> None:
        self._end_date = new_end_date

    @allotment.setter
    def allotment(self, new_allotment) -> None:
        self._allotment = new_allotment

    @complete.setter
    def complete(self, is_complete: bool, developer: Developer) -> None:
        if self.allotment == developer:
            self._complete = is_complete

    @retaliation.setter
    def retaliation(self, new_retaliation: int) -> None:
        self.retaliation = new_retaliation
