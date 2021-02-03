#include "Foo.h"

#include <iostream>

Foo::Foo() {}

Foo::~Foo() {}

void Foo::bar() {
  std::cout << "Hello" << std::endl;
}

std::int64_t Foo::add(std::int64_t _a, std::int64_t _b) {
  return _a + _b;
}

Foo* Foo_new() {
  return new Foo();
}

void Foo_bar(Foo* _foo) {
  _foo->bar();
}

std::int64_t Foo_add(Foo* _foo, std::int64_t _a, std::int64_t _b) {
  return _foo->add(_a, _b);
}
