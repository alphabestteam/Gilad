from task import Task
import datetime


class Project:
    def __init__(
        self, project_description: str, start_date: datetime, task_list: list
    ) -> None:
        self._project_description = project_description
        self._start_date = start_date
        self._task_list = task_list
        self._end_date = datetime.date.today()
        self._develop_list = []
        self._task_to_do = []
        self._task_preformed = []
        self._project_cost = 0
        self._complete = False

    @property
    def project_description(self) -> str:
        return self._project_description

    @property
    def start_date(self) -> datetime:
        return self._start_date

    @property
    def task_list(self) -> list:
        return self._task_list

    @property
    def end_date(self) -> datetime:
        for task in self._task_list:
            sum += task.work_day
        self._end_date = self._start_date + datetime.timedelta(days=sum)
        return self._end_date

    @property
    def develop_list(self) -> list:
        self._develop_list = []
        for task in self._task_list:
            self._develop_list.append(task.allotment)
        return self._develop_list

    @property
    def task_to_do(self) -> list:
        self._task_to_do = []
        for task in self._task_list:
            if not task.complete:
                self._task_to_do.append(task)
        return self._task_to_do

    @property
    def task_preformed(self) -> list:
        self._task_preformed = []
        for task in self._task_list:
            if task.complete:
                self._task_preformed.append(task)
        return self._task_preformed

    @property
    def _project_cost(self) -> int:
        self._project_cost = 0
        for task in self.task_preformed:
            self._project_cost += task.retaliation
        return self._project_cost

    @property
    def complete(self) -> bool:
        if len(self.task_preformed) == len(self.task_list):
            self._complete = True
        else:
            self._complete = False
        return self._complete

    @project_description.setter
    def project_description(self, new_project_description: str) -> None:
        self._project_description = new_project_description

    @start_date.setter
    def start_date(self, new_start_date: datetime) -> None:
        self._start_date = new_start_date

    @task_list.setter
    def task_list(self, task) -> None:
        if task not in self.task_list:
            self.task_list.append(task)
        
    @task_list.setter
    def task_list(self, task) -> None:
        if task in self.task_list:
            self.task_list.remove(task)

    @develop_list.setter
    def develop_list(self, developer) -> None:
        self.develop_list.append(developer)

    @develop_list.setter
    def develop_list(self, developer) -> None:
        self.develop_list.remove(developer)

    @task_to_do.setter
    def task_to_do(self, task) -> None:
        self.task_to_do.append(task)

    @task_to_do.setter
    def task_to_do(self, task) -> None:
        self.task_to_do.remove(task)

    @task_preformed.setter
    def task_preformed(self, task) -> None:
        self.task_preformed.append(task)

    @task_preformed.setter
    def task_preformed(self, task) -> None:
        self.task_preformed.remove(task)

    @project_description.setter
    def project_description(self, new_project_description: str) -> None:
        self._project_description = new_project_description

    @project_description.setter
    def project_description(self, new_project_description: str) -> None:
        self._project_description = new_project_description

    @project_description.setter
    def project_description(self, new_project_description: str) -> None:
        self._project_description = new_project_description

    @project_description.setter
    def project_description(self, new_project_description: str) -> None:
        self._project_description = new_project_description

    @project_description.setter
    def project_description(self, new_project_description: str) -> None:
        self._project_description = new_project_description

    @project_description.setter
    def project_description(self, new_project_description: str) -> None:
        self._project_description = new_project_description

