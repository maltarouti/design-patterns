from subject import Subject
from subject import RealSubject


class Proxy(Subject):
    def request(self) -> None:
        if self.verify_access():
            subject = RealSubject()
            subject.request()
            self.log()

    def verify_access(self) -> bool:
        print("Proxy: Checking access prior to firing a real request.")
        return True

    def log(self) -> None:
        print("Proxy: Logging the time of request.", end="")
