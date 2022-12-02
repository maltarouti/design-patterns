
from proxy import Proxy
from subject import RealSubject


if __name__ == "__main__":
    print("Client: Executing request using real subject directly:")
    real_subject = RealSubject()
    real_subject.request()

    print("\n")

    print("Client: Executing request with a proxy (lazy loading):")
    proxy = Proxy()
    proxy.request()
