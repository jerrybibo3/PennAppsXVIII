from Cocoa import *
import time
from Foundation import *
from PyObjCTools import AppHelper
from objc import NULL
from Quartz.CoreGraphics import CGEventCreate, CGEventCreateMouseEvent, \
    CGEventGetLocation, CGEventPost, CGEventSetFlags, CGEventSetIntegerValueField,   \
    CGEventSourceCreate, CGPointMake, kCGEventFlagMaskAlternate,                     \
    kCGEventFlagMaskCommand, kCGEventFlagMaskControl, kCGEventFlagMaskShift,         \
    kCGEventLeftMouseDown, kCGEventLeftMouseUp, kCGEventMouseMoved,                  \
    kCGEventRightMouseDown, kCGEventRightMouseUp, kCGEventSourceStateHIDSystemState, \
    kCGHIDEventTap, kCGMouseEventClickState, CGEventGetType, CGEventTapCreate,       \
    kCGHeadInsertEventTap, kCGEventTapOptionListenOnly, CGEventMaskBit
from AppKit import NSEvent, NSScreen, NSPointInRect
from sys import exit


isMouseDown = 0


class AppDelegate(NSObject):
    def applicationDidFinishLaunching_(self, aNotification):
        NSEvent.addGlobalMonitorForEventsMatchingMask_handler_(NSLeftMouseDownMask, handler)
        NSEvent.addGlobalMonitorForEventsMatchingMask_handler_(NSLeftMouseUpMask, handler)


def handler(event):
    print(event)


def main():
    app = NSApplication.sharedApplication()
    delegate = AppDelegate.alloc().init()
    NSApp().setDelegate_(delegate)
    AppHelper.runEventLoop()


main()
