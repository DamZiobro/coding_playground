// promise example
#include <iostream>       // std::cout
#include <functional>     // std::ref
#include <thread>         // std::thread
#include <future>         // std::promise, std::future
#include <unistd.h>

using namespace std;

void print_int (std::future<int>& fut) {
  cout << "waiting for fut.get()..." << endl;
  int x = fut.get();
  std::cout << "value: " << x << '\n';
}

int main ()
{
  std::promise<int> prom;                      // create promise

  std::future<int> fut = prom.get_future();    // engagement with future

  std::thread th1 (print_int, std::ref(fut));  // send future to new thread
  std::thread th2 (print_int, std::ref(fut));  // send future to new thread
  std::thread th3 (print_int, std::ref(fut));  // send future to new thread

  cout << "before set value " << endl;
  sleep(3);
  prom.set_value (10);                         // fulfill promise
  cout << "after set value " << endl;
                                               // (synchronizes with getting the future)
  th1.join();
  th2.join();
  th3.join();
  return 0;
}
