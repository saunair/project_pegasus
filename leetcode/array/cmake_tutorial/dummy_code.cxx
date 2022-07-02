#include <iostream>
#include "yocto_api.h"

using namespace std;

int main(int argc, const char * argv[])
{
  string errmsg;

  if(YAPI::RegisterHub("usb", errmsg) != YAPI::SUCCESS) {
      cerr << "RegisterHub error: " << errmsg << endl;
      return 1;
  }

  cout << "Device list: " << endl;
  YModule *module = YModule::FirstModule();
  while (module != NULL) {
      cout << module->get_serialNumber() << " ";
      cout << module->get_productName()  << endl;
      module = module->nextModule();
  }
  YAPI::FreeAPI();
  return 0;
}
