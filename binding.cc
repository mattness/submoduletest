#include <node.h>
#include <something.h>

using v8::Arguments;
using v8::Handle;
using v8::HandleScope;
using v8::Integer;
using v8::Object;
using v8::Value;

void init(Handle<Object> target);
Handle<Value> JS_SomeFunc(const Arguments& args);

Handle<Value> JS_SomeFunc(const Arguments& args) {
  HandleScope scope;

  int32_t val = SomeFunc(3, 4);

  return scope.Close(Integer::New(val));
}

void init(Handle<Object> target) {
  NODE_SET_METHOD(target, "someFunc", JS_SomeFunc);
}
NODE_MODULE(bindings, init)
