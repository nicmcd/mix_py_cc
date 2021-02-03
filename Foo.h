#include <cstdint>

class Foo {
 public:
  Foo();
  ~Foo();
  void bar();
  std::int64_t add(std::int64_t _a, std::int64_t _b);
};

extern "C" {
  Foo* Foo_new();
  void Foo_bar(Foo* _foo);
  std::int64_t Foo_add(Foo* _foo, std::int64_t _a, std::int64_t _b);
}
